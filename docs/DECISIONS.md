# Design decisions (mcp-test-suite)

## 1. Engine stays on PyPI (not vendored)

**Decision:** Depend on `mcp-test-harness` from PyPI. Do not copy engine source into this repo.

**Why:** One place to maintain transports, assertions, and reports. Suite upgrades by bumping/installing the package.

## 2. Declarative YAML is the cross-language contract

**Decision:** `mcp-suite.yaml` is the shared surface for Node, Java, Go, .NET, Rust, and Python.

**Why:** Teams share one contract file; adapters only orchestrate the CLI.

## 3. Thin adapters, not protocol reimplementation

**Decision:** Jest / JUnit / Go / xUnit shell out to `mcp-suite` / the engine.

**Why:** Avoid forked MCP client stacks per language.

## 4. Product story is multi-language, not “pytest-style”

**Decision:** Marketing and README emphasize connectors + YAML. Engine discovery conventions for Python `test_*.py` are documented in the harness repo.

See also [ARCHITECTURE.md](ARCHITECTURE.md) and [NO_PYPI_FROM_THIS_REPO.md](NO_PYPI_FROM_THIS_REPO.md).
