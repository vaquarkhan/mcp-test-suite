# Tutorial: Kotlin (JUnit 5)

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Java / Maven](https://github.com/vaquarkhan/mcp-test-suite/packages/3158511) ·
[Install guide](../DOWNLOADS.md)

Kotlin MCP servers use the same **JUnit 5** adapter as Java (`mcp-test-suite-junit5`).

## Framework tutorials

| Stack | Tutorial | Example |
|-------|----------|---------|
| Spring Boot (Kotlin) | [kotlin-spring.md](kotlin-spring.md) | [examples/frameworks/kotlin/spring-boot/](../../examples/frameworks/kotlin/spring-boot/) |
| Ktor | [ktor.md](ktor.md) | [examples/frameworks/kotlin/ktor/](../../examples/frameworks/kotlin/ktor/) |

## Install

```bash
pip install "mcp-test-harness>=3.0.9,<4"
pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"
```

Maven / Gradle test dependency: `io.github.vaquarkhan:mcp-test-suite-junit5:4.0.0` — [package page](https://github.com/vaquarkhan/mcp-test-suite/packages/3158511)

## Kotlin JUnit sketch

```kotlin
@MCPTest(
    serverCommand = "java -jar build/libs/server.jar",
    suite = "mcp-suite.yaml",
    binary = "mcp-suite"
)
class McpIT {
    @Test
    fun suite(mcp: MCPConnection) {
        mcp.runSuite().assertPassed()
    }
}
```

Or CLI-only:

```bash
mcp-suite run --suite mcp-suite.yaml --server-command "java -jar build/libs/server.jar"
```

## Related

- [java.md](java.md) · [yaml.md](yaml.md)
- Packs: [examples/frameworks/kotlin/](../../examples/frameworks/kotlin/)
