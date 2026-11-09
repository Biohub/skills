# Security

## Reporting a vulnerability

Email <security@biohub.org> if you believe you have found a security issue in this repository, the skills, or the Biohub services they call.
Do not open a public issue or pull request for a security report.

Include:

- what you found and where, such as a file path, skill, command, or service URL;
- the steps to reproduce it;
- the impact you expect.

Do not include passwords, tokens, other credentials, or personal data in the report.

## Scope

- The skills, references, and manifests in this repository.
- The Biohub MCP server at `https://biohub.ai/mcp` that the skills call.

## Handling credentials

The skills sign in to the Biohub MCP through the host's browser flow, and instruct the agent never to ask for a password, token, or key in chat.
If a skill or agent exposes a Biohub token, sign out of the Biohub MCP in your host, sign in again, and report the issue.
