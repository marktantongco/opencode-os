/**
 * app/demo/page.tsx — live demo route for the 3-Layer Animation Stack.
 *
 * This file is a Server Component so it can export route metadata.
 * The actual component mount happens in DemoClient.tsx (Client Component)
 * because Next.js 15 forbids `next/dynamic` with `ssr: false` in Server
 * Components, and the LayeredAnimationStack needs `ssr: false` to avoid
 * WebGL/window/document SSR errors.
 *
 * See app/demo/DemoClient.tsx for the full doctrine commentary.
 */

import type { Metadata } from 'next';
import DemoClient from './DemoClient';

export const metadata: Metadata = {
  title: '3-Layer Animation Stack — Live Demo · opencode OS',
  description:
    'Live reference implementation of the 3-Layer Animation Separation doctrine: Three.js (scene), GSAP (camera + scroll), Framer Motion (UI overlays).',
};

export default function DemoPage() {
  return (
    <main>
      <DemoClient scrollDistance={2400} />
    </main>
  );
}
