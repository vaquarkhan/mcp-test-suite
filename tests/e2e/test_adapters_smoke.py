# Adapter CLI smoke (optional): ensure language wrappers invoke mcp-suite.
# Skips when the language toolchain is not installed.

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SERVER = ROOT / "tests" / "fixtures" / "minimal_mcp_server.py"
SUITE = Path(__file__).resolve().parent / "mcp-suite.e2e.yaml"


def _which(*names: str) -> str | None:
    for name in names:
        found = shutil.which(name)
        if found:
            return found
    return None


def _mcp_suite() -> str:
    return _which("mcp-suite") or str(
        Path(sys.executable).resolve().parent / ("mcp-suite.exe" if os.name == "nt" else "mcp-suite")
    )


@pytest.mark.e2e
def test_go_adapter_module_builds_when_go_present():
    go = _which("go")
    if not go:
        pytest.skip("go not installed")
    mod = ROOT / "adapters" / "gotest"
    proc = subprocess.run(
        [go, "test", "./..."],
        cwd=str(mod),
        capture_output=True,
        text=True,
        timeout=120,
    )
    # Package may have no *_test.go; compile check via go test is still useful.
    # If there are zero tests, go test exits 0.
    assert proc.returncode == 0, proc.stdout + proc.stderr


@pytest.mark.e2e
def test_jest_adapter_package_json_valid():
    pkg = ROOT / "adapters" / "jest" / "package.json"
    data = json.loads(pkg.read_text(encoding="utf-8"))
    assert data.get("name") == "@mcp-test-suite/jest"
    assert "bin" in data or data.get("main") or data.get("exports")


@pytest.mark.e2e
def test_junit_adapter_pom_present():
    pom = ROOT / "adapters" / "junit5" / "pom.xml"
    text = pom.read_text(encoding="utf-8")
    assert "mcp-test-suite-junit5" in text


@pytest.mark.e2e
def test_xunit_csproj_present():
    csproj = list((ROOT / "adapters" / "xunit").glob("*.csproj"))
    assert csproj, "missing xUnit csproj"


@pytest.mark.e2e
def test_adapter_default_binary_is_mcp_suite():
    """Catch regressions that point adapters back at bare mcp-test for YAML run."""
    jest = (ROOT / "adapters" / "jest" / "src" / "index.ts").read_text(encoding="utf-8")
    assert "mcp-suite" in jest
    go = (ROOT / "adapters" / "gotest" / "mcp.go").read_text(encoding="utf-8")
    assert "mcp-suite" in go
    cs = (ROOT / "adapters" / "xunit" / "McpClient.cs").read_text(encoding="utf-8")
    assert "mcp-suite" in cs
