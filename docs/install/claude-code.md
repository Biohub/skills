# Install in Claude Code

The `biohub-esm` plugin adds the five Biohub skills and the Biohub MCP connection to Claude Code. It runs no local code.

## Requirements

- Claude Code with plugin support (`claude plugin --help` lists `marketplace` and `install`).
- A Biohub account, which you can create when you first sign in.

## Install from GitHub

```bash
claude plugin marketplace add Biohub/skills
claude plugin install biohub-esm@biohub-esm
```

The first command registers this repository as the marketplace `biohub-esm`, and the second installs the plugin of the same name from it.
Start a new Claude Code session afterwards.

## Install from a local clone

```bash
git clone https://github.com/Biohub/skills.git biohub-skills
claude plugin marketplace add ./biohub-skills
claude plugin install biohub-esm@biohub-esm
```

## Check the install

```bash
claude plugin list
claude plugin details biohub-esm@biohub-esm
claude mcp list
```

`claude plugin details` lists the five skills and the MCP server `biohub`.
`claude mcp list` shows the server as `plugin:biohub-esm:biohub`.
If you also added the server yourself with `claude mcp add`, Claude Code keeps only your entry and lists it as `biohub`.
Inside a session, `/mcp` shows the same server and its connection status.

## Sign in

Run `/mcp` inside a session, choose `biohub`, and authenticate.
Your browser opens a Biohub sign-in page; no API key is needed.
Never paste a password or token into a chat.
Ask Claude "Is the Biohub MCP connected, and am I signed in?" to check.

## Update or remove

```bash
claude plugin marketplace update biohub-esm
claude plugin update biohub-esm@biohub-esm
claude plugin uninstall biohub-esm@biohub-esm
claude plugin marketplace remove biohub-esm
```

## Notes

- Claude Code ignores the Codex-only `agents/openai.yaml` files, so any of the five skills can activate directly from a plain description of the task, not only through the router.
- Claude Code lists the plugin's skills with the plugin prefix, such as `biohub-esm:esm-atlas`.
- Some skill text refers to other skills as `$skill-name`, the Codex convention; Claude Code resolves the same skill by name.
