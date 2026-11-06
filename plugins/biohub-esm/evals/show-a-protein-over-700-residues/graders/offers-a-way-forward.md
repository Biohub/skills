---
type: llm
---

The viewer refused an 800-residue protein with no stored structure; its free fold takes at most 700 residues.
PASS if the reply states the limit and asks for a shorter domain, without clipping the sequence. Offering esmfold2_fold_complex is fine only as confidence scores, not as a way to see the structure.
FAIL if it clips or windows the sequence, retries the view, folds without asking, or says esmfold2_fold_complex will show the structure.
