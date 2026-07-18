/**
 * LayeredAnimationStack.tsx
 * ----------------------------------------------------------------------------
 * Reference implementation of the 3-Layer Animation Separation doctrine:
 *
 *   Layer 1 — THREE.JS    → 3D scene + objects only (renderer, scene, mesh,
 *                            mixer, render loop). NEVER animates camera.
 *   Layer 2 — GSAP        → camera + scroll-linked animation only. NEVER
 *                            creates Three.js objects, NEVER calls renderer.render().
 *   Layer 3 — FRAMER MOTION → React UI overlays only (HUD, modal, button
 *                            micro-interactions). NEVER touches canvas/camera.
 *
 * Cross-layer communication: refs only. No React state holds Three.js objects
 * (state updates cause re-renders → re-mount canvas → destroy WebGL context).
 *
 * Cleanup is per-layer:
 *   Layer 1: useEffect return → cancelAnimationFrame + dispose geometry/
 *            material/renderer/scene + disconnect ResizeObserver.
 *   Layer 2: useGSAP() auto-calls gsap.context().revert() on unmount/dep
 *            change, killing all ScrollTriggers and tweens created in scope.
 *   Layer 3: AnimatePresence + React lifecycle handle exit/unmount
 *            automatically; no manual cleanup needed.
 *
 * Install:
 *   npm install three gsap @gsap/react framer-motion
 *   npm install -D @types/three
 *
 * Usage:
 *   <LayeredAnimationStack scrollDistance={2400} />
 *
 * @source skills/animation-3d-layered-architect/SKILL.md
 * ----------------------------------------------------------------------------
 */

'use client';

import { useCallback, useEffect, useRef, useState } from 'react';
import * as THREE from 'three';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { useGSAP } from '@gsap/react';
import { AnimatePresence, motion } from 'framer-motion';

// Register GSAP plugins ONCE at module load.
gsap.registerPlugin(ScrollTrigger, useGSAP);

// ============================================================================
// TYPES
// ============================================================================

export interface LayeredAnimationStackProps {
  /** CSS selector or HTMLElement used as ScrollTrigger source. Defaults to viewport. */
  scrollSource?: string | HTMLElement;
  /** Total scroll distance (px) over which the camera path completes. Default 2400. */
  scrollDistance?: number;
  /** Mount Layer 1 (Three.js scene). Default true. */
  enableScene?: boolean;
  /** Mount Layer 2 (GSAP camera scroll). Default true. */
  enableCameraScroll?: boolean;
  /** Mount Layer 3 (Framer Motion UI overlay). Default true. */
  enableUI?: boolean;
  /** className applied to the outer wrapper. */
  className?: string;
}

interface SceneHandle {
  scene: THREE.Scene;
  camera: THREE.PerspectiveCamera;
  renderer: THREE.WebGLRenderer;
  mixer: THREE.AnimationMixer;
  dispose: () => void;
}

// ============================================================================
// LAYER 1 — THREE.JS (scene + objects only; never animates camera)
// ============================================================================

/**
 * Creates the Three.js scene, camera (at a FIXED initial position), renderer,
 * lights, a demo mesh, an AnimationMixer for object-level animation, and the
 * requestAnimationFrame render loop.
 *
 * The camera's INITIAL position is set here; after that, Layer 2 (GSAP) owns
 * camera.position and camera.lookAt. Layer 1 only continues to call
 * renderer.render() each frame and update the mixer (object animation).
 *
 * Cleanup: the returned useEffect disposes ALL GPU resources and cancels the
 * rAF loop on unmount — preventing GPU memory leaks.
 */
function useThreeScene(
  canvasRef: React.RefObject<HTMLCanvasElement | null>,
  enabled: boolean
): React.MutableRefObject<SceneHandle | null> {
  const handleRef = useRef<SceneHandle | null>(null);

  useEffect(() => {
    if (!enabled || !canvasRef.current) return;
    const canvas = canvasRef.current;

    // --- Scene ---
    const scene = new THREE.Scene();
    scene.background = new THREE.Color('#0a0b0f');

    // --- Camera (INITIAL position only — Layer 2 will animate from here) ---
    const camera = new THREE.PerspectiveCamera(
      55,
      canvas.clientWidth / Math.max(canvas.clientHeight, 1),
      0.1,
      100
    );
    camera.position.set(0, 1.5, 6);
    camera.lookAt(0, 0, 0);

    // --- Renderer ---
    const renderer = new THREE.WebGLRenderer({
      canvas,
      antialias: true,
      alpha: true,
      powerPreference: 'high-performance',
    });
    renderer.setSize(canvas.clientWidth, canvas.clientHeight, false);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.outputColorSpace = THREE.SRGBColorSpace;

    // --- Lights ---
    scene.add(new THREE.AmbientLight(0xffffff, 0.4));
    const key = new THREE.DirectionalLight(0xffd7a8, 1.2);
    key.position.set(5, 6, 4);
    scene.add(key);
    const rim = new THREE.DirectionalLight(0x6ea8ff, 0.7);
    rim.position.set(-4, 2, -3);
    scene.add(rim);

    // --- Demo mesh: icosahedron with flat shading ---
    const geometry = new THREE.IcosahedronGeometry(1.2, 1);
    const material = new THREE.MeshStandardMaterial({
      color: 0x88aaff,
      metalness: 0.4,
      roughness: 0.3,
      flatShading: true,
    });
    const mesh = new THREE.Mesh(geometry, material);
    scene.add(mesh);

    // --- AnimationMixer for OBJECT animation only (mesh bob, NOT camera) ---
    const mixer = new THREE.AnimationMixer(mesh);
    const bobTrack = new THREE.VectorKeyframeTrack(
      '.position',
      [0, 1, 2],
      [0, 0, 0, 0, 0.4, 0, 0, 0, 0]
    );
    const bobClip = new THREE.AnimationClip('bob', 2, [bobTrack]);
    const bobAction = mixer.clipAction(bobClip);
    bobAction.play();

    // --- Resize handler (ResizeObserver on the canvas) ---
    const handleResize = () => {
      const w = canvas.clientWidth;
      const h = canvas.clientHeight;
      if (w === 0 || h === 0) return;
      renderer.setSize(w, h, false);
      camera.aspect = w / h;
      camera.updateProjectionMatrix();
    };
    const resizeObserver = new ResizeObserver(handleResize);
    resizeObserver.observe(canvas);

    // --- Render loop (Layer 1 owns rAF; Layer 2 does NOT need its own) ---
    const clock = new THREE.Clock();
    let rafId = 0;
    const render = () => {
      const delta = clock.getDelta();
      mixer.update(delta); // OBJECT animation only — never camera
      // NOTE: camera.position is NOT touched here. Layer 2 (GSAP) owns it.
      renderer.render(scene, camera);
      rafId = requestAnimationFrame(render);
    };
    rafId = requestAnimationFrame(render);

    // --- Build handle ---
    handleRef.current = {
      scene,
      camera,
      renderer,
      mixer,
      dispose: () => {
        cancelAnimationFrame(rafId);
        resizeObserver.disconnect();
        mixer.stopAllAction();
        geometry.dispose();
        material.dispose();
        renderer.dispose();
        scene.clear();
      },
    };

    return () => {
      handleRef.current?.dispose();
      handleRef.current = null;
    };
  }, [enabled, canvasRef]);

  return handleRef;
}

// ============================================================================
// LAYER 2 — GSAP (camera + scroll-linked animation only)
// ============================================================================

/**
 * Drives the camera through a 5-keyframe path based on scroll progress.
 * Uses ScrollTrigger with scrub to map scroll → camera position. Writes ONLY
 * to camera.position and camera.lookAt — never creates Three.js objects,
 * never calls renderer.render() (Layer 1 owns the render loop).
 *
 * Cleanup is automatic: useGSAP() wraps everything in a gsap.context() and
 * calls .revert() on unmount or dependency change, which kills all
 * ScrollTriggers and tweens created in scope. No manual cleanup needed.
 */
function useCameraScroll(
  handleRef: React.MutableRefObject<SceneHandle | null>,
  scrollSource: string | HTMLElement | undefined,
  scrollDistance: number,
  enabled: boolean,
  scopeRef: React.RefObject<HTMLElement | null>
) {
  useGSAP(
    () => {
      const sceneHandle = handleRef.current;
      if (!enabled || !sceneHandle) return;
      const { camera } = sceneHandle;

      // 5-keyframe camera path. GSAP samples this piecewise-linearly by `t`.
      const cameraPath = [
        { x: 0, y: 1.5, z: 6, lookAt: new THREE.Vector3(0, 0, 0) },
        { x: 3, y: 2, z: 4, lookAt: new THREE.Vector3(0, 0.5, 0) },
        { x: 0, y: 4, z: 2, lookAt: new THREE.Vector3(0, 0, 0) },
        { x: -3, y: 2, z: 4, lookAt: new THREE.Vector3(0, 0.5, 0) },
        { x: 0, y: 1.5, z: 6, lookAt: new THREE.Vector3(0, 0, 0) },
      ];

      // Proxy object: tween `t` 0→1 and sample cameraPath in onUpdate.
      const camState = { t: 0 };
      const lookTarget = new THREE.Vector3();

      gsap.to(camState, {
        t: 1,
        ease: 'none',
        scrollTrigger: {
          trigger: scrollSource || scopeRef.current || undefined,
          start: 'top top',
          end: `+=${scrollDistance}`,
          scrub: 1,
          // markers: true, // enable for debugging only
        },
        onUpdate: () => {
          const t = camState.t;
          const seg = t * (cameraPath.length - 1);
          const i = Math.min(Math.floor(seg), cameraPath.length - 2);
          const localT = seg - i;
          const a = cameraPath[i];
          const b = cameraPath[i + 1];
          camera.position.set(
            a.x + (b.x - a.x) * localT,
            a.y + (b.y - a.y) * localT,
            a.z + (b.z - a.z) * localT
          );
          lookTarget.lerpVectors(a.lookAt, b.lookAt, localT);
          camera.lookAt(lookTarget);
        },
      });

      // Refresh after a frame so layout is settled before ScrollTrigger measures.
      const raf = requestAnimationFrame(() => ScrollTrigger.refresh());
      return () => cancelAnimationFrame(raf);
    },
    {
      scope: scopeRef,
      dependencies: [handleRef, scrollSource, scrollDistance, enabled],
    }
  );
}

// ============================================================================
// LAYER 3 — FRAMER MOTION (UI overlays only)
// ============================================================================

interface UIOverlayProps {
  scrollProgress: number; // 0..1, fed from a separate scroll listener (NOT GSAP)
  onReset: () => void;
}

/**
 * Fixed-position UI overlay: top scroll-progress bar, top-right HUD,
 * bottom-right "Reset camera" button, bottom-left info button, and an
 * info modal with AnimatePresence-driven exit.
 *
 * This layer NEVER touches the canvas, NEVER writes to camera, and NEVER
 * creates ScrollTrigger instances. It only animates DOM elements via
 * Framer Motion. Cleanup is automatic via AnimatePresence + React lifecycle.
 */
function UIOverlay({ scrollProgress, onReset }: UIOverlayProps) {
  const [modalOpen, setModalOpen] = useState(false);

  return (
    <div className="pointer-events-none fixed inset-0 z-50">
      {/* Top scroll-progress bar — Framer Motion reads scrollProgress prop */}
      <motion.div
        className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500 origin-left"
        style={{ scaleX: scrollProgress }}
      />

      {/* HUD: top-right info panel */}
      <motion.div
        className="absolute top-4 right-4 pointer-events-auto bg-black/60 backdrop-blur-md text-white rounded-lg p-3 text-xs font-mono"
        initial={{ opacity: 0, y: -10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.3, duration: 0.4 }}
      >
        <div>Scroll: {(scrollProgress * 100).toFixed(0)}%</div>
        <div className="text-[10px] opacity-60 mt-1">3-Layer Animation Stack</div>
      </motion.div>

      {/* Reset camera button */}
      <motion.button
        type="button"
        className="absolute bottom-4 right-4 pointer-events-auto px-4 py-2 bg-white/10 hover:bg-white/20 backdrop-blur-md text-white rounded-lg text-sm font-medium border border-white/20"
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.4, duration: 0.4 }}
        whileHover={{ scale: 1.05 }}
        whileTap={{ scale: 0.95 }}
        onClick={onReset}
      >
        Reset camera
      </motion.button>

      {/* Info button */}
      <motion.button
        type="button"
        className="absolute bottom-4 left-4 pointer-events-auto px-4 py-2 bg-white/10 hover:bg-white/20 backdrop-blur-md text-white rounded-lg text-sm font-medium border border-white/20"
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.5, duration: 0.4 }}
        whileHover={{ scale: 1.05 }}
        whileTap={{ scale: 0.95 }}
        onClick={() => setModalOpen(true)}
      >
        What am I looking at?
      </motion.button>

      {/* Modal — AnimatePresence handles exit animation on unmount */}
      <AnimatePresence>
        {modalOpen && (
          <>
            <motion.div
              className="absolute inset-0 bg-black/60 backdrop-blur-sm"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              onClick={() => setModalOpen(false)}
            />
            <motion.div
              className="absolute inset-0 flex items-center justify-center pointer-events-auto"
              initial={{ opacity: 0, scale: 0.9, y: 20 }}
              animate={{ opacity: 1, scale: 1, y: 0 }}
              exit={{ opacity: 0, scale: 0.9, y: 20 }}
              transition={{ type: 'spring', damping: 25, stiffness: 300 }}
            >
              <div className="bg-zinc-900 text-white rounded-xl p-6 max-w-md mx-4 border border-white/10">
                <h2 className="text-lg font-semibold mb-2">3-Layer Animation Stack</h2>
                <p className="text-sm opacity-80 mb-3">
                  This scene demonstrates strict separation of animation concerns:
                </p>
                <ul className="text-sm space-y-1.5 opacity-80 mb-4">
                  <li>
                    <b className="text-blue-400">Three.js</b> — owns the scene, mesh, and
                    render loop (Layer 1).
                  </li>
                  <li>
                    <b className="text-purple-400">GSAP</b> — owns the camera path, driven
                    by ScrollTrigger (Layer 2).
                  </li>
                  <li>
                    <b className="text-pink-400">Framer Motion</b> — owns this overlay,
                    modal, and buttons (Layer 3).
                  </li>
                </ul>
                <button
                  type="button"
                  className="px-4 py-2 bg-white text-black rounded-lg text-sm font-medium w-full hover:bg-white/90"
                  onClick={() => setModalOpen(false)}
                >
                  Got it
                </button>
              </div>
            </motion.div>
          </>
        )}
      </AnimatePresence>
    </div>
  );
}

// ============================================================================
// ROOT — wires the three layers together via refs (NO React state for Three.js)
// ============================================================================

export function LayeredAnimationStack({
  scrollSource,
  scrollDistance = 2400,
  enableScene = true,
  enableCameraScroll = true,
  enableUI = true,
  className,
}: LayeredAnimationStackProps) {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);
  const scopeRef = useRef<HTMLDivElement | null>(null);
  const [scrollProgress, setScrollProgress] = useState(0);

  // Layer 1: mount Three.js scene. Returns a ref to the SceneHandle.
  const sceneHandleRef = useThreeScene(canvasRef, enableScene);

  // Layer 2: GSAP camera scroll. Reads sceneHandleRef.current; cleanup is
  // automatic via useGSAP().
  useCameraScroll(
    sceneHandleRef,
    scrollSource,
    scrollDistance,
    enableCameraScroll,
    scopeRef
  );

  // Separate scroll listener for the UI progress bar (Layer 3). This is
  // intentionally NOT GSAP — Framer Motion's useScroll could also be used.
  // Keeping it separate ensures Layer 3 never depends on Layer 2 internals.
  useEffect(() => {
    if (!enableUI) return;
    const onScroll = () => {
      const max = Math.max(
        document.body.scrollHeight - window.innerHeight,
        1
      );
      setScrollProgress(Math.min(window.scrollY / max, 1));
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
    return () => window.removeEventListener('scroll', onScroll);
  }, [enableUI]);

  const handleReset = useCallback(() => {
    if (typeof window === 'undefined') return;
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }, []);

  return (
    <div ref={scopeRef} className={`relative w-full ${className ?? ''}`}>
      {/* Layer 1 canvas — fixed to viewport so it stays put while scrolling */}
      <canvas
        ref={canvasRef}
        aria-hidden="true"
        className="fixed inset-0 w-screen h-screen"
        style={{ zIndex: 0 }}
      />

      {/* Layer 3: UI overlays (fixed-position) */}
      {enableUI && <UIOverlay scrollProgress={scrollProgress} onReset={handleReset} />}

      {/* Scrollable spacer — this gives Layer 2 (GSAP ScrollTrigger) room
          to scroll through, which drives the camera path. */}
      <div className="relative" style={{ zIndex: 1, height: `${scrollDistance}px` }} />
    </div>
  );
}

export default LayeredAnimationStack;
