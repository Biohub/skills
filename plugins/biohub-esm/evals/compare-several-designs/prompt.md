---
description: Folding several inputs asks first.
expected_outcome: esmfold2 says how many folds the request needs and asks a yes or no question before folding anything.
tags: [esmfold2, cost]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Skill, Read]
---
Compare ESMFold2 confidence for these three designs:

1. MKTAYIAKQRQISFVKSHFSRQ
2. MKTAYIAKQRQISFVKSHFSRE
3. MKTAYIAKQRQISFVKSHFSRK
