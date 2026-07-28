# Tutorial: Express (TypeScript)

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Node / npm](https://github.com/users/vaquarkhan/packages/npm/package/mcp-test-suite-jest) ·
[Install guide](../DOWNLOADS.md)

Test an **Express**-hosted MCP server with YAML + Jest.

Example pack: [examples/frameworks/typescript/express/](../../examples/frameworks/typescript/express/)

## 1. Install

```bash
pip install "mcp-test-harness>=3.0.9,<4"
pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"
npm install -D @vaquarkhan/mcp-test-suite-jest@4.0.0   # GitHub Packages — see DOWNLOADS.md
```

## 2. Suite

```yaml
server:
  command: node dist/server.js
  transport: stdio
cases:
  - name: Echo
    call: echo
    args: { text: hello-express }
    tags: [smoke, express]
```

If MCP is exposed over HTTP from Express, use `transport: http` and the engine URL options instead of a stdio command.

## 3. Run

```bash
npm run build
mcp-suite run --suite mcp-suite.yaml --server-command "node dist/server.js"
```

Jest:

```ts
import { MCPClient } from "@vaquarkhan/mcp-test-suite-jest";

test("Express MCP suite", async () => {
  const client = new MCPClient({
    command: "node dist/server.js",
    suite: "mcp-suite.yaml",
  });
  await client.runSuite();
});
```

## Related

- [typescript.md](typescript.md) · [nestjs.md](nestjs.md) · [fastify.md](fastify.md)
