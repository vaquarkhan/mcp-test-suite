import { MCPClient } from '@vaquarkhan/mcp-test-suite-jest';

describe('Fastify MCP server', () => {
  const server = new MCPClient({ command: 'node dist/server.js', suite: 'mcp-suite.yaml' });

  it('suite passes', async () => {
    await expect(server.runSuite()).resolves.toMatchObject({ ok: true });
  });
});
