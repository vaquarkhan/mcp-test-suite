# Tutorial: NestJS (TypeScript)

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Node / npm](https://github.com/users/vaquarkhan/packages/npm/package/mcp-test-suite-jest) ·
[Install guide](../DOWNLOADS.md)

Test a **NestJS** MCP server with `mcp-suite.yaml` and the Jest adapter.

Example pack: [examples/frameworks/typescript/nestjs/](../../examples/frameworks/typescript/nestjs/)

## 1. Install engine + suite

```bash
pip install "mcp-test-harness>=3.0.9,<4"
pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"
```

## 2. Install Jest adapter

**Package page:** [@vaquarkhan/mcp-test-suite-jest](https://github.com/users/vaquarkhan/packages/npm/package/mcp-test-suite-jest)

```ini
# .npmrc
@vaquarkhan:registry=https://npm.pkg.github.com
//npm.pkg.github.com/:_authToken=YOUR_GITHUB_PAT
```

```bash
npm install -D @vaquarkhan/mcp-test-suite-jest@4.0.0
```

## 3. Suite

```yaml
# mcp-suite.yaml
server:
  command: node dist/main.js
  transport: stdio
cases:
  - name: Health / ping
    call: ping
    args: {}
    tags: [smoke, nestjs]
  - name: Echo
    call: echo
    args: { text: hello-nest }
    tags: [smoke, nestjs]
```

## 4. Run (CLI)

```bash
npm run build
mcp-suite run --suite mcp-suite.yaml --server-command "node dist/main.js"
mcp-test try --server-command "node dist/main.js"
```

## 5. Run (Jest)

```ts
import { MCPClient } from "@vaquarkhan/mcp-test-suite-jest";

const client = new MCPClient({
  command: "node dist/main.js",
  suite: "mcp-suite.yaml",
});

test("NestJS MCP suite", async () => {
  await client.runSuite();
});
```

```bash
npx jest
```

## NestJS notes

- Build before CI (`nest build` / `tsc`) so `dist/main.js` exists.
- Do not write logs to stdout on stdio MCP.
- Align `call` names with Nest MCP tool handlers.

## Related

- [typescript.md](typescript.md) · [express.md](express.md) · [fastify.md](fastify.md)
