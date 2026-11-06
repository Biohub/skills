# Install in any Agent Skills runtime

The [`skills` CLI](https://github.com/vercel-labs/skills) installs the Biohub skills into Claude Code, Codex, Cursor, Gemini CLI, and other runtimes that read the open [Agent Skills](https://agentskills.io) format.
It needs Node.js 22.20 or newer.

## Install

List the skills first:

```bash
npx skills add Biohub/skills --list
```

Choose the skills and agents interactively; the CLI then asks for the scope and install method:

```bash
npx skills add Biohub/skills
```

Install all of them for Claude Code and Codex, without prompts:

```bash
npx skills add Biohub/skills --skill '*' --agent claude-code codex --yes
```

Install one skill for one agent, without prompts:

```bash
npx skills add Biohub/skills --skill esm-atlas --agent claude-code --yes
```

Add `--global` to install for your user instead of the current project.
Run `npx skills add --help` for every option.

## What you get

The CLI installs each skill's own folder, such as `.claude/skills/esm-atlas/` for Claude Code or `.agents/skills/esm-atlas/` for Codex, Cursor, and Gemini CLI, and records the source in `skills-lock.json`.
When you pick several agents, it keeps one copy in `.agents/skills/` and links the other agents to it; add `--copy` for separate copies.
It does not copy the plugin's shared references, and it does not connect the Biohub MCP.

| Skill | Works standalone | Needs the plugin for |
| --- | --- | --- |
| `esm-atlas` | Everything, once you [connect the Biohub MCP](../connect-mcp.md) | The shared viewer and safety references it links to |
| `biohub-esm` | Routing | The shared references it links to |
| `esmc` | Everything, once you connect the Biohub MCP | The shared viewer reference it links to |
| `esmfold2` | Everything, once you connect the Biohub MCP | The shared viewer reference it links to |
| `biohub-esm-setup` | Everything | Nothing |

The skills work without the shared references; they hold the viewer and safety details that every skill follows.
For those, install the plugin in [Claude Code](claude-code.md) or [Codex](codex.md).

## Connect the Biohub MCP

A standalone install does not connect the MCP, so add it for your host and sign in as described in [connect-mcp.md](../connect-mcp.md).
The skills find the tools by name, whatever prefix your host adds.
