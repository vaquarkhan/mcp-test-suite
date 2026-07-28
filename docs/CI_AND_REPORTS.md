# CI, reports, and the GitHub Action

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Java JAR](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/mcp-test-suite-junit5-4.0.0.jar) ·
[Node / npm tgz](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/vaquarkhan-mcp-test-suite-jest-4.0.0.tgz) ·
[Go module](https://pkg.go.dev/github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0) ·
[.NET nupkg](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/McpTestSuite.Xunit.4.0.0.nupkg) ·
[All release assets](https://github.com/vaquarkhan/mcp-test-suite/releases/tag/v4.0.0) ·
[Install guide](DOWNLOADS.md)

## Short answer

| Question | Answer |
|----------|--------|
| Must we publish reports publicly? | **No.** Non-zero exit code is enough to gate merges. |
| Keep artifacts for the team? | **Optional** — JUnit/JSON/HTML via the engine CLI. |
| Suite Action | Installs **mcp-test-harness** from PyPI + connectors; runs `mcp-suite` / `mcp-test`. |

## Recommended pattern

```yaml
- uses: vaquarkhan/mcp-test-suite@init
  with:
    suite-file: mcp-suite.yaml
    server-command: "node dist/server.js"
```

Or locally:

```bash
mcp-suite run --suite mcp-suite.yaml \
  --report-format junit --report-output junit.xml
```

Report formats are produced by the **engine** (`mcp-test-harness`). See that project’s docs for full reporter options.

## This repo’s CI

[`.github/workflows/validate.yml`](../.github/workflows/validate.yml) runs connector unit tests + `tests/e2e/` so language packs and `mcp-suite` breakages fail early.
