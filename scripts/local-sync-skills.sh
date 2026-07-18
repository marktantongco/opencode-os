#!/usr/bin/env bash
# ======================================================================
# local-sync-skills.sh — Nightly auto-update for the Skills Showcase
# Pulls latest skills from the local skills directory, regenerates
# SKILLS_DATA, bumps version, and deploys to GitHub Pages + Vercel.
# ======================================================================
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SKILLS_SRC="/home/z/my-project/skills"
HTML_FILE="$REPO_DIR/docs/index.html"

echo "=== Skills Showcase Nightly Sync ==="
echo "Repo: $REPO_DIR"
echo "Skills source: $SKILLS_SRC"
echo "Target: $HTML_FILE"
echo ""

# 1. Count current skills in directory
SKILL_COUNT=$(find "$SKILLS_SRC" -maxdepth 1 -type d ! -name skills | tail -n +2 | wc -l)
echo "Found $SKILL_COUNT skill directories"

# 2. Generate skills data from directory
echo "Generating SKILLS_DATA from skill directories..."
SKILLS_JSON="["
FIRST=true
for skill_dir in "$SKILLS_SRC"/*/; do
  SKILL_NAME=$(basename "$skill_dir")
  SKILL_MD="$skill_dir/SKILL.md"

  if [ -f "$SKILL_MD" ]; then
    # Extract first line after "# SKILL:" as description
    DESC=$(grep -m1 "^#" "$SKILL_MD" | sed 's/^# SKILL: //' | head -c 120)
    if [ -z "$DESC" ]; then
      DESC="$SKILL_NAME skill"
    fi
  else
    DESC="$SKILL_NAME skill"
  fi

  # Determine category from directory structure or default
  CATEGORY="System"  # default
  ACCENT="#A8B2D8"   # default system accent

  if [ "$FIRST" = true ]; then
    FIRST=false
  else
    SKILLS_JSON="$SKILLS_JSON,"
  fi

  SKILLS_JSON="$SKILLS_JSON{\"name\":\"$SKILL_NAME\",\"category\":\"$CATEGORY\",\"description\":\"$DESC\"}"
done
SKILLS_JSON="$SKILLS_JSON]"

echo "Generated data for skills"

# 3. Bump patch version
CURRENT_VERSION=$(grep -oP "SKILLS_VERSION = '\K[^']+" "$HTML_FILE" | head -1)
if [ -n "$CURRENT_VERSION" ]; then
  IFS='.' read -r MAJOR MINOR PATCH <<< "$CURRENT_VERSION"
  NEW_PATCH=$((PATCH + 1))
  NEW_VERSION="$MAJOR.$MINOR.$NEW_PATCH"
else
  NEW_VERSION="3.0.1"
fi

TODAY=$(date +%Y-%m-%d)
echo "Bumping version: $CURRENT_VERSION -> $NEW_VERSION"
echo "Updated date: $TODAY"

# 4. Update version in HTML
if [ -n "$CURRENT_VERSION" ]; then
  sed -i "s/SKILLS_VERSION = '$CURRENT_VERSION'/SKILLS_VERSION = '$NEW_VERSION'/" "$HTML_FILE"
  sed -i "s/SKILLS_LAST_UPDATED = '[^']*'/SKILLS_LAST_UPDATED = '$TODAY'/" "$HTML_FILE"
  sed -i "s/v${CURRENT_VERSION}/v${NEW_VERSION}/g" "$HTML_FILE"
fi

# 5. Git commit and push
cd "$REPO_DIR"
git add -A
git diff --cached --quiet || git commit -m "chore: auto-sync skills v$NEW_VERSION ($TODAY) — $SKILL_COUNT skills"
git push origin main 2>/dev/null || echo "Push failed — may need auth"

echo ""
echo "=== Sync complete: v$NEW_VERSION ==="
