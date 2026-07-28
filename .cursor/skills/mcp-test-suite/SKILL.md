---
name: mcp-test-suite
description: >-
  Test MCP servers with mcp-test-suite connectors and the mcp-test-harness
  engine. Use when adding MCP tools, writing mcp-suite.yaml, running mcp-suite
  / mcp-test try, wiring IDE MCP configs, or installing language adapters.
---

# MCP Test Suite skill

## Install (engine + connectors)

```bash
pip install "mcp-test-harness>=3.0.9"
pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"
mcp-test --version && mcp-suite --version
```

## Before changing MCP tools / resources / prompts

1. `mcp-test try --server-command "<command>"`
2. `mcp-suite run --suite mcp-suite.yaml`
3. Only then update IDE MCP config

## Contracts

- Prefer **`mcp-suite.yaml`** for cross-language tests.
- stdio servers: logs to **stderr only**.
- Complex flows: Python `test_*.py` + engine assertions.

## Package installs (v4.0.0)

| Language | Package page | Install |
|----------|--------------|---------|
| Python engine | [PyPI](https://pypi.org/project/mcp-test-harness/) | `pip install mcp-test-harness` |
| Java / Maven | [GitHub Packages](https://github.com/vaquarkhan/mcp-test-suite/packages/3158511) | `io.github.vaquarkhan:mcp-test-suite-junit5:4.0.0` |
| Node / npm | [GitHub Packages](https://github.com/users/vaquarkhan/packages/npm/package/mcp-test-suite-jest) | `npm i -D @vaquarkhan/mcp-test-suite-jest@4.0.0` |
| .NET / NuGet | [GitHub Packages](https://github.com/users/vaquarkhan/packages/nuget/package/McpTestSuite.Xunit) | `dotnet add package McpTestSuite.Xunit --version 4.0.0` |
| Go | [pkg.go.dev](https://pkg.go.dev/github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0) | `go get …/adapters/gotest@v4.0.0` |
| Release assets | [v4.0.0](https://github.com/vaquarkhan/mcp-test-suite/releases/tag/v4.0.0) | JAR / tgz / nupkg (no registry auth) |

GitHub Packages downloads need a PAT with `read:packages`. Release assets do not.

## Docs

- [docs/IDE_INTEGRATION.md](../../docs/IDE_INTEGRATION.md)
- [docs/DOWNLOADS.md](../../docs/DOWNLOADS.md)
- [docs/tutorials/](../../docs/tutorials/)
