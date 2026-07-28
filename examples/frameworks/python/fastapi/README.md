# FastAPI MCP — test pack

For Streamable HTTP / SSE endpoints:

```bash
# Terminal 1
uvicorn server:app --port 8000

# Terminal 2
mcp-test run --suite mcp-suite.yaml \
  --transport http \
  --server-command "http://127.0.0.1:8000/mcp"
```
