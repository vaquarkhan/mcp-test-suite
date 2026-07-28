# .NET / ASP.NET MCP — test pack

Uses the [`adapters/xunit`](../../../adapters/xunit/) helper.

```bash
dotnet build
mcp-suite run --suite mcp-suite.yaml --server-command "dotnet run --project src/McpServer"
# or
dotnet test
```
