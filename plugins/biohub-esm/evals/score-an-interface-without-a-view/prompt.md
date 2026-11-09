---
description: A confidence question without a request to see the structure uses the scoring fold tool.
expected_outcome: esmfold2 calls esmfold2_fold_complex once for alpha and beta, does not open the viewer, reports pTM and ipTM, and reports the 0.4177 credits returned.
tags: [esmfold2, complex]
max_turns: 25
timeout_seconds: 600
allowed_tools: [Skill, Read]
---
How confident is ESMFold2 in the interface between hemoglobin alpha (P69905) and beta (P68871)? I don't need to see it.
