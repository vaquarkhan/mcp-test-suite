# `@vaquarkhan/mcp-test-suite-jest`

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Java JAR](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/mcp-test-suite-junit5-4.0.0.jar) ·
[Node / npm tgz](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/vaquarkhan-mcp-test-suite-jest-4.0.0.tgz) ·
[Go module](https://pkg.go.dev/github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0) ·
[.NET nupkg](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/McpTestSuite.Xunit.4.0.0.nupkg) ·
[All release assets](https://github.com/vaquarkhan/mcp-test-suite/releases/tag/v4.0.0) ·
[Install guide](../../docs/DOWNLOADS.md)

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
