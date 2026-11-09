---
# Captured from the Biohub MCP (https://biohub.ai/mcp, server 0.88.0+a496d14bff) on 2026-11-04, signed in.
# Call: esm_atlas_get_cluster_info with the top GB1 hit
# Body: the tool's text content block, pretty-printed; non-ASCII is written as JSON escapes.
type: fixed
expect:
  sequence: '/^\s*MVKGKLERKYKLIHNGRELSKGLLSEAGKYDAMQILVQKFDEGREGAIDPDAVEVIDVTKEK\s*$/i'
---

{
  "accession": "Boeuf_2021_marine_HOT_ALOHA|SAMN11874620|k141_556014_1",
  "source": "spire",
  "protein_name": "Hypothetical protein",
  "cluster_size": 68,
  "cluster_pct_characterized": 0,
  "cluster_mean_domain_coverage": 0.0,
  "top_pfam_domains": null,
  "representative_features": [
    {
      "feature_index": 2822,
      "label": "Central helix-strand acidic-hydrophobic motif",
      "description": "A short central sequence motif found in small bacterial/viral/eukaryotic proteins, typically falling around residues ~55-70 and characterized by a mix of hydrophobic (I/L/F/V) and acidic/charged residues in patterns such as \"Ex[FILV][ILV]xLSD\" or \"[FY]D[FILV]xDD\". The activation tends to coincide with an \u03b1-helix to \u03b2-strand transition in compact globular folds.",
      "value": 0.8742370836096838
    },
    {
      "feature_index": 4328,
      "label": "Charged amphipathic recognition helix",
      "description": "A short, charged, amphipathic alpha-helix used as a generic interaction element across diverse proteins, often serving as the recognition helix in nucleic acid-binding domains or as a surface helix within compact folds (including the single helix of Kunitz-type inhibitors), rather than a family-specific motif.",
      "value": 0.6967252402963403
    },
    {
      "feature_index": 12780,
      "label": "Short aromatic acidic loop motif",
      "description": "A short, exposed loop/strand motif typically centered on an aromatic\u2013aliphatic core flanked by acidic residues, used as a surface element. The feature recurs in several unrelated protein families, often in nucleic-acid-related contexts.",
      "value": 0.5986732934965565
    },
    {
      "feature_index": 1089,
      "label": "N-terminal leader docking helix",
      "description": "N-terminal alpha-helix of small accessory proteins and peptide precursors used as a docking/processing module, mediating partner/chaperone engagement, complex assembly, or export recognition across diverse systems.",
      "value": 0.5466009527012339
    },
    {
      "feature_index": 7643,
      "label": "N-terminal \u03b2/Cys-loop micro-motifs",
      "description": "Short, localized micro-motifs in N-terminal \u03b2-strands and disulfide-stabilized loops; one mode is a hydrophobic N-terminal \u03b2-strand \"SH[T/I]ILL\"-type segment, another is a cysteine-rich loop containing YCC/WCC/CYCC patterns within multi-disulfide cores.",
      "value": 0.44951516224728694
    },
    {
      "feature_index": 830,
      "label": "Terminal signals and tails",
      "description": "Terminal leader/tail segments of proteins\u2014especially N-termini\u2014comprising low-complexity and/or hydrophobic stretches such as signal/anchor peptides, short transmembrane or amphipathic helices, and flexible linkers; in large multi-domain effectors the feature preferentially marks these non-core terminal modules over downstream catalytic/repeat regions, and can include reactive Cys or metal-binding sites embedded in such tails. In smaller single-domain proteins the activation can extend broadly across the chain.",
      "value": 0.37936700048805605
    },
    {
      "feature_index": 5864,
      "label": "Coil-to-structure initiators",
      "description": "Short leader segments that mark the transition from disordered tails or signal peptides into the first structured element of a fold (coil-to-\u03b2/\u03b1 initiators), and analogous short coil-to-strand transitions within small folded proteins.",
      "value": 0.3784412554107397
    },
    {
      "feature_index": 2189,
      "label": "Small, globally activated proteins",
      "description": "Small, compact proteins (~70-170 residues) showing near whole-protein activation, enriched for viral/phage host-defense antagonists and nucleic-acid\u2013associated factors, alongside small bacterial accessory subunits with similar size and fold characteristics.",
      "value": 0.3760586324574075
    },
    {
      "feature_index": 179,
      "label": "Short hydrophobic beta-strand motif",
      "description": "A short hydrophobic micro-motif (~4-10 residues) enriched in V/L/I/F/Y/W and often adjacent to basic residues (K/R). It frequently coincides with short beta-strands but also appears within C-terminal tail segments in some proteins. It recurs across small beta-sheet modules (e.g., SH3-, KOW-, GYF-, PWWP-, PHD-like folds) and comparable hydrophobic stretches in diverse proteins and taxa.",
      "value": 0.2933198949185301
    },
    {
      "feature_index": 5632,
      "label": "Glycine coil-to-beta junctions",
      "description": "Residue-level signal for glycine- (often with acidic) enriched short coils that nucleate \u03b2-strands\u2014i.e., coil\u2192\u03b2 junctions forming edge turns of \u03b2-sheets\u2014most prominent in WD40/Kelch/NHL propellers but also present in other \u03b2-sheet domains (e.g., OB-folds, \u03b2-sandwiches) within eukaryotic scaffold/adaptor proteins (BBSome/IFT, APC/C machinery, DDB1\u2013CUL4 adaptors, F-box/WD) and in \u03b2-sheet C-termini of some TRIM E3 ligases; can occur in mixed-architecture or membrane/secreted proteins when a \u03b2-sheet subdomain is present.",
      "value": 0.28178145541964084
    }
  ],
  "taxonomy_info": null,
  "top_phyla": null
}
