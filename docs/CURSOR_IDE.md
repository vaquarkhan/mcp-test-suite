## Cursor IDE Integration

Cursor is an AI-first code editor with native MCP support. Use **mcp-test-suite** connectors (engine from PyPI) so you and the agent validate tools while coding.

### Prereq

```bash
pip install "mcp-test-harness>=3.0.9"
pip install .   # installs mcp-suite
```

### 1. Agent rules

See [`.cursorrules`](../.cursorrules) and [`.cursor/rules/mcp-testing.mdc`](../.cursor/rules/mcp-testing.mdc):

1. Prefer `mcp-suite run --suite mcp-suite.yaml`
2. Probe new tools with `mcp-test try --server-command "…"` (engine CLI)
3. Keep contracts in `mcp-suite.yaml` for cross-language reuse

### 2. Tasks (`.vscode/tasks.json`)

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "MCP: Run declarative suite",
      "type": "shell",
      "command": "mcp-suite run --suite mcp-suite.yaml",
      "group": { "kind": "test", "isDefault": true }
    },
    {
      "label": "MCP: Zero-config probe",
      "type": "shell",
      "command": "mcp-test try --server-command \"python src/server.py\"",
      "group": "test"
    }
  ]
}
```

### 3. Before `.cursor/mcp.json`

```bash
mcp-test try --server-command "node build/index.js"
mcp-suite run --suite mcp-suite.yaml --server-command "node build/index.js"
```

Tutorials: [tutorials/](tutorials/) · Multi-language: [MULTI_LANGUAGE.md](MULTI_LANGUAGE.md)
