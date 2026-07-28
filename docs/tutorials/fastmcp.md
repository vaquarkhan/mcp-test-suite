# Tutorial: FastMCP (Python)

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Install guide](../DOWNLOADS.md)

Test a **FastMCP** stdio server with declarative YAML and/or the engine Python API.

Example pack: [examples/frameworks/python/fastmcp/](../../examples/frameworks/python/fastmcp/)

## 1. Install

```bash
pip install "mcp-test-harness>=3.0.9,<4"
pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"
pip install "mcp>=1.2,<2"   # FastMCP lives in the mcp SDK (1.x)
```

## 2. Suite

```yaml
server:
  command: python server.py
  transport: stdio
cases:
  - name: Echo
    call: echo
    args: { text: hello-fastmcp }
    tags: [smoke, fastmcp]
  - name: Latency
    call: echo
    args: { text: ping }
    max_latency_ms: 3000
    tags: [perf]
```

## 3. Path A — declarative (recommended)

```bash
mcp-suite run --suite mcp-suite.yaml --server-command "python server.py"
mcp-suite run --suite mcp-suite.yaml --report-format html --report-output report.html
mcp-test try --server-command "python server.py"
```

## 4. Path B — Python assertions (engine)

```python
# tests/test_echo.py
from mcp_test_harness import assert_tool_call, assert_capabilities

async def test_echo(mcp_server):
    await assert_capabilities(mcp_server, tools=True)
    await assert_tool_call(mcp_server, "echo", {"text": "hi"})
```

```bash
mcp-test --server-command "python server.py" tests/
```

## FastMCP notes

- Pin `mcp>=1.2,<2` until the harness supports SDK 2.0 stdio types.
- FastMCP must not print to stdout (JSON-RPC channel).
- This suite’s CI fixture uses a stdlib NDJSON server; your app can still use FastMCP.

## Related

- [python.md](python.md) · [fastapi.md](fastapi.md) · [yaml.md](yaml.md)
