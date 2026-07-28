"""Checks that this repo is a thin connector over PyPI mcp-test-harness."""

from __future__ import annotations

from pathlib import Path


def test_pyproject_depends_on_harness_pypi() -> None:
    root = Path(__file__).resolve().parents[1]
    text = (root / "pyproject.toml").read_text(encoding="utf-8")
    assert "mcp-test-harness>=" in text.replace(" ", "")
    assert 'packages = ["src/mcp_test_suite"]' in text
    assert "src/mcp_test_harness" not in text


def test_changelog_and_contributing_exist_and_are_in_sdist() -> None:
    root = Path(__file__).resolve().parents[1]
    toml = (root / "pyproject.toml").read_text(encoding="utf-8")
    for name in ("CHANGELOG.md", "CONTRIBUTING.md"):
        assert (root / name).is_file()
        assert f'  "{name}"' in toml, f"sdist should include {name}"


def test_engine_not_vendored() -> None:
    root = Path(__file__).resolve().parents[1]
    assert not (root / "src" / "mcp_test_harness").exists()
    assert (root / "src" / "mcp_test_suite").is_dir()
