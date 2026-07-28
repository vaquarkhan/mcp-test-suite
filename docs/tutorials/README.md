# Language & framework tutorials

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Java / Maven](https://github.com/vaquarkhan/mcp-test-suite/packages/3158511) ·
[Node / npm](https://github.com/users/vaquarkhan/packages/npm/package/mcp-test-suite-jest) ·
[Go module](https://pkg.go.dev/github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0) ·
[.NET / NuGet](https://github.com/users/vaquarkhan/packages/nuget/package/McpTestSuite.Xunit) ·
[Release assets](https://github.com/vaquarkhan/mcp-test-suite/releases/tag/v4.0.0) ·
[Install guide](../DOWNLOADS.md)

Each tutorial uses the same **`mcp-suite.yaml`** contract and the PyPI engine (`mcp-test-harness`). This repo adds connectors only.

## Prereq (all tutorials)

```bash
pip install "mcp-test-harness>=3.0.9"
pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"
mcp-suite --version
```

## Any language

| Tutorial | Audience |
|----------|----------|
| [yaml.md](yaml.md) | Declarative suites only (CLI / CI) |

## Python

| Tutorial | Stack |
|----------|-------|
| [python.md](python.md) | Overview — YAML + engine API |
| [fastmcp.md](fastmcp.md) | FastMCP stdio servers |
| [fastapi.md](fastapi.md) | FastAPI + MCP |

## TypeScript / Node

| Tutorial | Stack |
|----------|-------|
| [typescript.md](typescript.md) | Overview — Jest adapter |
| [nestjs.md](nestjs.md) | NestJS |
| [express.md](express.md) | Express |
| [fastify.md](fastify.md) | Fastify |

## Java

| Tutorial | Stack |
|----------|-------|
| [java.md](java.md) | Overview — JUnit 5 adapter |
| [spring-boot.md](spring-boot.md) | Spring Boot MCP |
| [spring-ai.md](spring-ai.md) | Spring AI `@Tool` MCP |
| [quarkus.md](quarkus.md) | Quarkus |
| [micronaut.md](micronaut.md) | Micronaut |

## Kotlin

| Tutorial | Stack |
|----------|-------|
| [kotlin.md](kotlin.md) | Overview — JUnit 5 (Kotlin) |
| [kotlin-spring.md](kotlin-spring.md) | Spring Boot (Kotlin) |
| [ktor.md](ktor.md) | Ktor |

## Other languages

| Tutorial | Stack |
|----------|-------|
| [go.md](go.md) | Go module adapter |
| [dotnet.md](dotnet.md) | ASP.NET / xUnit |
| [rust.md](rust.md) | Rust via CLI |

Examples: [../../examples/frameworks/](../../examples/frameworks/) · Architecture: [../MULTI_LANGUAGE.md](../MULTI_LANGUAGE.md) · IDEs: [../IDE_INTEGRATION.md](../IDE_INTEGRATION.md)
