#!/usr/bin/env bash
# Restore agent model configuration from a previous git state.
#
# Usage:
#   bash scripts/restore_models.sh                    # show available versions
#   bash scripts/restore_models.sh <commit-sha>       # restore from specific commit
#   bash scripts/restore_models.sh v1.0.0             # restore from tag
#   bash scripts/restore_models.sh HEAD~3             # restore from 3 commits ago
#
# This restores the matrix from the given commit and applies it to both configs.
# Use when a model goes down or a bad config was merged.

set -euo pipefail

cd "$(git rev-parse --show-toplevel)"

if [ $# -eq 0 ]; then
    echo "Available versions (matrix changes):"
    echo ""
    git log --oneline --follow profiles/MODEL_ASSIGNMENT_MATRIX.md | head -20
    echo ""
    echo "Usage: bash scripts/restore_models.sh <commit-sha|tag>"
    exit 0
fi

REF="$1"

# Verify the ref exists
if ! git rev-parse --verify "$REF" > /dev/null 2>&1; then
    echo "❌ Invalid ref: $REF"
    exit 1
fi

# Check if matrix exists at that ref
if ! git show "$REF:profiles/MODEL_ASSIGNMENT_MATRIX.md" > /dev/null 2>&1; then
    echo "❌ No MODEL_ASSIGNMENT_MATRIX.md at $REF"
    exit 1
fi

echo "📋 Restoring agent models from: $(git log --oneline -1 "$REF")"
echo ""

# Show what will change
echo "Changes:"
git diff --stat "$REF" -- profiles/MODEL_ASSIGNMENT_MATRIX.md
echo ""

# Confirm
read -p "Apply this restore? (y/N) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Aborted."
    exit 0
fi

# Restore matrix from the ref
git show "$REF:profiles/MODEL_ASSIGNMENT_MATRIX.md" > profiles/MODEL_ASSIGNMENT_MATRIX.md
echo "✅ Restored profiles/MODEL_ASSIGNMENT_MATRIX.md from $REF"

# Apply matrix to configs
echo "🔧 Applying restored matrix to configs..."
python3 scripts/audit_agent_models.py --fix

echo ""
echo "✅ Done. Review changes with: git diff"
echo "   Commit with: git add -A && git commit -m 'fix: restore agent models from $REF'"
