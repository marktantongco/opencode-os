'use client';

/**
 * app/demo/DemoClient.tsx — Client Component wrapper for the 3-Layer
 * Animation Stack.
 *
 * Next.js 15 forbids `next/dynamic` with `ssr: false` inside Server
 * Components. The demo page (app/demo/page.tsx) is a Server Component
 * so it can export route metadata; this file is the Client Component
 * that actually mounts the WebGL canvas.
 *
 * The LayeredAnimationStack component uses Three.js (WebGL), GSAP
 * ScrollTrigger, and Framer Motion — none of which can run on the
 * server. We lazy-load it with next/dynamic and `ssr: false` so the
 * component is only ever imported in the browser, avoiding:
 *   - "window is not defined" / "document is not defined" SSR errors
 *   - WebGL context creation on the server (which would crash Node)
 *   - hydration mismatches (Three.js generates random IDs per mount)
 *
 * While the client bundle loads, a static placeholder is shown.
 *
 * The component itself enforces the 3-Layer Separation doctrine documented
 * in skills/animation-3d-layered-architect/SKILL.md:
 *   - Layer 1 (Three.js): scene + objects + render loop. NEVER animates camera.
 *   - Layer 2 (GSAP): camera + scroll-linked animation only. NEVER creates
 *                     Three.js objects, NEVER calls renderer.render().
 *   - Layer 3 (Framer Motion): React UI overlays only. NEVER touches canvas.
 * Cross-layer communication: refs only. Per-layer cleanup.
 */

import dynamic from 'next/dynamic';

const LayeredAnimationStack = dynamic(
  () =>
    import(
      '@/components/layered-animation-stack/LayeredAnimationStack'
    ).then((mod) => mod.LayeredAnimationStack),
  {
    ssr: false,
    loading: () => <DemoPlaceholder />,
  }
);

export default function DemoClient({
  scrollDistance = 2400,
}: {
  scrollDistance?: number;
}) {
  return <LayeredAnimationStack scrollDistance={scrollDistance} />;
}

/**
 * Placeholder shown while the Three.js + GSAP + Framer Motion chunk loads.
 * Kept intentionally lightweight — pure CSS animation, no JS deps — so it
 * paints instantly on first paint.
 */
function DemoPlaceholder() {
  return (
    <div
      style={{
        position: 'fixed',
        inset: 0,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        background:
          'radial-gradient(800px 400px at 50% 50%, rgba(80,120,255,0.18), transparent 60%), #05060a',
        color: '#9198ad',
        fontFamily: 'ui-monospace, SFMono-Regular, Menlo, monospace',
        fontSize: '0.875rem',
        letterSpacing: '0.08em',
      }}
    >
      <div style={{ textAlign: 'center' }}>
        <div
          style={{
            width: 48,
            height: 48,
            margin: '0 auto 1rem',
            border: '2px solid rgba(255,255,255,0.12)',
            borderTopColor: '#8ab4ff',
            borderRadius: '50%',
            animation: 'las-spin 0.8s linear infinite',
          }}
        />
        <style>{`@keyframes las-spin { to { transform: rotate(360deg); } }`}</style>
        Loading 3-Layer Animation Stack…
      </div>
    </div>
  );
}
