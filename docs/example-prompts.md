# Example prompts

You do not need to name a skill: in Codex the `biohub` router picks one, and in Claude Code the matching skill activates directly.
Every prompt needs the Biohub MCP connected and signed in.

## ESM Atlas (`esm-atlas`)

These are free.

- Find proteins similar to GB1.
- Which proteins are the nearest neighbors of GB1?
- Find proteins similar to hemoglobin.
- Show me the ESM Atlas structure for P69905.
- What SAE features does P69905 activate, and what do they mean?

When a protein name matches several UniProt records, the skill lists the candidates and asks you to choose.

## ESMC (`esmc`)

These use credits: one ESMC call per distinct scored position, or per scanned position.

- What might W43F do to GB1?
- Could W43F change how GB1 behaves?
- Where is GB1 most constrained or tolerant to mutation? Show me on its structure.
- Score these substitutions in my sequence: A12G, L45P, and K67R.

## ESMFold2 (`esmfold2`)

Showing one protein is free; complexes and score-only folds use credits.

- Show me what GB1 looks like.
- Could you display the 3D structure of GB1?
- Fold human hemoglobin as an alpha2-beta2 tetramer from P69905 and P68871, and show me the complex.
- Fold this protein with ATP and show me how they fit together.
- How confident is ESMFold2 in the interface between these two chains?

Prompts that say "my" or "this" use the sequences you supply and never substitute an example.

## Router (`biohub`)

- Help me choose the best ESM workflow for this project.
- Which ESM route should I use for a private 700-residue protein?
- How does ESMFold2 compare with AlphaFold?

## Setup (`biohub-setup`)

- Is the Biohub MCP connected, and am I signed in?
- Why are the Biohub tools missing?

## Addressing a skill directly

In Codex, prefix a prompt with the skill name, for example `$esm-atlas Find proteins similar to GB1.`
In Claude Code, the plugin's skills appear with the plugin prefix, such as `biohub:esm-atlas`; describe the task and the matching skill activates.
