# Install in Codex

The `biohub` plugin adds the five Biohub skills and the Biohub MCP connection to Codex. It runs no local code.

## Requirements

- A Codex build with plugin support (`codex plugin --help` lists `marketplace` and `add`).
  If `codex` is not on your `PATH`, use the executable bundled with the Codex app.
- A Biohub account, which you can create when you first sign in.

## Install from GitHub

```bash
codex plugin marketplace add Biohub/skills
codex plugin add biohub@biohub
```

The first command registers this repository as the marketplace `biohub`, and the second installs the plugin of the same name from it.
Restart Codex, then start a new thread.

## Install from a local clone

```bash
git clone https://github.com/Biohub/skills.git biohub-skills
codex plugin marketplace add ./biohub-skills
codex plugin add biohub@biohub
```

Codex registers the clone's absolute path as the marketplace source.
If you move or delete the clone, the installed plugin keeps working from Codex's cache, but `codex plugin list` and `codex plugin marketplace list` fail until you run `codex plugin marketplace remove biohub` and add the clone again from its new path.

## Replace an older Biohub ESM install

- If you previously installed `biohub-esm@biohub-esm`, remove that plugin before installing Biohub:

```bash
codex plugin remove biohub-esm@biohub-esm
```

- Then follow the installation steps above and start a new session.
- The plugin and marketplace are now named `biohub`; the source directory remains unchanged, and the router and setup skills are now `biohub` and `biohub-setup`.

## Check the install

```bash
codex plugin list --marketplace biohub
codex mcp list
```

`codex plugin list --marketplace biohub` shows `biohub@biohub` as `installed, enabled`.
`codex mcp list` shows the server `biohub` at `https://biohub.ai/mcp`, enabled.

## Use the skills

Codex offers the `biohub` router automatically.
The specialist skills run when the router hands off to them, or when you name one at the start of a prompt:

```text
$esm-atlas Find proteins similar to GB1.
$esmc What might W43F do to GB1?
$esmfold2 Show me what GB1 looks like.
$biohub-setup Is the Biohub MCP connected, and am I signed in?
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

1. For a GitHub install, run `codex plugin marketplace upgrade biohub`.
   For a local clone, run `git pull` in the clone.
2. Run `codex plugin add biohub@biohub`.
3. Start a new Codex thread. A thread that is already open keeps the skills that it loaded.

`codex plugin list --marketplace biohub` shows the installed version.

## Remove

```bash
codex plugin remove biohub@biohub
codex plugin marketplace remove biohub
```

Removing the marketplace does not delete your clone.
