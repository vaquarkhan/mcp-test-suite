# Tutorial: Micronaut (Java)

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Java / Maven](https://github.com/vaquarkhan/mcp-test-suite/packages/3158511) ·
[Install guide](../DOWNLOADS.md)

Test a **Micronaut** MCP server with declarative YAML and JUnit 5.

Example pack: [examples/frameworks/java/micronaut/](../../examples/frameworks/java/micronaut/)

## 1. Install

```bash
pip install "mcp-test-harness>=3.0.9"
pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"
```

Adapter: `io.github.vaquarkhan:mcp-test-suite-junit5:4.0.0` — [Maven package](https://github.com/vaquarkhan/mcp-test-suite/packages/3158511)

## 2. Suite

```yaml
server:
  command: java -jar build/libs/mcp-server-0.1-all.jar
  transport: stdio
cases:
  - name: Echo
    call: echo
    args: { text: hello-micronaut }
    tags: [smoke, micronaut]
```

## 3. Run

```bash
./gradlew shadowJar   # or mvn package
mcp-suite run --suite mcp-suite.yaml \
  --server-command "java -jar build/libs/mcp-server-0.1-all.jar"
```

JUnit `@MCPTest` same as [spring-boot.md](spring-boot.md) with your jar path.

## Micronaut notes

- Point `server.command` at the shaded/executable jar your build produces.
- Keep Micronaut logging on stderr.

## Related

- [java.md](java.md) · [quarkus.md](quarkus.md)
- Pack: [examples/frameworks/java/micronaut/](../../examples/frameworks/java/micronaut/)
