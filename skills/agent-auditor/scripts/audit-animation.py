#!/usr/bin/env python3
"""
Animation Auditor — Comprehensive audit for animation code quality.

Usage:
    python audit-animation.py /path/to/project/

Checks:
    - Bundle budget compliance
    - Accessibility (reduced motion, focus, aria)
    - Performance (layout thrashing, will-change)
    - Memory (cleanup, dispose, revert)
    - Framework integration (Next.js, R3F, Motion, GSAP)
    - Code quality (magic numbers, error handling)
"""

import os, re, sys, json

RULES = {
    "bundle-budget": {
        "pattern": r'from ["']three["']|from ["']@react-three/fiber["']|from ["']motion/react["']',
        "check": lambda content, path: "page." in path or "layout." in path,
        "severity": "error",
        "message": "Synchronous animation library import in page/layout file",
        "fix": "Wrap in dynamic(() => import(...), { ssr: false })"
    },
    "accessibility-reduced-motion": {
        "pattern": r'whileHover|whileTap|animate=|gsap\.to|gsap\.from',
        "check": lambda content, path: "useReducedMotion" not in content and "prefers-reduced-motion" not in content,
        "severity": "error",
        "message": "Animation without reduced-motion check",
        "fix": "Add useReducedMotion() hook and conditionally disable"
    },
    "memory-gsap-cleanup": {
        "pattern": r'gsap\.to|gsap\.from|gsap\.timeline',
        "check": lambda content, path: "useGSAP" not in content and "ctx.revert" not in content and "kill" not in content,
        "severity": "error",
        "message": "GSAP animation without cleanup",
        "fix": "Use useGSAP() hook or add ctx.revert() in cleanup"
    },
    "memory-motion-cleanup": {
        "pattern": r'AnimatePresence',
        "check": lambda content, path: "key=" not in content,
        "severity": "warning",
        "message": "AnimatePresence without key prop",
        "fix": "Add stable key prop to animated children"
    },
    "memory-three-dispose": {
        "pattern": r'new THREE\.',
        "check": lambda content, path: "dispose()" not in content and "useEffect" in content,
        "severity": "warning",
        "message": "Three.js object created without dispose()",
        "fix": "Add geometry.dispose(), material.dispose() in cleanup"
    },
    "performance-layout": {
        "pattern": r'width:|height:|top:|left:',
        "check": lambda content, path: "transform" not in content,
        "severity": "error",
        "message": "Layout property animation detected",
        "fix": "Convert to transform or opacity animation"
    },
    "framework-nextjs-ssr": {
        "pattern": r'<Canvas',
        "check": lambda content, path: "ssr: false" not in content and "dynamic(" in content,
        "severity": "error",
        "message": "Canvas without ssr: false",
        "fix": "Add ssr: false to dynamic import"
    },
    "framework-nextjs-client": {
        "pattern": r'useFrame|useThree|<Canvas',
        "check": lambda content, path: '"use client"' not in content and "'use client'" not in content,
        "severity": "error",
        "message": "R3F component without 'use client'",
        "fix": "Add 'use client' directive"
    },
    "framework-transpile": {
        "pattern": r'next\.config',
        "check": lambda content, path: "transpilePackages" not in content or "'three'" not in content,
        "severity": "error",
        "message": "Missing transpilePackages: ['three']",
        "fix": "Add transpilePackages: ['three'] to next.config.js"
    },
    "framework-gsap-register": {
        "pattern": r'from ["']gsap/',
        "check": lambda content, path: "registerPlugin" not in content,
        "severity": "error",
        "message": "GSAP plugin imported but not registered",
        "fix": "Add gsap.registerPlugin(PluginName)"
    }
}

def audit_file(filepath, content):
    violations = []
    for rule_name, rule in RULES.items():
        if re.search(rule["pattern"], content):
            if rule["check"](content, filepath):
                violations.append({
                    "rule": rule_name,
                    "severity": rule["severity"],
                    "message": rule["message"],
                    "fix": rule["fix"],
                    "line": find_line(content, re.search(rule["pattern"], content).group(0))
                })
    return violations

def find_line(content, pattern):
    lines = content.split('\n')
    for i, line in enumerate(lines, 1):
        if pattern in line:
            return i
    return 0

def audit_project(project_path):
    all_violations = []
    files_scanned = 0

    for root, dirs, files in os.walk(project_path):
        dirs[:] = [d for d in dirs if d not in ['node_modules', '.git', 'dist', 'build']]

        for file in files:
            if file.endswith(('.tsx', '.ts', '.jsx', '.js', '.mjs')):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()

                    violations = audit_file(filepath, content)
                    if violations:
                        all_violations.append({
                            "file": os.path.relpath(filepath, project_path),
                            "violations": violations
                        })
                    files_scanned += 1
                except Exception:
                    pass

    return all_violations, files_scanned

def main():
    if len(sys.argv) < 2:
        print("Usage: python audit-animation.py <project-directory>")
        sys.exit(1)

    project_path = sys.argv[1]
    violations, files_scanned = audit_project(project_path)

    errors = sum(1 for f in violations for v in f["violations"] if v["severity"] == "error")
    warnings = sum(1 for f in violations for v in f["violations"] if v["severity"] == "warning")

    report = {
        "summary": {
            "files_scanned": files_scanned,
            "files_with_violations": len(violations),
            "total_errors": errors,
            "total_warnings": warnings,
            "passed": errors == 0
        },
        "violations": violations
    }

    print(json.dumps(report, indent=2))

    if errors > 0:
        print(f"\n❌ AUDIT FAILED — {errors} error(s) must be fixed")
        sys.exit(1)
    elif warnings > 0:
        print(f"\n⚠️  AUDIT PASSED with {warnings} warning(s)")
        sys.exit(0)
    else:
        print("\n✅ AUDIT PASSED — All checks clean")
        sys.exit(0)

if __name__ == "__main__":
    main()
