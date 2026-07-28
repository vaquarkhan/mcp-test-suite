# Tutorial: Quarkus (Java)

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Java / Maven](https://github.com/vaquarkhan/mcp-test-suite/packages/3158511) ·
[Install guide](../DOWNLOADS.md)

Test a **Quarkus** MCP server with `mcp-suite.yaml` + JUnit 5.

Example pack: [examples/frameworks/java/quarkus/](../../examples/frameworks/java/quarkus/)

## 1. Install

```bash
pip install "mcp-test-harness>=3.0.9"
pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"
```

Maven test dep: `io.github.vaquarkhan:mcp-test-suite-junit5:4.0.0` — [package page](https://github.com/vaquarkhan/mcp-test-suite/packages/3158511)

## 2. Suite

```yaml
server:
  command: java -jar target/quarkus-app/quarkus-run.jar
  transport: stdio
cases:
  - name: Echo
    call: echo
    args: { text: hello-quarkus }
    tags: [smoke, quarkus]
```

Adjust `server.command` for `quarkus:dev` or your uber-jar layout.

## 3. Run

```bash
./mvnw -DskipTests package
mcp-suite run --suite mcp-suite.yaml \
  --server-command "java -jar target/quarkus-app/quarkus-run.jar"

mcp-test try --server-command "java -jar target/quarkus-app/quarkus-run.jar"
```

JUnit:

```java
@MCPTest(
    serverCommand = "java -jar target/quarkus-app/quarkus-run.jar",
    suite = "mcp-suite.yaml"
)
class QuarkusMcpIT {
    @Test
    void suite(MCPConnection mcp) {
        mcp.runSuite().assertPassed();
    }
}
```

## Quarkus notes

- Fast-jar vs uber-jar: set `command` to the entrypoint you ship in CI.
- Dev mode (`quarkus:dev`) is fine locally; prefer a packaged jar in CI for stable boot.

## Related

- [java.md](java.md) · [micronaut.md](micronaut.md)
- Pack: [examples/frameworks/java/quarkus/](../../examples/frameworks/java/quarkus/)
