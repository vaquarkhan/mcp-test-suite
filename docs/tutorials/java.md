# Tutorial: Java / Kotlin (JUnit 5)

## Install engine + suite

```bash
pip install "mcp-test-harness>=3.0.9"
pip install .
```

## Install JUnit adapter into local Maven

```bash
cd adapters/junit5
mvn -q clean install
```

## Dependency

```xml
<dependency>
  <groupId>io.github.vaquarkhan</groupId>
  <artifactId>mcp-test-suite-junit5</artifactId>
  <version>4.0.0</version>
  <scope>test</scope>
</dependency>
```

(Until Central publish, use the local `mvn install` artifact.)

## Test

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

Kotlin Spring / Ktor packs: [examples/frameworks/kotlin/](../../examples/frameworks/kotlin/)  
Java packs: [examples/frameworks/java/](../../examples/frameworks/java/)
