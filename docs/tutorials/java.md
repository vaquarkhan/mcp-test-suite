# Tutorial: Java / Kotlin (JUnit 5)

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Java JAR](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/mcp-test-suite-junit5-4.0.0.jar) ·
[Node / npm tgz](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/vaquarkhan-mcp-test-suite-jest-4.0.0.tgz) ·
[Go module](https://pkg.go.dev/github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0) ·
[.NET nupkg](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/McpTestSuite.Xunit.4.0.0.nupkg) ·
[All release assets](https://github.com/vaquarkhan/mcp-test-suite/releases/tag/v4.0.0) ·
[Install guide](../DOWNLOADS.md)

## Install engine + suite

```bash
pip install "mcp-test-harness>=3.0.9"
pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"
# mcp-suite must be on PATH
```

## Install JUnit adapter

**GitHub Packages** (see [DOWNLOADS.md](../DOWNLOADS.md) for `settings.xml`):

```xml
<dependency>
  <groupId>io.github.vaquarkhan</groupId>
  <artifactId>mcp-test-suite-junit5</artifactId>
  <version>4.0.0</version>
  <scope>test</scope>
</dependency>
```

Or from source / Release JAR:

```bash
cd adapters/junit5 && mvn -q clean install
# or download mcp-test-suite-junit5-4.0.0.jar from
# https://github.com/vaquarkhan/mcp-test-suite/releases/tag/v4.0.0
```

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
