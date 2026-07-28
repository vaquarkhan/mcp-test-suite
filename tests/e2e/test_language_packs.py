"""Language pack checks: every framework mcp-suite.yaml must load and compile."""

from __future__ import annotations

from pathlib import Path

import pytest

from mcp_test_suite.declarative import compile_suite, load_suite_file

ROOT = Path(__file__).resolve().parents[2]
FRAMEWORKS = ROOT / "examples" / "frameworks"


def _suite_files() -> list[Path]:
    if not FRAMEWORKS.is_dir():
        return []
    return sorted(FRAMEWORKS.rglob("mcp-suite.yaml"))


@pytest.mark.e2e
@pytest.mark.parametrize("suite_path", _suite_files(), ids=lambda p: str(p.relative_to(ROOT)))
def test_language_suite_loads(suite_path: Path):
    suite = load_suite_file(suite_path)
    assert suite.cases, f"no cases in {suite_path}"
    module = compile_suite(suite)
    assert module.test_cases, f"compile produced no cases: {suite_path}"
    for case in module.test_cases:
        assert case.name.startswith("test_")


@pytest.mark.e2e
def test_declarative_example_suite_loads():
    path = ROOT / "examples" / "declarative" / "mcp-suite.yaml"
    suite = load_suite_file(path)
    assert len(suite.cases) >= 2
    assert compile_suite(suite).test_cases


@pytest.mark.e2e
def test_tutorials_exist_for_each_language():
    tutorials = ROOT / "docs" / "tutorials"
    required = [
        "README.md",
        "yaml.md",
        "python.md",
        "typescript.md",
        "java.md",
        "go.md",
        "dotnet.md",
        "rust.md",
    ]
    for name in required:
        assert (tutorials / name).is_file(), f"missing tutorial {name}"


@pytest.mark.e2e
def test_framework_ecosystems_present():
    for eco in ("java", "kotlin", "typescript", "python", "go", "dotnet", "rust"):
        assert (FRAMEWORKS / eco).is_dir(), f"missing examples/frameworks/{eco}"
