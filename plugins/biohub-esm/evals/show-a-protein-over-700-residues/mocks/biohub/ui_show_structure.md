---
# Captured from the Biohub MCP (https://biohub.ai/mcp, server 0.88.0+a496d14bff) on 2026-11-04, signed in.
# Call: ui_show_structure with an 800-residue sequence not in the Atlas
# Body: the tool's text content block, pretty-printed; non-ASCII is written as JSON escapes.
type: fixed
error: true
---

{
  "actual_length": 800,
  "code": "sequence_too_long_to_fold",
  "max_length": 700,
  "message": "The sequence is 800 residues, over the 700-residue limit for folding after an ESM Atlas miss."
}
