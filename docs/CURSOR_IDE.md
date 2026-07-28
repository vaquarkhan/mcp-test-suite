## Cursor IDE Integration

Cursor is an AI-first code editor with native support for Model Context Protocol (MCP). Integrate **mcp-test-suite** so you and the Cursor agent can validate MCP tool schemas and implementations while coding.

### 1. Auto-validate via Cursor Agent Rules

Create `.cursor/rules/mcp-testing.mdc` (or `.cursorrules`) in your project root:

```yaml
---
description: Rules for modifying and testing MCP servers
globs: ["src/**/*.ts", "src/**/*.py", "src/**/*.java", "src/**/*.go", "mcp-suite.yaml", "mcp-test.yaml"]
---

# MCP Server Testing Guidelines

When adding or modifying MCP tools, resources, or prompts:
1. Always run the test suite before finalizing code changes:
   `mcp-test --config mcp-test.yaml` or `mcp-test run --suite mcp-suite.yaml`
2. If creating a new tool or handler, perform a zero-config probe:
   `mcp-test try --server-command "<your-server-command>"`
3. Prefer declarative cases in `mcp-suite.yaml` for cross-language contract checks.
4. Verify schema assertions and latency thresholds pass without warnings.
```

### 2. One-click Build & Test Tasks

Create `.vscode/tasks.json` so developers can trigger tests with **Ctrl+Shift+B** / **Cmd+Shift+B**:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "MCP: Run Test Suite",
      "type": "shell",
      "command": "mcp-test run --suite mcp-suite.yaml",
      "group": { "kind": "test", "isDefault": true },
      "presentation": { "echo": true, "reveal": "always", "focus": false, "panel": "shared" },
      "problemMatcher": []
    },
    {
      "label": "MCP: Zero-Config Probe (mcp-test try)",
      "type": "shell",
      "command": "mcp-test try --server-command \"python src/server.py\"",
      "group": "test",
      "presentation": { "echo": true, "reveal": "always" }
    }
  ]
}
```

### 3. Debug local servers before `.cursor/mcp.json`

Before connecting your MCP server to Cursor (Settings → Features → MCP or `.cursor/mcp.json`), run `mcp-test try` to verify stdio and transport sanity:

```bash
# 1. Probe the server for stdio cleanliness and protocol compliance
mcp-test try --server-command "node build/index.js"

# 2. Once passed, add to .cursor/mcp.json:
```

```json
{
  "mcpServers": {
    "my-local-server": {
      "command": "node",
      "args": ["build/index.js"]
    }
  }
}
```

> **Tip:** Running `mcp-test try` before adding your server to Cursor prevents silent stdio pollution crashes (for example `console.log` breaking JSON-RPC framing) inside Cursor IDE.

### 4. Launch configurations

See [`.vscode/launch.json`](../.vscode/launch.json) for debugging an MCP server process under Cursor / VS Code.
