# Biohub ESM eval suite

This folder holds the `claude plugin eval` suite for the Biohub ESM plugin.
It needs Claude Code v2.1.269 or later and git 2.31 or later.
Every agent run and every `llm` grader is a real model call that counts against your Claude plan's usage or your API bill, so set `--max-cost-usd` on every run.
Results land in `evals/results/`, which the repository ignores.

## Cases

| Case | Tags | What it checks |
| --- | --- | --- |
| `find-proteins-similar-to-gb1` | smoke, atlas | One mocked similarity search, the returned top hit, the source line, and no binding or efficacy claim |
| `look-up-uniprot-p69905-and-show-its-structure` | smoke, atlas | UniProt lookup before the structure view, and the structure labeled as a prediction |
| `explain-sae-feature-13` | atlas | The returned feature label, framed as a learned model feature rather than a validated annotation |
| `find-the-longest-increasing-subsequence` | smoke, negative | No plugin skill and no Biohub MCP call for an unrelated request |

## Run the suite

Run every command from the plugin folder, `plugins/biohub-esm`.

Full suite, with the no-plugin baseline:

```bash
claude plugin eval . --trust-plugin --judge-model sonnet --max-cost-usd 15 --no-publish
```

One case, one run, without the baseline, for iterating on a grader:

```bash
claude plugin eval . --trust-plugin --runs 1 --ablation none --max-cost-usd 5 --no-publish --case explain-sae-feature-13
```

Pass `--trust-plugin` only for a checkout you trust, because a run loads the plugin and runs its suite on your machine as you.
Add `--model <model>` to pin the agent model when you compare scores over time.
In a two-arm run, `tool_used: Skill` graders and graders marked `arm: with-only` are reported as indicators and do not count toward the score.

## Read a low score

Check the `NOTES` column, or `cases[].arms.with[].error` in `aggregate-result.json`, before you read a low score as a plugin regression.
A rate limit, a usage limit, or a model safeguard can end a run early, and the run is still graded on what it produced.
A call whose input misses a mock's `expect:` guard aborts the run with a score of 0; the result's `aborted` field names the tool.
Add `--keep-temp` to keep each run's `trace.jsonl`.

## Mocks

No run calls the real Biohub MCP.
`mocks/biohub/` answers each Atlas tool with a response captured from `https://biohub.ai/mcp` (server 0.81.0) on 2026-10-27, and `_tools.json` is that server's real `tools/list` result.
Each mock's `expect:` guard pins the input its captured answer belongs to, so an off-script call aborts the run instead of receiving another input's answer.
`find-proteins-similar-to-gb1/mocks/` overrides the structure view with the answer for the top GB1 hit.
The structure-view mocks are the result without `include_png`, so `preview_status` is `not_requested` and there is no image, which a fixed mock could not return anyway.
`list_resources` and `read_resource` have no mock, so a run that calls them is denied.
The suite holds no credentials.

To refresh a mock, send the server `initialize`, `notifications/initialized`, and then `tools/list` or `tools/call` as JSON-RPC over streamable HTTP, and replace the mock body with the call's text content.
