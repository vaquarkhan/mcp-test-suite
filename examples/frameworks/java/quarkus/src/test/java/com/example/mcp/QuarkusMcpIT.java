package com.example.mcp;

import io.github.vaquarkhan.mcp.test.suite.junit5.MCPConnection;
import io.github.vaquarkhan.mcp.test.suite.junit5.MCPTest;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertTrue;

@MCPTest(
        serverCommand = "java -jar target/quarkus-app/quarkus-run.jar",
        suite = "mcp-suite.yaml"
)
class QuarkusMcpIT {
    @Test
    void suitePasses(MCPConnection mcp) {
        assertTrue(mcp.runSuite().passed());
    }
}
