# mcp-test-suite/gotest

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Java JAR](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/mcp-test-suite-junit5-4.0.0.jar) ·
[Node / npm tgz](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/vaquarkhan-mcp-test-suite-jest-4.0.0.tgz) ·
[Go module](https://pkg.go.dev/github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0) ·
[.NET nupkg](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/McpTestSuite.Xunit.4.0.0.nupkg) ·
[All release assets](https://github.com/vaquarkhan/mcp-test-suite/releases/tag/v4.0.0) ·
[Install guide](../../docs/DOWNLOADS.md)

Go adapter for **mcp-test-suite**.

## Install

```bash
go get github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0
```

Docs: [pkg.go.dev](https://pkg.go.dev/github.com/vaquarkhan/mcp-test-suite/adapters/gotest)

Engine: `mcp-suite` on PATH — `pip install mcp-test-harness` + suite connectors ([DOWNLOADS.md](../../docs/DOWNLOADS.md)).

## Usage

```go
client := gotest.New(gotest.Options{Command: "go run ./cmd/server", Suite: "mcp-suite.yaml"})
res, err := client.RunSuite(ctx)
```

Examples: [examples/frameworks/go](../../examples/frameworks/go/)
