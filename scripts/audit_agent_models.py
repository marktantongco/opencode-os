#!/usr/bin/env python3
"""
Audit, fix, and generate agent model configuration.

Compares opencode agent model assignments against the spec and can:
  --fix              Apply matrix to both config files
  --generate-matrix  Regenerate MODEL_ASSIGNMENT_MATRIX.md from config

Usage:
  python3 scripts/audit_agent_models.py                    # audit only
  python3 scripts/audit_agent_models.py --fix              # apply matrix to configs
  python3 scripts/audit_agent_models.py --generate-matrix  # regenerate spec from config
  python3 scripts/audit_agent_models.py --fix --generate-matrix  # both

Exit code 0 = success / in sync.
Exit code 1 = drift detected (used by pre-commit hook).
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OPENCODE_JSONC = ROOT / "opencode.jsonc"
OPCODE_INSTALLED = Path.home() / ".opencode" / "opencode.json"
MATRIX_MD = ROOT / "profiles" / "MODEL_ASSIGNMENT_MATRIX.md"

# Agent metadata for matrix generation: {agent: (mode, tier, rationale)}
AGENT_METADATA = {
    "orchestrator": ("primary", "Premium", "Task decomposition + subagent dispatch needs deep reasoning"),
    "blueprint": ("primary", "Code-Spec", "Spec-first architecture, plan grammar"),
    "explorer": ("subagent", "Premium", "Balanced code understanding + pattern discovery"),
    "librarian": ("subagent", "Premium", "Balanced doc retrieval + API interpretation"),
    "fixer": ("subagent", "Code-Spec", "Code refinement + refactoring efficiency"),
    "oracle": ("subagent", "Premium", "Strategic advice needs deep reasoning"),
    "designer": ("subagent", "Premium", "Balanced for visual design + frontend"),
    "observer": ("subagent", "Mid", "Fast monitoring, no deep reasoning needed"),
    "council": ("subagent", "Premium", "Creative multi-perspective deliberation"),
    "brainstorming": ("subagent", "Premium", "Divergent thinking + ideation"),
    "plan": ("subagent", "Code-Spec", "Plan grammar validation"),
    "compaction": ("subagent", "Lightweight", "Token-efficient context compression"),
    "researcher": ("subagent", "Premium", "Web research + synthesis"),
    "owl-dns": ("subagent", "Premium", "Scraping + data interpretation"),
    "browser-use": ("subagent", "Lightweight", "Natural-language browser automation"),
    "agent-browser": ("subagent", "Lightweight", "Structured CDP browser automation"),
    "oracle-lite": ("subagent", "Mid", "Fallback — general purpose"),
    "designer-lite": ("subagent", "Mid", "Fallback — general purpose"),
    "observer-lite": ("subagent", "Mid", "Fallback — general purpose"),
    "council-lite": ("subagent", "Mid", "Fallback — general purpose"),
}

# Tier descriptions for matrix header
TIER_DESCRIPTIONS = {
    "Premium": ("Deep reasoning, balanced, or creative", "4,400–6,100"),
    "Mid": ("Fast general purpose", "4,400"),
    "Code-Spec": ("Code-specialized, efficient", "3,100"),
    "Lightweight": ("Fastest, token-efficient", "2,000"),
}


def parse_jsonc(path: Path) -> dict:
    """Parse JSONC/JSON using json5 library (handles comments, trailing commas)."""
    import json5
    return json5.loads(path.read_text(encoding="utf-8"))


def extract_spec_agents(matrix_path: Path) -> dict[str, str]:
    """Extract agent -> model mapping from MODEL_ASSIGNMENT_MATRIX.md.

    Parses the 'Agent → Model Mapping (20 Agents)' table.
    Returns {agent_name: model_id}.
    """
    text = matrix_path.read_text()
    agents = {}
    table_pattern = re.compile(
        r'`([a-z][a-z0-9_-]+)`\s*\|\s*\w+\s*\|\s*`([^`]+)`'
    )

    in_agent_table = False
    for line in text.splitlines():
        if '## Agent → Model Mapping' in line:
            in_agent_table = True
            continue
        if in_agent_table and line.startswith('## '):
            break
        if in_agent_table:
            m = table_pattern.search(line)
            if m:
                agents[m.group(1)] = m.group(2)

    return agents


def extract_config_agents(config_path: Path) -> dict[str, str]:
    """Extract agent -> model mapping from an opencode config file.
    Works for both .jsonc (with comments) and .json.
    Returns {agent_name: model_id}.
    """
    config = parse_jsonc(config_path)
    agents = {}
    for agent_name, agent_conf in config.get("agent", {}).items():
        if isinstance(agent_conf, dict) and "model" in agent_conf:
            agents[agent_name] = agent_conf["model"]
    return agents


def audit_config(config_path: Path, spec: dict[str, str], label: str) -> list[str]:
    """Audit a single config file against the spec. Returns list of issues."""
    if not config_path.exists():
        return [f"SKIP: {label} not found at {config_path}"]

    try:
        config = extract_config_agents(config_path)
    except Exception as e:
        return [f"ERROR: Failed to parse {label}: {e}"]

    issues = []
    for agent, expected_model in sorted(spec.items()):
        if agent not in config:
            issues.append(f"  MISSING: '{agent}' is in MATRIX but not in {label}")
        elif config[agent] != expected_model:
            issues.append(
                f"  DRIFT: '{agent}'\n"
                f"      spec:    {expected_model}\n"
                f"      config:  {config[agent]}"
            )

    for agent in sorted(config.keys()):
        if agent not in spec:
            issues.append(f"  EXTRA: '{agent}' in {label} but not in MATRIX (add to spec?)")

    return issues


def fix_config(config_path: Path, spec: dict[str, str]) -> int:
    """Fix any opencode config file using json5 load-modify-write.

    Loads with json5 (preserves structure), updates agent model fields,
    writes back as formatted JSON. Works for both .jsonc and .json.
    Returns number of changes made.
    """
    import json5

    text = config_path.read_text(encoding="utf-8")
    config = json5.loads(text)
    changes = 0
    agents = config.get("agent", {})

    for agent, expected_model in spec.items():
        if agent not in agents:
            print(f"    SKIP missing agent '{agent}' (needs manual creation)")
            continue
        current = agents[agent].get("model", "")
        if current != expected_model:
            print(f"    {agent}: {current} -> {expected_model}")
            agents[agent]["model"] = expected_model
            changes += 1

    if changes > 0:
        backup_path = config_path.with_suffix(config_path.suffix + ".bak.audit")
        backup_path.write_text(text, encoding="utf-8")
        config_path.write_text(
            json.dumps(config, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8"
        )

    return changes


def fix(spec: dict[str, str]) -> int:
    """Apply the matrix spec to all config files. Returns total changes."""
    total = 0

    print("🔧 Applying matrix to opencode.jsonc (repo)...")
    total += fix_config(OPENCODE_JSONC, spec)

    print("🔧 Applying matrix to ~/.opencode/opencode.json (installed)...")
    total += fix_config(OPCODE_INSTALLED, spec)

    print(f"\n✅ Applied {total} change(s) total.")
    print("   Backups saved with .bak.audit suffix.")
    return 0


def generate_matrix(config_path: Path) -> int:
    """Regenerate MODEL_ASSIGNMENT_MATRIX.md from an opencode config file.

    Reads agent model assignments from config and writes a new matrix spec.
    Returns number of agents written.
    """
    agents = extract_config_agents(config_path)

    lines = []
    lines.append("# OpenCode Agent + Skill Model Assignment Matrix")
    lines.append("")
    lines.append(f"> **Version**: {agents.__len__()}.0 (Auto-Generated)")
    lines.append(f"> **Date**: {__import__('datetime').date.today().isoformat()}")
    lines.append("> **Status**: Auto-Generated from opencode.jsonc")
    lines.append("> **Source**: `opencode.jsonc` (single source of truth)")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Model Tier Hierarchy")
    lines.append("")
    lines.append("| Tier | Model ID | Display Name | Strength | Token Budget | Use Case |")
    lines.append("|------|----------|--------------|----------|-------------|----------|")

    # Collect unique models
    model_agents: dict[str, list[str]] = {}
    for agent, model in agents.items():
        model_agents.setdefault(model, []).append(agent)

    # Build tier rows from unique models
    seen_tiers = set()
    for model, agent_list in sorted(model_agents.items()):
        # Find tier from metadata
        tier = "Other"
        budget = "—"
        for a in agent_list:
            if a in AGENT_METADATA:
                tier = AGENT_METADATA[a][1]
                break
        if tier in TIER_DESCRIPTIONS:
            budget = TIER_DESCRIPTIONS[tier][1]

        display_name = model.split("/")[-1].replace("-", " ").title()
        strength = TIER_DESCRIPTIONS.get(tier, ("—",))[0]
        use_cases = ", ".join(f"`{a}`" for a in sorted(agent_list)[:3])
        if len(agent_list) > 3:
            use_cases += f" (+{len(agent_list) - 3} more)"

        tier_key = (tier, model)
        if tier_key not in seen_tiers:
            seen_tiers.add(tier_key)
            lines.append(f"| **{tier}** | `{model}` | {display_name} | {strength} | {budget} | {use_cases} |")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"## Agent → Model Mapping ({len(agents)} Agents)")
    lines.append("")
    lines.append("| Agent | Mode | Model | Tier | Rationale |")
    lines.append("|-------|------|-------|------|-----------|")

    for agent, model in sorted(agents.items()):
        meta = AGENT_METADATA.get(agent, ("subagent", "—", "—"))
        mode, tier, rationale = meta
        lines.append(f"| `{agent}` | {mode} | `{model}` | {tier} | {rationale} |")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Source")
    lines.append("")
    lines.append("This file is auto-generated from `opencode.jsonc`.")
    lines.append("To change agent model assignments, edit `opencode.jsonc` and run:")
    lines.append("```")
    lines.append("python3 scripts/audit_agent_models.py --generate-matrix")
    lines.append("```")
    lines.append("")

    # Write
    MATRIX_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"📝 Regenerated {MATRIX_MD}")
    print(f"   {len(agents)} agents written from {config_path}")
    return len(agents)


def audit() -> int:
    """Run the audit against all config sources. Returns 0 on success."""
    try:
        spec = extract_spec_agents(MATRIX_MD)
    except Exception as e:
        print(f"❌ Failed to parse MODEL_ASSIGNMENT_MATRIX.md: {e}", file=sys.stderr)
        return 1

    all_issues = {}

    repo_issues = audit_config(OPENCODE_JSONC, spec, "opencode.jsonc (repo)")
    if repo_issues and not repo_issues[0].startswith("SKIP"):
        all_issues["opencode.jsonc (repo)"] = repo_issues

    installed_issues = audit_config(OPCODE_INSTALLED, spec, "~/.opencode/opencode.json (installed)")
    if installed_issues and not installed_issues[0].startswith("SKIP"):
        all_issues["~/.opencode/opencode.json (installed)"] = installed_issues

    total = sum(len(v) for v in all_issues.values())

    if total > 0:
        print(f"🔴 AGENT MODEL AUDIT FAILED — {total} issue(s) across {len(all_issues)} config(s)\n")
        print(f"   Spec: {MATRIX_MD}\n")
        for source, issues in all_issues.items():
            print(f"   [{source}]")
            for issue in issues:
                print(f"   {issue}")
            print()
        print("   Run with --fix to auto-apply corrections.")
        return 1
    else:
        print(f"🟢 AGENT MODEL AUDIT PASSED — {len(spec)} agents in sync")
        print(f"   Spec: {MATRIX_MD}")
        print(f"   Checked: opencode.jsonc (repo) + ~/.opencode/opencode.json (installed)")
        return 0


def main() -> int:
    args = sys.argv[1:]

    if "--generate-matrix" in args:
        try:
            count = generate_matrix(OPENCODE_JSONC)
            if count == 0:
                return 1
        except Exception as e:
            print(f"❌ Failed to generate matrix: {e}", file=sys.stderr)
            return 1

    if "--fix" in args:
        try:
            spec = extract_spec_agents(MATRIX_MD)
        except Exception as e:
            print(f"❌ Failed to parse MODEL_ASSIGNMENT_MATRIX.md: {e}", file=sys.stderr)
            return 1
        fix(spec)

    # If no flags, run audit
    if not args:
        return audit()

    # If --generate-matrix was the only flag and succeeded, we're done
    if args == ["--generate-matrix"]:
        return 0

    # If --fix was used, also run audit to verify
    if "--fix" in args:
        return audit()

    return 0


if __name__ == "__main__":
    sys.exit(main())
