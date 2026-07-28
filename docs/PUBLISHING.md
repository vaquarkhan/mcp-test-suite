# Publishing adapters

## Default (works today — no external secrets)

GitHub Actions workflow **Publish language adapters** publishes to:

1. **GitHub Packages** (Maven / npm / NuGet) using `GITHUB_TOKEN`
2. **GitHub Release** `vX.Y.Z` with JAR / `.tgz` / `.nupkg` assets

```text
Actions → Publish language adapters → version 4.0.0 → dry_run: false
```

Install instructions: [DOWNLOADS.md](DOWNLOADS.md)

**Go:** `git tag adapters/gotest/v4.0.0 && git push origin adapters/gotest/v4.0.0`

## Optional later (Maven Central / npmjs / nuget.org)

Requires secrets (`CENTRAL_*`, `NPM_TOKEN`, `NUGET_API_KEY`, GPG). Use profile `maven-central` in the JUnit POM. See historical notes in older commits if needed.

**Do not publish the Python engine from this repo** — PyPI `mcp-test-harness` only: [NO_PYPI_FROM_THIS_REPO.md](NO_PYPI_FROM_THIS_REPO.md).
