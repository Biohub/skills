---
description: A protein name that matches several UniProt records is resolved by asking the user, not by guessing.
expected_outcome: esm-atlas searches UniProt for hemoglobin once, lists the candidates with accessions and organisms, and asks which one to use before any similarity search.
tags: [atlas]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Skill, Read]
---
Find proteins similar to hemoglobin.
