import { MCPClient } from '@mcp-test-suite/jest';

const server = new MCPClient({
  command: 'node dist/main.js',
  suite: 'mcp-suite.yaml',
});

describe('NestJS MCP server', () => {
  it('passes declarative suite', async () => {
    const result = await server.runSuite();
    expect(result.ok).toBe(true);
  });

  it('echo tool works', async () => {
    const result = await server.callTool('echo', { text: 'nest' });
    expect(result.ok).toBe(true);
  });

  it('try probe succeeds', async () => {
    const result = await server.try();
    expect(result.ok).toBe(true);
  });
});
