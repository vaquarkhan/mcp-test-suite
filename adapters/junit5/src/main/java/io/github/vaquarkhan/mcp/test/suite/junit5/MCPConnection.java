package io.github.vaquarkhan.mcp.test.suite.junit5;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.concurrent.TimeUnit;

/**
 * Connection handle injected into JUnit tests — shells out to {@code mcp-suite}.
 *
 * <p>Requires the Python engine ({@code mcp-test-harness}) and suite CLI on PATH,
 * or an absolute {@code binary} path from {@link MCPTest#binary()}.
 */
public final class MCPConnection {
    private final String binary;
    private final String serverCommand;
    private final String suite;
    private final String config;
    private final String transport;
    private final long timeoutMinutes;

    public MCPConnection(
            String binary,
            String serverCommand,
            String suite,
            String config,
            String transport) {
        this(binary, serverCommand, suite, config, transport, 10L);
    }

    public MCPConnection(
            String binary,
            String serverCommand,
            String suite,
            String config,
            String transport,
            long timeoutMinutes) {
        this.binary = resolveBinary(binary);
        this.serverCommand = serverCommand;
        this.suite = suite;
        this.config = config;
        this.transport = transport;
        this.timeoutMinutes = timeoutMinutes > 0 ? timeoutMinutes : 10L;
    }

    /** Run the shared declarative suite. */
    public MCPCallResult runSuite() {
        List<String> args = baseRunArgs();
        return exec(args);
    }

    /**
     * Run suite cases whose names match {@code tool} ({@code mcp-suite run -k}).
     *
     * <p>Tool contracts still live in {@code mcp-suite.yaml}; this filters by case name.
     */
    public MCPCallResult call(String tool) {
        if (tool == null || tool.isBlank()) {
            return runSuite();
        }
        List<String> args = baseRunArgs();
        args.add("-k");
        args.add(tool.trim());
        return exec(args);
    }

    /** Zero-config handshake / conformance probe ({@code mcp-test try} / {@code mcp-suite try}). */
    public MCPCallResult probe() {
        List<String> args = new ArrayList<>();
        args.add(binary);
        args.add("try");
        args.add("--server-command");
        args.add(serverCommand);
        args.add("--transport");
        args.add(transport);
        return exec(args);
    }

    /**
     * @deprecated Use {@link #probe()} then {@link #runSuite()}, or {@link #call(String)} to
     *     filter by case name. Kept for source compatibility.
     */
    @Deprecated
    public MCPCallResult probeThenRunSuite() {
        MCPCallResult probe = probe();
        if (!probe.passed()) {
            return probe;
        }
        return runSuite();
    }

    private List<String> baseRunArgs() {
        List<String> args = new ArrayList<>();
        args.add(binary);
        args.add("run");
        args.add("--suite");
        args.add(suite);
        args.add("--server-command");
        args.add(serverCommand);
        args.add("--transport");
        args.add(transport);
        if (config != null && !config.isBlank()) {
            args.add("--config");
            args.add(config);
        }
        return args;
    }

    private MCPCallResult exec(List<String> command) {
        long start = System.nanoTime();
        try {
            ProcessBuilder pb = new ProcessBuilder(command);
            Process p = pb.start();
            String stdout = read(p.getInputStream());
            String stderr = read(p.getErrorStream());
            boolean finished = p.waitFor(timeoutMinutes, TimeUnit.MINUTES);
            int code = finished ? p.exitValue() : 124;
            if (!finished) {
                p.destroyForcibly();
            }
            long ms = (System.nanoTime() - start) / 1_000_000L;
            return new MCPCallResult(code, stdout, stderr, ms);
        } catch (Exception e) {
            long ms = (System.nanoTime() - start) / 1_000_000L;
            String msg = e.getMessage() == null ? e.getClass().getSimpleName() : e.getMessage();
            String hint =
                    msg
                            + "\nInstall Python engine + suite CLI and ensure they are on PATH:\n"
                            + "  pip install \"mcp-test-harness>=3.0.9,<4\"\n"
                            + "  pip install \"git+https://github.com/vaquarkhan/mcp-test-suite.git\"\n"
                            + "Or set @MCPTest(binary = \"/absolute/path/to/mcp-suite\").";
            return new MCPCallResult(1, "", hint, ms);
        }
    }

    static String resolveBinary(String binary) {
        if (binary == null || binary.isBlank()) {
            binary = "mcp-suite";
        }
        Path asPath = Path.of(binary);
        if (asPath.isAbsolute() || binary.contains("/") || binary.contains("\\")) {
            return binary;
        }
        String pathEnv = System.getenv("PATH");
        if (pathEnv == null || pathEnv.isBlank()) {
            return binary;
        }
        boolean windows = System.getProperty("os.name", "").toLowerCase(Locale.ROOT).contains("win");
        String[] suffixes = windows
                ? new String[] {"", ".exe", ".cmd", ".bat"}
                : new String[] {""};
        for (String dir : pathEnv.split(java.util.regex.Pattern.quote(java.io.File.pathSeparator))) {
            if (dir.isBlank()) {
                continue;
            }
            for (String suffix : suffixes) {
                Path candidate = Path.of(dir, binary + suffix);
                if (Files.isRegularFile(candidate) && Files.isExecutable(candidate)) {
                    return candidate.toAbsolutePath().toString();
                }
                // Windows: .cmd/.bat may not report isExecutable consistently.
                if (windows && Files.isRegularFile(candidate)) {
                    return candidate.toAbsolutePath().toString();
                }
            }
        }
        return binary;
    }

    private static String read(java.io.InputStream in) throws Exception {
        StringBuilder sb = new StringBuilder();
        try (BufferedReader br = new BufferedReader(new InputStreamReader(in, StandardCharsets.UTF_8))) {
            String line;
            while ((line = br.readLine()) != null) {
                sb.append(line).append('\n');
            }
        }
        return sb.toString();
    }
}
