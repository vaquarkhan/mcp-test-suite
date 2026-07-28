# Tutorial: Ktor (Kotlin)

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Java / Maven](https://github.com/vaquarkhan/mcp-test-suite/packages/3158511) ·
[Install guide](../DOWNLOADS.md)

Test a **Ktor** MCP server with declarative YAML (+ optional JUnit).

Example pack: [examples/frameworks/kotlin/ktor/](../../examples/frameworks/kotlin/ktor/)

## 1. Install

```bash
pip install "mcp-test-harness>=3.0.9,<4"
pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"
```

## 2. Suite

```yaml
server:
  command: java -jar build/libs/ktor-mcp-all.jar
  transport: stdio
cases:
  - name: Echo
    call: echo
    args: { text: hello-ktor }
    tags: [smoke, ktor]
```

## 3. Run

```bash
./gradlew shadowJar
mcp-suite run --suite mcp-suite.yaml \
  --server-command "java -jar build/libs/ktor-mcp-all.jar"

# or during development
mcp-suite run --suite mcp-suite.yaml --server-command "./gradlew -q run"
```

Probe first:

```bash
mcp-test try --server-command "java -jar build/libs/ktor-mcp-all.jar"
```

## Notes

- If Ktor exposes MCP over HTTP/SSE, set `transport: http` or `sse` and `server.command` / URL per [yaml.md](yaml.md) and engine docs.
- For stdio, ensure the process speaks Content-Length or newline JSON matching the harness client.

## Related

- [kotlin.md](kotlin.md) · [kotlin-spring.md](kotlin-spring.md)
