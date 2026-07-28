# Docker (OCI image with `mcp-test`)

**Pre-built (GHCR)** after a **`v*`** release: `docker pull ghcr.io/vaquarkhan/mcp-test-suite:latest` — see [../docs/RELEASING.md](../docs/RELEASING.md).

**Build** (from repo root — same as [README #docker](../README.md#docker)):

```bash
docker build -t mcp-test-suite:local .
docker run --rm mcp-test-suite:local --version
```

**Run harness against a mounted project** (POSIX):

```bash
docker run --rm -v "$PWD":/work -w /work mcp-test-suite:local .
```

**Dev image (pytest in container):** `docker build -t mcp-test-suite:dev --target dev .` then override `--entrypoint pytest` to run the suite.

**Deeper** (registries, `ghcr.io`, diagram): [DOCKER.md](../docs/DOCKER.md)
