# Language tutorials

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Java JAR](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/mcp-test-suite-junit5-4.0.0.jar) ·
[Node / npm tgz](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/vaquarkhan-mcp-test-suite-jest-4.0.0.tgz) ·
[Go module](https://pkg.go.dev/github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0) ·
[.NET nupkg](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/McpTestSuite.Xunit.4.0.0.nupkg) ·
[All release assets](https://github.com/vaquarkhan/mcp-test-suite/releases/tag/v4.0.0) ·
[Install guide](../DOWNLOADS.md)

Each tutorial uses the **same** `mcp-suite.yaml` contract and the **PyPI** engine (`mcp-test-harness`). This repo only adds connectors.

| Tutorial | Audience |
|----------|----------|
| [yaml.md](yaml.md) | Any language — declarative suites only |
| [python.md](python.md) | FastMCP / FastAPI / Python MCP servers |
| [typescript.md](typescript.md) | Nest / Express / Fastify / Node |
| [java.md](java.md) | Spring Boot / Quarkus / Micronaut / Kotlin |
| [go.md](go.md) | Go MCP servers |
| [dotnet.md](dotnet.md) | ASP.NET / .NET MCP |
| [rust.md](rust.md) | Rust MCP via CLI |

**Prereq (all tutorials):**

```bash
pip install "mcp-test-harness>=3.0.9"
pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"   # → mcp-suite
# or from a clone: pip install .
mcp-suite --version
```

Adapter downloads (Maven / npm / NuGet / Go / Release assets): [../DOWNLOADS.md](../DOWNLOADS.md)

Architecture overview: [../MULTI_LANGUAGE.md](../MULTI_LANGUAGE.md) · Examples: [../../examples/frameworks/](../../examples/frameworks/)
