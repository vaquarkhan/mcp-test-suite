# mcp-test-suite-junit5

JUnit 5 adapter for **mcp-test-suite** (Spring Boot, Spring AI, Quarkus, Micronaut, Kotlin).

## Install (GitHub Packages)

Add to `~/.m2/settings.xml` (PAT with `read:packages`):

```xml
<server>
  <id>github</id>
  <username>YOUR_GITHUB_USERNAME</username>
  <password>YOUR_GITHUB_PAT</password>
</server>
```

```xml
<repositories>
  <repository>
    <id>github</id>
    <url>https://maven.pkg.github.com/vaquarkhan/mcp-test-suite</url>
  </repository>
</repositories>
<dependency>
  <groupId>io.github.vaquarkhan</groupId>
  <artifactId>mcp-test-suite-junit5</artifactId>
  <version>4.0.0</version>
  <scope>test</scope>
</dependency>
```

**Gradle:**

```kotlin
testImplementation("io.github.vaquarkhan:mcp-test-suite-junit5:4.0.0")
```

Or download `mcp-test-suite-junit5-4.0.0.jar` from [Releases](https://github.com/vaquarkhan/mcp-test-suite/releases/tag/v4.0.0).

Engine: `pip install mcp-test-harness` + `mcp-suite` on PATH ([DOWNLOADS.md](../../docs/DOWNLOADS.md)).

## Usage

```java
@MCPTest(serverCommand = "java -jar target/spring-ai-server.jar", suite = "mcp-suite.yaml")
public class WeatherToolTest {
    @Test
    public void suitePasses(MCPConnection mcp) {
        assertTrue(mcp.runSuite().passed());
    }
}
```

Examples: [examples/frameworks/java](../../examples/frameworks/java/)
