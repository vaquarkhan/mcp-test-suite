# Downloads & worldwide distribution

**Current version (planned):** `4.0.0`

## Status — read this first

| Package | Live? | Why 404? |
|---------|-------|----------|
| `mcp-test-harness` (PyPI) | **Yes** | Published from [mcp-test-harness](https://github.com/vaquarkhan/mcp-test-harness) |
| `ghcr.io/vaquarkhan/mcp-test-suite` | **No** | This repo has not pushed its own GHCR image yet |
| `mcp-test-suite-junit5` (Maven) | **No** | Never uploaded to Central yet |
| `@mcp-test-suite/jest` (npm) | **No** | Never `npm publish` yet |
| `McpTestSuite.Xunit` (NuGet) | **No** | Never pushed to nuget.org yet |
| `adapters/gotest` (Go) | **No** | Needs public GitHub repo + module tag |

The Maven / npm / NuGet / pkg.go.dev URLs below are **future** links. They return **404 until the first successful publish**.  
To go live: follow **[PUBLISHING.md](PUBLISHING.md)** (Sonatype, npm token, NuGet key, push repo + tags).

### Works today (no registry required)

```bash
pip install mcp-test-harness
docker build -t mcp-test-suite:local .

# Adapters from this source tree
cd adapters/junit5 && mvn -q clean install
cd adapters/jest && npm install && npm run build
```

---

## Quick pick (by language)

| You use | Install from | Coordinates / command |
|---------|--------------|------------------------|
| **Any language / CI** | Docker (local now, GHCR after first publish) | `docker build -t mcp-test-suite:local .` |
| **Any language** | GitHub Releases (binary) | [Releases](https://github.com/vaquarkhan/mcp-test-suite/releases) → `mcp-test` |
| **Python** | PyPI (**from mcp-test-harness only**) | `pip install mcp-test-harness` |
| **Java / Spring / Quarkus / Micronaut / Kotlin** | **Maven Central** | `io.github.vaquarkhan:mcp-test-suite-junit5:4.0.0` |
| **Gradle** | Maven Central | same GAV as Maven |
| **Node / Nest / Express / Fastify** | **npm** | `npm i -D @mcp-test-suite/jest` |
| **Go** | Go module proxy | `go get github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0` |
| **.NET / ASP.NET** | **NuGet** | `dotnet add package McpTestSuite.Xunit --version 4.0.0` |
| **GitHub Actions** | Marketplace / this repo | `uses: vaquarkhan/mcp-test-suite@v4.0.0` |

> **PyPI is not published from this repo.** The Python engine ships from [mcp-test-harness](https://github.com/vaquarkhan/mcp-test-harness). See [NO_PYPI_FROM_THIS_REPO.md](NO_PYPI_FROM_THIS_REPO.md).

> Until first publish of each *adapter* registry completes, install from **GitHub source** (paths below) or build the **Docker** image locally / `pip install mcp-test-harness` for the engine.

---

## 1. Maven Central (Java / Kotlin) — **planned (not live)**

> Status: **unpublished**. Central / MVN links will 404 until `mvn deploy` succeeds.

**Group:** `io.github.vaquarkhan`  
**Artifact:** `mcp-test-suite-junit5`  
**Version:** `4.0.0`

### Maven (`pom.xml`)

```xml
<dependency>
  <groupId>io.github.vaquarkhan</groupId>
  <artifactId>mcp-test-suite-junit5</artifactId>
  <version>4.0.0</version>
  <scope>test</scope>
</dependency>
```

### Gradle (Kotlin DSL)

```kotlin
testImplementation("io.github.vaquarkhan:mcp-test-suite-junit5:4.0.0")
```

### Gradle (Groovy)

```groovy
testImplementation 'io.github.vaquarkhan:mcp-test-suite-junit5:4.0.0'
```

### Browse

| Site | URL |
|------|-----|
| Maven Central Search | https://central.sonatype.com/artifact/io.github.vaquarkhan/mcp-test-suite-junit5 |
| MVN Repository | https://mvnrepository.com/artifact/io.github.vaquarkhan/mcp-test-suite-junit5 |
| Badge | `https://img.shields.io/maven-central/v/io.github.vaquarkhan/mcp-test-suite-junit5` |

**Also required:** the `mcp-test` engine on PATH (PyPI, Docker, or release binary) — the JUnit adapter orchestrates the CLI; it does not embed the Python engine.

### Local install (before Central is live)

```bash
cd adapters/junit5
mvn -q clean install
```

---

## 2. npm (TypeScript / Node) — **planned (not live)**

> Status: **unpublished**. npmjs.com link will 404 until `npm publish`.

```bash
npm install -D @mcp-test-suite/jest
# or
yarn add -D @mcp-test-suite/jest
# or
pnpm add -D @mcp-test-suite/jest
```

| Site | URL |
|------|-----|
| npm package | https://www.npmjs.com/package/@mcp-test-suite/jest |
| Badge | `https://img.shields.io/npm/v/@mcp-test-suite/jest` |

---

## 3. PyPI (Python engine + CLI) — **not published from this repo**

Install from the **mcp-test-harness** project (canonical PyPI package):

```bash
pip install mcp-test-harness
mcp-test --version
mcp-test run --suite mcp-suite.yaml
```

| Site | URL |
|------|-----|
| PyPI | https://pypi.org/project/mcp-test-harness/ |
| Source repo | https://github.com/vaquarkhan/mcp-test-harness |
| Badge | `https://img.shields.io/pypi/v/mcp-test-harness` |

This suite repo publishes **Maven / npm / NuGet / Go** adapters only — see [PUBLISHING.md](PUBLISHING.md).

---

## 4. Go modules — **planned (not live)**

> Status: **unpublished**. Needs the `mcp-test-suite` GitHub repo public + tag `adapters/gotest/v4.0.0`.

```bash
go get github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0
```

Module path: `github.com/vaquarkhan/mcp-test-suite/adapters/gotest`  
pkg.go.dev: https://pkg.go.dev/github.com/vaquarkhan/mcp-test-suite/adapters/gotest

---

## 5. NuGet (.NET) — **planned (not live)**

> Status: **unpublished**. nuget.org link will 404 until `dotnet nuget push`.

```bash
dotnet add package McpTestSuite.Xunit --version 4.0.0
```

Or `PackageReference`:

```xml
<PackageReference Include="McpTestSuite.Xunit" Version="4.0.0" />
```

| Site | URL |
|------|-----|
| NuGet.org | https://www.nuget.org/packages/McpTestSuite.Xunit |
| Badge | `https://img.shields.io/nuget/v/McpTestSuite.Xunit` |

### Local pack (before NuGet.org is live)

```bash
cd adapters/xunit
dotnet pack -c Release -o ../../dist/nuget
dotnet nuget push ../../dist/nuget/*.nupkg --api-key $NUGET_API_KEY --source https://api.nuget.org/v3/index.json
```

---

## 6. Docker / GHCR (universal)

Works for every language. Until the first GHCR push from this repo, build locally:

```bash
docker build -t mcp-test-suite:local .
# pin:
docker build -t mcp-test-suite:4.0.0 .

docker run --rm -v "$PWD":/work -w /work \
  mcp-test-suite:local \
  run --suite mcp-suite.yaml --server-command "node build/index.js"
```

| Site | URL |
|------|-----|
| GHCR package | https://github.com/vaquarkhan/mcp-test-suite/pkgs/container/mcp-test-suite |
| Docs | [DOCKER.md](DOCKER.md) |

Target image after first publish: `ghcr.io/vaquarkhan/mcp-test-suite:latest`.

---

## 7. GitHub Releases (standalone binary)

For air-gapped or non-Python hosts:

1. Open https://github.com/vaquarkhan/mcp-test-suite/releases  
2. Download `mcp-test` for your OS (`linux-amd64`, `darwin-arm64`, `windows-amd64.exe`)  
3. `chmod +x mcp-test` and put it on `PATH`

Build locally:

```bash
pip install -e ".[dev]"
python scripts/build_binary.py
# → dist/mcp-test
```

---

## 8. GitHub Action (CI worldwide)

```yaml
- uses: vaquarkhan/mcp-test-suite@v4.0.0
  with:
    server-command: "java -jar target/app.jar"
    suite-file: mcp-suite.yaml
    pr-comment: "true"
```

Legacy: `vaquarkhan/mcp-test-harness@v3.0.9` still runs the Python suite path.

---

## Maintainer: publish checklist (make it world-available)

| Registry | One-time setup | Publish command / workflow |
|----------|----------------|----------------------------|
| **PyPI** | **Disabled here** — publish only from `mcp-test-harness` | — |
| **GHCR** | Packages write permission | Same tag → `docker-publish.yml` |
| **Maven Central** | Sonatype Central Portal account + GPG | See [PUBLISHING.md](PUBLISHING.md) · `adapters/junit5` |
| **npm** | npm org `@mcp-test-suite` | `npm publish` from `adapters/jest` |
| **NuGet** | nuget.org API key | `dotnet nuget push` from `adapters/xunit` |
| **Go** | Tag `gotest/v4.0.0` or monorepo module path | `git tag` + push |
| **GitHub Releases** | Softprops/action-gh-release + PyInstaller matrix | Attach binaries to `v*` release |

Full steps: **[PUBLISHING.md](PUBLISHING.md)**.

---

## Badges (copy into README)

```markdown
[![PyPI](https://img.shields.io/pypi/v/mcp-test-harness)](https://pypi.org/project/mcp-test-harness/)
[![Maven Central](https://img.shields.io/maven-central/v/io.github.vaquarkhan/mcp-test-suite-junit5)](https://central.sonatype.com/artifact/io.github.vaquarkhan/mcp-test-suite-junit5)
[![npm](https://img.shields.io/npm/v/@mcp-test-suite/jest)](https://www.npmjs.com/package/@mcp-test-suite/jest)
[![NuGet](https://img.shields.io/nuget/v/McpTestSuite.Xunit)](https://www.nuget.org/packages/McpTestSuite.Xunit)
[![GHCR](https://img.shields.io/badge/ghcr.io-mcp--test--harness-2496ed?logo=docker)](https://github.com/vaquarkhan/mcp-test-harness/pkgs/container/mcp-test-harness)
```
