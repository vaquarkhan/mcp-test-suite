# Publishing adapters worldwide

Maintainer guide to ship **mcp-test-suite** adapters to public registries.

## Policy

**Do not publish to PyPI from this repository.**  
The Python engine (`mcp-test-harness` / `mcp-test` CLI) is released only from  
https://github.com/vaquarkhan/mcp-test-harness — see [NO_PYPI_FROM_THIS_REPO.md](NO_PYPI_FROM_THIS_REPO.md).

## Order of publish (this repo)

1. **Maven Central** (JUnit 5)
2. **npm** (`@mcp-test-suite/jest`)
3. **NuGet** (`McpTestSuite.Xunit`)
4. **Go** module tag (`adapters/gotest`)
5. **GHCR** (optional Docker) via `docker-publish.yml`

---

## Maven Central — `mcp-test-suite-junit5`

### Coordinates

- **groupId:** `io.github.vaquarkhan`
- **artifactId:** `mcp-test-suite-junit5`
- **version:** align with repo (e.g. `4.0.0`)

### One-time

1. Create a [Central Portal](https://central.sonatype.com/) account (Sonatype).
2. Register namespace `io.github.vaquarkhan` (GitHub-verified OSS namespace).
3. Generate a GPG key and distribute the public key to a keyserver (`keys.openpgp.org`).
4. Add GitHub secrets: `JRELEASER_GPG_SECRET_KEY`, `JRELEASER_GPG_PASSPHRASE`, `CENTRAL_USERNAME`, `CENTRAL_PASSWORD`.

### Publish

```bash
cd adapters/junit5
mvn -B clean deploy
```

Or **Actions → Publish language adapters** (`target: junit5`, `dry_run: false`).

### Verify

```bash
curl -sI "https://repo1.maven.org/maven2/io/github/vaquarkhan/mcp-test-suite-junit5/4.0.0/mcp-test-suite-junit5-4.0.0.pom"
```

---

## npm — `@mcp-test-suite/jest`

```bash
cd adapters/jest
npm ci && npm run build
npm publish --access public
```

Secret: `NPM_TOKEN`.

---

## NuGet — `McpTestSuite.Xunit`

```bash
cd adapters/xunit
dotnet pack -c Release -o ../../dist/nuget
dotnet nuget push ../../dist/nuget/McpTestSuite.Xunit.*.nupkg \
  --api-key "$NUGET_API_KEY" \
  --source https://api.nuget.org/v3/index.json
```

---

## Go — `adapters/gotest`

```bash
git tag adapters/gotest/v4.0.0
git push origin adapters/gotest/v4.0.0
GOPROXY=proxy.golang.org go list -m github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0
```

---

## PyPI (engine) — use the other repo

```text
# In vaquarkhan/mcp-test-harness only:
git tag vX.Y.Z && git push origin vX.Y.Z
# → publish.yml → PyPI mcp-test-harness
```

---

## Announcement template

```text
mcp-test-suite adapters 4.0.0:

- Maven:  io.github.vaquarkhan:mcp-test-suite-junit5:4.0.0
- npm:    npm i -D @mcp-test-suite/jest
- NuGet:  dotnet add package McpTestSuite.Xunit
- Go:     go get github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0
- Engine: pip install mcp-test-harness   # from mcp-test-harness repo
- Docker: docker pull ghcr.io/vaquarkhan/mcp-test-harness:latest
- Docs:   https://github.com/vaquarkhan/mcp-test-suite/blob/main/docs/DOWNLOADS.md
```
