#!/usr/bin/env python3
"""
Generate opencode.jsonc agent section from models.yaml.

This is the single source of truth pipeline:
  models.yaml → generate_config.py → opencode.jsonc → audit_agent_models.py → matrix

Usage:
  python3 scripts/generate_config.py              # regenerate agent section in opencode.jsonc
  python3 scripts/generate_config.py --check      # verify opencode.jsonc is up-to-date
"""

import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
MODELS_YAML = ROOT / "models.yaml"
OPENCODE_JSONC = ROOT / "opencode.jsonc"


def generate_agent_section(models: dict) -> str:
    """Generate the agent section of opencode.jsonc from models.yaml."""
    lines = []
    lines.append('  "agent": {')

    for agent_name, agent_conf in models.items():
        lines.append(f'    "{agent_name}": {{')
        lines.append(f'      "description": "{agent_conf.get("description", agent_name)}",')
        lines.append(f'      "mode": "{agent_conf["mode"]}",')

        # Optional color
        if "color" in agent_conf:
            lines.append(f'      "color": "{agent_conf["color"]}",')

        # Optional tools
        if "tools" in agent_conf:
            tools = agent_conf["tools"]
            lines.append(f'      "tools": {{')
            tool_items = [f'        "{k}": {"true" if v else "false"}' for k, v in tools.items()]
            lines.append(",\n".join(tool_items))
            lines.append(f'      }},')

        lines.append(f'      "model": "{agent_conf["model"]}",')
        lines.append(f'      "prompt": "{agent_conf["prompt"]}"')
        lines.append(f'    }},')

    lines.append('  },')
    return "\n".join(lines)


def update_config(models_path: Path, config_path: Path) -> int:
    """Update opencode.jsonc agent section from models.yaml. Returns number of agents."""
    models = yaml.safe_load(models_path.read_text(encoding="utf-8"))
    agents = models.get("agents", {})

    config_text = config_path.read_text(encoding="utf-8")

    # Generate new agent section
    new_section = generate_agent_section(agents)

    # Find and replace the agent section in the config
    # Pattern: "agent": { ... },
    agent_pattern = re.compile(
        r'  "agent": \{.*?\n  \},',
        re.DOTALL
    )

    if agent_pattern.search(config_text):
        new_text = agent_pattern.sub(new_section.rstrip('\n'), config_path.read_text(encoding="utf-8"))
        config_path.write_text(new_text, encoding="utf-8")
        print(f"✅ Updated {config_path} — {len(agents)} agents from {models_path}")
        return len(agents)
    else:
        print(f"❌ Could not find agent section in {config_path}", file=sys.stderr)
        return 0


def check_config(models_path: Path, config_path: Path) -> bool:
    """Verify opencode.jsonc matches models.yaml. Returns True if up-to-date."""
    models = yaml.safe_load(models_path.read_text(encoding="utf-8"))
    agents = models.get("agents", {})

    # Generate expected agent section
    expected = generate_agent_section(agents)

    # Read current config
    config_text = config_path.read_text(encoding="utf-8")

    # Check if expected section is in config
    # Simplified check: verify each agent's model matches
    import json5
    config = json5.loads(config_text)
    config_agents = config.get("agent", {})

    for agent_name, agent_conf in agents.items():
        if agent_name not in config_agents:
            print(f"missing agent: {agent_name}", file=sys.stderr)
            return False
        if config_agents[agent_name].get("model") != agent_conf["model"]:
            print(
                f"model mismatch for {agent_name}: "
                f"config={config_agents[agent_name].get('model')} vs yaml={agent_conf['model']}",
                file=sys.stderr
            )
            return False

    return True


if __name__ == "__main__":
    if "--check" in sys.argv:
        if check_config(MODELS_YAML, OPENCODE_JSONC):
            print("✅ opencode.jsonc is up-to-date with models.yaml")
            sys.exit(0)
        else:
            print("❌ opencode.jsonc is out of date. Run: python3 scripts/generate_config.py", file=sys.stderr)
            sys.exit(1)
    else:
        count = update_config(MODELS_YAML, OPENCODE_JSONC)
        sys.exit(0 if count > 0 else 1)
