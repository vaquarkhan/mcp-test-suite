"""Minimal stdio MCP server for Action / CI smoke (FastMCP)."""

from __future__ import annotations

import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.WARNING)

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp-test-suite-smoke")


@mcp.tool()
def echo(text: str) -> str:
    """Echo text back to the client."""
    return text


if __name__ == "__main__":
    mcp.run(transport="stdio")
