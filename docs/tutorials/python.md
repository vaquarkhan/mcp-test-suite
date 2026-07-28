# Tutorial: Python (FastMCP / FastAPI)

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Java JAR](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/mcp-test-suite-junit5-4.0.0.jar) ·
[Node / npm tgz](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/vaquarkhan-mcp-test-suite-jest-4.0.0.tgz) ·
[Go module](https://pkg.go.dev/github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0) ·
[.NET nupkg](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/McpTestSuite.Xunit.4.0.0.nupkg) ·
[All release assets](https://github.com/vaquarkhan/mcp-test-suite/releases/tag/v4.0.0) ·
[Install guide](../DOWNLOADS.md)

## Install

```bash
pip install "mcp-test-harness>=3.0.9"
pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"
# or: pip install .   # from a clone
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
