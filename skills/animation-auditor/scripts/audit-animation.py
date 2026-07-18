#!/usr/bin/env python3
"""
Animation Auditor — Scans code for animation anti-patterns, bundle violations,
accessibility issues, and framework integration errors.

Usage:
    python audit-animation.py /path/to/project/

Checks:
    - Motion/GSAP import strategy vs. bundle budget
    - Tailwind transition-* conflicts with Motion
    - Missing "use client" for Motion in Next.js App Router
    - Missing AnimatePresence for exit animations
    - Missing prefers-reduced-motion checks
    - GSAP plugin registration
    - Raw useEffect instead of useGSAP
    - CSS transition + Motion prop conflicts
"""

import os, re, sys, json

BUDGET_KB = 5  # Design OS constraint

def scan_file(path, content):
    issues = []

    # 1. Check import strategy vs. budget
    if 'from "motion/react"' in content or "from 'motion/react'" in content:
        if 'import { motion' in content and 'LazyMotion' not in content:
            if 'useAnimate' not in content:
                issues.append({
                    "severity": "warning",
                    "line": find_line(content, "import { motion"),
                    "message": "Full motion import (34KB) detected. Consider LazyMotion + m (4.6KB) or useAnimate mini (2.3KB) if only simple animations needed.",
                    "rule": "bundle-optimization"
                })

    # 2. Tailwind transition conflict
    if 'motion.' in content or '<motion' in content:
        tw_transition = re.search(r'className=["'][^"']*transition-(all|colors|transform|opacity|duration)', content)
        if tw_transition:
            issues.append({
                "severity": "error",
                "line": find_line(content, tw_transition.group(0)),
                "message": "Tailwind transition-* class conflicts with Motion animation. Remove Tailwind transitions — let Motion handle animation.",
                "rule": "tailwind-conflict"
            })

    # 3. Missing "use client" for Next.js App Router
    if ('motion' in content or 'AnimatePresence' in content) and 'use client' not in content:
        # Check if this is likely App Router (has async components or server patterns)
        if 'async function' not in content and 'export default' in content:
            issues.append({
                "severity": "error",
                "line": 1,
                "message": "Motion components require 'use client' directive in Next.js App Router. Add "use client" at the top of the file.",
                "rule": "nextjs-client-directive"
            })

    # 4. Missing AnimatePresence for conditional rendering
    if 'exit=' in content and 'AnimatePresence' not in content:
        issues.append({
            "severity": "error",
            "line": find_line(content, "exit="),
            "message": "exit prop used without AnimatePresence wrapper. Exit animations won't work — wrap in <AnimatePresence>.",
            "rule": "missing-animate-presence"
        })

    # 5. Missing prefers-reduced-motion
    if ('whileHover' in content or 'whileTap' in content or 'animate=' in content) and 'useReducedMotion' not in content:
        issues.append({
            "severity": "warning",
            "line": 1,
            "message": "No prefers-reduced-motion check found. Add useReducedMotion() hook for accessibility compliance.",
            "rule": "a11y-reduced-motion"
        })

    # 6. GSAP plugin registration
    if 'gsap' in content and 'registerPlugin' not in content:
        plugins = ['ScrollTrigger', 'Flip', 'Draggable', 'MorphSVG', 'SplitText', 'DrawSVG']
        used = [p for p in plugins if p in content]
        if used:
            issues.append({
                "severity": "error",
                "line": find_line(content, used[0]),
                "message": f"GSAP plugin(s) {used} used but not registered. Add gsap.registerPlugin({', '.join(used)}).",
                "rule": "gsap-plugin-registration"
            })

    # 7. Raw useEffect with GSAP
    if 'gsap.to(' in content or 'gsap.from(' in content:
        if 'useGSAP' not in content and 'useEffect' in content:
            issues.append({
                "severity": "warning",
                "line": find_line(content, "useEffect"),
                "message": "Raw useEffect + GSAP detected. Use useGSAP() from @gsap/react for automatic cleanup and SSR safety.",
                "rule": "gsap-react-integration"
            })

    # 8. CSS animation + Motion conflict
    css_anim = re.search(r'@keyframes|animation:\s*\w+', content)
    if css_anim and ('motion.' in content or '<motion' in content):
        issues.append({
            "severity": "warning",
            "line": find_line(content, css_anim.group(0)),
            "message": "CSS animations detected alongside Motion. Choose one system — mixing causes transform conflicts.",
            "rule": "css-motion-conflict"
        })

    return issues

def find_line(content, pattern):
    lines = content.split('
')
    for i, line in enumerate(lines, 1):
        if pattern in line:
            return i
    return 0

def audit_project(project_path):
    all_issues = []
    files_scanned = 0

    for root, dirs, files in os.walk(project_path):
        # Skip node_modules
        dirs[:] = [d for d in dirs if d not in ['node_modules', '.git', 'dist', 'build']]

        for file in files:
            if file.endswith(('.tsx', '.ts', '.jsx', '.js')):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()

                    issues = scan_file(filepath, content)
                    if issues:
                        all_issues.append({
                            "file": os.path.relpath(filepath, project_path),
                            "issues": issues
                        })
                    files_scanned += 1
                except Exception as e:
                    pass

    return all_issues, files_scanned

def main():
    if len(sys.argv) < 2:
        print("Usage: python audit-animation.py /path/to/project/")
        sys.exit(1)

    project_path = sys.argv[1]
    issues, files_scanned = audit_project(project_path)

    errors = sum(1 for f in issues for i in f["issues"] if i["severity"] == "error")
    warnings = sum(1 for f in issues for i in f["issues"] if i["severity"] == "warning")

    report = {
        "summary": {
            "files_scanned": files_scanned,
            "files_with_issues": len(issues),
            "total_errors": errors,
            "total_warnings": warnings,
            "budget_kb": BUDGET_KB
        },
        "details": issues
    }

    print(json.dumps(report, indent=2))

    if errors > 0:
        print(f"
❌ {errors} error(s) found — fix before commit")
        sys.exit(1)
    elif warnings > 0:
        print(f"
⚠️  {warnings} warning(s) — review recommended")
        sys.exit(0)
    else:
        print("
✅ All checks passed")
        sys.exit(0)

if __name__ == "__main__":
    main()
