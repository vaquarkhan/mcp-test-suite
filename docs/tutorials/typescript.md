# Tutorial: TypeScript / Node (overview)

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Node / npm](https://github.com/users/vaquarkhan/packages/npm/package/mcp-test-suite-jest) ·
[Install guide](../DOWNLOADS.md)

Use the **Jest adapter** (`@vaquarkhan/mcp-test-suite-jest`) or CLI-only `mcp-suite` for Node MCP servers.

## Framework tutorials

| Stack | Tutorial |
|-------|----------|
| NestJS | [nestjs.md](nestjs.md) |
| Express | [express.md](express.md) |
| Fastify | [fastify.md](fastify.md) |

## Install

```bash
pip install "mcp-test-harness>=3.0.9"
pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"
```

```ini
# .npmrc
@vaquarkhan:registry=https://npm.pkg.github.com
//npm.pkg.github.com/:_authToken=YOUR_GITHUB_PAT
```

```bash
npm install -D @vaquarkhan/mcp-test-suite-jest@4.0.0
```

[npm package page](https://github.com/users/vaquarkhan/packages/npm/package/mcp-test-suite-jest)

## Minimal Jest

```ts
import { MCPClient } from "@vaquarkhan/mcp-test-suite-jest";

test("MCP suite", async () => {
  const client = new MCPClient({
    command: "node dist/main.js",
    suite: "mcp-suite.yaml",
  });
  await client.runSuite();
});
```

CLI:

```bash
mcp-suite run --suite mcp-suite.yaml --server-command "node dist/main.js"
```

Examples: [examples/frameworks/typescript/](../../examples/frameworks/typescript/)
