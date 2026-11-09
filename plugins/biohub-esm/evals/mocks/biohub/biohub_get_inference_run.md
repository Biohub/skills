---
# Captured from the Biohub MCP (https://biohub.ai/mcp, server 0.88.0+a496d14bff) on 2026-11-04, signed in.
# Call: biohub_get_inference_run for the queued GB1 fold
# Body: the tool's text content block, pretty-printed; non-ASCII is written as JSON escapes.
type: fixed
---

{
  "run_id": "6be7753e-a8fd-473b-a42a-51331f908758-00000",
  "execution_status": "done",
  "results_expire_at": "2026-12-06T02:20:48.631Z",
  "model_id": "esmfold2-fast-2026-05",
  "usage": {
    "credits": 0.0031
  },
  "summary": {
    "chains": [
      {
        "id": "A",
        "type": "protein",
        "length": 56,
        "mean_plddt": 0.827
      }
    ],
    "ptm": 0.738,
    "plddt_summary": {
      "mean": 0.827,
      "minimum": 0.715,
      "maximum": 0.888
    }
  },
  "warnings": []
}
