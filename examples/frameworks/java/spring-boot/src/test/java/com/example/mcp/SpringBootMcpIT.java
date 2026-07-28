package com.example.mcp;

import io.github.vaquarkhan.mcp.test.suite.junit5.MCPConnection;
import io.github.vaquarkhan.mcp.test.suite.junit5.MCPTest;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertTrue;

/**
 * Integration test for a Spring Boot MCP server.
 * Requires mcp-test on PATH (pip / binary / docker wrapper).
 */
@MCPTest(
        serverCommand = "java -jar target/my-mcp-server-0.0.1-SNAPSHOT.jar",
        suite = "mcp-suite.yaml",
        config = "mcp-test.yaml"
)
class SpringBootMcpIT {

    @Test
    @DisplayName("Declarative suite passes against Spring Boot MCP jar")
    void suitePasses(MCPConnection mcp) {
        var result = mcp.runSuite();
        assertTrue(result.passed(), () -> result.stderr() + "\n" + result.stdout());
        assertTrue(result.latency() < 60_000, "suite too slow: " + result.latency() + "ms");
    }

    @Test
    @DisplayName("Handshake probe (mcp-test try) succeeds")
    void tryProbe(MCPConnection mcp) {
        var result = mcp.call("echo");
        assertTrue(result.passed(), () -> result.stderr());
    }
}
