# Biohub TCR-Workbench plugin

Two skills for [TCR-Workbench](https://github.com/akdslab/tcr-workbench) on the user's own computer: setting it up, and running analyses of processed human or mouse alpha-beta TCR data.
They need a client that can run shell commands and a local TCR-Workbench checkout, and they use no Biohub MCP tools.

```bash
/plugin install biohub-tcr --marketplace Biohub/skills
```

| Skill | What it does |
| --- | --- |
| `tcr-workbench-setup` | Installs, configures, and verifies a local TCR-Workbench environment |
| `tcr-workbench` | Runs peptide-MHC predictions, DecoderTCR scores, and peptide profiles, with MHC uncertainty and auditable outputs |

## Source

The skill folders are byte-for-byte copies of `skills/` in [`akdslab/tcr-workbench`](https://github.com/akdslab/tcr-workbench) at commit [`38f8376`](https://github.com/akdslab/tcr-workbench/commit/38f83761917c43f83b13a1b6d27d8ad24c053353), maintained by the Khan Lab, and the same copies the Biohub MCP serves.
Each folder's git tree matches the `source_tree_sha` in its Biohub MCP pin. Change them upstream, then copy them again.
They are MIT licensed, copyright TCR-Workbench contributors, in each folder's `LICENSE.md`.
Each skill carries its own `evals/evals.json` in the [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) format.
