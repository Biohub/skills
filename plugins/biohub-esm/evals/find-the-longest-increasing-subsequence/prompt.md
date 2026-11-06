---
description: A request that mentions a sequence but has nothing to do with proteins must not fire any Biohub ESM skill or Biohub MCP tool.
expected_outcome: Claude answers 3, 10, 20 directly, with no plugin skill and no Biohub MCP call.
tags: [smoke, negative]
max_turns: 10
timeout_seconds: 300
allowed_tools: [Skill]
---

What is the longest increasing subsequence of [3, 10, 2, 1, 20]? Answer in one line.
