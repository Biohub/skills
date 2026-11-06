---
description: A UniProt accession is resolved to its sequence through the Biohub MCP before its structure is shown.
expected_outcome: The esm-atlas skill calls esm_atlas_search_uniprot for P69905 before ui_show_structure, names human hemoglobin subunit alpha, and labels the structure as a computational prediction.
tags: [smoke, atlas]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Skill, Read]
---

Look up UniProt P69905 and show me its structure.
