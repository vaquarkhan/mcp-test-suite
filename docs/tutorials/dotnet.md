# Tutorial: .NET (xUnit)

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Java JAR](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/mcp-test-suite-junit5-4.0.0.jar) ·
[Node / npm tgz](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/vaquarkhan-mcp-test-suite-jest-4.0.0.tgz) ·
[Go module](https://pkg.go.dev/github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0) ·
[.NET nupkg](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/McpTestSuite.Xunit.4.0.0.nupkg) ·
[All release assets](https://github.com/vaquarkhan/mcp-test-suite/releases/tag/v4.0.0) ·
[Install guide](../DOWNLOADS.md)

## Install engine + suite

```bash
pip install "mcp-test-harness>=3.0.9"
pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"
```

## Install adapter

**GitHub Packages** (see [DOWNLOADS.md](../DOWNLOADS.md)):

```bash
dotnet nuget add source "https://nuget.pkg.github.com/vaquarkhan/index.json" \
  --name github \
  --username YOUR_GITHUB_USERNAME \
  --password YOUR_GITHUB_PAT \
  --store-password-in-clear-text

dotnet add package McpTestSuite.Xunit --version 4.0.0
```

Or project reference / Release `.nupkg`:

```xml
<ProjectReference Include="..\mcp-test-suite\adapters\xunit\McpTestSuite.Xunit.csproj" />
```

## Test

```csharp
public class McpTests
{
    [Fact]
    public async Task SuitePasses()
    {
        var client = new McpClient(new McpClientOptions
        {
            Command = "dotnet run --project src/Server",
            Suite = "mcp-suite.yaml",
            // Binary defaults to mcp-suite
        });
        var result = await client.RunSuiteAsync();
        Assert.True(result.Passed, result.Stderr);
    }
}
```

Example: [examples/frameworks/dotnet/](../../examples/frameworks/dotnet/)
