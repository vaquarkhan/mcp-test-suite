---
name: mcp-adapter-install
description: >-
  Install mcp-test-suite language adapters from GitHub Packages or Releases
  (Java/Maven, npm, NuGet, Go). Use when the user asks how to download or add
  the JUnit, Jest, xUnit, or Go adapter.
---

# Install language adapters

## Maven (Java / Kotlin) — GitHub Packages

**Package page:** https://github.com/vaquarkhan/mcp-test-suite/packages/3158511

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

`~/.m2/settings.xml` needs `id=github` + PAT with `read:packages`.

**No PAT:** download JAR from https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/mcp-test-suite-junit5-4.0.0.jar

## npm

**Package page:** https://github.com/users/vaquarkhan/packages/npm/package/mcp-test-suite-jest

```ini
@vaquarkhan:registry=https://npm.pkg.github.com
//npm.pkg.github.com/:_authToken=YOUR_GITHUB_PAT
```

```bash
npm install -D @vaquarkhan/mcp-test-suite-jest@4.0.0
```

## NuGet

**Package page:** https://github.com/users/vaquarkhan/packages/nuget/package/McpTestSuite.Xunit

```bash
dotnet nuget add source "https://nuget.pkg.github.com/vaquarkhan/index.json" \
  --name github --username USER --password PAT --store-password-in-clear-text
dotnet add package McpTestSuite.Xunit --version 4.0.0
```

## Go

```bash
go get github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0
```

Full guide: [docs/DOWNLOADS.md](../../docs/DOWNLOADS.md)
