"""CLI for ``mcp-test run`` — execute declarative YAML/JSON suites."""

from __future__ import annotations

import argparse
import asyncio
import sys
from pathlib import Path

from dataclasses import replace

from mcp_test_harness.config import load_config
from mcp_test_harness.declarative import discover_suite_files, load_suite_file


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="mcp-test run",
        description=(
            "Run language-agnostic declarative MCP tests from YAML/JSON "
            "(mcp-suite.yaml). Same engine as Python test_*.py suites."
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
    """Entry point for ``mcp-test run``."""
    args = _build_parser().parse_args(argv)

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

    # Prefer server settings from the suite file when present.
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

    # Build a Namespace compatible with load_config / _async_main path.
    # Keep config test.dirs; suite directories are appended below so discovery finds YAML.
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

    # Ensure discovery looks at the suite directory.
    dirs = list(config.test_dirs)
    for sp in suite_paths:
        parent = str(sp.parent)
        if parent not in dirs:
            dirs.append(parent)
    config = replace(config, test_dirs=dirs)

    from mcp_test_harness.cli import _run_harness

    return asyncio.run(
        _run_harness(config, list_only=bool(args.list), fail_fast=False, last_failed=False)
    )
