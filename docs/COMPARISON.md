# Ecosystem comparison (suite + engine)

**mcp-test-suite** is the multi-language connector layer.  
**mcp-test-harness** (PyPI) is the deterministic CI engine under it.

| Need | Use |
|------|-----|
| Shared YAML / Jest / JUnit / Go / .NET | **mcp-test-suite** (this repo) |
| Python assertions, transports, reports, chaos | **mcp-test-harness** |
| Interactive explore | [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) |
| Runtime security | [MCP-Bastion](https://github.com/vaquarkhan/MCP-Bastion) |
| IDE config scanning | [mcp-shark](https://github.com/mcp-shark/mcp-shark) |

This is **not** an LLM-eval product. It proves *your MCP server* still meets contracts before merge.

Tutorials: [tutorials/](tutorials/) · Positioning (engine): see harness repo docs after install.
