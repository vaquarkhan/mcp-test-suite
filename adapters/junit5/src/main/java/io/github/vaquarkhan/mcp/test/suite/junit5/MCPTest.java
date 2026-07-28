package io.github.vaquarkhan.mcp.test.suite.junit5;

import org.junit.jupiter.api.extension.ExtendWith;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

/**
 * Marks a JUnit 5 test class as an MCP server suite.
 * Injects an {@link MCPConnection} that shells out to the mcp-suite CLI.
 *
 * <p>Requires Python packages {@code mcp-test-harness} and {@code mcp-test-suite}
 * so {@code mcp-suite} is on {@code PATH} (or set {@link #binary()}).
 */
@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@ExtendWith(MCPTestExtension.class)
public @interface MCPTest {
    /** Shell command that starts the MCP server under test. */
    String serverCommand();

    /** Optional path to mcp-suite.yaml */
    String suite() default "mcp-suite.yaml";

    /** Optional mcp-test.yaml config */
    String config() default "";

    String transport() default "stdio";

    /** Binary name or absolute path (default: mcp-suite on PATH). */
    String binary() default "mcp-suite";

    /** Max wall-clock minutes for each CLI invocation (default: 10). */
    long timeoutMinutes() default 10L;
}
