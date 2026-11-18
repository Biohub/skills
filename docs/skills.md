# Skills

The Biohub skills teach an agent to answer protein questions with ESMC, ESMFold2, and the ESM Atlas.
They live in [`plugins/biohub-esm/skills/`](../plugins/biohub-esm/skills/), one folder per skill, each with a `SKILL.md` file in the [Agent Skills](https://agentskills.io) format.
Every skill runs on the [Biohub MCP](connect-mcp.md), which needs a Biohub sign-in and no API key.

## Available skills

| Skill | What it does | Biohub MCP tools |
| --- | --- | --- |
| [`biohub`](../plugins/biohub-esm/skills/biohub/) | The entry point: identifies the scientific goal, routes it to one skill, and says plainly what the plugin does not offer | None |
| [`esm-atlas`](../plugins/biohub-esm/skills/esm-atlas/) | Finds similar proteins, resolves protein names and accessions, reports Atlas records, SAE features, and cluster context, and shows Atlas structures | `esm_atlas_*`, `ui_show_structure` |
| [`esmc`](../plugins/biohub-esm/skills/esmc/) | Scores named substitutions and scans a protein for constrained and tolerant positions, then shows them on the structure | `esmc_score_mutations`, `esmc_scan_mutation_tolerance`, `ui_show_structure` |
| [`esmfold2`](../plugins/biohub-esm/skills/esmfold2/) | Folds and shows proteins, and complexes with DNA, RNA, or ligands, with pTM, ipTM, and pLDDT | `ui_show_structure`, `esmfold2_fold_complex`, `esmfold2_fold_max_accuracy`, `biohub_get_inference_run` |
| [`biohub-setup`](../plugins/biohub-esm/skills/biohub-setup/) | Connects the Biohub MCP, signs you in, and fixes connection, sign-in, and credit problems | None |

## Installation

Install the `biohub` plugin for the complete set of skills and the MCP connection:

- [Claude Code](install/claude-code.md)
- [Codex](install/codex.md)
- [Cursor, Gemini CLI, or any Agent Skills runtime](install/agent-skills.md)

## How the skills work

### Routing

The `biohub` skill is the entry point.
It identifies the scientific goal first, because ESMC, ESMFold2, and the Atlas answer different questions, then hands the request to one specialist skill.
It declines binder design, and says when a request needs something the Biohub MCP does not offer, such as an MSA, modified residues, or embeddings.

### Grounding in the Biohub MCP

Every answer comes from what the Biohub MCP tools return, and ends with a source line naming the tools called, followed by one link to the model or dataset.
If the MCP is not connected or you are not signed in, the skill says so and points to setup.
If a tool fails, the skill names the tool and its error code, and does not fill the gap from memory, literature, or its own sequence comparison.
Sequences are never clipped: a sequence over a tool's limit is reported back with its length.

### Cost

Showing one protein's structure is free.
Complex folds, ESMFold2 folds, and ESMC calls use your Biohub account's credits.
The skills report the credits each tool returns and never estimate them, confirm before maximum-accuracy folds and before running many inputs, and never repeat a call whose outcome was unclear.

### Structures

Every skill shows structures with the Biohub MCP's `ui_show_structure` tool, in an interactive Mol* viewer where the host renders MCP Apps.
`esm-atlas` shows any protein you name or supply, and the top hit of a similarity search.
`esmc` shows the analyzed protein with the residues its analysis singled out highlighted.
`esmfold2` shows proteins and complexes, and labels a single protein's view as the stored Atlas structure or the server's own prediction.
The view has no image unless the agent asks for one to inspect the shape, and the skills never draw their own structure images.
The Biohub MCP returns no PDB or mmCIF files.

## Standalone installs

A plugin install copies the whole plugin, so every skill can reach the shared references and the MCP connection.
A standalone install, for example with `npx skills add`, copies only each skill's own folder; see [what a standalone install includes](install/agent-skills.md#what-you-get).

## Scientific foundations

- **ESMC** is a masked protein language model trained on protein sequences.
  It takes sequence only, and comes in 300M, 600M, and 6B parameter sizes.
  A mutation score is the log-probability of the substituted residue minus that of the wild-type residue at a masked position.
  It is a model preference, not a measured effect.
- **ESMFold2** predicts all-atom structures of proteins, nucleic acids, and ligands from sequence.
  Its confidence scores, such as pLDDT, pTM, and ipTM, estimate the model's own reliability; they do not measure experimental accuracy.
- **The ESM Atlas** (v1) holds ESMC SAE features for about 6.8 billion proteins and ESMFold2-predicted structures for about 1.1 billion of them.
  Proteins are grouped into about 7.7 million clusters by SAE feature similarity, not by sequence identity.
- **SAE features** come from a sparse autoencoder with 16,384 features on ESMC 6B layer 60 (`esmc-6b-2024-12-sae-layer60-k64-codebook16384`).
  Feature labels are agent-generated descriptions.
  The Atlas also reports a `label_reliability` band (high, moderate, or low) computed from each feature's activation value; it is not a rating of the label's accuracy.
  Labels help interpretation but are not validated biological annotations, and features do not transfer to other models, layers, or codebooks.

The models, the SAE, and the Atlas are described in Candido et al., "Language Modeling Materializes a World Model of Protein Biology", [bioRxiv 2026](https://www.biorxiv.org/content/10.64898/2026.06.03.729735).
