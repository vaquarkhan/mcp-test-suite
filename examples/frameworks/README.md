# Framework examples (mcp-test-suite)

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Java JAR](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/mcp-test-suite-junit5-4.0.0.jar) ·
[Node / npm tgz](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/vaquarkhan-mcp-test-suite-jest-4.0.0.tgz) ·
[Go module](https://pkg.go.dev/github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0) ·
[.NET nupkg](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/McpTestSuite.Xunit.4.0.0.nupkg) ·
[All release assets](https://github.com/vaquarkhan/mcp-test-suite/releases/tag/v4.0.0) ·
[Install guide](../../docs/DOWNLOADS.md)

Copy-paste packs for popular MCP server stacks. Every pack shares the same idea:

1. Put contracts in `mcp-suite.yaml`
2. Launch the server with `--server-command` (or `server.command` in the YAML)
3. Optionally use a native adapter (JUnit / Jest / Go / xUnit / Python)

**Requires:** `pip install mcp-test-harness` + `pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"` (`mcp-suite` on PATH).

| Ecosystem | Path | Frameworks | Tutorial |
|-----------|------|------------|----------|
| **Java** | [java/](java/) | Spring Boot, Spring AI, Quarkus, Micronaut | [docs/tutorials/java.md](../../docs/tutorials/java.md) |
| **Kotlin** | [kotlin/](kotlin/) | Spring Boot (Kotlin), Ktor | [docs/tutorials/java.md](../../docs/tutorials/java.md) |
| **TypeScript** | [typescript/](typescript/) | NestJS, Express, Fastify | [docs/tutorials/typescript.md](../../docs/tutorials/typescript.md) |
| **Python** | [python/](python/) | FastMCP, FastAPI | [docs/tutorials/python.md](../../docs/tutorials/python.md) |
| **Go** | [go/](go/) | stdlib MCP server | [docs/tutorials/go.md](../../docs/tutorials/go.md) |
| **.NET** | [dotnet/](dotnet/) | ASP.NET Minimal / MCP | [docs/tutorials/dotnet.md](../../docs/tutorials/dotnet.md) |
| **Rust** | [rust/](rust/) | release binary + integration test | [docs/tutorials/rust.md](../../docs/tutorials/rust.md) |

Run any pack’s **suite file** (after pointing `server.command` at your binary):

```bash
mcp-suite run --suite examples/frameworks/<lang>/<framework>/mcp-suite.yaml \
  --server-command "<see each README>"
```

CI also loads every `mcp-suite.yaml` under this tree in `tests/e2e/` so broken suite files fail early.
