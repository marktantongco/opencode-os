#!/usr/bin/env bash
# Set up shared git hooks for this repo.
# Run this once after cloning:
#   bash scripts/setup-hooks.sh
#
# This configures git to use .githooks/ via core.hooksPath,
# so all contributors get the same pre-commit checks.

set -euo pipefail

cd "$(git rev-parse --show-toplevel 2>/dev/null || echo '.')"

# Configure git to use our shared hooks directory
git config core.hooksPath .githooks

echo "✅ Git hooks configured: core.hooksPath = .githooks/"
echo "   Pre-commit hook runs on staged changes:"
echo "   • agent model assignment audit (opencode.jsonc vs matrix)"
echo "   • v8.0 doctrine compliance (skills/ agents/ profiles/ docs/)"
echo "   • config drift check (opencode.jsonc vs models.yaml)"
echo ""
echo "   Requires Python deps: pip install json5 pyyaml"
echo "   Manual checks: make audit | make check-doctrine | make check-config"
echo "   Auto-fix agent drift: python3 scripts/audit_agent_models.py --fix"
