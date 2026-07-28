package server_test

import (
	"context"
	"testing"
	"time"

	"github.com/vaquarkhan/mcp-test-suite/adapters/gotest"
)

func TestMCPSuite(t *testing.T) {
	client := gotest.New(gotest.Options{
		Command: "go run ./cmd/server",
		Suite:   "mcp-suite.yaml",
	})
	ctx, cancel := context.WithTimeout(context.Background(), 2*time.Minute)
	defer cancel()

	res, err := client.RunSuite(ctx)
	if err != nil {
		t.Fatalf("suite failed: %v\n%s", err, res.Stderr)
	}
}
