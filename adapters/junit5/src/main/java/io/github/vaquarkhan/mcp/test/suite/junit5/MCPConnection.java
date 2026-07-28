package io.github.vaquarkhan.mcp.test.suite.junit5;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;

/** Connection handle injected into JUnit tests — shells out to mcp-test. */
public final class MCPConnection {
    private final String binary;
    private final String serverCommand;
    private final String suite;
    private final String config;
    private final String transport;

    public MCPConnection(
            String binary,
            String serverCommand,
            String suite,
            String config,
            String transport) {
        this.binary = binary;
        this.serverCommand = serverCommand;
        this.suite = suite;
        this.config = config;
        this.transport = transport;
    }

    /** Run the shared declarative suite. */
    public MCPCallResult runSuite() {
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
        return exec(args);
    }

    /** Probe handshake then run the suite (tool contracts live in mcp-suite.yaml). */
    public MCPCallResult call(String tool) {
        List<String> args = new ArrayList<>();
        args.add(binary);
        args.add("try");
        args.add("--server-command");
        args.add(serverCommand);
        args.add("--transport");
        args.add(transport);
        MCPCallResult probe = exec(args);
        if (!probe.passed()) {
            return probe;
        }
        return runSuite();
    }

    private static MCPCallResult exec(List<String> command) {
        long start = System.nanoTime();
        try {
            ProcessBuilder pb = new ProcessBuilder(command);
            Process p = pb.start();
            String stdout = read(p.getInputStream());
            String stderr = read(p.getErrorStream());
            boolean finished = p.waitFor(10, TimeUnit.MINUTES);
            int code = finished ? p.exitValue() : 124;
            if (!finished) {
                p.destroyForcibly();
            }
            long ms = (System.nanoTime() - start) / 1_000_000L;
            return new MCPCallResult(code, stdout, stderr, ms);
        } catch (Exception e) {
            long ms = (System.nanoTime() - start) / 1_000_000L;
            return new MCPCallResult(1, "", e.getMessage(), ms);
        }
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
