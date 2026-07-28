# Spring AI MCP server — test pack

Targets apps using `@Tool` / Spring AI MCP server starters.

```bash
mcp-test run --suite mcp-suite.yaml --server-command "mvn -q spring-boot:run"
# or after package:
mcp-test run --suite mcp-suite.yaml --server-command "java -jar target/spring-ai-mcp-0.0.1-SNAPSHOT.jar"
```

Map `cases[].call` to your `@Tool` method names (often camelCase).
