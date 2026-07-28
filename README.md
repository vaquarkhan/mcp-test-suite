<p align="center">
  <img src="./docs/images/hero-banner-suite.jpg" alt="MCP Test Suite - multi-language testing for MCP servers" width="100%" />
</p>

# MCP Test Suite

> **Multi-language connectors for MCP servers.** One shared `mcp-suite.yaml`. Native adapters for Node, Java, Go, and .NET. Engine from PyPI — never vendored here.

[![PyPI engine](https://img.shields.io/pypi/v/mcp-test-harness?label=engine%20(mcp-test-harness))](https://pypi.org/project/mcp-test-harness/)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![GHCR](https://img.shields.io/badge/ghcr.io-mcp--test--suite-2496ed?logo=github)](https://github.com/vaquarkhan/mcp-test-suite/pkgs/container/mcp-test-suite)
[![Downloads](https://img.shields.io/badge/docs-DOWNLOADS.md-0ea5e9)](docs/DOWNLOADS.md)

## How this relates to mcp-test-harness

| Repo | Role |
|------|------|
| **[mcp-test-harness](https://github.com/vaquarkhan/mcp-test-harness)** | **Main engine** — already on **[PyPI](https://pypi.org/project/mcp-test-harness/)**. Assertions, transports, HTML dashboard, reports. |
| **This repo (`mcp-test-suite`)** | **Connectors only** — declarative YAML, language adapters, Docker, GitHub Action. |

```bash
pip install "mcp-test-harness>=3.0.9"   # engine (PyPI — already live)
```

![Architecture](./docs/images/architecture-suite.jpg)

## Download & install (by language)

Full guide: **[docs/DOWNLOADS.md](docs/DOWNLOADS.md)** · Publish steps: **[docs/PUBLISHING.md](docs/PUBLISHING.md)**

### 1) Python engine (PyPI — live today)

```bash
pip install "mcp-test-harness>=3.0.9"
mcp-test --version
```

Optional: install this repo’s connectors (`mcp-suite` CLI) from GitHub:

```bash
pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"
# or clone and: pip install .
mcp-suite --version
```

### 2) Java / Kotlin — Maven

**Coordinates:** `io.github.vaquarkhan:mcp-test-suite-junit5:4.0.0`

**Maven `pom.xml`:**

```xml
<dependency>
  <groupId>io.github.vaquarkhan</groupId>
  <artifactId>mcp-test-suite-junit5</artifactId>
  <version>4.0.0</version>
  <scope>test</scope>
</dependency>
```

**Gradle (Kotlin DSL):**

```kotlin
testImplementation("io.github.vaquarkhan:mcp-test-suite-junit5:4.0.0")
```

**Until Maven Central is live**, install from this repo into your local `~/.m2`:

```bash
git clone https://github.com/vaquarkhan/mcp-test-suite.git
cd mcp-test-suite/adapters/junit5
mvn -q clean install
```

Also put the engine on PATH: `pip install mcp-test-harness` (adapters call `mcp-suite` / `mcp-test`).

Tutorial: [docs/tutorials/java.md](docs/tutorials/java.md)

### 3) Node / TypeScript — npm

```bash
npm install -D @mcp-test-suite/jest
# yarn add -D @mcp-test-suite/jest
# pnpm add -D @mcp-test-suite/jest
```

**Until npm publish is live**, link from source:

```bash
cd adapters/jest && npm install && npm run build && npm link
# in your app:
npm link @mcp-test-suite/jest
```

Tutorial: [docs/tutorials/typescript.md](docs/tutorials/typescript.md)

### 4) Go — module

```bash
go get github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0
```

Or with a local replace:

```go
require github.com/vaquarkhan/mcp-test-suite/adapters/gotest v0.0.0
replace github.com/vaquarkhan/mcp-test-suite/adapters/gotest => ../mcp-test-suite/adapters/gotest
```

Tutorial: [docs/tutorials/go.md](docs/tutorials/go.md)

### 5) .NET — NuGet

```bash
dotnet add package McpTestSuite.Xunit --version 4.0.0
```

**Until NuGet is live**, project-reference the adapter:

```xml
<ProjectReference Include="..\mcp-test-suite\adapters\xunit\McpTestSuite.Xunit.csproj" />
```

Tutorial: [docs/tutorials/dotnet.md](docs/tutorials/dotnet.md)

### 6) Docker / CI

```bash
docker build -t mcp-test-suite:local .
docker run --rm -v "$PWD":/work -w /work mcp-test-suite:local \
  run --suite mcp-suite.yaml --server-command "node dist/server.js"
```

```yaml
- uses: vaquarkhan/mcp-test-suite@init
  with:
    suite-file: mcp-suite.yaml
    server-command: "node dist/server.js"
```

---

## 60-second start (any language)

```yaml
# mcp-suite.yaml
server:
  command: node dist/server.js   # or java -jar … / go run … / python …
  transport: stdio
cases:
  - name: Echo works
    call: echo
    args: { text: hello }
```

```bash
mcp-suite run --suite mcp-suite.yaml --report-format html --report-output report.html
```

**Same dashboard & reports as Python** — HTML / JUnit / JSON / SARIF are engine features available to every language via `mcp-suite.yaml` (you do not need `test_*.py`).

![Multi-language](./docs/images/multi-language-suite.jpg)

![Features for any language](./docs/images/features-any-language.jpg)

## Language support

| Language | Download | Tutorial | Examples |
|----------|----------|----------|----------|
| **Any (YAML)** | PyPI engine + `mcp-suite` | [yaml](docs/tutorials/yaml.md) | [declarative/](examples/declarative/) |
| **Python** | `pip install mcp-test-harness` | [python](docs/tutorials/python.md) | [frameworks/python](examples/frameworks/python/) |
| **TypeScript** | `@mcp-test-suite/jest` | [typescript](docs/tutorials/typescript.md) | [frameworks/typescript](examples/frameworks/typescript/) |
| **Java / Kotlin** | Maven `mcp-test-suite-junit5` | [java](docs/tutorials/java.md) | [frameworks/java](examples/frameworks/java/) · [kotlin](examples/frameworks/kotlin/) |
| **Go** | `adapters/gotest` module | [go](docs/tutorials/go.md) | [frameworks/go](examples/frameworks/go/) |
| **.NET** | `McpTestSuite.Xunit` | [dotnet](docs/tutorials/dotnet.md) | [frameworks/dotnet](examples/frameworks/dotnet/) |
| **Rust** | YAML + CLI | [rust](docs/tutorials/rust.md) | [frameworks/rust](examples/frameworks/rust/) |

![Feature overview](./docs/images/feature-overview-suite.jpg)

## Cursor IDE

[docs/CURSOR_IDE.md](docs/CURSOR_IDE.md) · [`.cursorrules`](.cursorrules)

## End-to-end confidence

```bash
pip install -e ".[dev]"
python -m pytest tests/ -q   # includes tests/e2e/
```

![E2E](./docs/images/dogfood-e2e.jpg)

## Docs map

| Doc | Purpose |
|-----|---------|
| [docs/DOWNLOADS.md](docs/DOWNLOADS.md) | Maven / npm / NuGet / Go / PyPI / Docker |
| [docs/QUICK_START.md](docs/QUICK_START.md) | First green run |
| [docs/tutorials/](docs/tutorials/) | Per-language walkthroughs |
| [docs/MULTI_LANGUAGE.md](docs/MULTI_LANGUAGE.md) | Adoption paths |
| [docs/NO_PYPI_FROM_THIS_REPO.md](docs/NO_PYPI_FROM_THIS_REPO.md) | Engine stays on harness PyPI |

Author: [Vaquar Khan](https://github.com/vaquarkhan) · **License:** [MIT](LICENSE) · **Cite:** [CITATION.cff](CITATION.cff)
