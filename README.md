<img src="assets/biohub-banner.png" alt="Biohub" width="100%">

# Biohub Skills

Agent skills for protein research with Biohub's ESM models and the ESM Atlas.

## About

Biohub Skills teach an AI agent to use three resources from [Biohub](https://biohub.org): the [ESMC](https://github.com/Biohub/esm#esmc) protein language model, the [ESMFold2](https://github.com/Biohub/esm#esmfold2) structure prediction model, and the [ESM Atlas](https://biohub.ai/esm/protein/atlas).
The ESM Atlas is a public database of ESMC sparse autoencoder (SAE) features for about 6.8 billion proteins, with ESMFold2-predicted structures for about 1.1 billion of them.
Each skill is a folder with a `SKILL.md` file in the open [Agent Skills](https://agentskills.io) format, plus the references it relies on.
They are for researchers and developers who study proteins with an agent such as Claude Code, Codex, Cursor, or Gemini CLI.

With the skills installed, an agent can:

- search the ESM Atlas for proteins with ESMC feature profiles similar to a sequence, name, or accession, and show their structures;
- report the SAE features a protein activates, with their generated labels;
- score named mutations and find where a protein is most constrained or tolerant to mutation with ESMC;
- fold and show proteins, and complexes with DNA, RNA, or small-molecule ligands, with ESMFold2.

Every skill runs on the [Biohub MCP](https://biohub.ai/mcp), a remote server you sign in to with a Biohub account.
The skills pick the right tool for each request, cite the tools behind every answer, report credits used, and report model confidence as a prediction.
They ship together as the `biohub` plugin for Claude Code and Codex, and they also install into other Agent Skills runtimes.

## Project status

Biohub Skills is in active development.
Skills, tools, and install steps may change between releases.
We're not accepting contributions yet; see [CONTRIBUTING.md](CONTRIBUTING.md).

## Repository contents

| Path | Contents |
| --- | --- |
| [`plugins/biohub-esm/`](plugins/biohub-esm/) | The `biohub` plugin: skills, references, the MCP connection, and evals |
| [`plugins/biohub-esm/skills/`](plugins/biohub-esm/skills/) | The five skills |
| [`docs/`](docs/) | Skill catalog, install guides, MCP connection guide, example prompts, and how to evaluate answers |
| [`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json) | Claude Code marketplace |
| [`.agents/plugins/marketplace.json`](.agents/plugins/marketplace.json) | Codex marketplace |
| [`LICENSE.md`](LICENSE.md), [`THIRD_PARTY_NOTICE.md`](THIRD_PARTY_NOTICE.md) | License and third-party notices |
| [`CONTRIBUTING.md`](CONTRIBUTING.md), [`SECURITY.md`](SECURITY.md) | Contribution policy (not accepting contributions yet) and how to report security issues |

## Skills

| Skill | What it does |
| --- | --- |
| `biohub` | Routes a protein request to the right skill, and says plainly what the plugin does not offer |
| `esm-atlas` | Finds similar proteins, resolves names and accessions, describes SAE features and clusters, and shows Atlas structures |
| `esmc` | Scores named mutations and scans a protein for constrained and tolerant positions |
| `esmfold2` | Folds and shows proteins and complexes, and reports pTM, ipTM, and pLDDT |
| `biohub-setup` | Connects the Biohub MCP, signs you in, and fixes connection or sign-in problems |

See [docs/skills.md](docs/skills.md) for what each skill does, how the skills work together, and their scientific foundations.

## Quick Start

### 1. Install the skills

The plugin is the complete install: it adds the skills and the Biohub MCP connection. It runs no local code.

In Claude Code:

```bash
claude plugin marketplace add Biohub/skills
claude plugin install biohub@biohub
```

In Codex:

```bash
codex plugin marketplace add Biohub/skills
codex plugin add biohub@biohub
```

In Cursor, Gemini CLI, or any other [Agent Skills](https://agentskills.io) runtime:

```bash
npx skills add Biohub/skills
```

This installs the skill folders only, so connect the Biohub MCP yourself in step 2.
See the [Claude Code](docs/install/claude-code.md), [Codex](docs/install/codex.md), and [Agent Skills](docs/install/agent-skills.md) install guides for details.

### 2. Connect and sign in to the Biohub MCP

The Biohub MCP at `https://biohub.ai/mcp` serves ESMC, ESMFold2, ESM Atlas search, and a Mol* structure viewer.
The plugin adds it for you as the server `biohub`. To add it yourself, for example after `npx skills add`:

```bash
# Claude Code
claude mcp add --transport http biohub https://biohub.ai/mcp

# Codex
codex mcp add biohub --url https://biohub.ai/mcp
```

Then sign in: in Claude Code run `/mcp` and authenticate `biohub`; in Codex run `codex mcp login biohub`.
Your browser opens a Biohub sign-in page, where you can also create a free account. No API key is needed.
For Claude.ai, ChatGPT, and Cursor, see [docs/connect-mcp.md](docs/connect-mcp.md).

Showing one protein's structure is free. Folds of complexes and every ESMC call use your Biohub account's credits, and each answer reports what it used.

### 3. Try it

- _Find proteins similar to GB1._
- _Show me the ESM Atlas structure for P69905._
- _What might W43F do to GB1?_
- _Fold human hemoglobin as an alpha2-beta2 tetramer from P69905 and P68871, and show me the complex._

See [docs/example-prompts.md](docs/example-prompts.md) for more prompts per skill.

### 4. Evaluate the output

Check that each answer names the tools or models it used, keeps structure confidence separate from experimental evidence, and makes no binding or efficacy claims.
See [docs/evaluating.md](docs/evaluating.md) for the checklist and the eval suite.

## Support & Feedback

Open an issue at <https://github.com/Biohub/skills/issues>, or email <support@biohub.org>.
Tell us which host and skill you used, the prompt, and what you expected.
Do not include passwords, tokens, or sequences you cannot share publicly.

## Code of Conduct

This project follows the [Contributor Covenant](https://www.contributor-covenant.org/) code of conduct.
By taking part, you agree to uphold it.
Report unacceptable behavior to <opensource@chanzuckerberg.com>.

## Reporting Security Issues

Email <security@biohub.org> and do not open a public issue.
See [SECURITY.md](SECURITY.md).

## License and attribution

The code and skills in this repository are released under the [MIT License](LICENSE.md), except the WaveOrder plugin in [`plugins/biohub-waveorder/`](plugins/biohub-waveorder/), which is released under the [BSD 3-Clause License](plugins/biohub-waveorder/LICENSE.md).
Each skill folder carries a copy of its license, so a standalone install keeps it.
Third-party software, model weights, and data are listed in [THIRD_PARTY_NOTICE.md](THIRD_PARTY_NOTICE.md).
ESM Atlas data is provided by Chan Zuckerberg Biohub, Inc. under CC BY 4.0, except the "Sequences" and "All Data" datasets, which are CC BY-SA 4.0; see the [dataset registry entry](https://registry.opendata.aws/biohub-esm-atlas).
If you use ESMC, ESMFold2, or the ESM Atlas in your work, cite Candido et al., "Language Modeling Materializes a World Model of Protein Biology", [bioRxiv 2026](https://www.biorxiv.org/content/10.64898/2026.06.03.729735).

## Disclaimer

These skills are provided "as is", without warranties of any kind.
They guide an agent, and agents make mistakes, so check every result before you rely on it.

- Predicted structures and confidence scores are model outputs, not experimental measurements.
- Mutation scores are model log-likelihood ratios, not measured fitness, stability, or activity.
- SAE feature labels describe learned model features; they are not validated biological annotations.
- The skills make no binding affinity or efficacy claims, and binder design is not included.
- Any biological conclusion needs experimental validation and appropriate safety review.

Use of Biohub services is subject to the Biohub [Terms of Use](https://biohub.org/terms-of-use/) and [Acceptable Use Policy](https://biohub.org/acceptable-use-policy/).
Biohub restricts requests involving controlled pathogens and toxins.
