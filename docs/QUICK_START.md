# Quick start (mcp-test-suite)

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Java JAR](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/mcp-test-suite-junit5-4.0.0.jar) ·
[Node / npm tgz](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/vaquarkhan-mcp-test-suite-jest-4.0.0.tgz) ·
[Go module](https://pkg.go.dev/github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0) ·
[.NET nupkg](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/McpTestSuite.Xunit.4.0.0.nupkg) ·
[All release assets](https://github.com/vaquarkhan/mcp-test-suite/releases/tag/v4.0.0) ·
[Install guide](DOWNLOADS.md)

Minimal path from zero to a green MCP suite. Engine deep-dives live in [mcp-test-harness](https://github.com/vaquarkhan/mcp-test-harness).

## 1. Install engine + connectors

```bash
pip install "mcp-test-harness>=3.0.9"
pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"
mcp-suite --version
```

## 2. Add `mcp-suite.yaml`

```yaml
server:
  command: python tests/fixtures/minimal_mcp_server.py
  transport: stdio
cases:
  - name: Echo
    call: echo
    args: { text: hello }
```

(From the suite repo root you can also use [examples/declarative/mcp-suite.yaml](../examples/declarative/mcp-suite.yaml).)

## 3. Run

```bash
mcp-suite run --suite mcp-suite.yaml
```

## 4. Pick your language

| Next | Doc |
|------|-----|
| Shared YAML only | [tutorials/yaml.md](tutorials/yaml.md) |
| Node / Java / Go / .NET / Rust / Python | [tutorials/](tutorials/) |
| Framework copy-paste packs | [examples/frameworks/](../examples/frameworks/) |
| CI Action | [../action.yml](../action.yml) |
| Docker | [DOCKER.md](DOCKER.md) |

## 5. Prove it (e2e)

```bash
pip install -e ".[dev]"
pytest tests/e2e/ -q
```

These tests drive a **real** stdio MCP fixture through `mcp-suite` and validate every language pack’s `mcp-suite.yaml` parses — so connector breakages fail CI early.
