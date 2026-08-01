#!/usr/bin/env python3
"""
opencode-os — Config Consistency Audit

Compares three sources of truth for opencode agent definitions:
  1. ~/.opencode/opencode.json   (active config loaded at runtime)
  2. opencode-os/opencode.jsonc  (source config, JSON with comments)
  3. opencode-os/agents/*.md     (agent definition files)

Only REAL agent files are audited: an .md file in agents/ is treated as an
agent definition ONLY if its YAML frontmatter contains a `mode:` field
(subagent|primary). Guide/documentation files (00_START_HERE, SKILL_*.md,
numbered playbooks, etc.) carry no `mode:` frontmatter and are skipped, so a
fully-synced tree reports 0 issues.

Exit codes:
  0  — everything in sync
  1  — one or more inconsistencies found
  2  — a required source file is missing

Usage:
  python3 scripts/audit-consistency.py
"""

import json
import os
import re
import sys
from pathlib import Path

# ─── Paths ──────────────────────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent.parent
ACTIVE_CONFIG = Path.home() / ".opencode" / "opencode.json"
SOURCE_CONFIG = PROJECT_ROOT / "opencode.jsonc"
AGENT_DIR = PROJECT_ROOT / "agents"

VALID_MODES = {"subagent", "primary"}


# ─── Loaders ────────────────────────────────────────────────────────────
def load_json(path: Path) -> dict:
    with open(path) as f:
        return json.load(f)


def load_jsonc(path: Path) -> dict:
    """Load a JSON-with-comments file, stripping // comments outside strings."""
    content = path.read_text()
    out_lines = []
    for line in content.split("\n"):
        res = ""
        in_str = False
        i = 0
        while i < len(line):
            ch = line[i]
            if ch == '"' and (i == 0 or line[i - 1] != "\\"):
                in_str = not in_str
            if ch == "/" and i + 1 < len(line) and line[i + 1] == "/" and not in_str:
                break
            res += ch
            i += 1
        out_lines.append(res)
    stripped = re.sub(r",\s*([}\]])", r"\1", "\n".join(out_lines))
    return json.loads(stripped)


def parse_frontmatter(content: str) -> dict:
    """Extract the --- delimited YAML frontmatter block as a dict of strings."""
    m = re.search(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not m:
        return {}
    front = m.group(1)
    fields = {}
    for line in front.split("\n"):
        kv = re.match(r"^([a-zA-Z_][a-zA-Z0-9_]*):\s*(.+)$", line)
        if kv:
            fields[kv.group(1)] = kv.group(2).strip()
    return fields


def load_agent_md_files(agent_dir: Path) -> dict:
    """Return {agent_name: {model, description}} for REAL agents only.

    A file is a real agent iff its frontmatter has a `mode:` value in
    VALID_MODES. Guide/docs files are skipped entirely.
    """
    agents = {}
    if not agent_dir.exists():
        return agents
    for fn in sorted(os.listdir(agent_dir)):
        if not fn.endswith(".md"):
            continue
        front = parse_frontmatter((agent_dir / fn).read_text())
        if front.get("mode") not in VALID_MODES:
            continue  # guide / documentation file — not an agent
        agents[fn[:-3]] = {
            "model": front.get("model"),
            "description": front.get("description"),
        }
    return agents


# ─── Audit ──────────────────────────────────────────────────────────────
def main() -> int:
    issues = 0

    for label, path in [
        ("active config", ACTIVE_CONFIG),
        ("source config", SOURCE_CONFIG),
    ]:
        if not path.exists():
            print(f"❌ MISSING {label}: {path}")
            return 2

    main = load_json(ACTIVE_CONFIG)
    src = load_jsonc(SOURCE_CONFIG)
    md_agents = load_agent_md_files(AGENT_DIR)

    main_agents = main.get("agent", {})
    src_agents = src.get("agent", {})

    print("════════════════════════════════════════════════════════")
    print("OpenCode CONFIG CONSISTENCY AUDIT")
    print("════════════════════════════════════════════════════════")

    if not md_agents and (main_agents or src_agents):
        issues += 1
        print("  ❌ agents/ directory contains zero agent definition files")

    # [1] Agent name coverage across all three sources
    print("\n[1] AGENT NAME COVERAGE")
    all_names = sorted(set(main_agents) | set(src_agents) | set(md_agents))
    for name in all_names:
        missing = [
            src
            for src, present in (
                ("opencode.json", name in main_agents),
                ("opencode.jsonc", name in src_agents),
                (".md", name in md_agents),
            )
            if not present
        ]
        if missing:
            issues += 1
            print(f"  ❌ {name}: MISSING from {missing}")
        else:
            print(f"  ✅ {name}")

    # Orphan .md files (agent frontmatter but no config entry)
    for name in sorted(set(md_agents) - set(main_agents) - set(src_agents)):
        issues += 1
        print(f"  ❌ {name}: has agent frontmatter but no config entry")

    # [2] Model assignments — all three sources must match
    print("\n[2] MODEL ASSIGNMENTS (json + jsonc + .md)")
    for name in sorted(main_agents):
        mm = main_agents.get(name, {}).get("model")
        sm = src_agents.get(name, {}).get("model")
        mdm = md_agents.get(name, {}).get("model")
        desc = md_agents.get(name, {}).get("description") or ""
        if mm and mm == sm == mdm:
            suffix = f" — {desc}" if desc else ""
            print(f"  ✅ {name}: {mm}{suffix}")
        else:
            issues += 1
            print(f"  ❌ {name}: json={mm} | jsonc={sm} | md={mdm}")

    # [3] Top-level settings
    print("\n[3] TOP-LEVEL SETTINGS")
    for key in ("model", "small_model", "default_agent"):
        mv, sv = main.get(key), src.get(key)
        if mv == sv:
            print(f"  ✅ {key}: {mv}")
        else:
            issues += 1
            print(f"  ❌ {key}: json={mv} | jsonc={sv}")

    # [4] Fallback chains
    print("\n[4] FALLBACK CHAINS")
    main_chains = main.get("experimental", {}).get("modelFallbackChain", {}).get("chains", [])
    src_chains = src.get("experimental", {}).get("modelFallbackChain", {}).get("chains", [])
    if main_chains == src_chains:
        print(f"  ✅ {len(main_chains)} chains identical")
        for c in main_chains:
            print(f"     {c}")
    else:
        issues += 1
        print(f"  ❌ main has {len(main_chains)}, jsonc has {len(src_chains)}")

    # [5] Distribution summary
    print("\n[5] DISTRIBUTION SUMMARY (from opencode.json)")
    dist = {}
    for k, v in main_agents.items():
        dist.setdefault(v.get("model", "?"), []).append(k)
    for m, a in sorted(dist.items()):
        print(f"  {m}: {len(a)} agents")

    print("\n════════════════════════════════════════════════════════")
    print(f"TOTAL ISSUES: {issues}")
    print("════════════════════════════════════════════════════════")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
