# Declarative MCP suites

Language-agnostic tests for **mcp-test-suite**. One YAML file works for Go, Java, TypeScript, and Python teams.

## Quick start

```bash
# From repo root (after pip install -e .)
mcp-test run --suite examples/declarative/mcp-suite.yaml \
  --server-command "python tests/fixtures/minimal_mcp_server.py"
```

Or place `mcp-suite.yaml` in your project root and run:

```bash
mcp-test run
```

## Case schema

| Field | Description |
|-------|-------------|
| `name` | Human-readable case title |
| `call` / `tool` | Tool name to invoke |
| `args` / `arguments` | Tool arguments object |
| `expected` | Optional expected content (same as `assert_tool_call`) |
| `assert_schema` | Named schema under `schemas:` (JSON Schema) |
| `max_latency_ms` | Fail if call exceeds this latency |
| `validate_input_schema` | Validate args against the tool's `inputSchema` |
| `expect_error` | Assert the call fails (`true`, a substring, or `{code, message_matches}`) |
| `error_matches` | Substring that must appear in the error message |
| `resource` | Read a resource URI instead of calling a tool |
| `prompt` | Get a prompt instead of calling a tool |
| `tags` | Filter with `mcp-test run -m smoke` |
| `timeout` | Per-case timeout (seconds) |

## Trust / safety

`server.command` (and CLI `--server-command`) launches a real process. Only run suite files you trust — especially in CI Actions that accept a suite path from the workflow.

## Why declarative?

Python `test_*.py` remains first-class for complex multi-step flows. Declarative suites remove the Python runtime requirement for teams that only need contract / schema / latency gates — and they are the shared contract that native adapters (Jest, JUnit 5, Go testing) orchestrate.
