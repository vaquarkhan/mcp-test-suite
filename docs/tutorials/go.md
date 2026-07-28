# Tutorial: Go

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Go module](https://pkg.go.dev/github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0) ·
[Install guide](../DOWNLOADS.md)

Test Go MCP servers with the **gotest** adapter or CLI-only `mcp-suite`.

Example pack: [examples/frameworks/go/](../../examples/frameworks/go/)

## 1. Install engine + suite

```bash
pip install "mcp-test-harness>=3.0.9,<4"
pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"
mcp-suite --version
```

## 2. Add Go module

```bash
go get github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0
```

Local replace while developing this repo:

```go
require github.com/vaquarkhan/mcp-test-suite/adapters/gotest v4.0.0

replace github.com/vaquarkhan/mcp-test-suite/adapters/gotest => ../mcp-test-suite/adapters/gotest
```

## 3. Suite

```yaml
# mcp-suite.yaml
server:
  command: go run ./cmd/server
  transport: stdio
cases:
  - name: Echo
    call: echo
    args: { text: hello-go }
    tags: [smoke, go]
  - name: Unknown tool fails
    call: __missing__
    args: {}
    expect_error: true
```

## 4. Run (CLI)

```bash
mcp-suite run --suite mcp-suite.yaml --server-command "go run ./cmd/server"
mcp-test try --server-command "go run ./cmd/server"
```

## 5. Run (Go test)

```go
package mcp_test

import (
    "context"
    "testing"

    gotest "github.com/vaquarkhan/mcp-test-suite/adapters/gotest"
)

func TestMCPSuite(t *testing.T) {
    c := gotest.New(gotest.Options{
        Command: "go run ./cmd/server",
        Suite:   "mcp-suite.yaml",
    })
    if _, err := c.RunSuite(context.Background()); err != nil {
        t.Fatal(err)
    }
}
```

```bash
go test ./...
```

## Go notes

- Prefer a built binary in CI (`go build -o bin/server ./cmd/server`) for faster, stable boots.
- Logs → stderr only on stdio.

## Related

- [yaml.md](yaml.md) · [IDE_INTEGRATION.md](../IDE_INTEGRATION.md)
