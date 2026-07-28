# Tutorial: .NET / ASP.NET (xUnit)

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[.NET / NuGet](https://github.com/users/vaquarkhan/packages/nuget/package/McpTestSuite.Xunit) ·
[Install guide](../DOWNLOADS.md)

Test **ASP.NET / .NET** MCP servers with `mcp-suite.yaml` and the xUnit adapter.

Example pack: [examples/frameworks/dotnet/](../../examples/frameworks/dotnet/)

## 1. Install engine + suite

```bash
pip install "mcp-test-harness>=3.0.9"
pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"
```

## 2. Install NuGet adapter

**Package page:** [McpTestSuite.Xunit](https://github.com/users/vaquarkhan/packages/nuget/package/McpTestSuite.Xunit)

```bash
dotnet nuget add source "https://nuget.pkg.github.com/vaquarkhan/index.json" \
  --name github \
  --username YOUR_GITHUB_USERNAME \
  --password YOUR_GITHUB_PAT \
  --store-password-in-clear-text

dotnet add package McpTestSuite.Xunit --version 4.0.0
```

Or download `.nupkg` from [Releases](https://github.com/vaquarkhan/mcp-test-suite/releases/tag/v4.0.0).

## 3. Suite

```yaml
server:
  command: dotnet run --project src/McpServer
  transport: stdio
cases:
  - name: Echo
    call: echo
    args: { text: hello-dotnet }
    tags: [smoke, dotnet]
```

## 4. Run (CLI)

```bash
dotnet build
mcp-suite run --suite mcp-suite.yaml \
  --server-command "dotnet run --project src/McpServer"
```

## 5. Run (xUnit)

```csharp
public class McpTests
{
    [Fact]
    public async Task SuitePasses()
    {
        var client = new McpClient(new McpClientOptions
        {
            Command = "dotnet run --project src/McpServer",
            Suite = "mcp-suite.yaml",
        });
        var result = await client.RunSuiteAsync();
        Assert.True(result.Passed, result.Stderr);
    }
}
```

```bash
dotnet test
```

## .NET notes

- In CI, prefer `dotnet build` then run the built DLL/exe instead of `dotnet run` for faster cold starts.
- Keep console logging off stdout for stdio MCP.

## Related

- [yaml.md](yaml.md) · Pack: [examples/frameworks/dotnet/](../../examples/frameworks/dotnet/)
