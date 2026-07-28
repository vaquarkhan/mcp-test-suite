# Releasing (mcp-test-suite)

## Policy: no PyPI from this repo

**PyPI is not published from `mcp-test-suite`.**  
Python wheels (`mcp-test-harness`) ship only from  
https://github.com/vaquarkhan/mcp-test-harness (see that repo’s `publish.yml`).

Details: [NO_PYPI_FROM_THIS_REPO.md](NO_PYPI_FROM_THIS_REPO.md).

---

## What *this* repo publishes

| Artifact | Where | Trigger |
|----------|-------|---------|
| **Maven** `io.github.vaquarkhan:mcp-test-suite-junit5` | GitHub Packages + Release JAR | [publish-adapters.yml](../.github/workflows/publish-adapters.yml) |
| **npm** `@vaquarkhan/mcp-test-suite-jest` | GitHub Packages + Release `.tgz` | same |
| **NuGet** `McpTestSuite.Xunit` | GitHub Packages + Release `.nupkg` | same |
| **Go module** | git tag `adapters/gotest/v*` | push tag |
| **GHCR Docker** (optional) | tag `v*` | [docker-publish.yml](../.github/workflows/docker-publish.yml) |

Install coordinates: [DOWNLOADS.md](DOWNLOADS.md).

## Release checklist (adapters)

1. Bump versions in `adapters/*/pom.xml`, `package.json`, `.csproj`, Go tag.
2. Update [CHANGELOG.md](../CHANGELOG.md) and [DOWNLOADS.md](DOWNLOADS.md).
3. Run **Actions → Publish language adapters** (`dry_run: false`, version e.g. `4.0.0`).
4. Tag Go module if needed: `git tag adapters/gotest/v4.0.0 && git push origin adapters/gotest/v4.0.0`.
5. For the **Python engine**, cut the release in **mcp-test-harness**, not here.

## Engine constraint

Suite connectors pin `mcp>=1.2,<2` until `mcp-test-harness` supports MCP SDK 2.0 stdio types.
