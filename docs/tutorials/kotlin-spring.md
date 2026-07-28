# Tutorial: Spring Boot (Kotlin)

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Java / Maven](https://github.com/vaquarkhan/mcp-test-suite/packages/3158511) ·
[Install guide](../DOWNLOADS.md)

Test a **Kotlin Spring Boot** MCP server with `mcp-suite.yaml` and JUnit 5.

Example pack: [examples/frameworks/kotlin/spring-boot/](../../examples/frameworks/kotlin/spring-boot/)

## 1. Install

```bash
pip install "mcp-test-harness>=3.0.9"
pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"
```

Add `io.github.vaquarkhan:mcp-test-suite-junit5:4.0.0` — [Maven package](https://github.com/vaquarkhan/mcp-test-suite/packages/3158511)

## 2. Suite

```yaml
server:
  command: java -jar build/libs/mcp-server-0.0.1-SNAPSHOT.jar
  transport: stdio
cases:
  - name: Echo
    call: echo
    args: { text: hello-kotlin-spring }
    tags: [smoke, kotlin, spring-boot]
```

## 3. Run

```bash
./gradlew bootJar   # or ./mvnw -DskipTests package
mcp-suite run --suite mcp-suite.yaml \
  --server-command "java -jar build/libs/mcp-server-0.0.1-SNAPSHOT.jar"
```

Kotlin test:

```kotlin
@MCPTest(
    serverCommand = "java -jar build/libs/mcp-server-0.0.1-SNAPSHOT.jar",
    suite = "mcp-suite.yaml"
)
class KotlinSpringMcpIT {
    @Test
    fun suite(mcp: MCPConnection) {
        mcp.runSuite().assertPassed()
    }
}
```

## Notes

- Same stdio / stderr logging rules as Java Spring Boot ([spring-boot.md](spring-boot.md)).
- Prefer packaged jar in CI over `bootRun` for stable process lifecycle.

## Related

- [kotlin.md](kotlin.md) · [spring-boot.md](spring-boot.md) · [ktor.md](ktor.md)
