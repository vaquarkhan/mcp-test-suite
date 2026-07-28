# mcp-test-suite/gotest

## Download (Go modules)

```bash
go get github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0
```

| Registry | Link |
|----------|------|
| pkg.go.dev | https://pkg.go.dev/github.com/vaquarkhan/mcp-test-suite/adapters/gotest |

Engine: `mcp-test` on `PATH` (PyPI, Docker, or release binary).

## Usage

```go
client := gotest.New(gotest.Options{Command: "go run ./cmd/server", Suite: "mcp-suite.yaml"})
res, err := client.RunSuite(ctx)
```

Examples: [examples/frameworks/go](../../examples/frameworks/go/) · [docs/DOWNLOADS.md](../../docs/DOWNLOADS.md)
