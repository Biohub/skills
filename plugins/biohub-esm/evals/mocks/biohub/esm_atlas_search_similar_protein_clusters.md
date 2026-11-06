---
# Captured from the Biohub MCP (https://biohub.ai/mcp, server 0.88.0+a496d14bff) on 2026-11-04, signed in.
# Call: esm_atlas_search_similar_protein_clusters {"sequence": GB1, "top_k": 10, "uncharacterized_only": false}
# Body: the tool's text content block, pretty-printed; non-ASCII is written as JSON escapes.
type: fixed
expect:
  sequence: '/^\s*MTYKLILNGKTLKGETTTEAVDAATAEKVFKQYANDNGVDGEWTYDDATKTFTVTE\s*$/i'
---

{
  "query_sequence_length": 56,
  "hits": [
    {
      "protein_accession": "Boeuf_2021_marine_HOT_ALOHA|SAMN11874620|k141_556014_1",
      "sequence": "MVKGKLERKYKLIHNGRELSKGLLSEAGKYDAMQILVQKFDEGREGAIDPDAVEVIDVTKEK",
      "sequence_length": 62,
      "similarity_score": 0.8239336436709238,
      "cluster_size": 68,
      "protein_name": "Hypothetical protein"
    },
    {
      "protein_accession": "Larkin_2021_GO-SHIP_marine|SAMN15783066|k141_7518_2",
      "sequence": "MVKGRLEKKYKLIYNGRELSQGLLSEAGKYDAMQILVQKFDQGIEDAIDPDEVEIIDMSLKENQ",
      "sequence_length": 64,
      "similarity_score": 0.8195625044955465,
      "cluster_size": 65,
      "protein_name": "Hypothetical protein"
    },
    {
      "protein_accession": "Boeuf_2021_marine_HOT_ALOHA|SAMN11874733|k141_109969_1",
      "sequence": "MVKGKLERKYKLIHNGRELSQGLLSEAGKYDAMQILVQKFDEGRPDAIDPDEVEIIDMSLE",
      "sequence_length": 61,
      "similarity_score": 0.8189739645058629,
      "cluster_size": 50,
      "protein_name": "Hypothetical protein"
    },
    {
      "protein_accession": "Raes_2018_Australia_SPO|SAMN07483203|k141_100589_1",
      "sequence": "MVKGKLERKFKLIHNGRELSQGLLSEAGKYDAMQILVQKFDSGIEGAIDPDEVTVVEKPEEE",
      "sequence_length": 62,
      "similarity_score": 0.8181219073595004,
      "cluster_size": 72,
      "protein_name": "Hypothetical protein"
    },
    {
      "protein_accession": "Boeuf_2021_marine_HOT_ALOHA|SAMN11874715|k141_475100_2",
      "sequence": "MVKGKLEKKYKLIYNGRELSKGLLSEAGKYDAMQILVQRFDEGRPDAIDPDEVEIIDVTKEK",
      "sequence_length": 62,
      "similarity_score": 0.8131196648080506,
      "cluster_size": 71,
      "protein_name": "Hypothetical protein"
    },
    {
      "protein_accession": "Boeuf_2021_marine_HOE_Legacy_2|SAMN07224090|k141_505082_1",
      "sequence": "MVKGKLERKYKLIHNGRELSQGLLSEAGKYDAMQILVQRFDEGREGAIDPDEVEIIDMSLKENQH",
      "sequence_length": 65,
      "similarity_score": 0.8122905810601742,
      "cluster_size": 81,
      "protein_name": "Hypothetical protein"
    },
    {
      "protein_accession": "Boeuf_2021_marine_HOT_ALOHA|SAMN11874631|k141_792725_2",
      "sequence": "MAKGKLEKKYKLIYNGRELSQGLLSEAGKYDAMQILVQRFDEGREGAIDPDEVEIIDMSLKENQE",
      "sequence_length": 65,
      "similarity_score": 0.8115791351896118,
      "cluster_size": 65,
      "protein_name": "Hypothetical protein"
    },
    {
      "protein_accession": "Boeuf_2021_marine_HOT_ALOHA|SAMN11874730|k141_398590_1",
      "sequence": "MVKGKLEKKYRLIHNGRELSQGLLSEAGKYDAMQILVQKFDEGREDAIAPDEVEIIDVTKEKS",
      "sequence_length": 63,
      "similarity_score": 0.810716962630147,
      "cluster_size": 93,
      "protein_name": "Hypothetical protein"
    },
    {
      "protein_accession": "TARA_Oceans_protists_metaG|SAMEA2623985|k119_1008707_2",
      "sequence": "MVKGKLERKYKLIHNGRELSLGLLSEAGKYDAMQILVQKFDEGVEGAIDPDEVEIIDMSLEENQ",
      "sequence_length": 64,
      "similarity_score": 0.8101724591465467,
      "cluster_size": 73,
      "protein_name": "Hypothetical protein"
    },
    {
      "protein_accession": "Mukherjee_2020_lakes_Europe_Asia|SAMEA8659996|k141_566270_41",
      "sequence": "MKYRVIVNGVSFYTTGAAIKRGVGDSDGVNTVVRQLFESMFNAIGIASTMHVYDHKMNRVSYDVQISKV",
      "sequence_length": 69,
      "similarity_score": 0.8085391070029808,
      "cluster_size": 54,
      "protein_name": "Hypothetical protein"
    }
  ],
  "top_features_across_results": [
    {
      "feature_index": 2822,
      "occurrence_count": 10,
      "mean_activation": 0.853146567350894
    },
    {
      "feature_index": 4328,
      "occurrence_count": 10,
      "mean_activation": 0.6570169577385606
    },
    {
      "feature_index": 12780,
      "occurrence_count": 10,
      "mean_activation": 0.5614017843806813
    },
    {
      "feature_index": 1089,
      "occurrence_count": 10,
      "mean_activation": 0.5482838109462873
    },
    {
      "feature_index": 7643,
      "occurrence_count": 10,
      "mean_activation": 0.43637674863970355
    },
    {
      "feature_index": 2189,
      "occurrence_count": 10,
      "mean_activation": 0.40803577881596187
    },
    {
      "feature_index": 830,
      "occurrence_count": 10,
      "mean_activation": 0.3544960540697678
    },
    {
      "feature_index": 5864,
      "occurrence_count": 10,
      "mean_activation": 0.32428710126503824
    },
    {
      "feature_index": 179,
      "occurrence_count": 10,
      "mean_activation": 0.3136177962610913
    },
    {
      "feature_index": 15089,
      "occurrence_count": 10,
      "mean_activation": 0.2870204439146988
    },
    {
      "feature_index": 1801,
      "occurrence_count": 10,
      "mean_activation": 0.24903745009320194
    },
    {
      "feature_index": 2803,
      "occurrence_count": 10,
      "mean_activation": 0.2479185414525431
    },
    {
      "feature_index": 5632,
      "occurrence_count": 10,
      "mean_activation": 0.2469508581747895
    },
    {
      "feature_index": 168,
      "occurrence_count": 10,
      "mean_activation": 0.24339451426820807
    },
    {
      "feature_index": 5684,
      "occurrence_count": 10,
      "mean_activation": 0.23812108862035292
    },
    {
      "feature_index": 7125,
      "occurrence_count": 10,
      "mean_activation": 0.2308130215976548
    },
    {
      "feature_index": 13094,
      "occurrence_count": 10,
      "mean_activation": 0.22845689676389788
    },
    {
      "feature_index": 6827,
      "occurrence_count": 10,
      "mean_activation": 0.2280927827365821
    },
    {
      "feature_index": 5574,
      "occurrence_count": 1,
      "mean_activation": 0.19899198974477514
    },
    {
      "feature_index": 15657,
      "occurrence_count": 10,
      "mean_activation": 0.1940198362667557
    }
  ],
  "restricted_count": 0
}
