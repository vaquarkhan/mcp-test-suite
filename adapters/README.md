# Language adapters

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Java JAR](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/mcp-test-suite-junit5-4.0.0.jar) ·
[Node / npm tgz](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/vaquarkhan-mcp-test-suite-jest-4.0.0.tgz) ·
[Go module](https://pkg.go.dev/github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0) ·
[.NET nupkg](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/McpTestSuite.Xunit.4.0.0.nupkg) ·
[All release assets](https://github.com/vaquarkhan/mcp-test-suite/releases/tag/v4.0.0) ·
[Install guide](../docs/DOWNLOADS.md)

Native wrappers around the **mcp-test-harness** engine. Each adapter shells out to `mcp-suite` for shared YAML contracts.

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
