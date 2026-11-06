# Evaluate the output

Use this checklist to judge an answer produced with the Biohub skills.
A good answer passes every item that applies to it.
The plugin's [eval suite](../plugins/biohub-esm/evals/README.md) checks many of these items automatically against mocked Biohub MCP responses.

## Grounding

- Every answer ends with a source line that names the Biohub MCP tools called, followed by one link to the model or dataset.
- Every protein, accession, score, and structure in the answer comes from a tool result, not from memory.
- When a tool fails, the answer names the tool and its error code, and stops instead of guessing.

## Scientific claims

- Structure answers report confidence, such as pLDDT, pTM, or ipTM, and describe it as the model's own estimate, not experimental accuracy.
- A single protein's view is labelled as the stored Atlas structure or the server's own prediction, not as an ESMFold2 prediction.
- Mutation answers state the score definition and residue numbering, and call the score a model log-likelihood ratio, not a measured effect.
- SAE feature labels are presented as descriptions of learned model features, not as validated biology.
- No answer claims binding affinity, efficacy, or experimental confirmation from a prediction.
- Atlas neighbors are described as proteins with similar SAE feature profiles, not as homologs by sequence identity.

## Inputs and limits

- The answer says which sequence it used, and never silently substitutes an example for yours.
- Over-length sequences are reported with their length, never silently clipped.
- Requests the tools cannot take, such as an MSA or modified residues, are declined plainly, not approximated.

## Cost and safety

- Credits are reported as the tool returned them, or the answer says the tool did not report them; they are never estimated.
- Maximum-accuracy folds and runs over several inputs ask for a yes or no confirmation first.
- A call whose outcome was unclear is not repeated.
- The answer never asks you to paste a password, token, or key into the chat.

## Red flags

- Invented PDB IDs, UniProt accessions, or literature.
- "Experimentally determined" or "confirmed" used for a predicted structure.
- A description of a structure's shape when no image was requested.
- A structure drawn or rendered by the agent itself.

## Manually test the structure viewer

- Install the candidate plugin version and start a new thread so the updated skills load.
- Sign in to the Biohub MCP.

| Case | Prompt or setup | Expected behavior |
| --- | --- | --- |
| One protein | `Show me the ESM Atlas structure for P69905.` | One `ui_show_structure` call with one protein entity, free, labelled as the Atlas structure. |
| Complex | `Fold human hemoglobin as an alpha2-beta2 tetramer from P69905 and P68871, and show me the complex.` | Two UniProt lookups, then one `ui_show_structure` call with four protein entities; pTM, ipTM, and credits reported; no extra fold call. |
| Highlights | `Where is GB1 most constrained or tolerant to mutation? Show me on its structure.` | One `esmc_scan_mutation_tolerance` call, then one view with constrained and tolerant residues highlighted in two colors. |
| Not signed in | Sign out of the Biohub MCP and ask any prompt. | The answer says you are not signed in and points to setup, with no result. |
| Denied approval | Deny the view approval. | The answer reports the failure without calling it a missing connection, and does not draw a structure. |

- Record the actual tool calls and a screenshot of each view; the eval suite alone does not show that a viewer opened in the host.
