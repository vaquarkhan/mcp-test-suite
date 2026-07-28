package io.github.vaquarkhan.mcp.test.suite.junit5;

import org.junit.jupiter.api.extension.ExtensionContext;
import org.junit.jupiter.api.extension.ParameterContext;
import org.junit.jupiter.api.extension.ParameterResolutionException;
import org.junit.jupiter.api.extension.ParameterResolver;

/** Resolves {@link MCPConnection} parameters from {@link MCPTest} class annotation. */
public final class MCPTestExtension implements ParameterResolver {
    @Override
    public boolean supportsParameter(ParameterContext parameterContext, ExtensionContext extensionContext)
            throws ParameterResolutionException {
        return parameterContext.getParameter().getType() == MCPConnection.class;
    }

    @Override
    public Object resolveParameter(ParameterContext parameterContext, ExtensionContext extensionContext)
            throws ParameterResolutionException {
        Class<?> testClass = extensionContext.getRequiredTestClass();
        MCPTest ann = testClass.getAnnotation(MCPTest.class);
        if (ann == null) {
            throw new ParameterResolutionException("@MCPTest required on test class");
        }
        return new MCPConnection(
                ann.binary(),
                ann.serverCommand(),
                ann.suite(),
                ann.config(),
                ann.transport(),
                ann.timeoutMinutes());
    }
}
