"""CLI entry: wrap mcp-test-harness and add ``run`` for declarative suites."""

from __future__ import annotations

import sys


def main(argv: list[str] | None = None) -> int:
    """``mcp-suite`` / ``mcp-test`` entry point."""
    av = list(sys.argv[1:] if argv is None else argv)
    if av and av[0] == "run":
        from mcp_test_suite.declarative_cli import run_declarative

        return run_declarative(av[1:])

    # Delegate all other subcommands to the PyPI engine.
    from mcp_test_harness.cli import main as harness_main

    # Restore argv for the harness argparse (it reads sys.argv).
    if argv is not None:
        old = sys.argv
        try:
            sys.argv = [old[0], *av]
            result = harness_main()
            return int(result or 0)
        finally:
            sys.argv = old
    result = harness_main()
    return int(result or 0)


if __name__ == "__main__":
    raise SystemExit(main())
