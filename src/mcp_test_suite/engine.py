"""Version-gated bridge to the mcp-test-harness scheduler.

Harness 3.x does not yet expose a public ``run_harness`` symbol. This module
is the *only* place that may import ``mcp_test_harness.cli._run_harness``,
and it refuses to run outside the pinned major range.
"""

from __future__ import annotations

import re
from typing import Any

_INSTALL_HINT = (
    'pip install "mcp-test-harness>=3.0.9,<4"\n'
    'pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"'
)


def harness_version() -> str:
    """Return the installed mcp-test-harness version string."""
    try:
        import mcp_test_harness

        ver = getattr(mcp_test_harness, "__version__", None)
        if ver:
            return str(ver)
    except Exception:
        pass
    try:
        from importlib.metadata import version

        return version("mcp-test-harness")
    except Exception as exc:  # pragma: no cover
        raise RuntimeError(
            "mcp-test-harness is not installed.\n" + _INSTALL_HINT
        ) from exc


def _major_minor_patch(ver: str) -> tuple[int, int, int]:
    m = re.match(r"^(\d+)\.(\d+)\.(\d+)", ver.strip())
    if not m:
        raise RuntimeError(f"Unparseable mcp-test-harness version: {ver!r}")
    return int(m.group(1)), int(m.group(2)), int(m.group(3))


def require_compatible_harness() -> str:
    """Ensure installed harness is within ``>=3.0.9,<4``; return version."""
    ver = harness_version()
    major, minor, patch = _major_minor_patch(ver)
    if major != 3 or (minor == 0 and patch < 9):
        raise RuntimeError(
            f"mcp-test-suite requires mcp-test-harness>=3.0.9,<4 "
            f"(found {ver}).\n{_INSTALL_HINT}"
        )
    return ver


async def run_harness(
    config: Any,
    *,
    list_only: bool = False,
    fail_fast: bool = False,
    last_failed: bool = False,
) -> int:
    """Run the engine scheduler (public suite API over a private harness symbol)."""
    require_compatible_harness()
    try:
        from mcp_test_harness.cli import run_harness as _impl  # type: ignore[attr-defined]
    except ImportError:
        from mcp_test_harness.cli import _run_harness as _impl

    return await _impl(
        config, list_only=list_only, fail_fast=fail_fast, last_failed=last_failed
    )
