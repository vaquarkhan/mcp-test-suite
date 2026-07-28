# mcp-test-suite-junit5

JUnit 5 adapter for **mcp-test-suite** (Spring Boot, Spring AI, Quarkus, Micronaut, Kotlin).

## Download (Maven Central)

```xml
<dependency>
  <groupId>io.github.vaquarkhan</groupId>
  <artifactId>mcp-test-suite-junit5</artifactId>
  <version>4.0.0</version>
  <scope>test</scope>
</dependency>
```

**Gradle (Kotlin):**

```kotlin
testImplementation("io.github.vaquarkhan:mcp-test-suite-junit5:4.0.0")
```

| Registry | Link |
|----------|------|
| Maven Central | https://central.sonatype.com/artifact/io.github.vaquarkhan/mcp-test-suite-junit5 |
| MVN Repository | https://mvnrepository.com/artifact/io.github.vaquarkhan/mcp-test-suite-junit5 |

Also install the engine: `pip install mcp-test-suite` **or** use Docker / the release binary (`mcp-test` on `PATH`).

## Usage

```java
@MCPTest(serverCommand = "java -jar target/spring-ai-server.jar")
public class WeatherToolTest {
    @Test
    public void suitePasses(MCPConnection mcp) {
        assertTrue(mcp.runSuite().passed());
    }
}
```

Examples: [examples/frameworks/java](../../examples/frameworks/java/) · Downloads hub: [docs/DOWNLOADS.md](../../docs/DOWNLOADS.md)
