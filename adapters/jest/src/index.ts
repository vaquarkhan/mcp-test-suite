/**
 * @vaquarkhan/mcp-test-suite-jest — thin Node adapter over the mcp-suite CLI wrapper.
 *
 * Does not reimplement MCP protocol logic; shells out to ``mcp-suite``
 * (install: ``pip install mcp-test-harness`` + this suite package).
 */

import { spawn } from "node:child_process";
import { promises as fs } from "node:fs";
import * as path from "node:path";
import { tmpdir } from "node:os";

export type MCPClientOptions = {
  /** Shell command that starts the MCP server (stdio). */
  command: string;
  /** Optional path to mcp-suite.yaml / mcp-test.yaml */
  suite?: string;
  config?: string;
  /** Binary name or path (default: mcp-suite on PATH) */
  binary?: string;
  transport?: "stdio" | "sse" | "http";
  cwd?: string;
};

export type ToolCallResult = {
  ok: boolean;
  exitCode: number;
  stdout: string;
  stderr: string;
  report?: Record<string, unknown>;
};

async function runCli(
  args: string[],
  opts: { cwd?: string; binary?: string } = {},
): Promise<ToolCallResult> {
  const binary = opts.binary || process.env.MCP_SUITE_BIN || process.env.MCP_TEST_BIN || "mcp-suite";
  return new Promise((resolve) => {
    const child = spawn(binary, args, {
      cwd: opts.cwd,
      shell: true,
      env: process.env,
    });
    let stdout = "";
    let stderr = "";
    child.stdout.on("data", (d) => {
      stdout += d.toString();
    });
    child.stderr.on("data", (d) => {
      stderr += d.toString();
    });
    child.on("close", (code) => {
      resolve({
        ok: code === 0,
        exitCode: code ?? 1,
        stdout,
        stderr,
      });
    });
    child.on("error", (err) => {
      resolve({
        ok: false,
        exitCode: 1,
        stdout,
        stderr: `${stderr}\n${err.message}`,
      });
    });
  });
}

/**
 * Fluent client used inside Jest / Vitest tests.
 *
 * @example
 * ```ts
 * const server = new MCPClient({ command: "node index.js" });
 * await expect(server.callTool("weather", { city: "Chicago" }))
 *   .resolves.toMatchObject({ ok: true });
 * ```
 */
export class MCPClient {
  constructor(private readonly options: MCPClientOptions) {}

  /** Zero-config probe (stdio cleanliness + handshake). */
  async try(): Promise<ToolCallResult> {
    const args = ["try", "--server-command", this.options.command];
    if (this.options.transport) {
      args.push("--transport", this.options.transport);
    }
    return runCli(args, {
      cwd: this.options.cwd,
      binary: this.options.binary,
    });
  }

  /**
   * Run a single-tool declarative case via a temp suite file, then invoke
   * `mcp-test run`. Prefer sharing a project-level `mcp-suite.yaml` for CI.
   */
  async callTool(
    tool: string,
    args: Record<string, unknown> = {},
    asserts: {
      maxLatencyMs?: number;
      assertSchema?: string;
      expectError?: boolean;
    } = {},
  ): Promise<ToolCallResult> {
    const dir = await fs.mkdtemp(path.join(tmpdir(), "mcp-suite-"));
    const suitePath = path.join(dir, "mcp-suite.yaml");
    const reportPath = path.join(dir, "report.json");
    const caseBlock: Record<string, unknown> = {
      name: `call ${tool}`,
      call: tool,
      args,
    };
    if (asserts.maxLatencyMs != null) caseBlock.max_latency_ms = asserts.maxLatencyMs;
    if (asserts.assertSchema) caseBlock.assert_schema = asserts.assertSchema;
    if (asserts.expectError) caseBlock.expect_error = true;

    const lines = [
      "server:",
      `  command: ${JSON.stringify(this.options.command)}`,
      `  transport: ${this.options.transport || "stdio"}`,
      "cases:",
      `  - name: ${JSON.stringify(`call ${tool}`)}`,
      `    call: ${JSON.stringify(tool)}`,
      `    args: ${JSON.stringify(args)}`,
    ];
    if (asserts.maxLatencyMs != null) {
      lines.push(`    max_latency_ms: ${asserts.maxLatencyMs}`);
    }
    if (asserts.assertSchema) {
      lines.push(`    assert_schema: ${JSON.stringify(asserts.assertSchema)}`);
    }
    if (asserts.expectError) {
      lines.push(`    expect_error: true`);
    }
    await fs.writeFile(suitePath, lines.join("\n") + "\n", "utf8");

    const cliArgs = [
      "run",
      "--suite",
      suitePath,
      "--report-format",
      "json",
      "--report-output",
      reportPath,
    ];
    const result = await runCli(cliArgs, {
      cwd: this.options.cwd,
      binary: this.options.binary,
    });
    try {
      const raw = await fs.readFile(reportPath, "utf8");
      result.report = JSON.parse(raw) as Record<string, unknown>;
    } catch {
      /* report optional */
    }
    if (!result.ok) {
      throw new Error(
        `mcp-test failed (exit ${result.exitCode}):\n${result.stderr || result.stdout}`,
      );
    }
    return result;
  }

  /** Run a shared project suite file. */
  async runSuite(suitePath?: string): Promise<ToolCallResult> {
    const suite = suitePath || this.options.suite || "mcp-suite.yaml";
    const args = ["run", "--suite", suite, "--server-command", this.options.command];
    if (this.options.config) args.push("--config", this.options.config);
    if (this.options.transport) args.push("--transport", this.options.transport);
    const result = await runCli(args, {
      cwd: this.options.cwd,
      binary: this.options.binary,
    });
    if (!result.ok) {
      throw new Error(
        `mcp-test suite failed (exit ${result.exitCode}):\n${result.stderr || result.stdout}`,
      );
    }
    return result;
  }
}

/** Jest helper: `expect(await server.callTool(...)).toPass()` */
export function toPass(received: ToolCallResult): {
  pass: boolean;
  message: () => string;
} {
  return {
    pass: received.ok,
    message: () =>
      received.ok
        ? "expected mcp-test run to fail"
        : `mcp-test failed:\n${received.stderr || received.stdout}`,
  };
}
