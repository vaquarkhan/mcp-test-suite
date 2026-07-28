# mcp-test-suite/gotest

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
