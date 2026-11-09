# Install in Codex

The `biohub-esm` plugin adds the five Biohub skills and the Biohub MCP connection to Codex. It runs no local code.

## Requirements

- A Codex build with plugin support (`codex plugin --help` lists `marketplace` and `add`).
  If `codex` is not on your `PATH`, use the executable bundled with the Codex app.
- A Biohub account, which you can create when you first sign in.

## Install from GitHub

```bash
codex plugin marketplace add Biohub/skills
codex plugin add biohub-esm@biohub-esm
```

The first command registers this repository as the marketplace `biohub-esm`, and the second installs the plugin of the same name from it.
Restart Codex, then start a new thread.

## Install from a local clone

```bash
git clone https://github.com/Biohub/skills.git biohub-skills
codex plugin marketplace add ./biohub-skills
codex plugin add biohub-esm@biohub-esm
```

Codex registers the clone's absolute path as the marketplace source.
If you move or delete the clone, the installed plugin keeps working from Codex's cache, but `codex plugin list` and `codex plugin marketplace list` fail until you run `codex plugin marketplace remove biohub-esm` and add the clone again from its new path.

## Check the install

```bash
codex plugin list --marketplace biohub-esm
codex mcp list
```

`codex plugin list --marketplace biohub-esm` shows `biohub-esm@biohub-esm` as `installed, enabled`.
`codex mcp list` shows the server `biohub` at `https://biohub.ai/mcp`, enabled.

## Use the skills

Codex offers the `biohub-esm` router automatically.
The specialist skills run when the router hands off to them, or when you name one at the start of a prompt:

```text
$esm-atlas Find proteins similar to GB1.
$esmc What might W43F do to GB1?
$esmfold2 Show me what GB1 looks like.
$biohub-esm-setup Is the Biohub MCP connected, and am I signed in?
```

Codex may ask you to approve Biohub MCP tools that are not marked read-only, such as the similarity search; approve them to continue.

## Sign in

```bash
codex mcp login biohub
```

Your browser opens a Biohub sign-in page; no API key is needed.
Never paste a password or token into a chat.

## Update

Codex runs the plugin from its own cached copy, and it does not update that copy when the source changes.
To update, refresh the source, install the plugin again, and start a new thread:

1. For a GitHub install, run `codex plugin marketplace upgrade biohub-esm`.
   For a local clone, run `git pull` in the clone.
2. Run `codex plugin add biohub-esm@biohub-esm`.
3. Start a new Codex thread. A thread that is already open keeps the skills that it loaded.

`codex plugin list --marketplace biohub-esm` shows the installed version.

## Remove

```bash
codex plugin remove biohub-esm@biohub-esm
codex plugin marketplace remove biohub-esm
```

Removing the marketplace does not delete your clone.
