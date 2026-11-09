#!/usr/bin/env bash
# Fails when a skill, reference, or doc names a Biohub MCP tool that the captured tools/list does not serve.
# The captured list is the eval suite's _tools.json, so a server rename shows up here once the mocks are recaptured.
set -euo pipefail

tools_json="plugins/biohub-esm/evals/mocks/biohub/_tools.json"
# SDK identifiers that share a tool prefix but are not MCP tools.
not_tools="esmfold2_client"

served="$(jq -r '.tools[].name' "$tools_json" | sort -u)"
named="$(git grep -ohE '`(ui|esm_atlas|esmfold2|esmc|biohub)_[a-z0-9_]+`' -- \
  'plugins/biohub-esm/skills' 'plugins/biohub-esm/references' 'plugins/biohub-esm/README.md' \
  'docs' 'README.md' | tr -d '`' | sort -u)"

missing="$(comm -23 <(echo "$named") <(echo "$served") | grep -vxF -f <(tr ' ' '\n' <<<"$not_tools") || true)"
if [ -n "$missing" ]; then
  echo "::error::These tools are named in the plugin but not served in $tools_json:"
  while read -r tool; do
    echo "  $tool"
    git grep -n "\`$tool\`" -- 'plugins/biohub-esm/skills' 'plugins/biohub-esm/references' \
      'plugins/biohub-esm/README.md' 'docs' 'README.md' | sed 's/^/    /'
  done <<<"$missing"
  echo "Recapture the mocks if the server added or renamed a tool, or fix the name."
  exit 1
fi

echo "Every named MCP tool is served: $(echo "$named" | wc -l | tr -d ' ') tools checked against $tools_json."
