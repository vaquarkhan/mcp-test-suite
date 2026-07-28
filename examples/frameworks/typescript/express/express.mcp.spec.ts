import { MCPClient } from '@mcp-test-suite/jest';

describe('Express MCP server', () => {
  const server = new MCPClient({ command: 'node dist/server.js', suite: 'mcp-suite.yaml' });

  it('suite passes', async () => {
    await expect(server.runSuite()).resolves.toMatchObject({ ok: true });
  });
});
