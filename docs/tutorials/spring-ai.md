# Tutorial: Spring AI (Java)

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Java / Maven](https://github.com/vaquarkhan/mcp-test-suite/packages/3158511) ·
[Install guide](../DOWNLOADS.md)

Test MCP servers built with **Spring AI** (`@Tool` / MCP server starters).

Example pack: [examples/frameworks/java/spring-ai/](../../examples/frameworks/java/spring-ai/)

## 1. Install

```bash
pip install "mcp-test-harness>=3.0.9"
pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"
```

Add JUnit adapter: [Maven package](https://github.com/vaquarkhan/mcp-test-suite/packages/3158511) — `io.github.vaquarkhan:mcp-test-suite-junit5:4.0.0`

## 2. Suite

Map `call` to `@Tool` method names (often camelCase):

```yaml
server:
  command: java -jar target/spring-ai-mcp-0.0.1-SNAPSHOT.jar
  transport: stdio
cases:
  - name: Weather tool
    call: getWeather
    args: { city: Seattle }
    tags: [smoke, spring-ai]
  - name: Unknown tool fails
    call: __missing__
    args: {}
    expect_error: true
```

## 3. Run

```bash
# while developing
mcp-suite run --suite mcp-suite.yaml --server-command "mvn -q spring-boot:run"

# packaged
mvn -DskipTests package
mcp-suite run --suite mcp-suite.yaml \
  --server-command "java -jar target/spring-ai-mcp-0.0.1-SNAPSHOT.jar"
```

Or JUnit `@MCPTest` (same pattern as [spring-boot.md](spring-boot.md)).

## Spring AI notes

- Tool names in YAML must match the exposed MCP tool name (check `tools/list` via `mcp-test try`).
- Keep AI/model logs off stdout.
- Use tags like `[spring-ai]` to filter CI jobs.

## Related

- [spring-boot.md](spring-boot.md) · [java.md](java.md)
- Pack: [examples/frameworks/java/spring-ai/](../../examples/frameworks/java/spring-ai/)
