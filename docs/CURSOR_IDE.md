# Cursor IDE integration

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Java JAR](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/mcp-test-suite-junit5-4.0.0.jar) ·
[Node / npm tgz](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/vaquarkhan-mcp-test-suite-jest-4.0.0.tgz) ·
[Go module](https://pkg.go.dev/github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0) ·
[.NET nupkg](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/McpTestSuite.Xunit.4.0.0.nupkg) ·
[All release assets](https://github.com/vaquarkhan/mcp-test-suite/releases/tag/v4.0.0) ·
[All IDEs](IDE_INTEGRATION.md)

Cursor is an AI-first editor with native MCP support. Use **mcp-test-suite** connectors (engine from PyPI) so you and the agent validate tools while coding.

**Other IDEs:** Kiro, Google Antigravity, Gemini, ChatGPT, VS Code, Windsurf, JetBrains — see **[IDE_INTEGRATION.md](IDE_INTEGRATION.md)**.

### Prereq

```bash
pip install "mcp-test-harness>=3.0.9,<4"
pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"
```

### 1. Agent rules

See [`.cursorrules`](../.cursorrules):

1. Prefer `mcp-suite run --suite mcp-suite.yaml`
2. Probe new tools with `mcp-test try --server-command "…"` (engine CLI)
3. Keep contracts in `mcp-suite.yaml` for cross-language reuse
4. Green try/suite before adding the server to `.cursor/mcp.json`

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

```json
{
  "mcpServers": {
    "my-server": {
      "command": "node",
      "args": ["build/index.js"]
    }
  }
}
```

Tutorials: [tutorials/](tutorials/) · Multi-language: [MULTI_LANGUAGE.md](MULTI_LANGUAGE.md)
