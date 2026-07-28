# Tutorial: Fastify (TypeScript)

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Node / npm](https://github.com/users/vaquarkhan/packages/npm/package/mcp-test-suite-jest) ·
[Install guide](../DOWNLOADS.md)

Test a **Fastify** MCP server with `mcp-suite` / Jest.

Example pack: [examples/frameworks/typescript/fastify/](../../examples/frameworks/typescript/fastify/)

## 1. Install

```bash
pip install "mcp-test-harness>=3.0.9,<4"
pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"
npm install -D @vaquarkhan/mcp-test-suite-jest@4.0.0
```

([npm package page](https://github.com/users/vaquarkhan/packages/npm/package/mcp-test-suite-jest))

## 2. Suite

```yaml
server:
  command: node dist/app.js
  transport: stdio
cases:
  - name: Echo
    call: echo
    args: { text: hello-fastify }
    tags: [smoke, fastify]
```

## 3. Run

```bash
npm run build
mcp-suite run --suite mcp-suite.yaml --server-command "node dist/app.js"
npx jest   # if using MCPClient in *.mcp.spec.ts
```

## Related

- [typescript.md](typescript.md) · [express.md](express.md) · [nestjs.md](nestjs.md)
