---
description: A request to see one protein uses one free view and no fold tool.
expected_outcome: esmfold2 calls ui_show_structure once with GB1 as one protein entity, calls no fold tool, and labels the view as the stored Atlas structure or the server's own prediction.
tags: [smoke, esmfold2, viewer]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Skill, Read]
---
Show me what GB1 looks like.
