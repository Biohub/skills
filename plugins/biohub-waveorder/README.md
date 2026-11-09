# Biohub WaveOrder plugin

Two skills that walk a user through [waveorder](https://github.com/Biohub/waveorder) on their own computer: a first phase or fluorescence reconstruction, and a visualization of the transfer function for a reconstruction config.
They run locally with `uv` and use no Biohub MCP tools.

```bash
/plugin install biohub-waveorder --marketplace Biohub/skills
```

| Skill | What it does |
| --- | --- |
| `waveorder-tutorial` | Walks a user from raw imaging data (TIFF, zarr, or array) to a tuned reconstruction |
| `waveorder-visualize-otf` | Computes the transfer function for a config and opens it in napari |

## Source

The skill folders are copies of `.skills/` in [`Biohub/waveorder`](https://github.com/Biohub/waveorder) at commit [`0f07a77`](https://github.com/Biohub/waveorder/commit/0f07a7733b896f91310df27bef6449c6d566d76c), the same copies the Biohub MCP serves.
They match upstream byte for byte except the copyright line of each `LICENSE.md`, which names Chan Zuckerberg Biohub, Inc. instead of Chan Zuckerberg Biohub. Change them upstream, then copy them again.
The plugin is released under the BSD 3-Clause License, in [`LICENSE.md`](LICENSE.md), not the MIT License of the rest of this repository.
Ruff skips the skill folders so they keep their upstream formatting.
Each skill carries its own `evals/evals.json` in the [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) format.
