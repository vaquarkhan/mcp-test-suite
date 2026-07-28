# McpTestSuite.Xunit

xUnit adapter for **mcp-test-suite** (.NET MCP servers).

## Install (GitHub Packages)

```bash
dotnet nuget add source "https://nuget.pkg.github.com/vaquarkhan/index.json" \
  --name github \
  --username YOUR_GITHUB_USERNAME \
  --password YOUR_GITHUB_PAT \
  --store-password-in-clear-text

dotnet add package McpTestSuite.Xunit --version 4.0.0
```

Or download `McpTestSuite.Xunit.4.0.0.nupkg` from [Releases](https://github.com/vaquarkhan/mcp-test-suite/releases/tag/v4.0.0).

Engine: `pip install mcp-test-harness` + `mcp-suite` on PATH ([DOWNLOADS.md](../../docs/DOWNLOADS.md)).

## Usage

```csharp
var client = new McpClient(new McpClientOptions
{
    Command = "dotnet run --project src/McpServer",
    Suite = "mcp-suite.yaml",
});
Assert.True((await client.RunSuiteAsync()).Passed);
```

Examples: [examples/frameworks/dotnet](../../examples/frameworks/dotnet/)
