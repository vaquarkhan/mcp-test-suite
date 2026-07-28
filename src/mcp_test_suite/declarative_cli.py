"""CLI for ``mcp-suite run`` / ``mcp-test run`` — declarative YAML/JSON suites."""

from __future__ import annotations

import argparse
import asyncio
import sys
from dataclasses import replace
from pathlib import Path

from mcp_test_suite.declarative import discover_suite_files, load_suite_file
from mcp_test_suite.runtime import RUNTIME, reset_runtime

_INSTALL_HINT = (
    "Install the engine and suite CLI:\n"
    '  pip install "mcp-test-harness>=3.0.9,<4"\n'
    '  pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"\n'
    "Then ensure `mcp-suite` is on PATH."
)


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="mcp-suite run",
        description=(
            "Run language-agnostic declarative MCP tests from YAML/JSON "
            "(mcp-suite.yaml). Uses the installed mcp-test-harness engine."
        ),
    )
    p.add_argument(
        "--suite",
        default=None,
        help="Path to mcp-suite.yaml / .json (default: auto-discover)",
    )
    p.add_argument(
        "--config",
        default=None,
        help="Path to mcp-test.yaml for server/transport settings",
    )
    p.add_argument(
        "--server-command",
        dest="server_command",
        default=None,
        help="Override server launch command",
    )
    p.add_argument(
        "--transport",
        default=None,
        choices=["stdio", "sse", "http"],
        help="Transport type (default: stdio)",
    )
    p.add_argument(
        "--report-format",
        dest="report_format",
        default=None,
        choices=["json", "junit", "html", "sarif"],
    )
    p.add_argument(
        "--report-output",
        dest="report_output",
        default=None,
    )
    p.add_argument("-k", dest="filter_name", default=None, help="Filter by case name")
    p.add_argument("-m", dest="filter_marker", default=None, help="Filter by tag")
    p.add_argument("--list", action="store_true", help="List cases and exit")
    p.add_argument("--verbose", action="store_true", default=None)
    return p


def run_declarative(argv: list[str] | None = None) -> int:
    """Entry point for ``mcp-suite run`` / ``mcp-test run``."""
    try:
        from mcp_test_harness.config import load_config
    except ImportError as exc:
        print(f"mcp-test-harness is required but not importable: {exc}", file=sys.stderr)
        print(_INSTALL_HINT, file=sys.stderr)
        return 1

    args = _build_parser().parse_args(argv)
    reset_runtime()

    suite_paths: list[Path] = []
    if args.suite:
        suite_paths = [Path(args.suite)]
        if not suite_paths[0].is_file():
            print(f"Suite file not found: {args.suite}", file=sys.stderr)
            return 2
    else:
        suite_paths = discover_suite_files([Path.cwd()])
        if not suite_paths:
            print(
                "No mcp-suite.yaml found. Create one or pass --suite PATH.",
                file=sys.stderr,
            )
            return 5

    suite_cmd = None
    suite_transport = None
    for sp in suite_paths:
        try:
            suite = load_suite_file(sp)
            suite_cmd = suite.server_command or suite_cmd
            suite_transport = suite.transport or suite_transport
        except Exception as exc:
            print(f"Error loading {sp}: {exc}", file=sys.stderr)
            return 2

    ns = argparse.Namespace(
        test_path=None,
        server_command=args.server_command or suite_cmd,
        transport=args.transport or suite_transport,
        config=args.config,
        verbose=args.verbose,
        timeout=None,
        parallel=None,
        workers=None,
        report_format=args.report_format,
        report_output=args.report_output,
        pdf_output=None,
        sarif_output=None,
        cra_output=None,
        pr_summary_output=None,
        filter_name=args.filter_name,
        filter_marker=args.filter_marker,
        list=args.list,
        watch=False,
        update_snapshots=False,
        fail_fast=False,
        last_failed=False,
    )

    try:
        config = load_config(ns)
    except SystemExit as exc:
        return int(exc.code) if isinstance(exc.code, int) else 2

    # Declarative-only: do not discover Python test_*.py under the project's tests/.
    # Cases come exclusively from the suite plugin + RUNTIME.suite_paths.
    suite_parents = [str(sp.parent.resolve()) for sp in suite_paths]
    config = replace(config, test_dirs=[])

    RUNTIME.suite_paths = list(suite_paths)
    RUNTIME.search_roots = [Path(p) for p in suite_parents] + [Path.cwd()]
    RUNTIME.filter_name = args.filter_name
    RUNTIME.filter_marker = args.filter_marker

    try:
        from mcp_test_suite.engine import run_harness
    except Exception as exc:
        print(f"Cannot load mcp-test-harness engine bridge: {exc}", file=sys.stderr)
        print(_INSTALL_HINT, file=sys.stderr)
        return 1

    try:
        return asyncio.run(
            run_harness(
                config, list_only=bool(args.list), fail_fast=False, last_failed=False
            )
        )
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    finally:
        reset_runtime()
