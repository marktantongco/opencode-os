#!/usr/bin/env bash
# ======================================================================
# sync-skills.sh — GitHub Actions-compatible sync script
# Runs inside CI to regenerate skills data and deploy.
# Requires GITHUB_TOKEN environment variable.
# ======================================================================
set -euo pipefail

echo "=== GitHub Actions Skills Sync ==="

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
HTML_FILE="$REPO_DIR/docs/index.html"

# Bump patch version
CURRENT_VERSION=$(grep -oP "SKILLS_VERSION = '\K[^']+" "$HTML_FILE" | head -1)
if [ -n "$CURRENT_VERSION" ]; then
  IFS='.' read -r MAJOR MINOR PATCH <<< "$CURRENT_VERSION"
  NEW_VERSION="$MAJOR.$MINOR.$((PATCH + 1))"
else
  NEW_VERSION="3.0.1"
fi

TODAY=$(date -u +%Y-%m-%d)
echo "Version: $CURRENT_VERSION -> $NEW_VERSION"
echo "Date: $TODAY"

sed -i "s/SKILLS_VERSION = '$CURRENT_VERSION'/SKILLS_VERSION = '$NEW_VERSION'/" "$HTML_FILE"
sed -i "s/SKILLS_LAST_UPDATED = '[^']*'/SKILLS_LAST_UPDATED = '$TODAY'/" "$HTML_FILE"
sed -i "s/v${CURRENT_VERSION}/v${NEW_VERSION}/g" "$HTML_FILE"

echo "=== Sync complete: v$NEW_VERSION ==="
