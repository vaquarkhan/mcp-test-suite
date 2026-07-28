"""CLI entry: wrap mcp-test-harness and add ``run`` for declarative suites."""

from __future__ import annotations

import sys

from mcp_test_suite import __version__ as SUITE_VERSION

_INSTALL_HINT = (
    "Install the engine and suite CLI:\n"
    '  pip install "mcp-test-harness>=3.0.9,<4"\n'
    '  pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"\n'
    "Then ensure `mcp-suite` is on PATH."
)


def _print_versions() -> None:
    engine = "unknown"
    try:
        import mcp_test_harness

        engine = getattr(mcp_test_harness, "__version__", None) or engine
        if engine == "unknown":
            from importlib.metadata import version

            engine = version("mcp-test-harness")
    except Exception:
        pass
    print(f"mcp-test-suite {SUITE_VERSION} (engine mcp-test {engine})")


def _normalize_system_exit(exc: SystemExit) -> int:
    """Map argparse help/version SystemExit to a process exit code."""
    code = exc.code
    if code is None or code is False:
        return 0
    if code is True:
        return 1
    if isinstance(code, int):
        # argparse --help/--version historically used exit(0); treat 0 as success.
        return code
    return 0


def main(argv: list[str] | None = None) -> int:
    """``mcp-suite`` / ``mcp-test`` entry point."""
    av = list(sys.argv[1:] if argv is None else argv)

    if av and av[0] in ("--version", "-V"):
        _print_versions()
        return 0

    if av and av[0] == "run":
        try:
            from mcp_test_suite.declarative_cli import run_declarative
        except ImportError as exc:
            print(f"mcp-test-harness is required but not importable: {exc}", file=sys.stderr)
            print(_INSTALL_HINT, file=sys.stderr)
            return 1
        try:
            return run_declarative(av[1:])
        except SystemExit as exc:
            return _normalize_system_exit(exc)

    try:
        from mcp_test_harness.cli import main as harness_main
    except ImportError as exc:
        print(f"mcp-test-harness is required but not importable: {exc}", file=sys.stderr)
        print(_INSTALL_HINT, file=sys.stderr)
        return 1

    # Restore argv for the harness argparse (it reads sys.argv).
    try:
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
    except SystemExit as exc:
        return _normalize_system_exit(exc)


if __name__ == "__main__":
    raise SystemExit(main())
