# Developer notes (mcp-test-suite)

> **Connectors repo.** Engine internals and the large engine self-test suite live in
> [mcp-test-harness](https://github.com/vaquarkhan/mcp-test-harness).

## Run connector tests

```bash
pip install "mcp-test-harness>=3.0.9"
pip install -e ".[dev]"
python -m pytest tests/ -q
# includes tests/e2e/ (real mcp-suite → MCP fixture)
```

## Layout

| Path | Purpose |
|------|---------|
| `src/mcp_test_suite/` | Declarative YAML + `mcp-suite` CLI + harness plugin |
| `adapters/` | Jest, JUnit5, Go, xUnit |
| `examples/frameworks/` | Per-language packs |
| `docs/tutorials/` | Language tutorials |
| `tests/e2e/` | Fail-early connector smoke |

## Engine docs

For discovery, scheduler, assertions, and “pytest-style” runner conventions, see the harness repo — those APIs come from the **PyPI** package, not from source in this tree.
