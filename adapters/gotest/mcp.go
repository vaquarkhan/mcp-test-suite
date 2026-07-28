// Package gotest is the Go adapter for mcp-test-suite.
// It orchestrates the mcp-test CLI / standalone binary — it does not reimplement MCP.
package gotest

import (
	"bytes"
	"context"
	"fmt"
	"os"
	"os/exec"
	"time"
)

// Options configure how the adapter invokes mcp-test.
type Options struct {
	Command   string // server launch command (stdio)
	Suite     string // path to mcp-suite.yaml
	Config    string // optional mcp-test.yaml
	Binary    string // mcp-test binary (default: mcp-test)
	Transport string // stdio | sse | http
	Dir       string // working directory
}

// Result is the outcome of an mcp-test invocation.
type Result struct {
	ExitCode  int
	Stdout    string
	Stderr    string
	LatencyMs int64
}

// Passed reports whether the CLI exited 0.
func (r Result) Passed() bool { return r.ExitCode == 0 }

// Client wraps the mcp-test CLI for use with testing.T.
type Client struct {
	opts Options
}

// New returns a Client. Empty Binary defaults to "mcp-test" on PATH.
func New(opts Options) *Client {
	if opts.Binary == "" {
		opts.Binary = envOr("MCP_SUITE_BIN", envOr("MCP_TEST_BIN", "mcp-suite"))
	}
	if opts.Transport == "" {
		opts.Transport = "stdio"
	}
	if opts.Suite == "" {
		opts.Suite = "mcp-suite.yaml"
	}
	return &Client{opts: opts}
}

// Try runs mcp-test try (handshake / stdio probe).
func (c *Client) Try(ctx context.Context) (Result, error) {
	args := []string{"try", "--server-command", c.opts.Command, "--transport", c.opts.Transport}
	return c.run(ctx, args)
}

// RunSuite executes the declarative suite via mcp-suite run.
func (c *Client) RunSuite(ctx context.Context) (Result, error) {
	args := []string{
		"run",
		"--suite", c.opts.Suite,
		"--server-command", c.opts.Command,
		"--transport", c.opts.Transport,
	}
	if c.opts.Config != "" {
		args = append(args, "--config", c.opts.Config)
	}
	return c.run(ctx, args)
}

func (c *Client) run(ctx context.Context, args []string) (Result, error) {
	start := time.Now()
	cmd := exec.CommandContext(ctx, c.opts.Binary, args...)
	if c.opts.Dir != "" {
		cmd.Dir = c.opts.Dir
	}
	var stdout, stderr bytes.Buffer
	cmd.Stdout = &stdout
	cmd.Stderr = &stderr
	err := cmd.Run()
	res := Result{
		Stdout:    stdout.String(),
		Stderr:    stderr.String(),
		LatencyMs: time.Since(start).Milliseconds(),
	}
	if err != nil {
		if ee, ok := err.(*exec.ExitError); ok {
			res.ExitCode = ee.ExitCode()
			return res, fmt.Errorf("mcp-test exit %d: %s", res.ExitCode, stderr.String())
		}
		res.ExitCode = 1
		return res, err
	}
	return res, nil
}

func envOr(key, fallback string) string {
	if v := os.Getenv(key); v != "" {
		return v
	}
	return fallback
}
