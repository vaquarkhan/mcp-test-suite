# Java framework examples

Uses [`mcp-test-suite-junit5`](../../../adapters/junit5/) plus shared `mcp-suite.yaml`.

| Example | Stack | Server command (typical) |
|---------|-------|--------------------------|
| [spring-boot/](spring-boot/) | Spring Boot + Spring AI MCP | `java -jar target/*-SNAPSHOT.jar` |
| [spring-ai/](spring-ai/) | Spring AI MCP server (tool annotations) | `mvn -q spring-boot:run` |
| [quarkus/](quarkus/) | Quarkus MCP server extension | `mvn -Dquarkus-plugin.goal=dev` / packaged jar |
| [micronaut/](micronaut/) | Micronaut MCP | `java -jar build/libs/*-all.jar` |
