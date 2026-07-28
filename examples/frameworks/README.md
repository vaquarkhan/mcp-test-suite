# Framework examples (mcp-test-suite)

Copy-paste packs for popular MCP server stacks. Every pack shares the same idea:

1. Put contracts in `mcp-suite.yaml`
2. Launch the server with `--server-command` (or `server.command` in the YAML)
3. Optionally use a native adapter (JUnit / Jest / Go / xUnit / Python)

**Requires:** `pip install mcp-test-harness` + `pip install` this suite (`mcp-suite` on PATH).

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
