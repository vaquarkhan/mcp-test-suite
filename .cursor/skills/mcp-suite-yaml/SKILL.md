---
name: mcp-suite-yaml
description: >-
  Author and run declarative mcp-suite.yaml contracts for MCP servers. Use when
  creating suite YAML, adding cases, expect_error, latency budgets, or running
  mcp-suite run for any language.
---

# Declarative mcp-suite.yaml

## Minimal suite

```yaml
server:
  command: node dist/server.js
  transport: stdio
cases:
  - name: Echo works
    call: echo
    args: { text: hello }
  - name: Unknown tool fails
    call: __missing__
    args: {}
    expect_error: true
  - name: Latency budget
    call: echo
    args: { text: ping }
    max_latency_ms: 5000
```

## Run

```bash
mcp-suite run --suite mcp-suite.yaml
mcp-suite run --suite mcp-suite.yaml --list
mcp-suite run --suite mcp-suite.yaml --report-format html --report-output report.html
```

## Case fields

| Field | Purpose |
|-------|---------|
| `call` / `tool` | Tool name |
| `args` | Tool arguments object |
| `expected` | Optional expected payload |
| `expect_error` | Pass when tool/protocol errors |
| `max_latency_ms` | Fail if slower |
| `resource` / `prompt` | Alternative to tool call |

Tutorial: [docs/tutorials/yaml.md](../../docs/tutorials/yaml.md)
