# AGENTS.md

Guidance for AI coding agents (Cursor, Kiro, Codex, Copilot, Windsurf, Gemini, ChatGPT connectors, etc.) working in MCP server repos that use **mcp-test-suite**.

## Install

```bash
pip install "mcp-test-harness>=3.0.9,<4"
pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"
```

## Before changing MCP tools

1. `mcp-test try --server-command "<your server command>"`
2. `mcp-suite run --suite mcp-suite.yaml`
3. Only then update IDE MCP config (`.cursor/mcp.json`, Kiro MCP panel, Codex `config.toml`, ChatGPT connectors, etc.)

## Conventions

- Shared contracts → **`mcp-suite.yaml`** (works for every language adapter).
- stdio servers: **logs to stderr only** (stdout is JSON-RPC).
- Complex flows only → Python `test_*.py` with `mcp-test-harness` assertions.
- CI should run the same suite (GitHub Action or Jest/JUnit/Go/xUnit adapter).

## Docs

- [docs/IDE_INTEGRATION.md](docs/IDE_INTEGRATION.md) — Cursor, Kiro, Google, ChatGPT, VS Code, Windsurf, JetBrains, …
- [docs/DOWNLOADS.md](docs/DOWNLOADS.md) — package install links
- [docs/tutorials/](docs/tutorials/) — per-language walkthroughs
