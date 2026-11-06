# Biohub ESM plugin

This plugin turns protein questions into calls to the [Biohub MCP](https://biohub.ai/mcp), which runs ESMC, ESMFold2, and the ESM Atlas.
It is instructions only: five skills, two shared references, and `.mcp.json`, which declares the server as `biohub`.
It runs no local code and needs no API key; the user signs in to Biohub through the host.

Install it in Claude Code 2.1.275 or later with:

```bash
/plugin install biohub-esm --marketplace Biohub/skills
```

## Skills

| Skill | Uses |
| --- | --- |
| `biohub-esm` | Routes a request to one of the skills below |
| `esm-atlas` | `esm_atlas_*` tools and `ui_show_structure` |
| `esmc` | `esmc_score_mutations`, `esmc_scan_mutation_tolerance`, and `ui_show_structure` |
| `esmfold2` | `ui_show_structure`, `esmfold2_fold_complex`, `esmfold2_fold_max_accuracy`, and `biohub_get_inference_run` |
| `biohub-esm-setup` | Connecting and signing in to the Biohub MCP |

Shared references:

- [`references/show-a-structure.md`](references/show-a-structure.md): how every skill calls the structure viewer.
- [`references/safety-and-provenance.md`](references/safety-and-provenance.md): scientific claims, biosafety, licensing, and source lines.

## Plugin-page prompts

- `Where is GB1 most constrained or tolerant to mutation? Show me on its structure.`
- `Fold human hemoglobin as an alpha2-beta2 tetramer from P69905 and P68871, and show me the complex.`
- `Find proteins similar to GB1 and show me the closest one.`

## Checks

Run these from the repository root.

```bash
claude plugin validate plugins/biohub-esm
```

The [eval suite](evals/README.md) checks how agents use the skills against mocked Biohub MCP responses.
