---
description: A queued fold is read with its run ID and not submitted again.
expected_outcome: esmfold2 calls esmfold2_fold_complex once with use_batch_api, gets queued with a run_id, reads it with biohub_get_inference_run, and reports the result.
tags: [esmfold2, runs]
max_turns: 25
timeout_seconds: 600
allowed_tools: [Skill, Read]
---
Fold GB1 with the batch API and tell me its pTM when it is done.
