# @mcp-test-suite/jest

## Download (npm)

```bash
npm install -D @mcp-test-suite/jest
```

| Registry | Link |
|----------|------|
| npm | https://www.npmjs.com/package/@mcp-test-suite/jest |

Engine: `pip install mcp-test-suite` or Docker / release binary.

## Usage

```typescript
import { MCPClient } from '@mcp-test-suite/jest';

test('suite', async () => {
  const server = new MCPClient({ command: 'node dist/main.js', suite: 'mcp-suite.yaml' });
  await expect(server.runSuite()).resolves.toMatchObject({ ok: true });
});
```

Examples: [examples/frameworks/typescript](../../examples/frameworks/typescript/) · [docs/DOWNLOADS.md](../../docs/DOWNLOADS.md)
