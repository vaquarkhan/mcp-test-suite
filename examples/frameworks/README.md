# Framework examples (mcp-test-suite)

Copy-paste packs for popular MCP server stacks. Every pack shares the same idea:

1. Put contracts in `mcp-suite.yaml`
2. Launch the server with `--server-command`
3. Optionally use a native adapter (JUnit / Jest / Go / xUnit / pytest)

| Ecosystem | Path | Frameworks |
|-----------|------|------------|
| **Java** | [java/](java/) | Spring Boot, Spring AI, Quarkus, Micronaut |
| **Kotlin** | [kotlin/](kotlin/) | Spring Boot (Kotlin), Ktor |
| **TypeScript** | [typescript/](typescript/) | NestJS, Express, Fastify |
| **Python** | [python/](python/) | FastMCP, FastAPI |
| **Go** | [go/](go/) | stdlib MCP server |
| **.NET** | [dotnet/](dotnet/) | ASP.NET Minimal API / ModelContextProtocol |
| **Rust** | [rust/](rust/) | rmcp / tokio stdio server |

Run any pack:

```bash
mcp-test run --suite examples/frameworks/<lang>/<framework>/mcp-suite.yaml \
  --server-command "<see each README>"
```
