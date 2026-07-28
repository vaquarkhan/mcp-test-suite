package com.example.mcp;

import io.github.vaquarkhan.mcp.test.suite.junit5.MCPConnection;
import io.github.vaquarkhan.mcp.test.suite.junit5.MCPTest;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertTrue;

@MCPTest(
        serverCommand = "java -jar build/libs/my-micronaut-mcp-0.1-all.jar",
        suite = "mcp-suite.yaml"
)
class MicronautMcpIT {
    @Test
    void suitePasses(MCPConnection mcp) {
        assertTrue(mcp.runSuite().passed());
    }
}
