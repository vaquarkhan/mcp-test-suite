# Tutorial: .NET (xUnit)

## Install engine + suite

```bash
pip install "mcp-test-harness>=3.0.9"
pip install .
```

## Project reference

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
