# Tutorial: Python (FastMCP / FastAPI)

## Install

```bash
pip install "mcp-test-harness>=3.0.9"
pip install .
```

## Path A — declarative (recommended for shared contracts)

```bash
mcp-suite run --suite examples/frameworks/python/fastmcp/mcp-suite.yaml \
  --server-command "python -m your_package.server"
```

See [examples/frameworks/python/](../../examples/frameworks/python/).

## Path B — Python API (engine)

```python
# tests/test_weather.py
from mcp_test_harness import assert_tool_call, assert_capabilities

async def test_echo(mcp_server):
    await assert_capabilities(mcp_server, tools=True)
    await assert_tool_call(mcp_server, "echo", {"text": "hi"})
```

```bash
mcp-test --server-command "python your_server.py" tests/
```

(`mcp-test` comes from the PyPI engine; `mcp-suite` adds YAML `run`.)

## Verify e2e locally

```bash
pytest tests/e2e/test_declarative_e2e.py -q
```
