# McpTestSuite.Xunit

## Download (NuGet)

```bash
dotnet add package McpTestSuite.Xunit --version 4.0.0
```

| Registry | Link |
|----------|------|
| NuGet.org | https://www.nuget.org/packages/McpTestSuite.Xunit |

Engine: `pip install mcp-test-suite` or Docker / release binary.

## Usage

```csharp
var client = new McpClient(new McpClientOptions
{
    Command = "dotnet run --project src/McpServer",
    Suite = "mcp-suite.yaml",
});
Assert.True((await client.RunSuiteAsync()).Passed);
```

Examples: [examples/frameworks/dotnet](../../examples/frameworks/dotnet/) · [docs/DOWNLOADS.md](../../docs/DOWNLOADS.md)
