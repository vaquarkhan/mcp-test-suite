# Contributing (mcp-test-suite)

Thanks for helping improve **MCP Test Suite** (multi-language connectors over PyPI `mcp-test-harness`).

## Where things live

| What | Where |
|------|--------|
| Docs hub | [docs/README.md](docs/README.md) |
| Language tutorials | [docs/tutorials/](docs/tutorials/) |
| Framework examples | [examples/frameworks/](examples/frameworks/) |
| Adapters | [adapters/](adapters/) |
| Connector + e2e tests | [tests/](tests/) · [tests/e2e/](tests/e2e/) |
| Engine (not in this tree) | [mcp-test-harness](https://github.com/vaquarkhan/mcp-test-harness) |

## Develop & test

```bash
pip install "mcp-test-harness>=3.0.9,<4"
pip install -e ".[dev]"
python -m pytest tests/ -q
coverage run -m pytest tests/ -q
coverage report --fail-under=80
```

Engine bugfixes belong in **mcp-test-harness**. This repo accepts PRs for adapters, declarative YAML, tutorials, Docker/Action, and e2e smokes.

## Issues / PRs

Use [this repo’s Issues](https://github.com/vaquarkhan/mcp-test-suite/issues). Keep PRs focused; update tutorials when changing adapter CLI defaults.
