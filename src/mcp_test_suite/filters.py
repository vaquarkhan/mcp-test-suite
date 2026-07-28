"""Name/marker filters for declarative cases (suite-owned copies).

These mirror mcp-test-harness discovery helpers so we do not import
underscore-prefixed private APIs that can break across harness releases.
"""

from __future__ import annotations

import fnmatch
from typing import Any


def matches_name_filter(name: str, pattern: str) -> bool:
    """Return True if *name* matches a ``-k`` style filter pattern."""
    if "*" in pattern or "?" in pattern:
        return fnmatch.fnmatch(name, f"*{pattern}*")
    return pattern.lower() in name.lower()


def matches_marker_filter(markers: dict[str, Any], filter_marker: str) -> bool:
    """Return True if *markers* satisfy a ``-m`` marker/tag filter."""
    if filter_marker in markers:
        return True
    tags: list[str] = markers.get("tags", [])
    return filter_marker in tags


def filter_cases(
    cases: list[Any],
    *,
    filter_name: str | None = None,
    filter_marker: str | None = None,
) -> list[Any]:
    """Filter harness cases by optional name and marker patterns."""
    if not filter_name and not filter_marker:
        return list(cases)
    kept: list[Any] = []
    for case in cases:
        if filter_name and not matches_name_filter(case.name, filter_name):
            continue
        if filter_marker and not matches_marker_filter(case.markers, filter_marker):
            continue
        kept.append(case)
    return kept
