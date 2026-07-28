"""Minimal stdio MCP server for Action / CI smoke (stdlib only).

Uses **newline-delimited JSON** (one JSON-RPC object per line) to match
``mcp-test-harness`` / ``mcp.client.stdio`` framing — not Content-Length LSP style.
"""

from __future__ import annotations

import json
import logging
import sys
from typing import Any

logging.basicConfig(stream=sys.stderr, level=logging.WARNING)
log = logging.getLogger("minimal-mcp")

PROTOCOL_VERSION = "2024-11-05"

ECHO_TOOL = {
    "name": "echo",
    "description": "Echo text back to the client.",
    "inputSchema": {
        "type": "object",
        "properties": {"text": {"type": "string"}},
        "required": ["text"],
    },
}


def _write(payload: dict[str, Any]) -> None:
    sys.stdout.write(json.dumps(payload, separators=(",", ":")) + "\n")
    sys.stdout.flush()


def _result(req_id: Any, result: Any) -> dict[str, Any]:
    return {"jsonrpc": "2.0", "id": req_id, "result": result}


def _error(req_id: Any, code: int, message: str) -> dict[str, Any]:
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": code, "message": message}}


def _handle(msg: dict[str, Any]) -> dict[str, Any] | None:
    method = msg.get("method")
    req_id = msg.get("id")
    params = msg.get("params") or {}

    if req_id is None:
        return None

    if method == "initialize":
        return _result(
            req_id,
            {
                "protocolVersion": PROTOCOL_VERSION,
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "mcp-test-suite-smoke", "version": "1.0.0"},
            },
        )

    if method == "ping":
        return _result(req_id, {})

    if method == "tools/list":
        return _result(req_id, {"tools": [ECHO_TOOL]})

    if method == "tools/call":
        name = params.get("name")
        arguments = params.get("arguments") or {}
        if name != "echo":
            return _error(req_id, -32601, f"Unknown tool: {name}")
        text = arguments.get("text", "")
        return _result(
            req_id,
            {"content": [{"type": "text", "text": str(text)}], "isError": False},
        )

    return _error(req_id, -32601, f"Method not found: {method}")


def main() -> None:
    for raw in sys.stdin:
        line = raw.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError as exc:
            log.warning("bad json: %s", exc)
            continue
        try:
            reply = _handle(msg)
        except Exception as exc:  # noqa: BLE001
            log.exception("handle failed")
            if "id" in msg:
                reply = _error(msg["id"], -32603, str(exc))
            else:
                reply = None
        if reply is not None:
            _write(reply)


if __name__ == "__main__":
    main()
