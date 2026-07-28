# Language adapters

Thin native wrappers around the **mcp-test** engine. They do **not** reimplement MCP protocol logic.

**Install from public registries:** see **[docs/DOWNLOADS.md](../docs/DOWNLOADS.md)**.

| Adapter | Registry | Install |
|---------|----------|---------|
| [junit5/](junit5/) | **Maven Central** | `io.github.vaquarkhan:mcp-test-suite-junit5:4.0.0` |
| [jest/](jest/) | **npm** | `npm i -D @vaquarkhan/mcp-test-suite-jest` |
| [gotest/](gotest/) | **Go modules** | `go get github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0` |
| [xunit/](xunit/) | **NuGet** | `dotnet add package McpTestSuite.Xunit --version 4.0.0` |
| Python engine | **PyPI** (via **mcp-test-harness** repo only) | `pip install mcp-test-harness` |
| Universal | **Docker / GHCR** | `docker build -t mcp-test-suite:local .` now; later `docker pull ghcr.io/vaquarkhan/mcp-test-suite:latest` |

Framework packs: **[examples/frameworks/](../examples/frameworks/)**. Publish: **[docs/PUBLISHING.md](../docs/PUBLISHING.md)**.
