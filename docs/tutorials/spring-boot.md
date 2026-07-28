# Tutorial: Spring Boot (Java)

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Java / Maven](https://github.com/vaquarkhan/mcp-test-suite/packages/3158511) ·
[Install guide](../DOWNLOADS.md)

Test a **Spring Boot** MCP server with a shared `mcp-suite.yaml` and optional JUnit 5 adapter.

Example pack: [examples/frameworks/java/spring-boot/](../../examples/frameworks/java/spring-boot/)

## 1. Install engine + suite

```bash
pip install "mcp-test-harness>=3.0.9,<4"
pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"
mcp-suite --version
```

## 2. Add Maven test dependency

**Package:** [io.github.vaquarkhan.mcp-test-suite-junit5](https://github.com/vaquarkhan/mcp-test-suite/packages/3158511)

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

`~/.m2/settings.xml` needs a GitHub PAT with `read:packages` (see [DOWNLOADS.md](../DOWNLOADS.md)).

## 3. Create `mcp-suite.yaml`

```yaml
server:
  command: java -jar target/my-mcp-server-0.0.1-SNAPSHOT.jar
  transport: stdio
cases:
  - name: Echo tool responds
    call: echo
    args: { text: hello-spring }
    tags: [smoke, spring-boot]
  - name: Unknown tool is rejected
    call: __missing_tool__
    args: {}
    expect_error: true
```

Map `cases[].call` to your MCP tool names.

## 4. Run (CLI)

```bash
mvn -DskipTests package
mcp-suite run --suite mcp-suite.yaml \
  --server-command "java -jar target/my-mcp-server-0.0.1-SNAPSHOT.jar"

# optional HTML report
mcp-suite run --suite mcp-suite.yaml --report-format html --report-output report.html
```

Zero-config probe:

```bash
mcp-test try --server-command "java -jar target/my-mcp-server-0.0.1-SNAPSHOT.jar"
```

## 5. Run (JUnit)

```java
@MCPTest(
    serverCommand = "java -jar target/my-mcp-server-0.0.1-SNAPSHOT.jar",
    suite = "mcp-suite.yaml",
    binary = "mcp-suite"
)
class SpringBootMcpIT {
    @Test
    void suite(MCPConnection mcp) {
        mcp.runSuite().assertPassed();
    }
}
```

```bash
mvn test -Dtest=SpringBootMcpIT
```

## Spring Boot notes

- Prefer **stdio** for local CI; use HTTP/SSE when the app exposes Streamable HTTP.
- Never log MCP JSON-RPC to **stdout** — use SLF4J → stderr/file.
- Green `mcp-test try` before adding the jar to Cursor / Kiro / ChatGPT MCP config.

## Related

- [java.md](java.md) · [spring-ai.md](spring-ai.md) · [yaml.md](yaml.md)
- Pack README: [examples/frameworks/java/spring-boot/README.md](../../examples/frameworks/java/spring-boot/README.md)
