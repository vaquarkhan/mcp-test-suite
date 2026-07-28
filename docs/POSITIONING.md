# Product positioning — mcp-test-suite

**mcp-test-suite** removes language friction around MCP testing:

- One **`mcp-suite.yaml`** shared by every stack
- Thin **native adapters** (Jest, JUnit 5, Go, xUnit) that shell out to `mcp-suite`
- **Docker + GitHub Action** with language auto-detect
- Engine power (schema, reports, chaos, conformance) via **PyPI `mcp-test-harness`** — not vendored here

## Not “pytest-style” as the product story

The engine may use pytest-like *discovery conventions* for Python `test_*.py` files.  
**This product’s story is multi-language connectors + declarative YAML.** Engine deep-dives belong in [mcp-test-harness](https://github.com/vaquarkhan/mcp-test-harness).

## Split of responsibility

| Layer | Owner |
|-------|--------|
| CI gate for MCP servers (core) | mcp-test-harness |
| Adoption for TS / Java / Go / .NET / Rust | mcp-test-suite |

See [MULTI_LANGUAGE.md](MULTI_LANGUAGE.md) and [ARCHITECTURE.md](ARCHITECTURE.md).
