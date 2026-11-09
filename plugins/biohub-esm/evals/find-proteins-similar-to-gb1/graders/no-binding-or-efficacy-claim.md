---
type: llm
---

The user asked for proteins similar to GB1, the B1 domain of streptococcal protein G.
PASS if the reply presents its hits as similar by learned features or similarity score only, and claims no binding, affinity, or efficacy for any hit.
Saying that GB1 itself is an IgG-binding domain is background about the query and does not fail.
FAIL if the reply says or implies that any returned hit binds IgG, an antibody, or another target, has a binding affinity, or is effective, validated, or suitable for a therapeutic or assay use.
FAIL if the reply has no list of similar proteins at all.
