---
name: animation-3d-layered-architect
version: 1.0.0
description: Three-layer animation separation doctrine for Three.js + GSAP + Framer Motion. Three.js owns the 3D scene and objects only. GSAP owns the camera and scroll-linked animation only. Framer Motion owns React UI overlays only. Strict useEffect cleanup, no cross-layer DOM writes, refs-only cross-layer communication.
category: animation
triggers:
  - three.js and gsap and framer motion
  - 3d layered animation
  - animation layer split
  - camera scroll animation
  - three gsap framer
  - 3-layer animation
  - layered separation animation
  - three.js camera scroll
activation_rules:
  - IF user requests THREE.JS + GSAP + FRAMER MOTION in the same project
  - IF user asks for "layered separation" or "3-layer animation"
  - IF user wants to animate a Three.js camera with scroll AND has React UI overlays
  - IF user reports animation conflicts between Three.js / GSAP / Framer Motion
  - IF animation-orchestrator routes to a 3D + UI hybrid request
stack: [three, gsap, @gsap/react, ScrollTrigger, framer-motion]
performance:
  three_initial: 600KB
  gsap_initial: 60KB
  framer_motion_initial: 34KB
  ram_ceiling: 3.7GB
---

# Animation 3D Layered Architect

Three-layer animation separation doctrine for projects that combine **Three.js**, **GSAP**, and **Framer Motion**. Each library owns exactly one concern; layers communicate via refs only; cleanup is mandatory per layer.

## The 3-Layer Contract

```
┌──────────────────────────────────────────────────────────────────┐
│  LAYER 3 — FRAMER MOTION (UI overlays only)                     │
│  DOM: HTML overlays (modals, buttons, HUD, progress bars)       │
│  Owns: entrance / exit / gesture / layout animations            │
│  Forbidden: canvas, camera, scene, mixer, ScrollTrigger         │
│  Cleanup: AnimatePresence + component unmount (automatic)       │
├──────────────────────────────────────────────────────────────────┤
│  LAYER 2 — GSAP (camera + scroll-linked animation only)         │
│  DOM: reads `window.scrollY` via ScrollTrigger                  │
│  Owns: camera.position, camera.lookAt, scroll-driven timelines  │
│  Forbidden: creating Three.js objects, renderer.render(), DOM   │
│  Cleanup: useGSAP() → gsap.context().revert() (automatic)       │
├──────────────────────────────────────────────────────────────────┤
│  LAYER 1 — THREE.JS (scene + objects only)                      │
│  DOM: <canvas> only                                             │
│  Owns: renderer, scene, camera (INITIAL position only), mesh,   │
│        lights, AnimationMixer, requestAnimationFrame render loop│
│  Forbidden: animating camera after init, reading scroll, DOM    │
│  Cleanup: useEffect return → dispose renderer/geometry/material │
└──────────────────────────────────────────────────────────────────┘
```

## Layer 1 — Three.js (Scene + Objects Only)

**Owns:**
- `WebGLRenderer` (canvas creation, pixel ratio, color space)
- `Scene` (background, fog)
- `PerspectiveCamera` — **initial position only**, set once at construction
- `Mesh`, `Geometry`, `Material`, `Light`, `Texture`
- `AnimationMixer` for object animation (GLTF clips, morph targets, procedural bob)
- The render loop (`requestAnimationFrame` → `renderer.render()`)

**Forbidden:**
- Animating `camera.position` or `camera.lookAt` after init (Layer 2 owns this)
- Reading `window.scrollY` or `scroll` events
- Touching any DOM outside the canvas
- Calling `ScrollTrigger` APIs

**useEffect cleanup:**
```ts
useEffect(() => {
  // ... create scene, camera, renderer, mesh, mixer, rAF loop ...
  return () => {
    cancelAnimationFrame(rafId);
    resizeObserver.disconnect();
    mixer.stopAllAction();
    geometry.dispose();
    material.dispose();
    renderer.dispose();
    scene.clear();
  };
}, [enabled]);
```

## Layer 2 — GSAP (Camera + Scroll Only)

**Owns:**
- `ScrollTrigger` instances (one per camera move)
- `gsap.timeline({ scrollTrigger: { ... } })` for scroll-scrubbed camera paths
- `gsap.to(camera.position, ...)` for tweened camera moves
- `camera.lookAt()` calls (inside `onUpdate` of a ScrollTrigger tween)

**Forbidden:**
- Creating `THREE.*` objects (scene, mesh, material, etc.)
- Calling `renderer.render()` — Layer 1 already runs the rAF loop
- Touching DOM elements
- Animating mesh properties (only camera)

**useGSAP cleanup pattern:**
```ts
import { useGSAP } from '@gsap/react';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger, useGSAP);

useGSAP(
  () => {
    gsap.to(camState, {
      t: 1,
      ease: 'none',
      scrollTrigger: {
        trigger: scrollSource,
        start: 'top top',
        end: `+=${scrollDistance}`,
        scrub: 1,
      },
      onUpdate: () => {
        camera.position.set(...);
        camera.lookAt(...);
      },
    });
  },
  { scope: scopeRef, dependencies: [sceneHandle, scrollDistance] }
);
// On unmount or dep change, useGSAP automatically calls gsap.context().revert(),
// which kills all ScrollTriggers and tweens created in this scope. No manual cleanup needed.
```

## Layer 3 — Framer Motion (UI Overlays Only)

**Owns:**
- HTML overlays (modals, buttons, HUD, progress bars, tooltips)
- Entrance / exit animations via `AnimatePresence`
- Gesture animations (`whileHover`, `whileTap`, `drag`)
- Layout animations (`layout`, `layoutId`)
- UI-only scroll progress (via `useScroll` + `useTransform` — for **UI bars**, NOT for 3D camera)

**Forbidden:**
- Touching the `<canvas>` element
- Writing to `camera.position` or any Three.js object
- Creating `ScrollTrigger` instances (use Framer Motion's `useScroll` for UI bars)

**Cleanup:**
- `AnimatePresence` handles exit animations automatically.
- `motion.*` components revert inline styles on unmount.
- No manual `useEffect` cleanup needed for declarative Framer Motion usage.

## Cross-Layer Communication: Refs Only

The three layers MUST communicate via refs (or a `useRef` handle object), **never via React state**. State updates trigger re-renders, which can:
- Cause Three.js to re-mount the canvas (destroying the WebGL context)
- Cause GSAP to re-create ScrollTriggers in a hot loop
- Cause Framer Motion to replay entrance animations

**Correct pattern:**
```ts
const canvasRef = useRef<HTMLCanvasElement | null>(null);
const scopeRef  = useRef<HTMLDivElement | null>(null);
const sceneHandleRef = useRef<SceneHandle | null>(null);

// Layer 1 — writes sceneHandleRef.current
useThreeScene(canvasRef, enabled, sceneHandleRef);

// Layer 2 — reads sceneHandleRef.current, never writes
useCameraScroll(sceneHandleRef.current, scopeRef, scrollDistance);

// Layer 3 — receives only primitive props (scrollProgress: number)
<UIOverlay scrollProgress={scrollProgress} onReset={handleReset} />
```

**Wrong pattern (will cause re-render storms):**
```ts
const [camera, setCamera] = useState<THREE.PerspectiveCamera | null>(null);
// ↑ Every setCamera() re-renders the whole tree, re-running all three useEffects.
```

## The 7-Step Workflow

### Step 1 — Classify every animation

For each animation request, assign exactly one layer:

| Animation | Layer | Reason |
|-----------|-------|--------|
| Mesh bobbing (procedural or GLTF) | Three.js | Object animation in 3D scene |
| Camera orbit on scroll | GSAP | Camera move + scroll-linked |
| Modal open/close | Framer Motion | UI overlay |
| Material color cycle | Three.js | Object property in 3D scene |
| Button hover scale | Framer Motion | UI overlay |
| Scroll progress bar (UI) | Framer Motion | UI overlay (`useScroll`) |
| Camera dolly on click | GSAP | Camera move (use timeline, not ScrollTrigger) |

If you cannot assign an animation to exactly one layer, **redesign the animation**.

### Step 2 — Define layer boundaries in code

```ts
// boundaries.ts
export const LAYER_BOUNDARIES = {
  three: {
    dom: ['canvas#three-canvas'],
    owns: ['scene', 'mesh', 'material', 'light', 'mixer', 'renderer', 'rAF loop'],
    forbidden: ['camera animation after init', 'window.scroll', 'DOM outside canvas'],
  },
  gsap: {
    dom: [], // reads window.scrollY via ScrollTrigger; never writes DOM
    owns: ['camera.position', 'camera.lookAt', 'ScrollTrigger instances'],
    forbidden: ['THREE.* creation', 'renderer.render()', 'DOM elements'],
  },
  framerMotion: {
    dom: ['div.ui-overlay', 'button', '.modal', '.hud'],
    owns: ['entrance/exit', 'gestures', 'layout', 'UI progress bars'],
    forbidden: ['canvas', 'camera', 'scene', 'ScrollTrigger'],
  },
} as const;
```

### Step 3 — Mount order matters

Mount Layer 1 first (canvas + scene + camera at initial position), then Layer 2 (GSAP reads `sceneHandle.camera`), then Layer 3 (UI overlays read primitive props only).

```tsx
export function LayeredAnimationStack() {
  const canvasRef = useRef(null);
  const scopeRef  = useRef(null);
  const sceneHandle = useThreeScene(canvasRef, true);          // Layer 1
  useCameraScroll(sceneHandle, scopeRef, 2400);                // Layer 2 (reads sceneHandle)
  return (
    <div ref={scopeRef}>
      <canvas ref={canvasRef} />
      <UIOverlay scrollProgress={scrollProgress} onReset={...} />  {/* Layer 3 */}
    </div>
  );
}
```

### Step 4 — Cleanup is per-layer, not shared

Each layer has its own cleanup. **Do not** try to share a single useEffect that disposes everything — that creates coupling. Let each layer clean up after itself:

- Layer 1: `useEffect` return disposes geometry/material/renderer/scene + cancels rAF
- Layer 2: `useGSAP()` auto-calls `gsap.context().revert()` on unmount/dep change
- Layer 3: `AnimatePresence` + React lifecycle handle exit/unmount automatically

### Step 5 — Handle reduced motion

All three layers must respect `prefers-reduced-motion`:

```ts
const prefersReducedMotion = () =>
  typeof window !== 'undefined' &&
  window.matchMedia('(prefers-reduced-motion: reduce)').matches;

// Layer 1: still render, but skip mixer.update() (objects stay static)
// Layer 2: skip ScrollTrigger scrub — set camera to final position
// Layer 3: Framer Motion's useReducedMotion() hook handles this automatically
```

### Step 6 — Performance budgets

| Layer | Initial bundle | Runtime RAM ceiling |
|-------|---------------|---------------------|
| Three.js | ~600 KB (tree-shaken) | GPU memory depends on geometry/textures |
| GSAP + ScrollTrigger | ~60 KB | Negligible |
| Framer Motion (LazyMotion mini) | ~3 KB (useAnimate) / ~34 KB (domMax) | Negligible |
| **Total** | ~700 KB initial | < 3.7 GB |

Use `next/dynamic` with `ssr: false` to lazy-load Three.js only on the client.

### Step 7 — Audit before commit

```bash
# Pre-commit checks:
# 1. Layer 1 useEffect returns a cleanup that disposes ALL GPU resources
# 2. Layer 2 uses useGSAP() (NOT raw useEffect + gsap.to)
# 3. Layer 3 uses AnimatePresence for any exit animations
# 4. No React state holds Three.js objects (use refs only)
# 5. No layer writes to another layer's DOM
# 6. prefers-reduced-motion is respected by all three layers
# 7. Canvas is fixed/absolute and never re-mounted on state changes
```

## Anti-Patterns

- ❌ `setCamera(new THREE.PerspectiveCamera(...))` — stores Three.js object in React state, causes re-renders
- ❌ `useEffect(() => gsap.to(camera.position, ...), [camera])` — raw useEffect + GSAP, no auto-cleanup
- ❌ Calling `renderer.render()` inside a GSAP `onUpdate` — double render loop, wastes GPU
- ❌ Using Framer Motion `useScroll` to drive a Three.js camera — crosses Layer 2/3 boundary
- ❌ Creating `ScrollTrigger` inside the same useEffect that creates the Three.js scene — couples Layer 1 + Layer 2
- ❌ Animating `camera.position` inside the Three.js render loop — crosses Layer 1/2 boundary
- ❌ Storing `sceneHandle` in React state — causes Layer 2 to re-create ScrollTriggers on every render
- ❌ Forgetting `cancelAnimationFrame` in Layer 1 cleanup — leaks the render loop
- ❌ Forgetting `geometry.dispose()` / `material.dispose()` / `renderer.dispose()` in Layer 1 cleanup — leaks GPU memory

## Reference Implementation

See `components/layered-animation-stack/LayeredAnimationStack.tsx` for a complete, copy-pasteable reference implementation of this doctrine. The file includes:
- `useThreeScene()` hook — Layer 1
- `useCameraScroll()` hook — Layer 2
- `UIOverlay` component — Layer 3
- `LayeredAnimationStack` root — wires the three layers via refs

## Integration Notes

- **Upstream**: `animation-orchestrator` routes to this skill for 3D + UI hybrid requests
- **Sister skill**: `animation-hybrid-architect` covers the 2-layer Motion + GSAP split (no Three.js)
- **Downstream**: Delegates to `threejs-animation` for object animation specifics, `gsap-scrolltrigger` for camera scroll patterns, `framer-motion-animator` for UI overlay patterns
- **Audit**: `animation-auditor` validates layer boundaries before commit

## References

- `gsap-scrolltrigger` SKILL.md — Layer 2 API reference
- `threejs-animation` SKILL.md — Layer 1 AnimationMixer / AnimationAction reference
- `framer-motion-animator` SKILL.md — Layer 3 motion components and AnimatePresence
- `animation-hybrid-architect/references/cleanup-protocols.md` — memory leak prevention (applies to Layer 1)
- `animation-hybrid-architect/references/bundle-budgets.md` — per-tier budget allocation
