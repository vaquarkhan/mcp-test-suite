#!/usr/bin/env python3
"""Smoke: suite connectors + PyPI mcp-test-harness import cleanly."""

from __future__ import annotations

import importlib.metadata as metadata
import sys


def main() -> int:
    try:
        import mcp_test_harness  # noqa: F401
        import mcp_test_suite  # noqa: F401
        from mcp_test_suite.declarative import load_suite_file  # noqa: F401
    except ImportError as e:
        print("FAIL: import:", e, file=sys.stderr)
        return 1

    print("OK  mcp-test-harness", metadata.version("mcp-test-harness"))
    print("OK  mcp-test-suite", metadata.version("mcp-test-suite"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
