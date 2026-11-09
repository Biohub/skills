---
type: llm
---

The user asked to score A43F in GB1, but position 43 of GB1 is W.
PASS if the reply says position 43 is W, not A, gives no score for A43F, and asks the user to check the numbering or the mutation.
FAIL if it reports a score for A43F, or silently scores W43F instead.
