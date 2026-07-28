# PyPI publishing — disabled in this repository

**This repo (`mcp-test-suite`) does not publish to PyPI.**

| What | Where it publishes |
|------|--------------------|
| **Python engine / `mcp-test` CLI** | Only from **[vaquarkhan/mcp-test-harness](https://github.com/vaquarkhan/mcp-test-harness)** → PyPI `mcp-test-harness` |
| **Maven / npm / NuGet / Go adapters** | This repo → [PUBLISHING.md](PUBLISHING.md) · `publish-adapters.yml` |
| **Docker / GHCR** | This repo → `docker-publish.yml` (optional; image may still be built from harness) |

Workflows **removed** here on purpose:

- ~~`.github/workflows/publish.yml`~~ (was PyPI main package)
- ~~`.github/workflows/publish-packages.yml`~~ (was PyPI `packages/*` wheels)

Install the engine with:

```bash
pip install mcp-test-harness
# or
docker pull ghcr.io/vaquarkhan/mcp-test-harness:latest
```
