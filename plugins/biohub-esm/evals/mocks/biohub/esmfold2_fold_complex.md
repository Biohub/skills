---
# Captured from the Biohub MCP (https://biohub.ai/mcp, server 0.88.0+a496d14bff) on 2026-11-04, signed in.
# Call: esmfold2_fold_complex hemoglobin alpha and beta
# Body: the tool's text content block, pretty-printed; non-ASCII is written as JSON escapes.
type: fixed
---

{
  "execution_status": "done",
  "model_id": "esmfold2-fast-2026-05",
  "chains": [
    {
      "id": "A",
      "type": "protein",
      "length": 142
    },
    {
      "id": "B",
      "type": "protein",
      "length": 147
    }
  ],
  "cost": {
    "credits": 0.4177,
    "basis": "exact"
  },
  "summary": {
    "chains": [
      {
        "id": "A",
        "type": "protein",
        "length": 142,
        "mean_plddt": 0.874
      },
      {
        "id": "B",
        "type": "protein",
        "length": 147,
        "mean_plddt": 0.846
      }
    ],
    "ptm": 0.92,
    "interface_ptm": 0.918,
    "pair_chains_iptm": [
      {
        "chain_a": "A",
        "chain_b": "B",
        "iptm": 0.918
      }
    ],
    "plddt_summary": {
      "mean": 0.859,
      "minimum": 0.428,
      "maximum": 0.98
    }
  },
  "warnings": []
}
