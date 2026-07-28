# Tutorial: FastAPI (Python)

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Install guide](../DOWNLOADS.md)

Test MCP tools attached to a **FastAPI** app (stdio sidecar or HTTP transport).

Example pack: [examples/frameworks/python/fastapi/](../../examples/frameworks/python/fastapi/)

## 1. Install

```bash
pip install "mcp-test-harness>=3.0.9"
pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"
```

## 2. Suite (stdio MCP process)

```yaml
server:
  command: python -m app.mcp_server
  transport: stdio
cases:
  - name: Echo
    call: echo
    args: { text: hello-fastapi }
    tags: [smoke, fastapi]
```

## 3. Run

```bash
mcp-suite run --suite mcp-suite.yaml --server-command "python -m app.mcp_server"
```

If MCP is served over HTTP from FastAPI:

```yaml
server:
  # use engine HTTP/SSE URL options — see mcp-test-harness docs
  transport: http
```

## 4. Mixed: YAML + pytest

Keep contracts in `mcp-suite.yaml` for all languages; add Python-only deep tests with `mcp-test` + `assert_*` when needed ([python.md](python.md)).

## Related

- [fastmcp.md](fastmcp.md) · [python.md](python.md)
