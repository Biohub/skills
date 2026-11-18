The `biohub` plugin contains no runtime code; its skills call the Biohub MCP.
The skills point to the following model weights for running the models on your own compute, which you download separately:

| Model | License | Link |
|----------|----------|----------|
| ESMC 300M, ESMC 600M, ESMC 6B | MIT and other terms (see model card) | https://huggingface.co/biohub/ESMC-300M<br>https://huggingface.co/biohub/ESMC-600M<br>https://huggingface.co/biohub/ESMC-6B |
| ESMFold2, ESMFold2-Fast | MIT (see model card) | https://huggingface.co/biohub/ESMFold2<br>https://huggingface.co/biohub/ESMFold2-Fast |

The skills retrieve or include data from the following sources:

| Data | License | Link |
|----------|----------|----------|
| ESM Atlas | CC BY 4.0; "Sequences" and "All Data" datasets CC BY-SA 4.0 | https://registry.opendata.aws/biohub-esm-atlas |
| RCSB Protein Data Bank | CC0 1.0 | https://www.rcsb.org/pages/usage-policy |
| UniProt | CC BY 4.0 | https://www.uniprot.org/help/license |

ESM Atlas data is compiled and made available by Chan Zuckerberg Biohub, Inc. under the Creative Commons Attribution 4.0 International license (CC BY 4.0, https://creativecommons.org/licenses/by/4.0/).
The "Sequences" and "All Data" datasets include third-party data and are provided under the Creative Commons Attribution-ShareAlike 4.0 International license (CC BY-SA 4.0, https://creativecommons.org/licenses/by-sa/4.0/).
The full terms, including the third-party sources in those datasets, are in the registry entry "ESM Atlas - Protein Features and Structures" at https://registry.opendata.aws/biohub-esm-atlas.
This repository does not redistribute Atlas data; the skills retrieve it when you ask.

The skills include the sequence of PDB entry 1PGA chain A (GB1), from the RCSB Protein Data Bank.
