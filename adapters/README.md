# Language adapters

Native wrappers around the **mcp-test-harness** engine. Each adapter shells out to `mcp-suite` for shared YAML contracts.

**Install:** [docs/DOWNLOADS.md](../docs/DOWNLOADS.md) · **Release:** [v4.0.0](https://github.com/vaquarkhan/mcp-test-suite/releases/tag/v4.0.0)

| Adapter | Registry | Install |
|---------|----------|---------|
| [junit5/](junit5/) | GitHub Packages (Maven) | `io.github.vaquarkhan:mcp-test-suite-junit5:4.0.0` |
| [jest/](jest/) | GitHub Packages (npm) | `npm i -D @vaquarkhan/mcp-test-suite-jest` |
| [gotest/](gotest/) | Go module | `go get github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0` |
| [xunit/](xunit/) | GitHub Packages (NuGet) | `dotnet add package McpTestSuite.Xunit --version 4.0.0` |
| Python engine | PyPI | `pip install mcp-test-harness` |
| Connectors | git / pip | `pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"` |
| Docker | local build | `docker build -t mcp-test-suite:local .` |

Framework examples: [examples/frameworks/](../examples/frameworks/)
