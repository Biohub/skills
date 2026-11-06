---
description: Binder design is outside the plugin and is declined without a tool call.
expected_outcome: The reply says the plugin does not offer binder design, names what it covers, and calls no Biohub tool.
tags: [router, scope]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Skill, Read]
---
Design a minibinder against PD-L1.
