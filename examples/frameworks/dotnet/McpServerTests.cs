using McpTestSuite.Xunit;
using Xunit;

public class McpServerTests
{
    private readonly McpClient _client = new(new McpClientOptions
    {
        Command = "dotnet run --project src/McpServer --no-build",
        Suite = "mcp-suite.yaml",
    });

    [Fact]
    public async Task DeclarativeSuite_Passes()
    {
        var result = await _client.RunSuiteAsync();
        Assert.True(result.Passed, result.Stderr);
    }

    [Fact]
    public async Task TryProbe_Succeeds()
    {
        var result = await _client.TryAsync();
        Assert.True(result.Passed, result.Stderr);
    }
}
