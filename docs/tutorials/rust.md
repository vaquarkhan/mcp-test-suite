# Tutorial: Rust

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Java JAR](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/mcp-test-suite-junit5-4.0.0.jar) ·
[Node / npm tgz](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/vaquarkhan-mcp-test-suite-jest-4.0.0.tgz) ·
[Go module](https://pkg.go.dev/github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0) ·
[.NET nupkg](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/McpTestSuite.Xunit.4.0.0.nupkg) ·
[All release assets](https://github.com/vaquarkhan/mcp-test-suite/releases/tag/v4.0.0) ·
[Install guide](../DOWNLOADS.md)

Rust packs use the shared YAML file and shell out to `mcp-suite` from an integration test (no separate Rust MCP client required).

## Install

```bash
pip install "mcp-test-harness>=3.0.9"
pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"
```

## Integration test sketch

```rust
#[test]
fn mcp_suite() {
    let status = std::process::Command::new("mcp-suite")
        .args([
            "run",
            "--suite",
            "mcp-suite.yaml",
            "--server-command",
            "target/release/my_mcp_server",
        ])
        .status()
        .expect("mcp-suite on PATH");
    assert!(status.success());
}
```

Example: [examples/frameworks/rust/](../../examples/frameworks/rust/)
