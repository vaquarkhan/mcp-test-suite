# Tutorial: Go

## Install engine + suite

```bash
pip install "mcp-test-harness>=3.0.9"
pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"
```

## Module

```bash
go get github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0
```

Or local replace while developing:

```go
require github.com/vaquarkhan/mcp-test-suite/adapters/gotest v4.0.0

replace github.com/vaquarkhan/mcp-test-suite/adapters/gotest => ../mcp-test-suite/adapters/gotest
```

## Test

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
        // Binary defaults to mcp-suite
    })
    if _, err := c.RunSuite(context.Background()); err != nil {
        t.Fatal(err)
    }
}
```

CLI-only:

```bash
mcp-suite run --suite mcp-suite.yaml --server-command "go run ./cmd/server"
```

Example: [examples/frameworks/go/](../../examples/frameworks/go/)
