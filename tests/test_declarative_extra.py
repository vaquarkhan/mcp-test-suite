"""Additional coverage for declarative suite helpers and CLI."""

from __future__ import annotations

import asyncio
import json
import time
from pathlib import Path
from unittest.mock import patch

import pytest
import yaml

from mcp_test_harness.assertions import MCPAssertionError
from mcp_test_suite.declarative import (
    _build_case_func,
    _parse_suite,
    _result_payload,
    DeclarativeCase,
    compile_suite,
    discover_suite_files,
    load_declarative_modules,
    load_suite_file,
)
from mcp_test_suite.declarative_cli import run_declarative


def test_parse_suite_external_schema(tmp_path: Path):
    schema_file = tmp_path / "echo.json"
    schema_file.write_text(json.dumps({"type": "object"}), encoding="utf-8")
    data = {
        "schemas": {"Echo": "echo.json"},
        "cases": [{"name": "c", "call": "echo", "args": {}}],
        "server_command": "python srv.py",
    }
    suite = _parse_suite(data, tmp_path / "s.yaml")
    assert suite.schemas["Echo"] == {"type": "object"}
    assert suite.server_command == "python srv.py"


def test_parse_suite_invalid_cases():
    with pytest.raises(ValueError, match="must be a list"):
        _parse_suite({"cases": "nope"}, Path("x.yaml"))


def test_parse_suite_invalid_case_item():
    with pytest.raises(ValueError, match="must be a mapping"):
        _parse_suite({"cases": ["bad"]}, Path("x.yaml"))


def test_load_suite_not_mapping(tmp_path: Path):
    path = tmp_path / "mcp-suite.yaml"
    path.write_text("- just a list\n", encoding="utf-8")
    with pytest.raises(ValueError, match="must be a mapping"):
        load_suite_file(path)


def test_result_payload_variants():
    class ItemDict(dict):
        pass

    class Result:
        content = [{"text": "plain"}, {"data": {"a": 1}}]

    out = _result_payload(Result())
    assert isinstance(out, list)
    assert _result_payload({"content": []}) == {"content": []}

    class One:
        content = [ItemDict(text="only")]

    assert _result_payload(One()) == "only"


def test_build_case_expect_error_success_fails():
    class Session:
        async def call_tool(self, name, arguments):
            class R:
                content = []
                isError = False

            return R()

    case = DeclarativeCase(name="e", call="t", expect_error=True)
    func = _build_case_func(case, {})

    async def _run():
        with pytest.raises(MCPAssertionError, match="expected to error"):
            await func(Session())

    asyncio.run(_run())


def test_build_case_expect_error_ok():
    class Session:
        async def call_tool(self, name, arguments):
            class R:
                content = []
                isError = True

                def __str__(self):
                    return "boom"

            return R()

    case = DeclarativeCase(name="e", call="t", expect_error=True)
    func = _build_case_func(case, {})
    asyncio.run(func(Session()))


def test_build_case_latency_only():
    calls = {"n": 0}

    class Session:
        async def call_tool(self, name, arguments):
            calls["n"] += 1

            class R:
                content = []
                isError = False

            return R()

    case = DeclarativeCase(name="lat", call="echo", args={}, max_latency_ms=5000)
    func = _build_case_func(case, {})
    asyncio.run(func(Session()))
    assert calls["n"] >= 1


def test_build_case_schema_assert():
    class Item:
        text = '{"text": "hi"}'

    class Session:
        async def call_tool(self, name, arguments):
            class R:
                content = [Item()]
                isError = False

            return R()

    case = DeclarativeCase(
        name="s",
        call="echo",
        args={},
        assert_schema="Echo",
    )
    schemas = {
        "Echo": {
            "type": "object",
            "properties": {"text": {"type": "string"}},
            "required": ["text"],
        }
    }
    func = _build_case_func(case, schemas)
    asyncio.run(func(Session()))


def test_run_declarative_missing_suite(tmp_path: Path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    assert run_declarative([]) == 5


def test_run_declarative_suite_not_found():
    assert run_declarative(["--suite", "does-not-exist-xyz.yaml"]) == 2


def test_tags_as_string_and_transport(tmp_path: Path):
    suite = _parse_suite(
        {
            "transport": "http",
            "cases": [{"name": "t", "call": "x", "tags": "smoke", "timeout": 12}],
        },
        tmp_path / "s.yaml",
    )
    assert suite.transport == "http"
    assert suite.cases[0].tags == ["smoke"]
    mod = compile_suite(suite)
    assert mod.test_cases[0].markers.get("timeout") == 12.0


def test_discover_suite_file_path(tmp_path: Path):
    path = tmp_path / "mcp-suite.yaml"
    path.write_text("cases: []\n", encoding="utf-8")
    found = discover_suite_files([path])
    assert found == [path.resolve()]


def test_result_payload_multi_text():
    class Result:
        content = [{"text": "a"}, {"text": "b"}]

    assert _result_payload(Result()) == ["a", "b"]


def test_build_resource_and_prompt(monkeypatch):
    calls = []

    async def fake_resource(session, uri, **kwargs):
        calls.append(("resource", uri))

    async def fake_prompt(session, name, arguments=None, **kwargs):
        calls.append(("prompt", name, arguments))

    monkeypatch.setattr(
        "mcp_test_harness.assertions.assert_resource_read",
        fake_resource,
    )
    monkeypatch.setattr(
        "mcp_test_harness.assertions.assert_prompt",
        fake_prompt,
    )

    r_case = DeclarativeCase(name="r", resource="file:///x")
    p_case = DeclarativeCase(name="p", prompt="sum", prompt_args={"t": "1"})
    asyncio.run(_build_case_func(r_case, {})(object()))
    asyncio.run(_build_case_func(p_case, {})(object()))
    assert calls[0][0] == "resource"
    assert calls[1][0] == "prompt"


def test_build_case_latency_budget_exceeded(monkeypatch):
    class Session:
        async def call_tool(self, name, arguments):
            class R:
                content = []
                isError = False

            return R()

    # Force elapsed time over budget after successful call with schema
    case = DeclarativeCase(
        name="slow",
        call="echo",
        args={},
        assert_schema="Echo",
        max_latency_ms=0.0,
    )
    schemas = {"Echo": {"type": "object"}}

    clock = {"t": 100.0}

    def fake_monotonic():
        clock["t"] += 0.5  # each call advances 500ms
        return clock["t"]

    monkeypatch.setattr(time, "monotonic", fake_monotonic)
    monkeypatch.setattr(
        "mcp_test_suite.declarative._validate_against_named_schema",
        lambda *a, **k: None,
    )
    # Avoid assert_tool_call consuming the clock with its own timing helpers.
    async def fake_tool_call(*_a, **_k):
        class R:
            content = []
            isError = False

        return R()

    monkeypatch.setattr("mcp_test_suite.declarative.assert_tool_call", fake_tool_call)

    with pytest.raises(MCPAssertionError, match="latency"):
        asyncio.run(_build_case_func(case, schemas)(Session()))


def test_load_skips_bad_and_empty(tmp_path: Path):
    bad = tmp_path / "bad.suite.yaml"
    bad.write_text("cases: not-a-list\n", encoding="utf-8")
    empty = tmp_path / "mcp-suite.yaml"
    empty.write_text("cases: []\n", encoding="utf-8")
    good = tmp_path / "ok.suite.yaml"
    good.write_text(
        yaml.dump({"cases": [{"name": "Keep Me", "call": "echo"}, {"name": "Drop", "call": "x"}]}),
        encoding="utf-8",
    )
    mods = load_declarative_modules([tmp_path], filter_name="keep")
    assert len(mods) == 1
    assert len(mods[0].test_cases) == 1


def test_run_declarative_bad_suite_load(tmp_path: Path):
    suite = tmp_path / "mcp-suite.yaml"
    suite.write_text("cases: oops\n", encoding="utf-8")
    assert run_declarative(["--suite", str(suite)]) == 2


def test_run_declarative_config_systemexit(tmp_path: Path, monkeypatch):
    suite = tmp_path / "mcp-suite.yaml"
    suite.write_text(
        yaml.dump({"cases": [{"name": "A", "call": "echo"}]}),
        encoding="utf-8",
    )
    monkeypatch.chdir(tmp_path)

    def boom(_ns):
        raise SystemExit(2)

    with patch("mcp_test_harness.config.load_config", boom):
        assert run_declarative(["--suite", str(suite), "--server-command", "x"]) == 2


def test_run_declarative_list(tmp_path: Path, monkeypatch):
    suite_dir = tmp_path / "suites"
    suite_dir.mkdir()
    suite = suite_dir / "mcp-suite.yaml"
    suite.write_text(
        yaml.dump(
            {
                "server": {"command": "python -c pass"},
                "cases": [{"name": "A", "call": "echo", "args": {}}],
            }
        ),
        encoding="utf-8",
    )
    monkeypatch.chdir(tmp_path)
    cfg = tmp_path / "mcp-test.yaml"
    cfg.write_text(
        "server:\n  command: python -c pass\ntest:\n  dirs: [tests]\n",
        encoding="utf-8",
    )

    async def fake_run(*args, **kwargs):
        return 0

    with patch("mcp_test_suite.engine.run_harness", fake_run):
        code = run_declarative(
            ["--suite", str(suite), "--config", str(cfg), "--list"]
        )
        assert code == 0


def test_expect_error_from_tool_failure():
    async def boom(*args, **kwargs):
        raise MCPAssertionError("tool failed")

    async def _run():
        with patch(
            "mcp_test_suite.declarative.assert_tool_call",
            new=boom,
        ):
            case = DeclarativeCase(name="e", call="t", expect_error=True)
            await _build_case_func(case, {})(object())

    asyncio.run(_run())


def test_tool_failure_propagates_when_not_expect_error():
    async def boom(*args, **kwargs):
        raise MCPAssertionError("tool failed")

    async def _run():
        with patch(
            "mcp_test_suite.declarative.assert_tool_call",
            new=boom,
        ):
            case = DeclarativeCase(name="e", call="t", expect_error=False)
            with pytest.raises(MCPAssertionError, match="tool failed"):
                await _build_case_func(case, {})(object())

    asyncio.run(_run())


def test_expect_error_message_matches():
    from mcp_test_suite.declarative import ExpectErrorSpec

    async def boom(*args, **kwargs):
        raise MCPAssertionError("Unknown tool: nope")

    case = DeclarativeCase(
        name="e",
        call="t",
        expect_error=True,
        expect_error_spec=ExpectErrorSpec(message_matches="Unknown tool"),
    )

    async def _run():
        with patch("mcp_test_suite.declarative.assert_tool_call", new=boom):
            await _build_case_func(case, {})(object())

    asyncio.run(_run())


def test_expect_error_message_mismatch_fails():
    from mcp_test_suite.declarative import ExpectErrorSpec

    async def boom(*args, **kwargs):
        raise MCPAssertionError("connection reset")

    case = DeclarativeCase(
        name="e",
        call="t",
        expect_error=True,
        expect_error_spec=ExpectErrorSpec(message_matches="Unknown tool"),
    )

    async def _run():
        with patch("mcp_test_suite.declarative.assert_tool_call", new=boom):
            with pytest.raises(MCPAssertionError, match="did not match expect_error"):
                await _build_case_func(case, {})(object())

    asyncio.run(_run())


def test_expect_error_infra_not_swallowed():
    async def boom(*args, **kwargs):
        raise ConnectionError("server gone")

    case = DeclarativeCase(name="e", call="t", expect_error=True)

    async def _run():
        with patch("mcp_test_suite.declarative.assert_tool_call", new=boom):
            with pytest.raises(ConnectionError, match="server gone"):
                await _build_case_func(case, {})(object())

    asyncio.run(_run())


def test_parse_expect_error_dict_and_alias():
    from mcp_test_suite.declarative import _parse_expect_error

    enabled, spec = _parse_expect_error({"code": -32601, "message_matches": "SCOPE"})
    assert enabled is True
    assert spec is not None
    assert spec.code == -32601
    assert spec.message_matches == "SCOPE"

    enabled, spec = _parse_expect_error(False, error_matches="boom")
    assert enabled is True
    assert spec is not None
    assert spec.message_matches == "boom"


def test_expect_error_rejects_random_exceptions():
    async def boom(*args, **kwargs):
        raise RuntimeError("harness bug")

    case = DeclarativeCase(name="e", call="t", expect_error=True)

    async def _run():
        with patch("mcp_test_suite.declarative.assert_tool_call", new=boom):
            with pytest.raises(RuntimeError, match="harness bug"):
                await _build_case_func(case, {})(object())

    asyncio.run(_run())


def test_engine_require_compatible_harness():
    from mcp_test_suite.engine import require_compatible_harness

    ver = require_compatible_harness()
    assert ver.startswith("3.")


def test_discover_skips_node_modules(tmp_path: Path):
    (tmp_path / "mcp-suite.yaml").write_text("cases: []\n", encoding="utf-8")
    nested = tmp_path / "node_modules" / "pkg"
    nested.mkdir(parents=True)
    (nested / "evil.suite.yaml").write_text("cases: []\n", encoding="utf-8")
    found = discover_suite_files([tmp_path])
    names = {p.name for p in found}
    assert "mcp-suite.yaml" in names
    assert "evil.suite.yaml" not in names
