using System.Diagnostics;
using System.Text;

namespace McpTestSuite.Xunit;

public sealed class McpClientOptions
{
    public string Command { get; init; } = "";
    public string Suite { get; init; } = "mcp-suite.yaml";
    public string? Config { get; init; }
    public string Binary { get; init; } =
        Environment.GetEnvironmentVariable("MCP_SUITE_BIN")
        ?? Environment.GetEnvironmentVariable("MCP_TEST_BIN")
        ?? "mcp-suite";
    public string Transport { get; init; } = "stdio";
    public string? WorkingDirectory { get; init; }
}

public sealed class McpCallResult
{
    public int ExitCode { get; init; }
    public string Stdout { get; init; } = "";
    public string Stderr { get; init; } = "";
    public long LatencyMs { get; init; }
    public bool Passed => ExitCode == 0;
}

/// <summary>Thin xUnit helper that shells out to the mcp-test CLI / binary.</summary>
public sealed class McpClient
{
    private readonly McpClientOptions _options;

    public McpClient(McpClientOptions options) => _options = options;

    public Task<McpCallResult> TryAsync(CancellationToken ct = default) =>
        RunAsync(new[]
        {
            "try",
            "--server-command", _options.Command,
            "--transport", _options.Transport,
        }, ct);

    public Task<McpCallResult> RunSuiteAsync(CancellationToken ct = default)
    {
        var args = new List<string>
        {
            "run",
            "--suite", _options.Suite,
            "--server-command", _options.Command,
            "--transport", _options.Transport,
        };
        if (!string.IsNullOrWhiteSpace(_options.Config))
        {
            args.Add("--config");
            args.Add(_options.Config!);
        }
        return RunAsync(args, ct);
    }

    private async Task<McpCallResult> RunAsync(IReadOnlyList<string> args, CancellationToken ct)
    {
        var sw = Stopwatch.StartNew();
        var psi = new ProcessStartInfo
        {
            FileName = _options.Binary,
            RedirectStandardOutput = true,
            RedirectStandardError = true,
            UseShellExecute = false,
            CreateNoWindow = true,
        };
        if (!string.IsNullOrWhiteSpace(_options.WorkingDirectory))
            psi.WorkingDirectory = _options.WorkingDirectory!;
        foreach (var a in args)
            psi.ArgumentList.Add(a);

        using var proc = Process.Start(psi)
            ?? throw new InvalidOperationException($"Failed to start {_options.Binary}");
        var stdoutTask = proc.StandardOutput.ReadToEndAsync(ct);
        var stderrTask = proc.StandardError.ReadToEndAsync(ct);
        await proc.WaitForExitAsync(ct).ConfigureAwait(false);
        sw.Stop();
        return new McpCallResult
        {
            ExitCode = proc.ExitCode,
            Stdout = await stdoutTask.ConfigureAwait(false),
            Stderr = await stderrTask.ConfigureAwait(false),
            LatencyMs = sw.ElapsedMilliseconds,
        };
    }
}
