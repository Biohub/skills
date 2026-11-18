"""Static checks on the plugins' manifests and licenses, and on Biohub's skills.

They cover what `claude plugin validate` does not: the Codex manifest, version sync across
manifests, marketplace entries, license copies, the Biohub skills' shared rules, and the
argument names and limits the skills state for the Biohub MCP tools.
"""

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGINS = sorted(path for path in (ROOT / "plugins").iterdir() if path.is_dir())
PLUGIN = ROOT / "plugins" / "biohub-esm"
SKILLS = sorted(path for path in (PLUGIN / "skills").iterdir() if path.is_dir())
# A number followed by one of these units is a limit the skill takes from a tool's description.
LIMIT = re.compile(
    r"(\d[\d,]*)[- ](residues?|runs? a day|positions?|chains?|tokens?|characters|copies|folds?)\b"
)
TOOLS_JSON = PLUGIN / "evals" / "mocks" / "biohub" / "_tools.json"
TOOL_REFERENCE = PLUGIN / "skills" / "esm-atlas" / "references" / "mcp-tools.md"
MCP_URL = "https://biohub.ai/mcp"
PRECEDENCE = (
    "The user's instructions take precedence over guidelines provided in a skill.\n"
    "If explicit user instructions conflict with a skill's instructions, "
    "prioritize the user's instructions."
)


def read_json(path: Path) -> dict:
    return json.loads(path.read_text())


def frontmatter(skill: Path) -> dict[str, str]:
    """The `key: value` lines between the opening and closing `---` of a SKILL.md."""
    text = (skill / "SKILL.md").read_text()
    match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    if match is None:
        raise AssertionError(f"{skill.name}/SKILL.md has no frontmatter")
    return dict(line.split(": ", 1) for line in match.group(1).splitlines() if ": " in line)


def skill_dirs(plugin: Path) -> list[Path]:
    return sorted(path for path in (plugin / "skills").iterdir() if path.is_dir())


def plugin_license(plugin: Path) -> Path:
    """The plugin's own license file, `LICENSE.md` or `LICENSE`."""
    for name in ("LICENSE.md", "LICENSE"):
        if (plugin / name).is_file():
            return plugin / name
    raise AssertionError(f"{plugin.name} has no LICENSE.md or LICENSE")


def numbers_in(value: object) -> set[str]:
    """Every number in a JSON value's text and integer fields, without thousands separators."""
    text = json.dumps(value)
    return {number.replace(",", "") for number in re.findall(r"\d[\d,]*\d|\d", text)}


def license_text(path: Path) -> str:
    """License text without Markdown emphasis, so LICENSE and LICENSE.md copies compare equal."""
    return path.read_text().replace("**", "").strip()


def schema_property_names(schema: object) -> set[str]:
    """Every property name anywhere in a JSON schema, including nested option objects."""
    names: set[str] = set()
    if isinstance(schema, dict):
        for key, value in schema.items():
            if key == "properties" and isinstance(value, dict):
                names.update(value)
            names |= schema_property_names(value)
    elif isinstance(schema, list):
        for item in schema:
            names |= schema_property_names(item)
    return names


class PluginContractTest(unittest.TestCase):
    def test_claude_and_codex_manifests_agree(self) -> None:
        for plugin in PLUGINS:
            claude = read_json(plugin / ".claude-plugin" / "plugin.json")
            codex = read_json(plugin / ".codex-plugin" / "plugin.json")
            self.assertEqual(claude["name"], "biohub" if plugin == PLUGIN else plugin.name)
            for field in ("name", "version", "description", "license", "author", "homepage"):
                with self.subTest(plugin=plugin.name, field=field):
                    self.assertEqual(claude[field], codex[field])
            self.assertRegex(claude["version"], r"^\d+\.\d+\.\d+$")

    def test_mcp_config_is_the_biohub_server(self) -> None:
        manifest = read_json(PLUGIN / ".codex-plugin" / "plugin.json")
        servers = read_json(PLUGIN / manifest["mcpServers"])["mcpServers"]
        self.assertEqual(
            servers,
            {
                "biohub": {
                    "type": "http",
                    "url": MCP_URL,
                    "extensions": {
                        "com.openai": {"auth": {"type": "oauth", "client": {"mode": "cimd"}}}
                    },
                }
            },
        )

    def test_marketplaces_list_every_plugin(self) -> None:
        claude = read_json(ROOT / ".claude-plugin" / "marketplace.json")["plugins"]
        codex = read_json(ROOT / ".agents" / "plugins" / "marketplace.json")["plugins"]
        expected = {
            read_json(plugin / ".codex-plugin" / "plugin.json")["name"]: f"./plugins/{plugin.name}"
            for plugin in PLUGINS
        }
        self.assertEqual(len(expected), len(PLUGINS))
        self.assertEqual(read_json(ROOT / ".claude-plugin" / "marketplace.json")["name"], "biohub")
        self.assertEqual(read_json(ROOT / ".agents/plugins/marketplace.json")["name"], "biohub")
        self.assertEqual({entry["name"]: entry["source"] for entry in claude}, expected)
        self.assertEqual({entry["name"]: entry["source"]["path"] for entry in codex}, expected)

    def test_skill_frontmatter(self) -> None:
        for skill in SKILLS:
            with self.subTest(skill=skill.name):
                fields = frontmatter(skill)
                self.assertEqual(fields["name"], skill.name)
                # The Agent Skills format caps the description at 1,024 characters.
                self.assertLessEqual(len(fields["description"]), 1024)
                self.assertEqual(fields["license"], "MIT")

    def test_agent_metadata(self) -> None:
        for skill in SKILLS:
            with self.subTest(skill=skill.name):
                text = (skill / "agents" / "openai.yaml").read_text()
                for key in ("display_name", "short_description", "default_prompt"):
                    self.assertRegex(text, rf'\n  {key}: "[^"]+"\n')

    def test_biohub_esm_uses_the_repository_license(self) -> None:
        self.assertEqual(license_text(plugin_license(PLUGIN)), license_text(ROOT / "LICENSE.md"))

    def test_every_skill_license_matches_its_plugin_license(self) -> None:
        for plugin in PLUGINS:
            expected = license_text(plugin_license(plugin))
            for skill in skill_dirs(plugin):
                path = skill / "LICENSE.md"
                with self.subTest(path=str(path.relative_to(ROOT))):
                    self.assertEqual(license_text(path), expected)

    def test_every_skill_puts_user_instructions_first(self) -> None:
        for skill in SKILLS:
            with self.subTest(skill=skill.name):
                self.assertIn(PRECEDENCE, (skill / "SKILL.md").read_text())

    def test_tool_reference_arguments_exist_in_the_captured_schemas(self) -> None:
        schemas = {tool["name"]: tool["inputSchema"] for tool in read_json(TOOLS_JSON)["tools"]}
        sections = re.split(r"^### `([a-z0-9_]+)`$", TOOL_REFERENCE.read_text(), flags=re.M)
        for tool, body in zip(sections[1::2], sections[2::2], strict=True):
            with self.subTest(tool=tool):
                self.assertIn(tool, sorted(schemas), "recapture _tools.json if the server changed")
                arguments = next(
                    (line for line in body.splitlines() if line.startswith("- Argument")), ""
                )
                # An argument is a backticked name followed by its limits in parentheses.
                named = set(re.findall(r"`([a-z_]+)` \(", arguments))
                self.assertLessEqual(named, schema_property_names(schemas[tool]))

    def test_stated_limits_match_the_captured_tools(self) -> None:
        known = numbers_in(read_json(TOOLS_JSON)["tools"])
        pages = [*PLUGIN.glob("skills/**/*.md"), *PLUGIN.glob("references/*.md")]
        for page in sorted(pages):
            for number, unit in LIMIT.findall(page.read_text()):
                with self.subTest(page=str(page.relative_to(ROOT)), limit=f"{number} {unit}"):
                    self.assertIn(
                        number.replace(",", ""), known, "recapture _tools.json or fix the skill"
                    )


if __name__ == "__main__":
    unittest.main()
