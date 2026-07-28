"""Shared runtime state for declarative discovery (plugin + CLI)."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class DeclarativeRuntime:
    """Options the harness discovery hook reads while ``mcp-test`` / ``mcp-suite`` runs."""

    suite_paths: list[Path] = field(default_factory=list)
    search_roots: list[Path] = field(default_factory=list)
    filter_name: str | None = None
    filter_marker: str | None = None


RUNTIME = DeclarativeRuntime()


def reset_runtime() -> None:
    """Clear CLI overrides (used by tests)."""
    RUNTIME.suite_paths.clear()
    RUNTIME.search_roots.clear()
    RUNTIME.filter_name = None
    RUNTIME.filter_marker = None
