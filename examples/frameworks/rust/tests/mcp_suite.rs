//! Example: invoke mcp-test from a Rust integration test via std::process.
//! Prefer declarative mcp-suite.yaml; this file shows CI embedding.

#[test]
fn mcp_suite_passes() {
    let status = std::process::Command::new("mcp-test")
        .args([
            "run",
            "--suite",
            "mcp-suite.yaml",
            "--server-command",
            "./target/release/mcp-server",
        ])
        .status()
        .expect("mcp-test on PATH");
    assert!(status.success());
}
