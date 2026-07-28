# Tutorial: Rust

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Install guide](../DOWNLOADS.md)

Rust packs use shared YAML and shell out to **`mcp-suite`** from an integration test (no separate Rust MCP client required).

Example pack: [examples/frameworks/rust/](../../examples/frameworks/rust/)

## 1. Install

```bash
pip install "mcp-test-harness>=3.0.9"
pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"
mcp-suite --version
```

## 2. Suite

```yaml
server:
  command: target/release/my_mcp_server
  transport: stdio
cases:
  - name: Echo
    call: echo
    args: { text: hello-rust }
    tags: [smoke, rust]
```

## 3. Run (CLI)

```bash
cargo build --release
mcp-suite run --suite mcp-suite.yaml \
  --server-command "target/release/my_mcp_server"
mcp-test try --server-command "target/release/my_mcp_server"
```

## 4. Integration test sketch

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

```bash
cargo test
```

## Rust notes

- Use a release binary in CI for stable boot times.
- Logs → stderr only on stdio.

## Related

- [yaml.md](yaml.md)
