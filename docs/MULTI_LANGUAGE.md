# Multi-language adoption (mcp-test-suite)

**mcp-test-suite** is the multi-language evolution of [mcp-test-harness](https://github.com/vaquarkhan/mcp-test-harness). The Python engine stays the single source of truth (chaos, schema, JUnit/SARIF, conformance). Non-Python teams never need to write `test_*.py`.

## Architecture

```
┌──────────────────────────────────────────────────────────────────────┐
│  Native adapters                                                       │
│  Jest │ JUnit5 │ Go │ xUnit │ Python API │ (Rust via CLI)              │
└────────────────────────────┬───────────────────────────────────────────┘
                             ▼
                      mcp-suite.yaml  (shared contracts)
                             ▼
              mcp-test CLI / binary / GHCR Docker
                             ▼
     MCP server (Spring, Nest, FastAPI, .NET, Rust, Go, …)
```

## Paths to adoption

| Audience | How to test |
|----------|-------------|
| Any language | `mcp-suite.yaml` + `mcp-test run` or Docker |
| Node / Nest / Express / Fastify | `@mcp-test-suite/jest` |
| Java / Spring Boot / Spring AI / Quarkus / Micronaut | `mcp-test-suite-junit5` |
| Kotlin Spring / Ktor | Same JUnit 5 adapter |
| Go | `…/gotest` |
| .NET / ASP.NET | `adapters/xunit` |
| Python / FastMCP / FastAPI | `test_*.py` and/or YAML |
| Rust | YAML + `cargo test` shelling to `mcp-test` |
| CI | Universal GitHub Action (auto-detects language) |

## Framework example packs

See **[examples/frameworks/](../examples/frameworks/)** for copy-paste suites and native tests:

| Language | Frameworks covered |
|----------|--------------------|
| Java | Spring Boot, Spring AI, Quarkus, Micronaut |
| Kotlin | Spring Boot, Ktor |
| TypeScript | NestJS, Express, Fastify |
| Python | FastMCP, FastAPI (HTTP) |
| Go | stdlib / `go run` server |
| .NET | ASP.NET Minimal / MCP server |
| Rust | release binary + integration test |

## Standalone binary & Docker

```bash
docker run --rm -v "$PWD":/work -w /work \
  ghcr.io/vaquarkhan/mcp-test-suite:latest \
  run --suite mcp-suite.yaml --server-command "node build/index.js"

./dist/mcp-test run --suite mcp-suite.yaml
```

## Cursor IDE

See [CURSOR_IDE.md](CURSOR_IDE.md) for agent rules, tasks, and `mcp-test try` before `.cursor/mcp.json`.
