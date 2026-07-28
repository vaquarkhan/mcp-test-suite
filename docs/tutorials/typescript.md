# Tutorial: TypeScript / Node (Jest)

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Java JAR](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/mcp-test-suite-junit5-4.0.0.jar) ·
[Node / npm tgz](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/vaquarkhan-mcp-test-suite-jest-4.0.0.tgz) ·
[Go module](https://pkg.go.dev/github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0) ·
[.NET nupkg](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/McpTestSuite.Xunit.4.0.0.nupkg) ·
[All release assets](https://github.com/vaquarkhan/mcp-test-suite/releases/tag/v4.0.0) ·
[Install guide](../DOWNLOADS.md)

## Install engine + suite

```bash
pip install "mcp-test-harness>=3.0.9"
pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"
# ensure mcp-suite is on PATH
```

## Link / install the Jest adapter

Add `.npmrc` (GitHub Packages requires a PAT with `read:packages`):

```ini
@vaquarkhan:registry=https://npm.pkg.github.com
//npm.pkg.github.com/:_authToken=YOUR_GITHUB_PAT
```

```bash
npm install -D @vaquarkhan/mcp-test-suite-jest

# or from Release / source
# npm install -D ./vaquarkhan-mcp-test-suite-jest-4.0.0.tgz
cd adapters/jest && npm install && npm run build && npm link
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
