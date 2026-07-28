"""End-to-end: mcp-suite drives a real stdio MCP server (fail early in CI)."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SUITE = Path(__file__).resolve().parent / "mcp-suite.e2e.yaml"
SERVER = ROOT / "tests" / "fixtures" / "minimal_mcp_server.py"


def _mcp_suite_bin() -> str:
    found = shutil.which("mcp-suite")
    if found:
        return found
    # Editable install may put scripts next to the active interpreter.
    scripts = Path(sys.executable).resolve().parent
    for name in ("mcp-suite.exe", "mcp-suite"):
        candidate = scripts / name
        if candidate.is_file():
            return str(candidate)
    return "mcp-suite"


@pytest.mark.e2e
def test_mcp_suite_list_cases():
    cmd = [
        _mcp_suite_bin(),
        "run",
        "--suite",
        str(SUITE),
        "--server-command",
        f"{sys.executable} {SERVER}",
        "--list",
    ]
    proc = subprocess.run(
        cmd,
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        timeout=60,
        env={**os.environ},
    )
    out = (proc.stdout or "") + (proc.stderr or "")
    assert proc.returncode == 0, out
    assert "echo" in out.lower() or "test_echo" in out.lower() or "Echo" in out


@pytest.mark.e2e
def test_mcp_suite_runs_against_real_server():
    cmd = [
        _mcp_suite_bin(),
        "run",
        "--suite",
        str(SUITE),
        "--server-command",
        f"{sys.executable} {SERVER}",
        "--transport",
        "stdio",
    ]
    proc = subprocess.run(
        cmd,
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        timeout=120,
        env={**os.environ},
    )
    out = (proc.stdout or "") + (proc.stderr or "")
    assert proc.returncode == 0, out
