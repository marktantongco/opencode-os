---
name: gsap-animator
description: >
  Implement complex animations, scroll-driven sequences, timeline orchestration, SVG morphing, text effects, and physics-based motion using GSAP (GreenSock Animation Platform).
  Use when the user mentions GSAP, timeline, scroll animation, scroll trigger, pinned sections, parallax, text reveal, SVG morph, path animation, drag with inertia, or complex multi-step animation sequences.
  Also trigger for "scroll story", "narrative animation", "award-level animation", "marketing site animation", "hero sequence", "page load animation", or when the user needs animation beyond what React-native libraries (Motion) can provide.
  Always use this skill for complex timeline-based, scroll-driven, or SVG/text animation tasks — do not attempt complex sequences with CSS or raw requestAnimationFrame.
allowed-tools: Read, Write, Bash, Edit, Grep, Glob
user-invocable: true
---

# GSAP Animator

## context

This skill encodes production-grade GSAP patterns for complex web animation: timelines, scroll-driven narratives, SVG morphing, text effects, physics, and drag interactions. It is the escalation path from Motion when tasks exceed React-native capabilities. It enforces the GSAP v3.13+ free-license model and the Design OS performance budget.

## instructions

### Step 1: Determine if GSAP is the Right Tool

Use this decision matrix:

| Need | Tool | Why |
|---|---|---|
| Simple React UI transitions | Motion (Framer Motion) | Native React, declarative, smaller bundle |
| Complex multi-step timeline | **GSAP** | Unmatched sequencing, labels, nesting |
| Scroll-driven narrative | **GSAP ScrollTrigger** | Pin, scrub, snap, batch — best-in-class |
| SVG path morphing | **GSAP MorphSVG** | Smooth rotational mapping, shape interpolation |
| Text character animation | **GSAP SplitText** | Char/word/line splitting with auto-resize |
| Physics (gravity, bounce) | **GSAP Physics2D** | Realistic physics without manual math |
| Drag with inertia | **GSAP Draggable + Inertia** | Bounds, snapping, momentum, elastic |
| Cross-framework animation | **GSAP** | Works identically in React, Vue, Svelte, vanilla |

**Escalation rule:** If Motion can't do it cleanly, or the task needs timeline-level control, escalate to GSAP.

### Step 2: Set Up GSAP in React

```bash
npm install gsap @gsap/react
```

```tsx
"use client";
import { useGSAP } from "@gsap/react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { Flip } from "gsap/Flip";

// Register plugins once at module level
gsap.registerPlugin(ScrollTrigger, Flip);

export function AnimatedSection() {
  useGSAP(() => {
    // GSAP animations here — auto-cleanup on unmount
    gsap.from(".card", {
      y: 100,
      opacity: 0,
      stagger: 0.1,
      duration: 0.8,
      ease: "power3.out",
      scrollTrigger: {
        trigger: ".card-container",
        start: "top 80%",
        toggleActions: "play none none none",
      },
    });
  }, { scope: ".card-container" }); // Scoped to this component only

  return <div className="card-container">...</div>;
}
```

**Critical:** Always use `useGSAP()` instead of raw `useEffect()`/`useLayoutEffect()`. It handles:
- Automatic cleanup on unmount (prevents memory leaks)
- `useIsomorphicLayoutEffect` for SSR safety
- Context scoping (animations only affect the referenced DOM)
- React Strict Mode compatibility

### Step 3: Choose the Right Plugin

| Plugin | Purpose | Bundle Impact |
|---|---|---|
| Core (included) | Tweens, timelines, staggers | 23KB |
| ScrollTrigger | Scroll-linked animations | +7KB |
| ScrollSmoother | Smooth scroll wrapper | +8KB |
| Flip | Layout state transitions | +5KB |
| Draggable | Touch/mouse drag | +6KB |
| InertiaPlugin | Natural deceleration | +3KB |
| MorphSVG | SVG path morphing | +8KB |
| DrawSVG | Stroke drawing | +4KB |
| SplitText | Text char/word/line animation | +10KB |
| Physics2D | Realistic physics | +5KB |
| MotionPath | Animate along paths | +6KB |
| CustomEase | Custom easing curves | +2KB |

**Bundle rule:** Import only the plugins you need. GSAP core + 2 common plugins = ~35KB. Full stack = ~80KB. Still well within most budgets.

### Step 4: Implement Common Patterns

**Timeline Sequence:**
```tsx
useGSAP(() => {
  const tl = gsap.timeline({ defaults: { ease: "power2.out" } });

  tl.from(".hero-title", { y: 80, opacity: 0, duration: 1 })
    .from(".hero-subtitle", { y: 40, opacity: 0, duration: 0.8 }, "-=0.6")
    .from(".cta-button", { scale: 0.8, opacity: 0, duration: 0.5 }, "-=0.4")
    .addLabel("sequenceComplete");
}, []);
```

**ScrollTrigger Pin:**
```tsx
useGSAP(() => {
  gsap.to(".pinned-section", {
    scrollTrigger: {
      trigger: ".pinned-section",
      start: "top top",
      end: "+=2000",
      pin: true,
      scrub: 1,
    },
    scale: 1.2,
    rotation: 5,
  });
}, []);
```

**SplitText Reveal:**
```tsx
useGSAP(() => {
  const split = new SplitText(".headline", { type: "words,chars" });

  gsap.from(split.chars, {
    y: 50,
    opacity: 0,
    stagger: 0.02,
    duration: 0.6,
    ease: "back.out(1.7)",
    scrollTrigger: {
      trigger: ".headline",
      start: "top 85%",
    },
  });
}, []);
```

**MorphSVG Toggle:**
```tsx
useGSAP(() => {
  gsap.to("#icon-path", {
    morphSVG: "#target-path",
    duration: 0.4,
    ease: "power2.inOut",
  });
}, []);
```

**Draggable Slider:**
```tsx
useGSAP(() => {
  Draggable.create(".slider-track", {
    type: "x",
    bounds: ".slider-container",
    inertia: true,
    snap: { x: [0, -300, -600, -900] },
  });
}, []);
```

### Step 5: Handle React Integration Edge Cases

**Cleanup on unmount:**
```tsx
useGSAP(() => {
  const ctx = gsap.context(() => {
    gsap.to(".box", { rotation: 360, duration: 2 });
  });

  return () => ctx.revert(); // Clean up all GSAP animations in this context
}, []);
```

**Dynamic content (lists that change):**
```tsx
useGSAP(() => {
  gsap.from(".list-item", {
    y: 30,
    opacity: 0,
    stagger: 0.05,
    scrollTrigger: {
      trigger: ".list-container",
      start: "top 80%",
    },
  });
}, { dependencies: [items] }); // Re-run when items change
```

### Step 6: Output Complete Code

Always provide:
1. Full component with imports and plugin registration
2. `useGSAP()` hook with proper scoping
3. Comments explaining the animation strategy
4. Bundle size estimate
5. Any required npm install commands

## constraints

- NEVER use raw `useEffect()` + `gsap.to()` without `useGSAP()` — memory leaks in Strict Mode.
- NEVER forget `gsap.registerPlugin()` — unregistered plugins throw runtime errors.
- NEVER animate React state directly — GSAP mutates DOM, React reconciler doesn't know about it. Use refs for GSAP targets.
- NEVER ignore cleanup — always return `ctx.revert()` or use `useGSAP()` auto-cleanup.
- NEVER use GSAP in a tool competing with Webflow (license restriction). For visual no-code builders, use Motion instead.
- NEVER import all plugins "just in case" — import only what you need to keep bundle size minimal.
- NEVER use `gsap.set()` on every render — it causes layout thrashing. Batch DOM reads/writes.

## examples

### Example 1: Scroll-Pinned Hero Sequence

**Input:** "I need a hero section that pins while the user scrolls, and three text blocks fade in sequentially."

**Output:**
```tsx
"use client";
import { useGSAP } from "@gsap/react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);

export function PinnedHero() {
  useGSAP(() => {
    const tl = gsap.timeline({
      scrollTrigger: {
        trigger: ".hero-section",
        start: "top top",
        end: "+=3000",
        pin: true,
        scrub: 1,
      },
    });

    tl.from(".block-1", { opacity: 0, y: 50, duration: 1 })
      .from(".block-2", { opacity: 0, y: 50, duration: 1 }, "+=0.5")
      .from(".block-3", { opacity: 0, y: 50, duration: 1 }, "+=0.5");
  });

  return (
    <section className="hero-section h-screen bg-black text-white flex flex-col items-center justify-center">
      <div className="block-1 text-4xl font-bold">Discover</div>
      <div className="block-2 text-4xl font-bold mt-8">Build</div>
      <div className="block-3 text-4xl font-bold mt-8">Launch</div>
    </section>
  );
}
```

**Bundle:** GSAP core + ScrollTrigger = ~30KB. Acceptable for a hero section.

### Example 2: Text Character Reveal

**Input:** "Animate a headline so each character fades in from below with a stagger."

**Output:**
```tsx
"use client";
import { useGSAP } from "@gsap/react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { SplitText } from "gsap/SplitText";

gsap.registerPlugin(ScrollTrigger, SplitText);

export function TextReveal({ text }: { text: string }) {
  useGSAP(() => {
    const split = new SplitText(".headline", { type: "chars" });

    gsap.from(split.chars, {
      y: 60,
      opacity: 0,
      stagger: 0.03,
      duration: 0.8,
      ease: "back.out(1.7)",
      scrollTrigger: {
        trigger: ".headline",
        start: "top 85%",
        toggleActions: "play none none reverse",
      },
    });
  });

  return <h1 className="headline text-6xl font-bold">{text}</h1>;
}
```

**Bundle:** GSAP core + ScrollTrigger + SplitText = ~43KB. Worth it for the character-level control.

## references

- `references/plugin-guide.md` — Plugin selection matrix and bundle impact
- `references/react-patterns.md` — useGSAP patterns, cleanup, dynamic content, SSR
- `references/scrolltrigger-patterns.md` — Pin, scrub, snap, batch, and responsive patterns
