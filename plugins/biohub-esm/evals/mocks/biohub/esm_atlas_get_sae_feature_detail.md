---
# Captured from the Biohub MCP (https://biohub.ai/mcp, server 0.88.0+a496d14bff) on 2026-11-04, signed in.
# Call: esm_atlas_get_sae_feature_detail {"feature_index": 13}
# Body: the tool's text content block, pretty-printed; non-ASCII is written as JSON escapes.
type: fixed
expect:
  feature_index: '/^13$/'
---

{
  "feature_index": 13,
  "label": "N-terminal \u03b2-strand block",
  "summary": "N-terminal structural elements\u2014particularly the first \u03b2-strand(s) of small folded domains and the N-terminal segment immediately preceding/following them\u2014across phage capsid proteins, SecB-family chaperones, signal peptidase complex subunits, and other small bacterial/archaeal proteins.",
  "description": "Summary: N-terminal structural elements\u2014particularly the first \u03b2-strand(s) of small folded domains and the N-terminal segment immediately preceding/following them\u2014across phage capsid proteins, SecB-family chaperones, signal peptidase complex subunits, and other small bacterial/archaeal proteins.\n\nActivation pattern: Regional activation over a contiguous N-terminal block (roughly residues 1\u201350), with the strongest peaks landing on the first \u03b2-strand of the fold and tapering into adjacent loops and short helices. Activation is high across mixed residue compositions (hydrophobic, charged, and polar) rather than restricted to any single residue class, and drops sharply in the rest of the folded core.\n\nExemplars:\n- Phage capsid coat proteins (e.g., PP7, fr, PRR1, Q\u03b2 A1): activation on the N-terminal \u03b2-strands of the capsid fold.\n- SecB and SecB-like chaperones (E. coli SecB, H. influenzae SecB, Mtb Rv1957): activation on the first long \u03b2-strand and flanking helix near the N-terminus.\n- Signal peptidase complex subunit 3 (yeasts): activation across the N-terminal cytoplasmic segment, signal-anchor TM helix, and start of the lumenal domain.\n- Spore coat morphogenetic protein CotE: activation in the N-terminal region required for coat protein deposition.",
  "category": "Compositional bias",
  "activation_pattern": "Regional activation over a contiguous N-terminal block (roughly residues 1\u201350), with the strongest peaks landing on the first \u03b2-strand of the fold and tapering into adjacent loops and short helices. Activation is high across mixed residue compositions (hydrophobic, charged, and polar) rather than restricted to any single residue class, and drops sharply in the rest of the folded core.",
  "exemplar_protein_families": "- Phage capsid coat proteins (e.g., PP7, fr, PRR1, Q\u03b2 A1): activation on the N-terminal \u03b2-strands of the capsid fold.\n- SecB and SecB-like chaperones (E. coli SecB, H. influenzae SecB, Mtb Rv1957): activation on the first long \u03b2-strand and flanking helix near the N-terminus.\n- Signal peptidase complex subunit 3 (yeasts): activation across the N-terminal cytoplasmic segment, signal-anchor TM helix, and start of the lumenal domain.\n- Spore coat morphogenetic protein CotE: activation in the N-terminal region required for coat protein deposition.",
  "uniref90_frequency": 49268642,
  "top_swissprot_activations": [
    {
      "uniprot_id": "P03630",
      "activation": 10.025796890258789
    },
    {
      "uniprot_id": "P14016",
      "activation": 9.904528617858887
    },
    {
      "uniprot_id": "P44853",
      "activation": 9.788032531738281
    },
    {
      "uniprot_id": "P03614",
      "activation": 9.748165130615234
    },
    {
      "uniprot_id": "P03616",
      "activation": 9.308323860168457
    },
    {
      "uniprot_id": "P03615",
      "activation": 9.236960411071777
    },
    {
      "uniprot_id": "Q8LTE1",
      "activation": 9.059258460998535
    },
    {
      "uniprot_id": "Q12133",
      "activation": 8.882561683654785
    },
    {
      "uniprot_id": "P95257",
      "activation": 8.733137130737305
    },
    {
      "uniprot_id": "C0HK80",
      "activation": 8.66882610321045
    }
  ],
  "decoder_nearest_neighbors": [
    14228,
    5157,
    5301,
    7807,
    6038
  ]
}
