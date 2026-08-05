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
echo "   Pre-commit hook will audit agent model assignments."
echo ""
echo "   Run 'python3 scripts/audit_agent_models.py' to check manually."
echo "   Run 'python3 scripts/audit_agent_models.py --fix' to auto-fix drift."
echo "   Run 'python3 scripts/audit_agent_models.py --generate-matrix' to regenerate spec."
