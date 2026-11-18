# Connect the Biohub MCP

The Biohub MCP server runs ESMC, ESMFold2, ESM Atlas search, and a Mol* structure viewer for an agent.

| Setting | Value |
| --- | --- |
| URL | `https://biohub.ai/mcp` |
| Transport | Streamable HTTP |
| Authentication | OAuth sign-in with a Biohub account; no API key |
| Suggested server name | `biohub` |

The `biohub` plugin for Claude Code and Codex adds this server for you; you still sign in once.
Add it yourself when you use the skills without the plugin, or when you want the Biohub tools in a chat app.
Signing in opens a Biohub page in your browser, where you can also create a free account.

## Claude Code

```bash
claude mcp add --transport http biohub https://biohub.ai/mcp
```

Add `--scope user` to make it available in every project.
Then run `/mcp` inside a session, choose `biohub`, and authenticate.
If you also installed the plugin, Claude Code keeps only your entry and lists it as `biohub`.

## Claude.ai and Claude Desktop

Add it as a custom connector:

1. Open **Customize**, then **Connectors**.
2. Click **+**, then **Add custom connector**.
3. Enter `https://biohub.ai/mcp` as the remote MCP server URL, and `Biohub` as the name if asked.
   Leave **Advanced settings** empty and click **Add**.
4. Click **Connect** and sign in to Biohub in the page that opens.
5. In a chat, click **+** at the lower left, choose **Connectors**, and turn on Biohub.

On Team and Enterprise plans, only an Owner can add a custom connector, under **Organization settings**, then **Connectors**.
Members then find it under **Customize**, then **Connectors**, and click **Connect**.
Claude Desktop uses the connectors from your Claude account.

## ChatGPT

ChatGPT connects to custom MCP servers in developer mode:

1. In ChatGPT on the web, open **Settings**, then **Security and login**, and turn on **Developer mode**.
2. Go to <https://chatgpt.com/plugins> and select **+** to create a developer-mode app for a remote MCP server.
3. Enter `https://biohub.ai/mcp` as the server URL, choose **OAuth**, create it, and sign in to Biohub.
4. In a chat, choose **Developer mode** from the **+** menu and select Biohub.

## Codex

```bash
codex mcp add biohub --url https://biohub.ai/mcp
codex mcp login biohub
```

The first command writes the server to `~/.codex/config.toml`, and the second signs you in.
Check it with `codex mcp list`.

## Cursor

Add the server to `~/.cursor/mcp.json` for all projects, or to `.cursor/mcp.json` in one project:

```json
{
  "mcpServers": {
    "biohub": {
      "url": "https://biohub.ai/mcp"
    }
  }
}
```

Cursor prompts you to sign in the first time it connects.

## Other clients

Any MCP client that supports streamable HTTP and OAuth can connect with the URL above.

## Tools

| Tool | What it does | Cost |
| --- | --- | --- |
| `esm_atlas_search_uniprot` | Resolves a protein name or UniProt accession to sequences | Free |
| `esm_atlas_lookup_accession` | Resolves a UniParc, MGnify, or IMG accession to a sequence | Free |
| `esm_atlas_search_similar_protein_clusters` | Finds ESM Atlas proteins with similar ESMC SAE feature profiles | Free |
| `esm_atlas_get_protein_details` | Returns an ESM Atlas record and its top SAE features | Free |
| `esm_atlas_get_cluster_info` | Returns a protein's cluster, Pfam domains, and taxonomy | Free |
| `esm_atlas_get_sae_feature_detail` | Describes one of the 16,384 SAE features | Free |
| `ui_show_structure` | Shows a protein or complex in a Mol* viewer where the host supports MCP Apps | Free for one protein; a complex is a billed fold |
| `esmc_score_mutations` | Scores named substitutions with ESMC | Credits per distinct position |
| `esmc_scan_mutation_tolerance` | Finds a protein's most constrained and tolerant positions with ESMC | Credits per position |
| `esmfold2_fold_complex` | Folds proteins or a complex with ESMFold2 and returns confidence scores | Credits |
| `esmfold2_fold_max_accuracy` | Folds at maximum accuracy as a queued run | Credits, 10 runs a day by default |
| `biohub_get_inference_run` | Reads a queued fold run | Free |

Hosts may show the tools with a prefix, such as `mcp__biohub__esm_atlas_search_uniprot`.
Some hosts ask you to approve tools that are not marked read-only; approve them to continue.
Errors return a stable `code`, such as `invalid_input`, `not_found`, `restricted`, or `rate_limited`.
Requests involving controlled pathogens and toxins can return `restricted`.
