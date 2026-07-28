# Quarkus MCP server — test pack

```bash
# Dev mode (hot reload) — prefer packaged jar in CI
mcp-suite run --suite mcp-suite.yaml \
  --server-command "java -jar target/quarkus-app/quarkus-run.jar"
```

Quarkus MCP extension servers often speak stdio; set `transport: http` if you expose the Quarkus HTTP MCP endpoint.
