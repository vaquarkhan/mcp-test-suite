# CI, reports, and the GitHub Action

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
