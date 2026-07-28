# `@vaquarkhan/mcp-test-suite-jest`

## Install (GitHub Packages)

```ini
# .npmrc
@vaquarkhan:registry=https://npm.pkg.github.com
//npm.pkg.github.com/:_authToken=YOUR_GITHUB_PAT
```

```bash
npm install -D @vaquarkhan/mcp-test-suite-jest
```

Or download the `.tgz` from [Releases](https://github.com/vaquarkhan/mcp-test-suite/releases).

Engine: `pip install mcp-test-harness` + `pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"` (`mcp-suite` on PATH).

## Usage

```typescript
import { MCPClient } from "@vaquarkhan/mcp-test-suite-jest";

test("suite", async () => {
  const server = new MCPClient({ command: "node dist/main.js", suite: "mcp-suite.yaml" });
  await expect(server.runSuite()).resolves.toMatchObject({ ok: true });
});
```

Examples: [examples/frameworks/typescript](../../examples/frameworks/typescript/) · [docs/DOWNLOADS.md](../../docs/DOWNLOADS.md)
