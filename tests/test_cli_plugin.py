"""Tests for CLI wrapper and harness discovery plugin."""

from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import yaml

from mcp_test_suite import cli
from mcp_test_suite.plugin import DeclarativePlugin, register
from mcp_test_suite.runtime import RUNTIME, reset_runtime


def test_cli_run_delegates_to_declarative(monkeypatch):
    called = {}

    def fake_run(argv):
        called["argv"] = argv
        return 7

    monkeypatch.setattr("mcp_test_suite.declarative_cli.run_declarative", fake_run)
    assert cli.main(["run", "--suite", "x.yaml"]) == 7
    assert called["argv"] == ["--suite", "x.yaml"]


def test_cli_version_prints_suite_and_engine(capsys):
    assert cli.main(["--version"]) == 0
    out = capsys.readouterr().out
    assert "mcp-test-suite 4.0.0" in out
    assert "engine mcp-test" in out


def test_cli_delegates_other_commands_to_harness(monkeypatch):
    called = {}

    def fake_harness_main():
        called["ok"] = True
        return 0

    monkeypatch.setattr("mcp_test_harness.cli.main", fake_harness_main)
    assert cli.main(["try", "--help"]) == 0
    assert called["ok"] is True


def test_plugin_injects_explicit_suite(tmp_path: Path):
    reset_runtime()
    suite = tmp_path / "mcp-suite.yaml"
    suite.write_text(
        yaml.dump({"cases": [{"name": "Echo", "call": "echo", "args": {}}]}),
        encoding="utf-8",
    )
    RUNTIME.suite_paths = [suite]
    ctx = SimpleNamespace(hooks=[])
    ctx.add_discovery_hook = ctx.hooks.append
    register(ctx)
    out = ctx.hooks[0]([])
    assert len(out) == 1
    assert out[0].test_cases
    reset_runtime()


def test_plugin_discovers_under_cwd(tmp_path: Path, monkeypatch):
    reset_runtime()
    suite = tmp_path / "mcp-suite.yaml"
    suite.write_text(
        yaml.dump({"cases": [{"name": "A", "call": "echo"}]}),
        encoding="utf-8",
    )
    monkeypatch.chdir(tmp_path)
    plugin = DeclarativePlugin()
    ctx = MagicMock()
    hooks = []
    ctx.add_discovery_hook.side_effect = hooks.append
    plugin.register(ctx)
    out = hooks[0]([])
    assert len(out) == 1
    reset_runtime()


def test_plugin_applies_name_filter(tmp_path: Path):
    reset_runtime()
    suite = tmp_path / "mcp-suite.yaml"
    suite.write_text(
        yaml.dump(
            {
                "cases": [
                    {"name": "Keep Me", "call": "echo"},
                    {"name": "Drop", "call": "x"},
                ]
            }
        ),
        encoding="utf-8",
    )
    RUNTIME.suite_paths = [suite]
    RUNTIME.filter_name = "keep"
    ctx = SimpleNamespace()
    hooks = []
    ctx.add_discovery_hook = hooks.append
    register(ctx)
    out = hooks[0]([])
    assert len(out) == 1
    assert len(out[0].test_cases) == 1
    reset_runtime()
