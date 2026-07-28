# Tutorial: Java (overview)

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Java / Maven](https://github.com/vaquarkhan/mcp-test-suite/packages/3158511) ·
[Install guide](../DOWNLOADS.md)

Use **JUnit 5** + `mcp-suite.yaml` to test Java MCP servers. Shared engine reports (HTML / JUnit / SARIF) work without Python tests.

## Framework tutorials

| Stack | Tutorial |
|-------|----------|
| Spring Boot | [spring-boot.md](spring-boot.md) |
| Spring AI | [spring-ai.md](spring-ai.md) |
| Quarkus | [quarkus.md](quarkus.md) |
| Micronaut | [micronaut.md](micronaut.md) |
| Kotlin | [kotlin.md](kotlin.md) |

## Install

```bash
pip install "mcp-test-harness>=3.0.9,<4"
pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"
```

The JUnit adapter shells out to `mcp-suite` — Python + the engine must be on `PATH` (or set `@MCPTest(binary = "...")`).

Maven: `io.github.vaquarkhan:mcp-test-suite-junit5:4.0.0` — [package page](https://github.com/vaquarkhan/mcp-test-suite/packages/3158511)

## Minimal JUnit

```java
@MCPTest(
    serverCommand = "java -jar target/server.jar",
    suite = "mcp-suite.yaml",
    binary = "mcp-suite"
)
class McpIT {
    @Test
    void suite(MCPConnection mcp) {
        mcp.runSuite().assertPassed();
    }
}
```

CLI:

```bash
mcp-suite run --suite mcp-suite.yaml --server-command "java -jar target/server.jar"
```

Examples: [examples/frameworks/java/](../../examples/frameworks/java/)
