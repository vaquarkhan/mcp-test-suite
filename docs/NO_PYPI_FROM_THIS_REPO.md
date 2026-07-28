# PyPI publishing — disabled in this repository

**This repo (`mcp-test-suite`) does not publish the MCP test *engine* to PyPI.**

| What | Where it comes from |
|------|---------------------|
| **Python engine / core `mcp-test` CLI** | **[vaquarkhan/mcp-test-harness](https://github.com/vaquarkhan/mcp-test-harness)** → PyPI [`mcp-test-harness`](https://pypi.org/project/mcp-test-harness/) |
| **Declarative YAML + CLI wrapper + language adapters** | This repo (depends on the PyPI engine; **no vendored copy**) |
| **Maven / npm / NuGet / Go adapters** | This repo → [PUBLISHING.md](PUBLISHING.md) · `publish-adapters.yml` |
| **Docker / GHCR** | This repo → `docker-publish.yml` (image installs harness from PyPI) |

Workflows **removed** here on purpose:

- ~~`.github/workflows/publish.yml`~~ (was PyPI main package)
- ~~`.github/workflows/publish-packages.yml`~~ (was PyPI `packages/*` wheels)

Install:

```bash
# Engine only
pip install mcp-test-harness

# Suite connectors (declarative `mcp-test run` / `mcp-suite`) from this repo
pip install "mcp-test-harness>=3.0.9"
pip install .

# Or pull the suite image (engine + connectors)
docker pull ghcr.io/vaquarkhan/mcp-test-suite:latest
```

When the harness publishes a new version on PyPI, bump or refresh the dependency here — you do **not** need to copy engine source into this repository.
