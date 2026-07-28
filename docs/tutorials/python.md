# Tutorial: Python (overview)

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Install guide](../DOWNLOADS.md)

Python teams can use **declarative YAML** (`mcp-suite`) and/or the **engine API** (`mcp-test` + assertions).

## Framework tutorials

| Stack | Tutorial |
|-------|----------|
| FastMCP | [fastmcp.md](fastmcp.md) |
| FastAPI | [fastapi.md](fastapi.md) |
| YAML only | [yaml.md](yaml.md) |

## Install

```bash
pip install "mcp-test-harness>=3.0.9,<4"
pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"
```

## Path A — declarative

```bash
mcp-suite run --suite mcp-suite.yaml --server-command "python server.py"
```

## Path B — engine API

```python
from mcp_test_harness import assert_tool_call, assert_capabilities

async def test_echo(mcp_server):
    await assert_capabilities(mcp_server, tools=True)
    await assert_tool_call(mcp_server, "echo", {"text": "hi"})
```

```bash
mcp-test --server-command "python server.py" tests/
```

Examples: [examples/frameworks/python/](../../examples/frameworks/python/)
