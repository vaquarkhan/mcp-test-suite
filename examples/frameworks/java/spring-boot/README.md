# Spring Boot MCP server — test pack

## Layout

```
spring-boot/
  mcp-suite.yaml          # language-agnostic contracts
  mcp-test.yaml           # engine config
  src/test/java/.../SpringBootMcpIT.java
  pom-snippet.xml         # deps to paste into your app
```

## Wire-up

1. Build your Spring Boot MCP app (`mvn -DskipTests package`).
2. Point `server.command` at the fat jar (or `mvn spring-boot:run`).
3. Run:

```bash
mcp-test run --suite mcp-suite.yaml \
  --server-command "java -jar target/my-mcp-server-0.0.1-SNAPSHOT.jar"
```

Or from JUnit:

```bash
mvn test -Dtest=SpringBootMcpIT
```

## Spring Boot notes

- Prefer **stdio** for local CI; use HTTP transport when the app exposes Streamable HTTP / SSE.
- Do not log to **stdout** (breaks JSON-RPC). Use SLF2J → stderr / file.
- Green `mcp-test try` before adding the jar to `.cursor/mcp.json`.
