package io.github.vaquarkhan.mcp.test.suite.junit5;

import org.junit.jupiter.api.extension.ExtendWith;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

/**
 * Marks a JUnit 5 test class as an MCP server suite.
 * Injects an {@link MCPConnection} that shells out to the mcp-test CLI / binary.
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

    /** Binary name or absolute path (default: mcp-test on PATH). */
    String binary() default "mcp-test";
}
