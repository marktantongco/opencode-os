---
name: design-nested
version: 1.0.0
category: Design & UI
author: marktantongco
description: |
  Meta-design intelligence layer — a nested skill that orchestrates all design-oriented
  skills into a unified optimization tree. Acts as the single entry-point for any design
  request, routing to the optimal sub-skill based on context, complexity, and output target.
  Integrates the Supanova premium aesthetic suite from uxjoseph (skills.sh/uxjoseph) alongside
  existing design, animation, and visual composition skills.
invoke: |
  Use when the user requests ANY design work — UI design, landing pages, component styling,
  animation choreography, visual systems, presentation design, or aesthetic optimization.
  This skill analyses the request, selects the best sub-skill chain, and orchestrates
  execution across the design skill tree.
tags:
  - design
  - meta-skill
  - nested
  - orchestration
  - optimization-tree
  - supanova
  - uxjoseph
  - routing
  - aesthetic
  - ui
  - ux
  - visual-system
  - landing-page
  - presentation
accent: "#4338ca"
---

# Design Nested Skill

## Overview

The **Design Nested Skill** is a meta-orchestration layer that unifies all design-oriented
capabilities into a single, searchable optimization tree. Rather than requiring users to know
which specific design skill to invoke, this nested skill acts as an intelligent router that
analyzes the design request, maps it to the optimal skill chain, and coordinates execution.

## Design Skill Tree

The optimization tree organizes design skills into four tiers based on function and complexity:

```
design-nested (ROOT)
├── TIER 1: DESIGN INTELLIGENCE
│   ├── ui-ux-pro-max-v7          — Core design system (tokens, palettes, fonts, components)
│   ├── supanova-design-engine     — Tunable aesthetic engine (variance, motion, density)
│   └── anthropic-frontend-design  — AI-native interface aesthetics
│
├── TIER 2: OUTPUT GENERATION
│   ├── supanova-premium-aesthetic — Premium Korean-agency landing pages ($150k+ feel)
│   ├── frontend-design            — shadcn/ui + Tailwind + React components
│   ├── supanova-full-output       — Production-critical full output enforcement
│   ├── landing-page-generator     — High-conversion landing pages (Korean-optimized)
│   └── design-skill               — Professional presentation design system
│
├── TIER 3: REFINEMENT & AUDIT
│   ├── supanova-redesign-engine   — Scan → Diagnose → Fix existing designs
│   ├── animation-auditor          — Quality gates for animation code
│   ├── vercel-web-design-guidelines — Accessibility-first UX rules
│   ├── web-design-guidelines      — General web design standards
│   └── photography-ai             — AI-enhanced photography composition
│
├── TIER 4: MOTION & ANIMATION
│   ├── animation-orchestrator     — Routes all animation requests
│   ├── animation-hybrid-architect — Motion + GSAP boundary management
│   ├── gsap-animation-engineer    — GSAP v3.13+ cinematic animations
│   ├── motion-animation-engineer  — Motion v12 declarative UI animations
│   ├── gsap-animations            — GSAP animation patterns & presets
│   ├── gsap-animator              — Complex GSAP timeline animations
│   └── motion-animator            — React UI animations (Motion/Framer)
│
└── TIER 5: CONTENT & VISUAL
    ├── output-formatter           — Visual output formatting & styling
    ├── nanobanana-visual          — Instagram card-news & YouTube thumbnails
    ├── shorts-video-maker         — Video highlight extraction for Shorts
    └── pptx-skill                 — HTML slides → PowerPoint conversion
```

## Routing Logic

When a design request is received, the nested skill follows this decision tree:

1. **Is it a NEW design?** → Route to Tier 1 (pick design system), then Tier 2 (generate output)
2. **Is it a REDESIGN?** → Route to Tier 3 (audit current), then Tier 2 (regenerate)
3. **Is it ANIMATION only?** → Route to Tier 4 (orchestrator picks engine)
4. **Is it VISUAL CONTENT?** → Route to Tier 5 (formatter picks medium)
5. **Is it a LANDING PAGE?** → Route to supanova-premium-aesthetic (default) or landing-page-generator (Korean)
6. **Is it a PRESENTATION?** → Route to design-skill → pptx-skill pipeline

## Supanova Integration (uxjoseph)

The Supanova Design Suite from [skills.sh/uxjoseph](https://www.skills.sh/uxjoseph) provides
premium aesthetic generation capabilities:

- **supanova-design-engine** — Active baseline configuration with tunable parameters:
  - `DESIGN_VARIANCE: 8` — Layout uniqueness guarantee
  - `MOTION_INTENSITY: 6` — Animation depth level
  - `VISUAL_DENSITY: 3` — Content density control
  - `LANDING_PURPOSE: conversion` — Target outcome
- **supanova-premium-aesthetic** — $150k+ Korean-agency aesthetic enforcement
- **supanova-redesign-engine** — Scan → Diagnose → Fix redesign workflow
- **supanova-full-output** — Zero placeholder, production-critical output

Install: `npx skills add uxjoseph/supanova-design-skill`

## Optimization Tree Visualization

The optimization tree can be rendered as an interactive SVG or canvas visualization where:

- Each node represents a design skill
- Connections show routing paths
- Node size indicates usage frequency
- Color coding matches tier assignment
- Click a node to invoke that skill directly

## Constraints

- Never invoke Tier 4 (animation) skills directly for static design requests
- Always pass through Tier 1 design intelligence before Tier 2 generation
- The supanova suite outputs standalone HTML — no frameworks needed
- Animation orchestrator must approve before any animation skill executes
- Redesign requests must always audit before generating fixes

## Examples

### Example 1: New Landing Page
```
User: "Design a premium landing page for a SaaS product"
→ design-nested routes to:
  1. supanova-design-engine (set DESIGN_VARIANCE:8, LANDING_PURPOSE:conversion)
  2. supanova-premium-aesthetic (generate $150k+ aesthetic)
  3. supanova-full-output (ensure complete output)
```

### Example 2: Redesign Existing Page
```
User: "Redesign my current homepage, it looks generic"
→ design-nested routes to:
  1. supanova-redesign-engine (scan + diagnose)
  2. animation-auditor (check motion quality)
  3. supanova-premium-aesthetic (apply premium fixes)
```

### Example 3: UI Component Design
```
User: "Build a design system with tokens and components"
→ design-nested routes to:
  1. ui-ux-pro-max-v7 (tokens, palettes, fonts, components)
  2. frontend-design (shadcn/ui + Tailwind implementation)
```

### Example 4: Animation Choreography
```
User: "Create a cinematic scroll-driven animation sequence"
→ design-nested routes to:
  1. animation-orchestrator (plan the sequence)
  2. animation-hybrid-architect (assign Motion vs GSAP boundaries)
  3. gsap-animation-engineer (build the cinematic sequence)
  4. motion-animation-engineer (handle UI-layer animations)
```
