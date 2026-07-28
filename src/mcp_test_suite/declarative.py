"""Declarative YAML/JSON suite runner for cross-language MCP testing.

Universal test definitions (``mcp-suite.yaml``) are compiled into harness
:class:`~mcp_test_harness.discovery.HarnessCase` objects so the PyPI
``mcp-test-harness`` scheduler, fixtures, and reporters run unchanged.
Language adapters invoke the same path via ``mcp-suite run`` / ``mcp-test run``.
"""

from __future__ import annotations

import json
import logging
import re
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

import yaml

from mcp_test_harness.assertions import (
    MCPAssertionError,
    assert_latency,
    assert_tool_call,
)
from mcp_test_harness.discovery import HarnessCase, HarnessModule

logger = logging.getLogger(__name__)

_SUITE_FILE_NAMES = (
    "mcp-suite.yaml",
    "mcp-suite.yml",
    "mcp-suite.json",
    "mcp-test.suite.yaml",
    "mcp-test.suite.yml",
)
_SUITE_GLOBS = ("*.suite.yaml", "*.suite.yml", "*.suite.json")


@dataclass
class DeclarativeCase:
    """One declarative test case from YAML/JSON."""

    name: str
    call: str | None = None
    args: dict[str, Any] = field(default_factory=dict)
    expected: Any | None = None
    assert_schema: str | None = None
    max_latency_ms: float | None = None
    validate_input_schema: bool = False
    expect_error: bool = False
    tags: list[str] = field(default_factory=list)
    timeout: float | None = None
    resource: str | None = None
    prompt: str | None = None
    prompt_args: dict[str, Any] = field(default_factory=dict)
    raw: dict[str, Any] = field(default_factory=dict)


@dataclass
class DeclarativeSuite:
    """Parsed declarative suite with optional named JSON schemas."""

    path: Path
    cases: list[DeclarativeCase] = field(default_factory=list)
    schemas: dict[str, dict[str, Any]] = field(default_factory=dict)
    server_command: str | None = None
    transport: str | None = None


def _slug(name: str) -> str:
    slug = re.sub(r"[^0-9a-zA-Z]+", "_", name.strip()).strip("_").lower()
    return slug or "case"


def load_suite_file(path: Path) -> DeclarativeSuite:
    """Load a declarative suite from YAML or JSON."""
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        data = json.loads(text)
    else:
        data = yaml.safe_load(text) or {}
    if not isinstance(data, dict):
        raise ValueError(f"Suite file must be a mapping: {path}")
    return _parse_suite(data, path)


def _parse_suite(data: dict[str, Any], path: Path) -> DeclarativeSuite:
    schemas_raw = data.get("schemas") or {}
    schemas: dict[str, dict[str, Any]] = {}
    if isinstance(schemas_raw, dict):
        for key, value in schemas_raw.items():
            if isinstance(value, dict):
                schemas[str(key)] = value
            elif isinstance(value, str):
                schema_path = (path.parent / value).resolve()
                schemas[str(key)] = json.loads(schema_path.read_text(encoding="utf-8"))

    cases_raw = data.get("cases") or data.get("tests") or []
    if not isinstance(cases_raw, list):
        raise ValueError(f"'cases'/'tests' must be a list in {path}")

    cases: list[DeclarativeCase] = []
    for idx, item in enumerate(cases_raw):
        if not isinstance(item, dict):
            raise ValueError(f"Case #{idx} in {path} must be a mapping")
        name = str(item.get("name") or f"case_{idx + 1}")
        tags = item.get("tags") or []
        if not isinstance(tags, list):
            tags = [str(tags)]
        cases.append(
            DeclarativeCase(
                name=name,
                call=item.get("call") or item.get("tool"),
                args=dict(item.get("args") or item.get("arguments") or {}),
                expected=item.get("expected"),
                assert_schema=item.get("assert_schema") or item.get("schema"),
                max_latency_ms=(
                    float(item["max_latency_ms"])
                    if item.get("max_latency_ms") is not None
                    else None
                ),
                validate_input_schema=bool(item.get("validate_input_schema", False)),
                expect_error=bool(item.get("expect_error", False)),
                tags=[str(t) for t in tags],
                timeout=float(item["timeout"]) if item.get("timeout") is not None else None,
                resource=item.get("resource"),
                prompt=item.get("prompt"),
                prompt_args=dict(item.get("prompt_args") or {}),
                raw=item,
            )
        )

    server = data.get("server") or {}
    server_command = None
    transport = None
    if isinstance(server, dict):
        server_command = server.get("command")
        transport = server.get("transport")
    if isinstance(data.get("server_command"), str):
        server_command = data["server_command"]
    if isinstance(data.get("transport"), str):
        transport = data["transport"]

    return DeclarativeSuite(
        path=path,
        cases=cases,
        schemas=schemas,
        server_command=server_command,
        transport=transport,
    )


def discover_suite_files(paths: list[Path] | None = None) -> list[Path]:
    """Find declarative suite files under *paths* (default: cwd)."""
    roots = paths or [Path.cwd()]
    found: list[Path] = []
    seen: set[Path] = set()
    for root in roots:
        root = root.resolve()
        if root.is_file():
            candidates = [root]
        else:
            candidates = []
            for name in _SUITE_FILE_NAMES:
                p = root / name
                if p.is_file():
                    candidates.append(p)
            for pattern in _SUITE_GLOBS:
                candidates.extend(root.rglob(pattern))
        for path in candidates:
            resolved = path.resolve()
            if resolved not in seen and resolved.is_file():
                seen.add(resolved)
                found.append(resolved)
    return sorted(found, key=str)


def _result_payload(result: Any) -> Any:
    """Normalize an MCP tool result into a JSON-serializable value."""
    content = getattr(result, "content", None)
    if content is None and isinstance(result, dict):
        content = result.get("content")
    if not content:
        return result
    texts: list[str] = []
    structured: list[Any] = []
    for item in content:
        text = getattr(item, "text", None)
        if text is None and isinstance(item, dict):
            text = item.get("text")
        if text is not None:
            texts.append(str(text))
            try:
                structured.append(json.loads(text))
            except (TypeError, json.JSONDecodeError):
                structured.append(text)
            continue
        data = getattr(item, "data", None)
        if data is None and isinstance(item, dict):
            data = item.get("data")
        if data is not None:
            structured.append(data)
    if len(structured) == 1:
        return structured[0]
    if structured:
        return structured
    return texts[0] if len(texts) == 1 else texts  # pragma: no cover


def _validate_against_named_schema(
    payload: Any,
    schema_name: str,
    schemas: dict[str, dict[str, Any]],
) -> None:
    schema = schemas.get(schema_name)
    if schema is None:
        raise MCPAssertionError(
            f"Unknown schema '{schema_name}'. Define it under schemas: in the suite file."
        )
    try:
        import jsonschema
    except ImportError as exc:  # pragma: no cover
        raise MCPAssertionError(
            "assert_schema requires the jsonschema package "
            "(pip install jsonschema or 'mcp-test-suite[dev]')"
        ) from exc
    try:
        jsonschema.validate(instance=payload, schema=schema)
    except jsonschema.ValidationError as exc:  # type: ignore[attr-defined]
        raise MCPAssertionError(
            f"Response does not match schema '{schema_name}': {exc.message}"
        ) from exc


def _build_case_func(
    case: DeclarativeCase,
    schemas: dict[str, dict[str, Any]],
) -> Callable:
    """Compile a declarative case into an async test function."""

    async def _test(mcp_server: Any) -> None:
        if case.resource:
            from mcp_test_harness.assertions import assert_resource_read

            await assert_resource_read(mcp_server, case.resource)
            return

        if case.prompt:
            from mcp_test_harness.assertions import assert_prompt

            await assert_prompt(
                mcp_server,
                case.prompt,
                arguments=case.prompt_args or None,
            )
            return

        if not case.call:
            raise MCPAssertionError(
                f"Case '{case.name}' needs call/tool, resource, or prompt"
            )

        # Latency-only cases use assert_latency (single tool call).
        if (
            case.max_latency_ms is not None
            and case.expected is None
            and not case.assert_schema
            and not case.validate_input_schema
            and not case.expect_error
        ):
            await assert_latency(
                mcp_server,
                case.call,
                case.args,
                max_ms=case.max_latency_ms,
                runs=1,
                aggregate="max",
            )
            return

        started = time.monotonic()
        try:
            result = await assert_tool_call(
                mcp_server,
                case.call,
                case.args,
                expected=case.expected,
                validate_against_input_schema=case.validate_input_schema,
            )
        except Exception:
            # Protocol/tool errors (McpError) and assertion failures both satisfy expect_error.
            if case.expect_error:
                return
            raise

        if case.expect_error:
            raise MCPAssertionError(
                f"Tool '{case.call}' was expected to error but succeeded"
            )

        elapsed_ms = (time.monotonic() - started) * 1000.0
        if case.max_latency_ms is not None and elapsed_ms > case.max_latency_ms:
            raise MCPAssertionError(
                f"Tool '{case.call}' latency {elapsed_ms:.1f}ms exceeds "
                f"max_latency_ms={case.max_latency_ms}"
            )

        if case.assert_schema:
            payload = _result_payload(result)
            _validate_against_named_schema(payload, case.assert_schema, schemas)

    _test.__name__ = f"test_{_slug(case.name)}"
    _test.__qualname__ = _test.__name__
    _test.__doc__ = case.name
    return _test


def compile_suite(suite: DeclarativeSuite) -> HarnessModule:
    """Turn a declarative suite into a :class:`HarnessModule` for the scheduler."""
    cases: list[HarnessCase] = []
    for decl in suite.cases:
        func = _build_case_func(decl, suite.schemas)
        markers: dict[str, Any] = {}
        if decl.tags:
            markers["tags"] = list(decl.tags)
        if decl.timeout is not None:
            markers["timeout"] = decl.timeout
        cases.append(
            HarnessCase(
                name=func.__name__,
                module_path=suite.path,
                func=func,
                markers=markers,
                is_async=True,
            )
        )
    return HarnessModule(path=suite.path, test_cases=cases)


def load_declarative_modules(
    paths: list[Path] | None = None,
    *,
    filter_name: str | None = None,
    filter_marker: str | None = None,
) -> list[HarnessModule]:
    """Discover and compile declarative suites under *paths*."""
    from mcp_test_harness.discovery import _matches_marker_filter, _matches_name_filter

    modules: list[HarnessModule] = []
    for suite_path in discover_suite_files(paths):
        try:
            suite = load_suite_file(suite_path)
        except Exception as exc:
            logger.warning("Skipping suite %s: %s", suite_path, exc)
            continue
        if not suite.cases:
            continue
        module = compile_suite(suite)
        if filter_name or filter_marker:
            kept = []
            for case in module.test_cases:
                if filter_name and not _matches_name_filter(case.name, filter_name):
                    continue
                if filter_marker and not _matches_marker_filter(case.markers, filter_marker):
                    continue
                kept.append(case)
            module.test_cases = kept
        if module.test_cases:
            modules.append(module)
    return modules
