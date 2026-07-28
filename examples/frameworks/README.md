# Framework examples (mcp-test-suite)

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Java / Maven](https://github.com/vaquarkhan/mcp-test-suite/packages/3158511) ·
[Node / npm](https://github.com/users/vaquarkhan/packages/npm/package/mcp-test-suite-jest) ·
[Go module](https://pkg.go.dev/github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0) ·
[.NET / NuGet](https://github.com/users/vaquarkhan/packages/nuget/package/McpTestSuite.Xunit) ·
[Release assets](https://github.com/vaquarkhan/mcp-test-suite/releases/tag/v4.0.0) ·
[Install guide](../../docs/DOWNLOADS.md)

Copy-paste packs for popular MCP server stacks. Every pack shares the same idea:

1. Put contracts in `mcp-suite.yaml`
2. Launch the server with `--server-command` (or `server.command` in the YAML)
3. Optionally use a native adapter (JUnit / Jest / Go / xUnit / Python)

**Requires:** `pip install mcp-test-harness` + `pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"` (`mcp-suite` on PATH).

| Ecosystem | Path | Frameworks | Tutorials |
|-----------|------|------------|-----------|
| **Java** | [java/](java/) | Spring Boot, Spring AI, Quarkus, Micronaut | [spring-boot](../../docs/tutorials/spring-boot.md) · [spring-ai](../../docs/tutorials/spring-ai.md) · [quarkus](../../docs/tutorials/quarkus.md) · [micronaut](../../docs/tutorials/micronaut.md) |
| **Kotlin** | [kotlin/](kotlin/) | Spring Boot (Kotlin), Ktor | [kotlin](../../docs/tutorials/kotlin.md) · [kotlin-spring](../../docs/tutorials/kotlin-spring.md) · [ktor](../../docs/tutorials/ktor.md) |
| **TypeScript** | [typescript/](typescript/) | NestJS, Express, Fastify | [nestjs](../../docs/tutorials/nestjs.md) · [express](../../docs/tutorials/express.md) · [fastify](../../docs/tutorials/fastify.md) |
| **Python** | [python/](python/) | FastMCP, FastAPI | [fastmcp](../../docs/tutorials/fastmcp.md) · [fastapi](../../docs/tutorials/fastapi.md) |
| **Go** | [go/](go/) | stdlib MCP server | [go](../../docs/tutorials/go.md) |
| **.NET** | [dotnet/](dotnet/) | ASP.NET Minimal / MCP | [dotnet](../../docs/tutorials/dotnet.md) |
| **Rust** | [rust/](rust/) | release binary + integration test | [rust](../../docs/tutorials/rust.md) |

Full tutorial index: [docs/tutorials/README.md](../../docs/tutorials/README.md)

```bash
mcp-suite run --suite examples/frameworks/<lang>/<framework>/mcp-suite.yaml \
  --server-command "<see each README>"
```
