# Releasing (mcp-test-suite)

## Policy: no PyPI from this repo

**PyPI is not published from `mcp-test-suite`.**  
Python wheels (`mcp-test-harness`) ship only from  
https://github.com/vaquarkhan/mcp-test-harness (see that repo’s `publish.yml`).

Details: [NO_PYPI_FROM_THIS_REPO.md](NO_PYPI_FROM_THIS_REPO.md).

---

## What *this* repo publishes

| Artifact | Trigger | Workflow |
|----------|---------|----------|
| **Maven Central** (`mcp-test-suite-junit5`) | `workflow_dispatch` → adapters | [publish-adapters.yml](../.github/workflows/publish-adapters.yml) |
| **npm** (`@vaquarkhan/mcp-test-suite-jest`) | same | same |
| **NuGet** (`McpTestSuite.Xunit`) | same | same |
| **Go module** | git tag `adapters/gotest/v*` | push tag (no PyPI) |
| **GHCR Docker** (optional) | tag `v*` | [docker-publish.yml](../.github/workflows/docker-publish.yml) |

## Release checklist (adapters)

1. Bump versions in `adapters/*/pom.xml`, `package.json`, `.csproj`, `go.mod` tags.
2. Update [CHANGELOG.md](../CHANGELOG.md) and [DOWNLOADS.md](DOWNLOADS.md).
3. Run **Actions → Publish language adapters** (`dry_run: false`, target `all` or one adapter).
4. Tag Go module if needed: `git tag adapters/gotest/v4.0.0 && git push origin adapters/gotest/v4.0.0`.
5. For the **Python engine**, cut the release in **mcp-test-harness**, not here.

## Docker tags (optional, this repo)

If `docker-publish.yml` runs on `v*`:

```bash
docker pull ghcr.io/vaquarkhan/mcp-test-harness:latest
```

Prefer keeping GHCR publishing on the harness repo if you want a single image source of truth.
