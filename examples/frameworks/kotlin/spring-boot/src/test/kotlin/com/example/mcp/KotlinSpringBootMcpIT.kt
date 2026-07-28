package com.example.mcp

import io.github.vaquarkhan.mcp.test.suite.junit5.MCPConnection
import io.github.vaquarkhan.mcp.test.suite.junit5.MCPTest
import org.junit.jupiter.api.Assertions.assertTrue
import org.junit.jupiter.api.Test

@MCPTest(
    serverCommand = "java -jar build/libs/mcp-server-0.0.1-SNAPSHOT.jar",
    suite = "mcp-suite.yaml",
)
class KotlinSpringBootMcpIT {
    @Test
    fun suitePasses(mcp: MCPConnection) {
        assertTrue(mcp.runSuite().passed())
    }
}
