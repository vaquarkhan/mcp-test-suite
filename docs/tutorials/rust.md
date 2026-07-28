# Tutorial: Rust

Rust packs use the shared YAML file and shell out to `mcp-suite` from an integration test (no separate Rust MCP client required).

## Install

```bash
pip install "mcp-test-harness>=3.0.9"
pip install .
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
