"""Unit tests for declarative YAML/JSON suites (mcp-test-suite)."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml

from mcp_test_harness.assertions import MCPAssertionError
from mcp_test_suite.declarative import (
    compile_suite,
    discover_suite_files,
    load_declarative_modules,
    load_suite_file,
    _result_payload,
    _slug,
    _validate_against_named_schema,
)


def test_slug_basic():
    assert _slug("Validate Weather Tool") == "validate_weather_tool"
    assert _slug("  ") == "case"


def test_load_suite_yaml(tmp_path: Path):
    path = tmp_path / "mcp-suite.yaml"
    path.write_text(
        yaml.dump(
            {
                "server": {"command": "node server.js", "transport": "stdio"},
                "schemas": {
                    "Echo": {"type": "object", "properties": {"text": {"type": "string"}}}
                },
                "cases": [
                    {
                        "name": "Echo ok",
                        "call": "echo",
                        "args": {"message": "hi"},
                        "max_latency_ms": 500,
                        "tags": ["smoke"],
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    suite = load_suite_file(path)
    assert suite.server_command == "node server.js"
    assert suite.transport == "stdio"
    assert len(suite.cases) == 1
    assert suite.cases[0].call == "echo"
    assert suite.cases[0].max_latency_ms == 500
    assert "Echo" in suite.schemas

    module = compile_suite(suite)
    assert len(module.test_cases) == 1
    assert module.test_cases[0].name == "test_echo_ok"
    assert module.test_cases[0].is_async
    assert "smoke" in module.test_cases[0].markers.get("tags", [])


def test_load_suite_json_tests_alias(tmp_path: Path):
    path = tmp_path / "mcp-suite.json"
    path.write_text(
        json.dumps(
            {
                "tests": [
                    {"name": "R1", "tool": "ping", "arguments": {}},
                    {"name": "Bad", "call": "x", "expect_error": True},
                ]
            }
        ),
        encoding="utf-8",
    )
    suite = load_suite_file(path)
    assert len(suite.cases) == 2
    assert suite.cases[0].call == "ping"
    assert suite.cases[1].expect_error is True


def test_discover_suite_files(tmp_path: Path):
    (tmp_path / "mcp-suite.yaml").write_text("cases: []\n", encoding="utf-8")
    (tmp_path / "extra.suite.yml").write_text("cases: []\n", encoding="utf-8")
    found = discover_suite_files([tmp_path])
    names = {p.name for p in found}
    assert "mcp-suite.yaml" in names
    assert "extra.suite.yml" in names


def test_load_declarative_modules_filter(tmp_path: Path):
    path = tmp_path / "demo.suite.yaml"
    path.write_text(
        yaml.dump(
            {
                "cases": [
                    {"name": "Alpha", "call": "a", "tags": ["smoke"]},
                    {"name": "Beta", "call": "b", "tags": ["perf"]},
                ]
            }
        ),
        encoding="utf-8",
    )
    mods = load_declarative_modules([tmp_path], filter_marker="smoke")
    assert len(mods) == 1
    assert len(mods[0].test_cases) == 1
    assert "alpha" in mods[0].test_cases[0].name


def test_validate_named_schema_ok():
    schemas = {"Echo": {"type": "object", "properties": {"text": {"type": "string"}}, "required": ["text"]}}
    _validate_against_named_schema({"text": "hi"}, "Echo", schemas)


def test_validate_named_schema_missing():
    with pytest.raises(MCPAssertionError, match="Unknown schema"):
        _validate_against_named_schema({}, "Nope", {})


def test_validate_named_schema_fail():
    schemas = {"Echo": {"type": "object", "properties": {"text": {"type": "string"}}, "required": ["text"]}}
    with pytest.raises(MCPAssertionError, match="does not match"):
        _validate_against_named_schema({"other": 1}, "Echo", schemas)


def test_result_payload_text_json():
    class Item:
        text = '{"ok": true}'

    class Result:
        content = [Item()]

    assert _result_payload(Result()) == {"ok": True}


def test_compile_requires_action(tmp_path: Path):
    path = tmp_path / "mcp-suite.yaml"
    path.write_text(
        yaml.dump({"cases": [{"name": "Empty"}]}),
        encoding="utf-8",
    )
    suite = load_suite_file(path)
    module = compile_suite(suite)
    assert len(module.test_cases) == 1
    # Function raises when run without call/resource/prompt — exercised via coroutine creation
    import asyncio

    async def _run():
        with pytest.raises(MCPAssertionError, match="needs call"):
            await module.test_cases[0].func(object())

    asyncio.run(_run())


def test_examples_declarative_suite_parses():
    root = Path(__file__).resolve().parents[1]
    example = root / "examples" / "declarative" / "mcp-suite.yaml"
    if not example.is_file():
        pytest.skip("example suite not present")
    suite = load_suite_file(example)
    assert len(suite.cases) >= 2
    module = compile_suite(suite)
    assert all(c.is_async for c in module.test_cases)
