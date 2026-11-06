---
description: The GB1 starter launcher runs one ESM Atlas similarity search through the public Biohub MCP.
expected_outcome: The esm-atlas skill resolves the pinned GB1 fixture, calls esm_atlas_search_similar_protein_clusters once, lists the returned hits, and ends with a source line naming the tools, with no binding or efficacy claim.
tags: [smoke, atlas]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Skill, Read]
---

Find proteins similar to GB1.
