# Tutorial: declarative YAML (any language)

Write contracts once in `mcp-suite.yaml`. Every adapter and CI job reuses this file.

## 1. Install connectors + engine

```bash
pip install "mcp-test-harness>=3.0.9"
pip install .   # mcp-test-suite root
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

  - name: Unknown tool fails
    call: __does_not_exist__
    args: {}
    expect_error: true
```

## 3. Run (with the same reports Python teams use)

```bash
mcp-suite run --suite mcp-suite.yaml

# HTML dashboard / interactive report (engine feature — any language)
mcp-suite run --suite mcp-suite.yaml --report-format html --report-output report.html

# list cases without executing:
mcp-suite run --suite mcp-suite.yaml --list
```

You do **not** need Python `test_*.py` to get the HTML dashboard, JUnit, JSON, or SARIF — those come from the shared engine when you run `mcp-suite`.

## 4. CI

```yaml
- uses: ./   # or vaquarkhan/mcp-test-suite
  with:
    suite-file: mcp-suite.yaml
```

## Case fields (cheat sheet)

| Field | Meaning |
|-------|---------|
| `call` / `tool` | Tool name |
| `args` | Tool arguments |
| `expected` | Exact / partial expected payload |
| `assert_schema` | Named schema under `schemas:` |
| `max_latency_ms` | Latency budget |
| `expect_error` | Tool must fail |
| `resource` / `prompt` | Resource read or prompt get |
| `tags` | Filter with `-m` |

Full example: [../../examples/declarative/](../../examples/declarative/)
