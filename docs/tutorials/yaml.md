# Tutorial: declarative YAML (any language)

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Java / Maven](https://github.com/vaquarkhan/mcp-test-suite/packages/3158511) ·
[Node / npm](https://github.com/users/vaquarkhan/packages/npm/package/mcp-test-suite-jest) ·
[Go module](https://pkg.go.dev/github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0) ·
[.NET / NuGet](https://github.com/users/vaquarkhan/packages/nuget/package/McpTestSuite.Xunit) ·
[Install guide](../DOWNLOADS.md)

Write contracts once in `mcp-suite.yaml`. Every adapter and CI job reuses this file — no language-specific test code required for HTML / JUnit / JSON / SARIF reports.

## 1. Install

```bash
pip install "mcp-test-harness>=3.0.9"
pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"
mcp-suite --version
```

## 2. Create `mcp-suite.yaml`

```yaml
server:
  command: python tests/fixtures/minimal_mcp_server.py
  transport: stdio

cases:
  - name: Echo tool responds
    call: echo
    args: { text: hello }
    tags: [smoke]

  - name: Echo latency budget
    call: echo
    args: { text: ping }
    max_latency_ms: 5000
    tags: [perf]

  - name: Unknown tool fails
    call: __does_not_exist__
    args: {}
    expect_error: true
    tags: [negative]
```

## 3. Run

```bash
mcp-suite run --suite mcp-suite.yaml
mcp-suite run --suite mcp-suite.yaml --list
mcp-suite run --suite mcp-suite.yaml --report-format html --report-output report.html
mcp-suite run --suite mcp-suite.yaml --report-format junit --report-output junit.xml
```

Probe without a suite file:

```bash
mcp-test try --server-command "node dist/server.js"
```

## 4. CI

```yaml
- uses: vaquarkhan/mcp-test-suite@init
  with:
    suite-file: mcp-suite.yaml
    server-command: "node dist/server.js"
```

## Case fields

| Field | Meaning |
|-------|---------|
| `call` / `tool` | Tool name |
| `args` | Tool arguments |
| `expected` | Expected payload |
| `assert_schema` | Named schema under `schemas:` |
| `max_latency_ms` | Latency budget |
| `expect_error` | Tool/protocol must fail |
| `resource` / `prompt` | Resource read or prompt get |
| `tags` | Filter / CI grouping |

## Next

Pick your stack: [README.md](README.md) · Full example: [examples/declarative/](../../examples/declarative/)
