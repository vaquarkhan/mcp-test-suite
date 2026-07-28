# Publishing adapters

## Default (GitHub Packages + Release)

Workflow **Publish language adapters** publishes to:

1. **GitHub Packages** (Maven / npm / NuGet) using `GITHUB_TOKEN`
2. **GitHub Release** `vX.Y.Z` with JAR / `.tgz` / `.nupkg` assets

```text
Actions → Publish language adapters → version 4.0.0 → dry_run: false
```

Install instructions: [DOWNLOADS.md](DOWNLOADS.md)

**Go:** `git tag adapters/gotest/v4.0.0 && git push origin adapters/gotest/v4.0.0`

## Maven Central (JUnit adapter)

So the artifact appears in **Maven Central** search (like your other `io.github.vaquarkhan` libraries):

1. Follow **[MAVEN_CENTRAL.md](MAVEN_CENTRAL.md)** — create/add secrets:
   - `CENTRAL_USERNAME`
   - `CENTRAL_PASSWORD`
   - `GPG_PRIVATE_KEY`
   - `GPG_PASSPHRASE`
2. Run workflow with **`maven_central: true`**.

Coordinates: `io.github.vaquarkhan:mcp-test-suite-junit5:4.0.0`

The Python engine publishes from **mcp-test-harness** only — see [NO_PYPI_FROM_THIS_REPO.md](NO_PYPI_FROM_THIS_REPO.md).
