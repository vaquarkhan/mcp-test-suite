# Tutorial: TypeScript / Node (Jest)

## Install engine + suite

```bash
pip install "mcp-test-harness>=3.0.9"
pip install .
# ensure mcp-suite is on PATH
```

## Link / install the Jest adapter

```bash
# GitHub Packages
npm install -D @vaquarkhan/mcp-test-suite-jest

# or from source
cd adapters/jest
npm install && npm run build && npm link
```

In your app (when using link):

```bash
npm link @vaquarkhan/mcp-test-suite-jest
```

## Shared suite

```yaml
# mcp-suite.yaml
server:
  command: node dist/main.js
  transport: stdio
cases:
  - name: Health
    call: ping
    args: {}
```

## Spec

```ts
import { MCPClient } from "@vaquarkhan/mcp-test-suite-jest";

const server = new MCPClient({
  command: "node dist/main.js",
  suite: "mcp-suite.yaml",
  // binary defaults to mcp-suite
});

test("MCP suite", async () => {
  await server.runSuite();
});
```

Or CLI-only (no Jest):

```bash
mcp-suite run --suite mcp-suite.yaml --server-command "node dist/main.js"
```

Examples: [examples/frameworks/typescript/](../../examples/frameworks/typescript/) (Nest, Express, Fastify).
