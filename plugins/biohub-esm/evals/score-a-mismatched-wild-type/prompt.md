---
description: A substitution whose wild type does not match the sequence is flagged, not scored.
expected_outcome: esmc reports that position 43 of GB1 is W, not A, gives no score for A43F, and asks which numbering the user meant.
tags: [esmc, inputs]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Skill, Read]
---
Score A43F in GB1.
