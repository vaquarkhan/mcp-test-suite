"""Harness plugin: inject declarative YAML/JSON suites into discovery."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from mcp_test_suite.declarative import (
    compile_suite,
    load_declarative_modules,
    load_suite_file,
)
from mcp_test_suite.filters import filter_cases
from mcp_test_suite.runtime import RUNTIME

name = "mcp-test-suite-declarative"


def register(context: Any) -> None:
    """Register a discovery hook that appends compiled ``mcp-suite.yaml`` cases."""

    def _hook(modules: list[Any]) -> list[Any]:
        extra: list[Any] = []
        if RUNTIME.suite_paths:
            for path in RUNTIME.suite_paths:
                try:
                    suite = load_suite_file(path)
                except Exception:
                    continue
                if not suite.cases:
                    continue
                module = compile_suite(suite)
                module.test_cases = filter_cases(
                    module.test_cases,
                    filter_name=RUNTIME.filter_name,
                    filter_marker=RUNTIME.filter_marker,
                )
                if module.test_cases:
                    extra.append(module)
        else:
            roots = list(RUNTIME.search_roots) if RUNTIME.search_roots else [Path.cwd()]
            for mod in modules:
                path = getattr(mod, "path", None)
                if path is not None:
                    roots.append(Path(path).parent)
            # Deduplicate roots while preserving order.
            seen: set[Path] = set()
            unique_roots: list[Path] = []
            for root in roots:
                resolved = root.resolve()
                if resolved not in seen:
                    seen.add(resolved)
                    unique_roots.append(resolved)
            extra.extend(
                load_declarative_modules(
                    unique_roots,
                    filter_name=RUNTIME.filter_name,
                    filter_marker=RUNTIME.filter_marker,
                )
            )

        if not extra:
            return modules

        seen_keys: set[tuple[str, str]] = set()
        out: list[Any] = []
        for mod in list(modules) + extra:
            kept = []
            for tc in mod.test_cases:
                key = (str(Path(tc.module_path).resolve()), tc.name)
                if key in seen_keys:
                    continue
                seen_keys.add(key)
                kept.append(tc)
            if kept:
                mod.test_cases = kept
                out.append(mod)
        return out

    context.add_discovery_hook(_hook)


class DeclarativePlugin:
    """Class form of the plugin (also discovered by harness entry-point loader)."""

    name = name

    def register(self, context: Any) -> None:
        register(context)
