---
description: A complex is resolved from two accessions and folded and shown in one view call.
expected_outcome: UniProt lookups for P69905 and P68871, then one ui_show_structure call with four protein entities (alpha and beta, two copies each, or four entities), no esmfold2_fold_complex, pTM and ipTM reported, and the missing credit usage said plainly.
tags: [esmfold2, viewer, complex]
max_turns: 25
timeout_seconds: 600
allowed_tools: [Skill, Read]
---
Fold human hemoglobin as an alpha2-beta2 tetramer from P69905 and P68871, and show me the complex.
