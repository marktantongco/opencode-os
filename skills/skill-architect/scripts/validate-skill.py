#!/usrusr/bin/env python3
"""
Skill Validator — Validates Agent Skills against the open standard.

Usage:
    python validate-skill.py ./my-skill/

Checks:
    - SKILL.md exists and has valid YAML frontmatter
    - Required fields (name, description) are present
    - Description length is trigger-optimal (50-800 chars)
    - SKILL.md body is under 500 lines
    - Directory structure follows convention
    - No forbidden content (malware patterns, etc.)
    - Self-consistency (examples match instructions)

Exit codes:
    0 = validation passed
    1 = validation failed
"""

import os
import sys
import re
import yaml

def validate_skill(skill_path):
    errors = []
    warnings = []

    skill_path = os.path.abspath(skill_path)
    if not os.path.isdir(skill_path):
        errors.append(f"Path is not a directory: {skill_path}")
        return errors, warnings

    # 1. Check SKILL.md exists
    skill_md = os.path.join(skill_path, "SKILL.md")
    if not os.path.exists(skill_md):
        errors.append("SKILL.md is missing — this is required")
        return errors, warnings

    with open(skill_md, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split("
")

    # 2. Check YAML frontmatter
    if not content.startswith("---"):
        errors.append("SKILL.md must start with YAML frontmatter (---)")
        return errors, warnings

    try:
        parts = content.split("---", 2)
        if len(parts) < 3:
            errors.append("Invalid frontmatter format — missing closing ---")
            return errors, warnings

        frontmatter = yaml.safe_load(parts[1])
        body = parts[2].strip()

    except yaml.YAMLError as e:
        errors.append(f"Invalid YAML frontmatter: {e}")
        return errors, warnings

    # 3. Check required fields
    if not frontmatter:
        errors.append("Frontmatter is empty")
        return errors, warnings

    name = frontmatter.get("name")
    description = frontmatter.get("description")

    if not name:
        errors.append("Missing required field: name")
    elif not re.match(r"^[a-z0-9-]+$", name):
        errors.append(f"Invalid name '{name}' — must be kebab-case (lowercase, hyphens, numbers)")

    if not description:
        errors.append("Missing required field: description")
    else:
        desc_text = str(description).strip()
        if len(desc_text) < 50:
            errors.append(f"Description too short ({len(desc_text)} chars) — will under-trigger. Minimum 50 chars.")
        elif len(desc_text) < 100:
            warnings.append(f"Description is short ({len(desc_text)} chars) — consider expanding for better triggering")
        if len(desc_text) > 800:
            errors.append(f"Description too long ({len(desc_text)} chars) — may confuse trigger logic. Maximum 800 chars.")

        # Check for pushy clauses
        pushy_keywords = ["always use", "make sure to use", "do not", "without this skill", "trigger"]
        if not any(kw in desc_text.lower() for kw in pushy_keywords):
            warnings.append("Description lacks pushy/urgent clauses — may under-trigger. Consider adding 'Always use this skill for...'")

    # 4. Check body length
    body_lines = [l for l in body.split("
") if l.strip()]
    if len(body_lines) > 500:
        errors.append(f"SKILL.md body is {len(body_lines)} lines — exceeds 500-line recommendation. Move content to references/.")
    elif len(body_lines) > 400:
        warnings.append(f"SKILL.md body is {len(body_lines)} lines — approaching 500-line limit. Consider moving content to references/.")

    # 5. Check directory structure
    for subdir in ["scripts", "references", "assets"]:
        subdir_path = os.path.join(skill_path, subdir)
        if os.path.exists(subdir_path) and not os.path.isdir(subdir_path):
            errors.append(f"{subdir}/ exists but is not a directory")

    # 6. Check for forbidden patterns
    forbidden_patterns = [
        (r"rm\s+-rf\s+/", "Dangerous rm -rf / pattern detected"),
        (r"eval\s*\(", "Dangerous eval() pattern detected"),
        (r"os\.system\s*\(", "Dangerous os.system() pattern detected"),
        (r"subprocess\.call\s*\(", "Dangerous subprocess pattern detected"),
        (r"__import__\s*\(", "Dangerous dynamic import pattern detected"),
    ]

    for pattern, msg in forbidden_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            errors.append(f"Security concern: {msg}")

    # 7. Check for self-consistency issues
    if "## Examples" in body and "### Example" not in body:
        warnings.append("Examples section exists but no labeled examples (### Example 1:) — may be hard to follow")

    if "## Anti-Patterns" in body and "❌" not in body and "BAD" not in body:
        warnings.append("Anti-patterns section exists but no visual bad/good markers — consider adding ❌/✅ indicators")

    # 8. Check for template placeholders
    template_placeholders = re.findall(r"\{[A-Za-z-_]+\}", body)
    if template_placeholders:
        warnings.append(f"Template placeholders found in body: {set(template_placeholders)} — did you forget to customize the template?")

    return errors, warnings

def main():
    if len(sys.argv) < 2:
        print("Usage: python validate-skill.py <skill-directory>")
        sys.exit(1)

    skill_path = sys.argv[1]
    errors, warnings = validate_skill(skill_path)

    skill_name = os.path.basename(os.path.normpath(skill_path))

    print(f"
{'='*60}")
    print(f"Skill Validation: {skill_name}")
    print(f"{'='*60}")

    if warnings:
        print(f"
⚠️  WARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"   - {w}")

    if errors:
        print(f"
❌ ERRORS ({len(errors)}):")
        for e in errors:
            print(f"   - {e}")
        print(f"
{'='*60}")
        print("VALIDATION FAILED")
        print(f"{'='*60}")
        sys.exit(1)

    print(f"
✅ All checks passed")
    if warnings:
        print(f"   ({len(warnings)} warning(s) — non-blocking)")
    print(f"
{'='*60}")
    print("VALIDATION PASSED")
    print(f"{'='*60}")
    sys.exit(0)

if __name__ == "__main__":
    main()
