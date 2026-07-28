"""Python-native tests alongside declarative mcp-suite.yaml."""

from mcp_test_harness import assert_latency, assert_tool_call, marker


@marker(tags=["smoke", "fastmcp"])
async def test_echo(mcp_server):
    result = await assert_tool_call(mcp_server, "echo", {"text": "hi"})
    assert result is not None


@marker(tags=["perf", "fastmcp"])
async def test_echo_latency(mcp_server):
    await assert_latency(mcp_server, "echo", {"text": "ping"}, max_ms=2000)
