---
description: A tolerance scan finishes with the protein shown and its constrained and tolerant positions highlighted.
expected_outcome: esmc calls esmc_scan_mutation_tolerance once, then ui_show_structure once with highlights for the constrained and tolerant positions.
tags: [esmc, viewer]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Skill, Read]
---
Where is GB1 most constrained or tolerant to mutation? Show me on its structure.
