# Layered Animation Stack — Reference Implementation

> 3-Layer Separation: **Three.js** (scene + objects) · **GSAP** (camera + scroll) · **Framer Motion** (UI overlays)

This directory contains the canonical reference implementation of the 3-Layer Animation Separation doctrine defined in [`skills/animation-3d-layered-architect/SKILL.md`](../../skills/animation-3d-layered-architect/SKILL.md).

## Files

| File | Purpose |
|------|---------|
| `LayeredAnimationStack.tsx` | Drop-in React/Next.js component. Self-contained, fully typed, copy-pasteable. |

## The Contract

```
Layer 3 — Framer Motion   →  React UI overlays only (modals, buttons, HUD)
                              Cleanup: AnimatePresence + component unmount
                              Forbidden: canvas, camera, scene, ScrollTrigger
                                  ↓ communicates via props (primitives only)
Layer 2 — GSAP            →  Camera + scroll-linked animation only
                              Cleanup: useGSAP() → gsap.context().revert()
                              Forbidden: creating THREE.* objects, renderer.render()
                                  ↓ reads sceneHandleRef.current.camera
Layer 1 — Three.js        →  Scene + objects + render loop (rAF)
                              Cleanup: useEffect return → dispose everything
                              Forbidden: animating camera after init, reading scroll
```

## Install

```bash
npm install three gsap @gsap/react framer-motion
npm install -D @types/three
```

## Usage

```tsx
// app/demo/page.tsx
import { LayeredAnimationStack } from '@/components/layered-animation-stack/LayeredAnimationStack';

export default function DemoPage() {
  return <LayeredAnimationStack scrollDistance={2400} />;
}
```

The component renders:
- A fixed full-screen `<canvas>` running a Three.js scene (icosahedron + bob animation).
- A scroll-driven camera path (5 keyframes: wide → orbit right → top-down → orbit left → wide).
- A fixed UI overlay: top scroll-progress bar, top-right HUD, bottom-left info button (opens modal), bottom-right reset button.

Scroll the page → camera moves through the 5-keyframe path. Click "What am I looking at?" → modal opens with AnimatePresence-driven spring entrance and exit.

## What each layer does NOT do

**Layer 1 (Three.js) does NOT:**
- Animate `camera.position` or `camera.lookAt` after init (Layer 2 owns this)
- Read `window.scrollY` or listen to `scroll` events
- Call `ScrollTrigger` APIs
- Touch DOM outside the canvas

**Layer 2 (GSAP) does NOT:**
- Create any `THREE.*` object (scene, mesh, material, etc.)
- Call `renderer.render()` — Layer 1's rAF loop already does this every frame
- Touch any DOM element
- Animate mesh properties (only `camera.position` and `camera.lookAt`)

**Layer 3 (Framer Motion) does NOT:**
- Touch the `<canvas>` element
- Write to `camera`, `scene`, or any Three.js object
- Create `ScrollTrigger` instances (uses its own `scroll` listener for the UI bar)
- Store Three.js objects in React state

## Cross-layer communication

All cross-layer communication uses **refs**, never React state. State updates cause re-renders → re-mount canvas → destroy WebGL context.

```tsx
const canvasRef      = useRef<HTMLCanvasElement | null>(null);      // Layer 1 owns
const scopeRef       = useRef<HTMLDivElement | null>(null);         // Layer 2 uses as GSAP scope
const sceneHandleRef = useThreeScene(canvasRef, true);              // Layer 1 → Layer 2 bridge
//                                                               ↑
//                                          Layer 2 reads sceneHandleRef.current.camera
//                                          Layer 3 receives only primitive props
```

## Cleanup guarantees

| Layer | What | How |
|-------|------|-----|
| 1 | GPU resources (geometry, material, renderer, scene) + rAF loop + ResizeObserver | `useEffect` return calls `handle.dispose()` which calls `cancelAnimationFrame`, `mixer.stopAllAction()`, `geometry.dispose()`, `material.dispose()`, `renderer.dispose()`, `scene.clear()`, `resizeObserver.disconnect()` |
| 2 | ScrollTriggers + tweens | `useGSAP()` automatically calls `gsap.context().revert()` on unmount or dep change, which kills all ScrollTriggers and tweens created in the scope |
| 3 | AnimatePresence exit animations + motion component inline styles | `AnimatePresence` handles exit; `motion.*` components revert inline styles on unmount automatically |

## Performance notes

- Three.js bundle: ~600 KB (tree-shaken). Use `next/dynamic` with `ssr: false` to lazy-load only on client.
- GSAP + ScrollTrigger: ~60 KB.
- Framer Motion: 3 KB (`useAnimate` mini) or 34 KB (full `domMax`). For just this overlay, `motion` + `AnimatePresence` is enough.
- Total runtime RAM: well under the 3.7 GB ceiling on any modern device.

## prefers-reduced-motion

The current implementation does not gate on `prefers-reduced-motion` for brevity. To add it:

```ts
// In useThreeScene: skip mixer.update() if reduced motion
// In useCameraScroll: skip ScrollTrigger scrub, set camera to final position
// In UIOverlay: use Framer Motion's useReducedMotion() hook (auto-handled)
```

## See also

- [`skills/animation-3d-layered-architect/SKILL.md`](../../skills/animation-3d-layered-architect/SKILL.md) — full doctrine (7-step workflow, anti-patterns, audit checklist)
- [`skills/animation-hybrid-architect/SKILL.md`](../../skills/animation-hybrid-architect/SKILL.md) — 2-layer Motion + GSAP split (no Three.js)
- [`.agents/skills/threejs-animation/SKILL.md`](../../.agents/skills/threejs-animation/SKILL.md) — Layer 1 API reference (AnimationMixer, AnimationAction)
- [`.agents/skills/gsap-scrolltrigger/SKILL.md`](../../.agents/skills/gsap-scrolltrigger/SKILL.md) — Layer 2 API reference (ScrollTrigger, scrub, pin)
- [`.agents/skills/framer-motion-animator/SKILL.md`](../../.agents/skills/framer-motion-animator/SKILL.md) — Layer 3 API reference (motion, AnimatePresence, useScroll)
