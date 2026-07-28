"""Minimal stdio MCP server for Action / CI smoke (stdlib only — no FastMCP).

Speaks MCP over stdin/stdout with Content-Length framing so e2e works with
mcp SDK 1.x or 2.x (FastMCP was removed from ``mcp.server`` in 2.0).
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


def _read_message() -> dict[str, Any] | None:
    headers: dict[str, str] = {}
    while True:
        line = sys.stdin.buffer.readline()
        if not line:
            return None
        if line in (b"\r\n", b"\n"):
            break
        decoded = line.decode("utf-8", errors="replace").rstrip("\r\n")
        if ":" not in decoded:
            continue
        key, value = decoded.split(":", 1)
        headers[key.strip().lower()] = value.strip()
    length = int(headers.get("content-length", "0") or "0")
    if length <= 0:
        return None
    body = sys.stdin.buffer.read(length)
    if not body:
        return None
    return json.loads(body.decode("utf-8"))


def _write_message(payload: dict[str, Any]) -> None:
    data = json.dumps(payload, separators=(",", ":")).encode("utf-8")
    sys.stdout.buffer.write(f"Content-Length: {len(data)}\r\n\r\n".encode("ascii"))
    sys.stdout.buffer.write(data)
    sys.stdout.buffer.flush()


def _result(req_id: Any, result: Any) -> dict[str, Any]:
    return {"jsonrpc": "2.0", "id": req_id, "result": result}


def _error(req_id: Any, code: int, message: str) -> dict[str, Any]:
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": code, "message": message}}


def _handle(msg: dict[str, Any]) -> dict[str, Any] | None:
    method = msg.get("method")
    req_id = msg.get("id")
    params = msg.get("params") or {}

    # Notifications (no id) — acknowledge by ignoring.
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
    while True:
        try:
            msg = _read_message()
        except Exception as exc:  # noqa: BLE001 — keep server alive for bad frames
            log.warning("read failed: %s", exc)
            continue
        if msg is None:
            break
        try:
            reply = _handle(msg)
        except Exception as exc:  # noqa: BLE001
            log.exception("handle failed")
            if "id" in msg:
                reply = _error(msg["id"], -32603, str(exc))
            else:
                reply = None
        if reply is not None:
            _write_message(reply)


if __name__ == "__main__":
    main()
