---
# Captured from the Biohub MCP (https://biohub.ai/mcp, server 0.88.0+a496d14bff) on 2026-11-04, signed in.
# Call: esmc_scan_mutation_tolerance GB1 positions "all"
# Body: the tool's text content block, pretty-printed; non-ASCII is written as JSON escapes.
type: fixed
expect:
  sequence: '/^\s*MTYKLILNGKTLKGETTTEAVDAATAEKVFKQYANDNGVDGEWTYDDATKTFTVTE\s*$/i'
---

{
  "execution_status": "done",
  "model_id": "esmc-6b-2024-12",
  "most_constrained": [
    {
      "position": 46,
      "wild_type": "D",
      "entropy_bits": 0.6354,
      "negative_substitution_fraction": 1.0,
      "top_substitutions": [
        {
          "alternate": "E",
          "score": -3.4688
        },
        {
          "alternate": "N",
          "score": -3.7812
        },
        {
          "alternate": "S",
          "score": -4.25
        }
      ]
    },
    {
      "position": 53,
      "wild_type": "T",
      "entropy_bits": 0.6631,
      "negative_substitution_fraction": 1.0,
      "top_substitutions": [
        {
          "alternate": "K",
          "score": -4.25
        },
        {
          "alternate": "S",
          "score": -4.25
        },
        {
          "alternate": "E",
          "score": -4.3438
        }
      ]
    },
    {
      "position": 51,
      "wild_type": "T",
      "entropy_bits": 0.7513,
      "negative_substitution_fraction": 1.0,
      "top_substitutions": [
        {
          "alternate": "V",
          "score": -3.1875
        },
        {
          "alternate": "I",
          "score": -3.5
        },
        {
          "alternate": "E",
          "score": -4.25
        }
      ]
    },
    {
      "position": 14,
      "wild_type": "G",
      "entropy_bits": 1.2604,
      "negative_substitution_fraction": 0.3684,
      "top_substitutions": [
        {
          "alternate": "E",
          "score": 6.9609
        },
        {
          "alternate": "T",
          "score": 5.1797
        },
        {
          "alternate": "S",
          "score": 4.0234
        }
      ]
    },
    {
      "position": 1,
      "wild_type": "M",
      "entropy_bits": 1.3248,
      "negative_substitution_fraction": 1.0,
      "top_substitutions": [
        {
          "alternate": "Y",
          "score": -3.1953
        },
        {
          "alternate": "V",
          "score": -3.8125
        },
        {
          "alternate": "G",
          "score": -3.9219
        }
      ]
    },
    {
      "position": 9,
      "wild_type": "G",
      "entropy_bits": 1.445,
      "negative_substitution_fraction": 1.0,
      "top_substitutions": [
        {
          "alternate": "D",
          "score": -2.5781
        },
        {
          "alternate": "N",
          "score": -3.2578
        },
        {
          "alternate": "E",
          "score": -3.4062
        }
      ]
    },
    {
      "position": 45,
      "wild_type": "Y",
      "entropy_bits": 1.7375,
      "negative_substitution_fraction": 1.0,
      "top_substitutions": [
        {
          "alternate": "F",
          "score": -0.5312
        },
        {
          "alternate": "W",
          "score": -1.0
        },
        {
          "alternate": "L",
          "score": -4.0469
        }
      ]
    },
    {
      "position": 8,
      "wild_type": "N",
      "entropy_bits": 1.8155,
      "negative_substitution_fraction": 1.0,
      "top_substitutions": [
        {
          "alternate": "D",
          "score": -1.7969
        },
        {
          "alternate": "G",
          "score": -2.6094
        },
        {
          "alternate": "K",
          "score": -2.7812
        }
      ]
    },
    {
      "position": 49,
      "wild_type": "T",
      "entropy_bits": 1.8232,
      "negative_substitution_fraction": 1.0,
      "top_substitutions": [
        {
          "alternate": "S",
          "score": -0.9688
        },
        {
          "alternate": "A",
          "score": -1.9062
        },
        {
          "alternate": "E",
          "score": -3.0156
        }
      ]
    },
    {
      "position": 11,
      "wild_type": "T",
      "entropy_bits": 2.0365,
      "negative_substitution_fraction": 0.9474,
      "top_substitutions": [
        {
          "alternate": "E",
          "score": 2.2188
        },
        {
          "alternate": "L",
          "score": -0.4922
        },
        {
          "alternate": "V",
          "score": -0.5781
        }
      ]
    }
  ],
  "most_tolerant": [
    {
      "position": 38,
      "wild_type": "G",
      "entropy_bits": 4.083,
      "negative_substitution_fraction": 1.0,
      "top_substitutions": [
        {
          "alternate": "D",
          "score": -0.2852
        },
        {
          "alternate": "N",
          "score": -0.2891
        },
        {
          "alternate": "A",
          "score": -0.3945
        }
      ]
    },
    {
      "position": 17,
      "wild_type": "T",
      "entropy_bits": 3.993,
      "negative_substitution_fraction": 0.9474,
      "top_substitutions": [
        {
          "alternate": "V",
          "score": 0.0703
        },
        {
          "alternate": "L",
          "score": -0.0234
        },
        {
          "alternate": "F",
          "score": -0.2695
        }
      ]
    },
    {
      "position": 29,
      "wild_type": "V",
      "entropy_bits": 3.9607,
      "negative_substitution_fraction": 0.7368,
      "top_substitutions": [
        {
          "alternate": "L",
          "score": 0.3203
        },
        {
          "alternate": "Y",
          "score": 0.2812
        },
        {
          "alternate": "A",
          "score": 0.1367
        }
      ]
    },
    {
      "position": 18,
      "wild_type": "T",
      "entropy_bits": 3.9405,
      "negative_substitution_fraction": 0.9474,
      "top_substitutions": [
        {
          "alternate": "G",
          "score": 0.5234
        },
        {
          "alternate": "D",
          "score": -0.0078
        },
        {
          "alternate": "V",
          "score": -0.207
        }
      ]
    },
    {
      "position": 13,
      "wild_type": "K",
      "entropy_bits": 3.9404,
      "negative_substitution_fraction": 0.7895,
      "top_substitutions": [
        {
          "alternate": "A",
          "score": 0.9966
        },
        {
          "alternate": "D",
          "score": 0.6333
        },
        {
          "alternate": "E",
          "score": 0.5747
        }
      ]
    },
    {
      "position": 31,
      "wild_type": "K",
      "entropy_bits": 3.7948,
      "negative_substitution_fraction": 0.7368,
      "top_substitutions": [
        {
          "alternate": "T",
          "score": 0.8281
        },
        {
          "alternate": "A",
          "score": 0.5859
        },
        {
          "alternate": "E",
          "score": 0.4766
        }
      ]
    },
    {
      "position": 15,
      "wild_type": "E",
      "entropy_bits": 3.7596,
      "negative_substitution_fraction": 0.5263,
      "top_substitutions": [
        {
          "alternate": "I",
          "score": 1.6465
        },
        {
          "alternate": "V",
          "score": 1.6074
        },
        {
          "alternate": "L",
          "score": 1.584
        }
      ]
    },
    {
      "position": 36,
      "wild_type": "D",
      "entropy_bits": 3.7149,
      "negative_substitution_fraction": 1.0,
      "top_substitutions": [
        {
          "alternate": "E",
          "score": -0.125
        },
        {
          "alternate": "A",
          "score": -0.4375
        },
        {
          "alternate": "L",
          "score": -0.9531
        }
      ]
    },
    {
      "position": 37,
      "wild_type": "N",
      "entropy_bits": 3.6709,
      "negative_substitution_fraction": 0.9474,
      "top_substitutions": [
        {
          "alternate": "W",
          "score": 0.5
        },
        {
          "alternate": "A",
          "score": -0.1406
        },
        {
          "alternate": "F",
          "score": -0.4531
        }
      ]
    },
    {
      "position": 56,
      "wild_type": "E",
      "entropy_bits": 3.6559,
      "negative_substitution_fraction": 0.8947,
      "top_substitutions": [
        {
          "alternate": "A",
          "score": 0.6602
        },
        {
          "alternate": "K",
          "score": 0.0234
        },
        {
          "alternate": "G",
          "score": -0.2188
        }
      ]
    }
  ],
  "coverage": {
    "requested": 56,
    "scanned": 56,
    "skipped": [],
    "unscanned": []
  },
  "usage": {
    "credits": 0.3136,
    "logits_calls": 56
  },
  "warnings": []
}
