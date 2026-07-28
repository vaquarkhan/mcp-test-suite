# McpTestSuite.Xunit

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Java JAR](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/mcp-test-suite-junit5-4.0.0.jar) ·
[Node / npm tgz](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/vaquarkhan-mcp-test-suite-jest-4.0.0.tgz) ·
[Go module](https://pkg.go.dev/github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0) ·
[.NET nupkg](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/McpTestSuite.Xunit.4.0.0.nupkg) ·
[All release assets](https://github.com/vaquarkhan/mcp-test-suite/releases/tag/v4.0.0) ·
[Install guide](../../docs/DOWNLOADS.md)

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
