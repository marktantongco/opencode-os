#!/usr/bin/env python3
"""
Audit doctrine-scope docs for v5-era patterns (v8.0 compliance check).

Scope (files that must speak v8.0):
  - skills/**/*.md        (SKILL.md files plus docs like platform-guides)
  - agents/*.md
  - profiles/*            (text files only)

Files are SKIPPED when:
  - They carry a frozen-lineage marker ("FROZEN v<X>") — e.g. the v4 / v5.1
    profiles that are intentionally preserved as historical variants.
  - They are binary (e.g. profiles/system_master_v4.md is a .docx despite
    its .md extension).

Flags v5-era closing-structure markers:
  - ⚡⚡ (double-bolt, v5 closing marker)
  - "🔗 Hidden Assumption" footer (folded into Reasoning in v8.0)
  - Unconditional "✨ 3 Suggestions" (v8.0: design/architecture only, skipped on pure code)
  - "Zero fluff" DNA phrasing (v8.0: COMPILED CODE)
  - "RESPONSE FRAMEWORK" section title (v8.0: Output Schema / Compiled Execution)

The doctrine source itself (AGENTS.md, README.md) is intentionally NOT scanned —
it is the authority that documents the v8.0 schema (including the conditional
"✨ 3 Suggestions" element), not a consumer of it.

Usage:
  python3 scripts/audit_doctrine_v8.py              # audit and print findings
  python3 scripts/audit_doctrine_v8.py --check      # silent on pass (for CI / pre-commit)

Exit code 0 = all compliant.
Exit code 1 = v5-era patterns found.
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Directories whose docs must speak v8.0.
SCOPE_DIRS = ["skills", "agents", "profiles"]

# (label, regex) — regex matched per line.
# Patterns target the exact v5-era CLOSING STRUCTURE markers, not generic words
# (e.g. "hidden assumptions" as a reasoning technique is fine).
V5_PATTERNS = [
    ("v5 closing marker (⚡⚡)", re.compile(r"⚡⚡")),
    ("v5 footer (🔗 Hidden Assumption)", re.compile(r"🔗 Hidden Assumption")),
    ("v5 unconditional suggestions (✨ 3 Suggestions)", re.compile(r"✨ 3 Suggestions")),
    ("v5 DNA phrasing (Zero fluff)", re.compile(r"Zero fluff")),
    ("v5 section title (RESPONSE FRAMEWORK)", re.compile(r"RESPONSE FRAMEWORK")),
]

# Frozen/archived lineage marker: files carrying this are preserved historical
# variants (v4 / v5.1 profiles) and are exempt from the compliance check.
FROZEN_MARKER = re.compile(r"FROZEN v\d")


def iter_scope_files() -> list[Path]:
    """All in-scope files, sorted. skills/ is scanned recursively (all markdown);
    agents/ and profiles/ are flat, so every regular file is in scope."""
    files: list[Path] = []
    for dirname in SCOPE_DIRS:
        base = ROOT / dirname
        if not base.is_dir():
            continue
        if dirname == "skills":
            files.extend(sorted(base.rglob("*.md")))
        else:
            files.extend(sorted(p for p in base.iterdir() if p.is_file()))
    return files


def is_frozen(path: Path) -> bool:
    """True for preserved lineage variants (v4 / v5.1 profiles)."""
    try:
        head = path.read_text(encoding="utf-8", errors="replace")[:4000]
    except OSError:
        return False
    return bool(FROZEN_MARKER.search(head))


def is_binary(path: Path) -> bool:
    """True for non-text files (e.g. .docx files with a .md extension)."""
    try:
        with path.open("rb") as fh:
            return b"\x00" in fh.read(4096)
    except OSError:
        return True


def find_v5_files() -> tuple[list[tuple[Path, list[str]]], list[Path]]:
    """Return ([(file, [finding, ...]), ...], binary_skipped) for in-scope files."""
    findings: list[tuple[Path, list[str]]] = []
    binary_skipped: list[Path] = []
    for path in iter_scope_files():
        if is_frozen(path):
            continue
        if is_binary(path):
            binary_skipped.append(path)
            continue
        file_findings: list[str] = []
        try:
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError as exc:
            print(f"⚠️  Cannot read {path}: {exc}", file=sys.stderr)
            continue
        for lineno, line in enumerate(lines, start=1):
            for label, pattern in V5_PATTERNS:
                if pattern.search(line):
                    file_findings.append(f"  L{lineno}: {label} — {line.strip()[:100]}")
        if file_findings:
            findings.append((path, file_findings))
    return findings, binary_skipped


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check skills/, agents/ and profiles/ for v5-era doctrine patterns"
    )
    parser.add_argument("--check", action="store_true",
                        help="Silent on pass (exit 0); print findings and exit 1 on violations")
    args = parser.parse_args()

    findings, binary_skipped = find_v5_files()

    if binary_skipped and not args.check:
        for path in binary_skipped:
            print(f"ℹ️  Skipped (binary, not text-scannable): {path.relative_to(ROOT)}")

    if not findings:
        if not args.check:
            print("✅ All doctrine-scope files (skills/ agents/ profiles/) are v8.0 compliant.")
        return 0

    total = sum(len(f) for _, f in findings)
    print(f"❌ {len(findings)} file(s) contain v8.0 doctrine violations ({total} finding(s)):\n")
    for path, file_findings in findings:
        print(f"{path.relative_to(ROOT)}")
        print("\n".join(file_findings))
        print()

    print("Fix: update closing patterns to the v8.0 schema — ⚡ Next Step; ✨ suggestions")
    print("     design/architecture only (skip on pure code); assumptions folded into")
    print("     Reasoning. See AGENTS.md Part I — Output Schema (Compiled Execution).")
    return 1


if __name__ == "__main__":
    sys.exit(main())
