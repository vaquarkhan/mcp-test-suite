package io.github.vaquarkhan.mcp.test.suite.junit5;

/** Result of an mcp-suite / mcp-test CLI invocation. */
public final class MCPCallResult {
    private final int exitCode;
    private final String stdout;
    private final String stderr;
    private final long latencyMs;

    public MCPCallResult(int exitCode, String stdout, String stderr, long latencyMs) {
        this.exitCode = exitCode;
        this.stdout = stdout;
        this.stderr = stderr;
        this.latencyMs = latencyMs;
    }

    public int exitCode() { return exitCode; }
    public String stdout() { return stdout; }
    public String stderr() { return stderr; }
    public long latency() { return latencyMs; }
    public boolean passed() { return exitCode == 0; }

    /** Fail the calling test if the CLI exited non-zero. */
    public void assertPassed() {
        if (!passed()) {
            throw new AssertionError(
                    "mcp-suite failed (exit " + exitCode + "):\n" + stderr + "\n" + stdout);
        }
    }
}
