# IDE & AI assistant integration

**Package downloads (v4.0.0):**
[Python / PyPI](https://pypi.org/project/mcp-test-harness/) ·
[Java JAR](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/mcp-test-suite-junit5-4.0.0.jar) ·
[Node / npm tgz](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/vaquarkhan-mcp-test-suite-jest-4.0.0.tgz) ·
[Go module](https://pkg.go.dev/github.com/vaquarkhan/mcp-test-suite/adapters/gotest@v4.0.0) ·
[.NET nupkg](https://github.com/vaquarkhan/mcp-test-suite/releases/download/v4.0.0/McpTestSuite.Xunit.4.0.0.nupkg) ·
[All release assets](https://github.com/vaquarkhan/mcp-test-suite/releases/tag/v4.0.0) ·
[Install guide](DOWNLOADS.md)

Use **mcp-test-suite** from any editor or AI assistant that supports MCP. The workflow is the same everywhere: install the engine, write `mcp-suite.yaml`, run `mcp-test try` / `mcp-suite run`, then wire the server into your IDE’s MCP config.

## Prereq (all IDEs)

```bash
pip install "mcp-test-harness>=3.0.9"
pip install "git+https://github.com/vaquarkhan/mcp-test-suite.git"
mcp-test --version && mcp-suite --version
```

## Universal workflow

| Step | Command / artifact | Why |
|------|-------------------|-----|
| 1 | `mcp-test try --server-command "…"` | Zero-config boot + conformance probe |
| 2 | `mcp-suite run --suite mcp-suite.yaml` | Declarative contract tests (any language) |
| 3 | Add server to IDE MCP config | Agent can call your tools in-chat |
| 4 | CI: GitHub Action or adapter test | Same YAML in every pipeline |

**Rules of thumb**

- Logs on stdio servers → **stderr only** (stdout is JSON-RPC).
- Prefer **`mcp-suite.yaml`** for cross-language contracts; use Python `test_*.py` only for complex flows.
- Do not add a server to MCP config until **try** and **suite** are green.

---

## Quick reference — where to configure MCP

| IDE / assistant | MCP config location | Agent rules / steering |
|-----------------|---------------------|-------------------------|
| **[Cursor](CURSOR_IDE.md)** | `.cursor/mcp.json` | [`.cursorrules`](../.cursorrules) · `.cursor/rules/` |
| **[Kiro](https://kiro.dev/)** | IDE → MCP servers panel | `.kiro/steering/` · `.kiro/specs/` |
| **[Google Antigravity](https://antigravity.google/)** | Workspace MCP settings | Project `rules` / agent instructions |
| **[Gemini Code Assist](https://codeassist.google/)** (VS Code / JetBrains) | Extension MCP settings | Workspace rules file |
| **[ChatGPT](https://chatgpt.com/)** (desktop / web) | Settings → Apps & Connectors → MCP | Custom GPT instructions (optional) |
| **[OpenAI Codex](https://openai.com/codex/)** | `~/.codex/config.toml` → `[mcp_servers]` | `AGENTS.md` in repo root |
| **[VS Code](https://code.visualstudio.com/)** + Copilot | `.vscode/mcp.json` or user MCP config | `.github/copilot-instructions.md` |
| **[GitHub Copilot](https://github.com/features/copilot)** (Coding agent) | Repo MCP in Copilot settings | `AGENTS.md` · `.github/copilot-instructions.md` |
| **[Windsurf](https://windsurf.com/)** | `.windsurf/mcp.json` | `.windsurfrules` |
| **[JetBrains](https://www.jetbrains.com/)** (AI Assistant) | Settings → Tools → MCP | `.idea/` run configs · AI rules |
| **[Zed](https://zed.dev/)** | `~/.config/zed/settings.json` → `context_servers` | Project rules in settings |
| **[Visual Studio](https://visualstudio.microsoft.com/)** | GitHub Copilot / MCP extension settings | `.editorconfig` · Copilot instructions |
| **[Neovim](https://neovim.io/)** | Plugin-specific (`mcphub.nvim`, etc.) | `AGENTS.md` · project docs |
| **[Amazon Q Developer](https://aws.amazon.com/q/developer/)** | IDE plugin MCP panel | `.amazonq/rules/` (when enabled) |
| **[Cline / Roo Code](https://github.com/cline/cline)** (VS Code) | Extension MCP settings | `.clinerules` / `.roo/` |

Traditional editor tips (snippets, extensions, terminal): [EDITORS.md](EDITORS.md).

---

## Cursor skills

Project skills in [`.cursor/skills/`](../.cursor/skills/):

| Skill | When to use |
|-------|-------------|
| [`mcp-test-suite`](../.cursor/skills/mcp-test-suite/SKILL.md) | Install engine, run try/suite, IDE MCP wiring |
| [`mcp-suite-yaml`](../.cursor/skills/mcp-suite-yaml/SKILL.md) | Author declarative suite YAML |
| [`mcp-adapter-install`](../.cursor/skills/mcp-adapter-install/SKILL.md) | Maven / npm / NuGet / Go adapter installs |

Also: [`.cursorrules`](../.cursorrules) · [AGENTS.md](../AGENTS.md)

---

## Cursor

Full guide: **[CURSOR_IDE.md](CURSOR_IDE.md)**

```json
// .cursor/mcp.json (example — run mcp-test try first)
{
  "mcpServers": {
    "my-server": {
      "command": "node",
      "args": ["dist/index.js"]
    }
  }
}
```

Copy [`.cursorrules`](../.cursorrules) into your MCP server repo or symlink this repo’s rules.

---

## Kiro

[Kiro](https://kiro.dev/) is AWS’s agentic IDE. It supports MCP servers and project **steering** files.

1. Install engine + suite (prereq above).
2. Run `mcp-test try --server-command "…"` then `mcp-suite run --suite mcp-suite.yaml`.
3. In Kiro: **MCP Servers** → add your stdio command (same string as `--server-command`).
4. Add steering under `.kiro/steering/` so the agent runs tests before changing tools:

```markdown
# MCP testing (mcp-test-suite)
- Before changing MCP tools: `mcp-suite run --suite mcp-suite.yaml`
- New tools: `mcp-test try --server-command "<command>"` first
- Shared contracts live in `mcp-suite.yaml`; logs → stderr on stdio servers
```

5. Optional: `.kiro/hooks/` to run `mcp-suite run` on save or pre-commit (see [Kiro hooks docs](https://kiro.dev/docs/hooks/)).

---

## Google (Antigravity · Gemini Code Assist · AI Studio)

### Google Antigravity

Agent-first IDE from Google. Configure MCP the same way as other VS Code–family tools:

1. Green-light server with `mcp-test try` / `mcp-suite run`.
2. Add MCP server in workspace settings (stdio command + args).
3. Pin project rules: use `mcp-suite.yaml` as the contract source of truth.

### Gemini Code Assist (VS Code / JetBrains / Cloud Shell)

- Install **Gemini Code Assist** extension.
- Enable **MCP** in extension settings when available.
- Open `docs/DOWNLOADS.md` and your `mcp-suite.yaml` in-editor so the model has install + contract context.
- Run suites from the integrated terminal: `mcp-suite run --suite mcp-suite.yaml`.

### Google AI Studio

AI Studio is for **model + API** experimentation, not local stdio MCP. Use it to prototype prompts; validate MCP servers locally with **mcp-test** / **mcp-suite**, then expose tools via your server’s transport (stdio / SSE / HTTP).

---

## ChatGPT & OpenAI Codex

### ChatGPT (desktop / web)

1. **Settings → Apps & Connectors → MCP** (or **Developer mode** on desktop).
2. Add a connector with your server’s launch command (must pass `mcp-test try` first).
3. In a chat, enable the connector and ask the model to call your tools.
4. Keep `mcp-suite.yaml` in your repo; run `mcp-suite run` in CI so ChatGPT-facing tools match tested contracts.

### OpenAI Codex (CLI / cloud agent)

Codex reads **`AGENTS.md`** at the repo root and **`~/.codex/config.toml`** for MCP:

```toml
# ~/.codex/config.toml (example)
[mcp_servers.my-server]
command = "node"
args = ["dist/index.js"]
```

Add to your repo **`AGENTS.md`**:

```markdown
## MCP testing
- Engine: `pip install mcp-test-harness`; suite: `pip install git+https://github.com/vaquarkhan/mcp-test-suite.git`
- Run: `mcp-suite run --suite mcp-suite.yaml`
- Probe: `mcp-test try --server-command "node dist/index.js"`
```

---

## VS Code & GitHub Copilot

Works with **VS Code**, **VS Code Insiders**, and **github.dev**.

| File | Purpose |
|------|---------|
| [`.vscode/mcp-test-harness.code-snippets`](../.vscode/mcp-test-harness.code-snippets) | Test/assertion snippets |
| `.vscode/tasks.json` | Run `mcp-suite` / `mcp-test try` from Tasks |
| `.vscode/mcp.json` | MCP server definitions (when supported) |
| `.github/copilot-instructions.md` | Copilot agent behavior for this repo |

Example task (also in [CURSOR_IDE.md](CURSOR_IDE.md)):

```json
{
  "label": "MCP: Run declarative suite",
  "type": "shell",
  "command": "mcp-suite run --suite mcp-suite.yaml",
  "group": { "kind": "test", "isDefault": true }
}
```

**GitHub Copilot Coding Agent** (PRs / issues): ensure `mcp-suite.yaml` is committed; CI runs [validate workflow](../.github/workflows/validate.yml) or your language adapter tests.

---

## Windsurf

1. Install engine + suite.
2. **`mcp-test try`** → **`mcp-suite run`**.
3. MCP: `.windsurf/mcp.json` (stdio server entry).
4. Agent rules: **`.windsurfrules`** — copy the bullets from [`.cursorrules`](../.cursorrules).

---

## JetBrains (IntelliJ · WebStorm · PyCharm · …)

1. Install **AI Assistant** + enable MCP when offered in your IDE version.
2. Java/Kotlin projects: use **`mcp-test-suite-junit5`** adapter ([java tutorial](tutorials/java.md)).
3. Run configuration: external tool `mcp-suite run --suite mcp-suite.yaml`.
4. Terminal: same CLI workflow as VS Code.

---

## Zed

Add a **context server** in `~/.config/zed/settings.json`:

```json
{
  "context_servers": {
    "my-mcp-server": {
      "command": { "path": "node", "args": ["dist/index.js"] }
    }
  }
}
```

Run `mcp-test try` with the same command before enabling in Zed.

---

## Neovim & terminal-first editors

No single standard — use whichever MCP plugin you prefer (`mcphub.nvim`, etc.) with the **same stdio command** validated by `mcp-test try`.

Keep **`AGENTS.md`** or **`docs/IDE_INTEGRATION.md`** open in splits; run:

```bash
mcp-suite run --suite mcp-suite.yaml --report-format html --report-output report.html
```

---

## CI parity (every IDE)

Whatever the IDE, mirror the same checks in CI:

```yaml
- uses: vaquarkhan/mcp-test-suite@init
  with:
    suite-file: mcp-suite.yaml
    server-command: "node dist/server.js"
```

Or language-native: Jest / JUnit / Go test / xUnit — all invoke **`mcp-suite`** under the hood ([MULTI_LANGUAGE.md](MULTI_LANGUAGE.md)).

---

## Related docs

| Doc | Topic |
|-----|--------|
| [CURSOR_IDE.md](CURSOR_IDE.md) | Cursor-specific rules & tasks |
| [EDITORS.md](EDITORS.md) | Snippets, extensions, layout |
| [CI_AND_REPORTS.md](CI_AND_REPORTS.md) | GitHub Action + reports |
| [tutorials/](tutorials/) | Per-language setup |
