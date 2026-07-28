# Downloads (v4.0.0)

**Package downloads:**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Java JAR](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/mcp-test-suite-junit5-4.0.0.jar) ·
[Node / npm tgz](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/vaquarkhan-mcp-test-suite-jest-4.0.0.tgz) ·
[Go module](https://pkg.go.dev/github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0) ·
[.NET nupkg](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/McpTestSuite.Xunit.4.0.0.nupkg) ·
[All release assets](https://github.com/vaquarkhan/mcp-test-suite/releases/tag/v4.0.0)

**Engine (PyPI):** [`mcp-test-harness`](https://pypi.org/project/mcp-test-harness/)  
**Adapters:** GitHub Packages + [Release v4.0.0](https://github.com/vaquarkhan/mcp-test-suite/releases/tag/v4.0.0)

| You use | Install |
|---------|---------|
| **Python engine / CLI** | `pip install mcp-test-harness` |
| **Suite connectors (`mcp-suite`)** | `pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"` |
| **Java / Kotlin** | Maven from **GitHub Packages** (below) or download JAR from Releases |
| **Node / TypeScript** | npm from **GitHub Packages** `@vaquarkhan/mcp-test-suite-jest` |
| **Go** | `go get github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0` |
| **.NET** | NuGet from **GitHub Packages** `McpTestSuite.Xunit` |
| **Any / CI** | Docker build or [GitHub Action](../action.yml) |

---

## 0. Engine (required for every language)

```bash
pip install "mcp-test-harness>=3.0.9"
mcp-test --version

# Declarative CLI from this repo
pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"
mcp-suite --version
```

PyPI: https://pypi.org/project/mcp-test-harness/

---

## 1. Java / Kotlin — Maven (GitHub Packages)

**Coordinates:** `io.github.vaquarkhan:mcp-test-suite-junit5:4.0.0`

### `~/.m2/settings.xml` (one-time)

```xml
<settings>
  <servers>
    <server>
      <id>github</id>
      <username>YOUR_GITHUB_USERNAME</username>
      <!-- classic PAT with read:packages (and write:packages if you publish) -->
      <password>YOUR_GITHUB_PAT</password>
    </server>
  </servers>
</settings>
```

### `pom.xml`

```xml
<repositories>
  <repository>
    <id>github</id>
    <url>https://maven.pkg.github.com/vaquarkhan/mcp-test-suite</url>
  </repository>
</repositories>

<dependency>
  <groupId>io.github.vaquarkhan</groupId>
  <artifactId>mcp-test-suite-junit5</artifactId>
  <version>4.0.0</version>
  <scope>test</scope>
</dependency>
```

### Gradle

```kotlin
repositories {
  maven {
    url = uri("https://maven.pkg.github.com/vaquarkhan/mcp-test-suite")
    credentials {
      username = project.findProperty("gpr.user") as String? ?: System.getenv("GITHUB_ACTOR")
      password = project.findProperty("gpr.key") as String? ?: System.getenv("GITHUB_TOKEN")
    }
  }
}
dependencies {
  testImplementation("io.github.vaquarkhan:mcp-test-suite-junit5:4.0.0")
}
```

### No registry? Install from source or Release JAR

```bash
git clone https://github.com/vaquarkhan/mcp-test-suite.git
cd mcp-test-suite/adapters/junit5 && mvn -q clean install
```

Or download the JAR from https://github.com/vaquarkhan/mcp-test-suite/releases

---

## 2. Node / TypeScript — npm (GitHub Packages)

**Package:** `@vaquarkhan/mcp-test-suite-jest@4.0.0`

### `.npmrc` (project or user)

```ini
@vaquarkhan:registry=https://npm.pkg.github.com
//npm.pkg.github.com/:_authToken=YOUR_GITHUB_PAT
```

```bash
npm install -D @vaquarkhan/mcp-test-suite-jest
```

### No registry? Link from source

```bash
cd adapters/jest && npm install && npm run build && npm link
# in your app:
npm link @vaquarkhan/mcp-test-suite-jest
```

Or install the `.tgz` from [Releases](https://github.com/vaquarkhan/mcp-test-suite/releases):

```bash
npm install -D ./mcp-test-suite-jest-4.0.0.tgz
```

---

## 3. Go — module (live via git tag)

```bash
go get github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0
```

---

## 4. .NET — NuGet (GitHub Packages)

```bash
dotnet nuget add source "https://nuget.pkg.github.com/vaquarkhan/index.json" \
  --name github \
  --username YOUR_GITHUB_USERNAME \
  --password YOUR_GITHUB_PAT \
  --store-password-in-clear-text

dotnet add package McpTestSuite.Xunit --version 4.0.0
```

Or add a `PackageReference` after downloading the `.nupkg` from Releases.

---

## 5. Docker

```bash
git clone https://github.com/vaquarkhan/mcp-test-suite.git
cd mcp-test-suite
docker build -t mcp-test-suite:local .
docker run --rm mcp-test-suite:local --version
```

---

## 6. GitHub Action

```yaml
- uses: vaquarkhan/mcp-test-suite@init
  with:
    suite-file: mcp-suite.yaml
    server-command: "node dist/server.js"
```

---

## Publish (maintainers)

```text
Actions → Publish language adapters → version 4.0.0 → dry_run false
```

That workflow publishes to **GitHub Packages** and creates/updates **Release `v4.0.0`** with JAR / tgz / nupkg assets. See [PUBLISHING.md](PUBLISHING.md).
