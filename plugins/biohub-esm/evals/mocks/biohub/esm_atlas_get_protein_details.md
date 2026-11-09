---
# Captured from the Biohub MCP (https://biohub.ai/mcp, server 0.88.0+a496d14bff) on 2026-11-04, signed in.
# Call: esm_atlas_get_protein_details {"sequence": GB1}
# Body: the tool's text content block, pretty-printed; non-ASCII is written as JSON escapes.
type: fixed
expect:
  sequence: '/^\s*MTYKLILNGKTLKGETTTEAVDAATAEKVFKQYANDNGVDGEWTYDDATKTFTVTE\s*$/i'
---

{
  "sequence": "MTYKLILNGKTLKGETTTEAVDAATAEKVFKQYANDNGVDGEWTYDDATKTFTVTE",
  "sequence_length": 56,
  "accession": "UPI0000111872",
  "header": "ee915f5998df46aff7fb360a301cf505|UPI0000111872|uniparc",
  "source": "uniparc",
  "sae_features": [
    {
      "feature_index": 2822,
      "label": "Central helix-strand acidic-hydrophobic motif",
      "description": "A short central sequence motif found in small bacterial/viral/eukaryotic proteins, typically falling around residues ~55-70 and characterized by a mix of hydrophobic (I/L/F/V) and acidic/charged residues in patterns such as \"Ex[FILV][ILV]xLSD\" or \"[FY]D[FILV]xDD\". The activation tends to coincide with an \u03b1-helix to \u03b2-strand transition in compact globular folds.",
      "value": 0.7990338665598503,
      "label_reliability": "moderate",
      "residue_regions": [
        {
          "start": 34,
          "end": 55,
          "peak_residue": 49,
          "mean_activation": 5.8337
        }
      ]
    },
    {
      "feature_index": 4328,
      "label": "Charged amphipathic recognition helix",
      "description": "A short, charged, amphipathic alpha-helix used as a generic interaction element across diverse proteins, often serving as the recognition helix in nucleic acid-binding domains or as a surface helix within compact folds (including the single helix of Kunitz-type inhibitors), rather than a family-specific motif.",
      "value": 0.5752033699970652,
      "label_reliability": "moderate",
      "residue_regions": [
        {
          "start": 20,
          "end": 39,
          "peak_residue": 29,
          "mean_activation": 4.344
        }
      ]
    },
    {
      "feature_index": 1089,
      "label": "N-terminal leader docking helix",
      "description": "N-terminal alpha-helix of small accessory proteins and peptide precursors used as a docking/processing module, mediating partner/chaperone engagement, complex assembly, or export recognition across diverse systems.",
      "value": 0.5571125374460114,
      "label_reliability": "moderate",
      "residue_regions": [
        {
          "start": 0,
          "end": 34,
          "peak_residue": 5,
          "mean_activation": 3.1307
        }
      ]
    },
    {
      "feature_index": 12780,
      "label": "Short aromatic acidic loop motif",
      "description": "A short, exposed loop/strand motif typically centered on an aromatic\u2013aliphatic core flanked by acidic residues, used as a surface element. The feature recurs in several unrelated protein families, often in nucleic-acid-related contexts.",
      "value": 0.4869209377786424,
      "label_reliability": "low",
      "residue_regions": [
        {
          "start": 9,
          "end": 22,
          "peak_residue": 13,
          "mean_activation": 4.3485
        }
      ]
    },
    {
      "feature_index": 2189,
      "label": "Small, globally activated proteins",
      "description": "Small, compact proteins (~70-170 residues) showing near whole-protein activation, enriched for viral/phage host-defense antagonists and nucleic-acid\u2013associated factors, alongside small bacterial accessory subunits with similar size and fold characteristics.",
      "value": 0.38998673571038617,
      "label_reliability": "low",
      "residue_regions": [
        {
          "start": 7,
          "end": 46,
          "peak_residue": 22,
          "mean_activation": 1.9754
        },
        {
          "start": 2,
          "end": 2,
          "peak_residue": 2,
          "mean_activation": 1.3892
        },
        {
          "start": 55,
          "end": 55,
          "peak_residue": 55,
          "mean_activation": 0.9618
        }
      ]
    },
    {
      "feature_index": 7643,
      "label": "N-terminal \u03b2/Cys-loop micro-motifs",
      "description": "Short, localized micro-motifs in N-terminal \u03b2-strands and disulfide-stabilized loops; one mode is a hydrophobic N-terminal \u03b2-strand \"SH[T/I]ILL\"-type segment, another is a cysteine-rich loop containing YCC/WCC/CYCC patterns within multi-disulfide cores.",
      "value": 0.3647009864036971,
      "label_reliability": "low",
      "residue_regions": [
        {
          "start": 0,
          "end": 12,
          "peak_residue": 4,
          "mean_activation": 3.6087
        }
      ]
    },
    {
      "feature_index": 3150,
      "label": "Short conserved loop/turn motifs",
      "description": "Short conserved loop/turn motifs in diverse viral, bacterial, and eukaryotic proteins. The feature highlights compact \u03b2-turn or loop segments often following a \"DGxx\" or similar small-residue prelude, in disordered cytoplasmic tails, exposed loops, or surface-accessible segments of larger folded domains.",
      "value": 0.3091046288202152,
      "label_reliability": "low",
      "residue_regions": [
        {
          "start": 51,
          "end": 53,
          "peak_residue": 53,
          "mean_activation": 5.7172
        },
        {
          "start": 40,
          "end": 44,
          "peak_residue": 40,
          "mean_activation": 1.2824
        },
        {
          "start": 10,
          "end": 10,
          "peak_residue": 10,
          "mean_activation": 1.0686
        }
      ]
    },
    {
      "feature_index": 1801,
      "label": "C-terminal secondary-structure regional activation",
      "description": "A feature that activates over short stretches within small, often compact proteins, frequently located in the C-terminal half on a single \u03b1-helix or \u03b2-strand element. The activated residues are a mix of hydrophobic, polar, and charged amino acids rather than any clear single composition bias.",
      "value": 0.27695024432507287,
      "label_reliability": "low",
      "residue_regions": [
        {
          "start": 27,
          "end": 55,
          "peak_residue": 48,
          "mean_activation": 2.163
        }
      ]
    },
    {
      "feature_index": 15089,
      "label": "Short charged amphipathic interfaces",
      "description": "Short, charge-rich amphipathic interface segments used for partner binding and complex assembly\u2014most often a single \u03b1-helix with adjacent coil (and occasionally a short \u03b2-strand/loop)\u2014that act as linear binding modules in small proteins/peptides and small subunits (toxins/pheromones, toxin\u2013immunity pairs, secretion chaperones, chromatin and transcription complexes, and other oligomeric assemblies). These segments mix acidic/basic clusters with aliphatic (L/I) residues to create amphipathic surfaces and occur across all domains of life and viruses.",
      "value": 0.26191770994174485,
      "label_reliability": "low",
      "residue_regions": [
        {
          "start": 23,
          "end": 55,
          "peak_residue": 43,
          "mean_activation": 2.4234
        },
        {
          "start": 12,
          "end": 12,
          "peak_residue": 12,
          "mean_activation": 1.3892
        }
      ]
    },
    {
      "feature_index": 2232,
      "label": "Secreted beta-strand motifs",
      "description": "Short structured segments \u2014 predominantly \u03b2-strands within disulfide-stabilized folds of secreted proteins (toxins, immunity proteins, lectin/chitin-binding proteins, superantigen-like proteins) \u2014 typically 5-10 contiguous residues containing a mix of hydrophobic, polar, and charged amino acids, frequently with nearby aromatic (Y/W/F) residues.",
      "value": 0.24099112879547308,
      "label_reliability": "low",
      "residue_regions": [
        {
          "start": 35,
          "end": 49,
          "peak_residue": 41,
          "mean_activation": 3.7402
        }
      ]
    }
  ],
  "ptm": null,
  "mean_plddt": null,
  "structure_available": false,
  "structure_can_be_computed": true,
  "features_computed_on_miss": false,
  "structure_source": null,
  "structure_model": null,
  "structure_size_bytes": null,
  "residue_confidence_count": null,
  "folded_on_miss": false
}
