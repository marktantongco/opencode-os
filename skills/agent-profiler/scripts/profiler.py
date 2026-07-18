#!/usr/bin/env python3
"""
Animation Profiler — Generates a structured profiling checklist and interprets
Chrome DevTools Performance data for animation bottlenecks.

Usage:
    python profiler.py --mode=checklist
    python profiler.py --mode=interpret --file=performance.json
"""

import json, sys, argparse

def generate_checklist():
    checklist = {
        "pre_profile": [
            "Open Chrome DevTools → Performance tab",
            "Enable 'Screenshots' and 'Web Vitals'",
            "Set CPU throttling to 4× (mobile simulation)",
            "Clear cache and hard reload (Ctrl+Shift+R)"
        ],
        "during_profile": [
            "Click Record",
            "Perform the animation interaction 3 times",
            "Wait 2 seconds after animation completes",
            "Click Stop"
        ],
        "analysis_steps": [
            "Check Frame strip: Are frames green (60fps) or red (dropped)?",
            "Check Main thread: Any Long Tasks (>50ms)?",
            "Check for Layout (purple) events: Count per frame",
            "Check for Paint (green) events: Duration per frame",
            "Check GPU thread: Any GPU-bound operations?",
            "Check Memory graph: Continuous growth or flat?",
            "Check React Profiler (if React): Flamegraph for re-renders"
        ],
        "decision_tree": {
            "Long Tasks in Main Thread": {
                "JavaScript": "Heavy computation in animation loop → Move to Web Worker or use refs",
                "Layout": "Layout thrashing → Convert to transform/opacity animations",
                "Style": "Style recalculation → Reduce CSS complexity, use will-change",
                "Paint": "Paint bottleneck → Reduce layer count, simplify effects"
            },
            "GPU Thread Busy": {
                "Draw Calls": "Too many → Use InstancedMesh/BatchedMesh",
                "Textures": "Too large → Compress with KTX2/Basis",
                "Shaders": "Too complex → Simplify or use LOD"
            },
            "Memory Growing": {
                "GSAP": "Missing ctx.revert() → Add cleanup",
                "Motion": "AnimatePresence key mismatch → Fix keys",
                "Three.js": "Missing dispose() → Add disposal",
                "React": "Event listeners → Remove in cleanup"
            },
            "Excessive Re-renders": {
                "State in Loop": "Move state to refs → Use useRef instead of useState",
                "Context": "Split context → Use Zustand or atomic state",
                "Parent": "Memoize → Wrap in React.memo"
            }
        }
    }
    return checklist

def interpret_performance(data):
    # Parse Chrome DevTools Performance export
    frames = data.get("frames", [])
    main_thread = data.get("main_thread_events", [])

    report = {
        "frame_analysis": {},
        "bottleneck": None,
        "confidence": 0
    }

    # Analyze frames
    dropped_frames = [f for f in frames if f["duration"] > 16.67]
    report["frame_analysis"]["total"] = len(frames)
    report["frame_analysis"]["dropped"] = len(dropped_frames)
    report["frame_analysis"]["drop_rate"] = len(dropped_frames) / len(frames) if frames else 0

    # Analyze main thread
    long_tasks = [e for e in main_thread if e["duration"] > 50]
    layout_events = [e for e in main_thread if e["type"] == "Layout"]
    paint_events = [e for e in main_thread if e["type"] == "Paint"]

    # Determine bottleneck
    if long_tasks:
        task_types = {}
        for t in long_tasks:
            task_types[t.get("subtype", "Unknown")] = task_types.get(t.get("subtype", "Unknown"), 0) + 1
        dominant = max(task_types, key=task_types.get)
        report["bottleneck"] = f"Long Tasks: {dominant}"
        report["confidence"] = 0.9
    elif layout_events:
        report["bottleneck"] = "Layout Thrashing"
        report["confidence"] = 0.85
    elif paint_events:
        report["bottleneck"] = "Paint Bottleneck"
        report["confidence"] = 0.8
    elif report["frame_analysis"]["drop_rate"] > 0.1:
        report["bottleneck"] = "Unknown — requires deeper investigation"
        report["confidence"] = 0.5
    else:
        report["bottleneck"] = "No significant bottleneck detected"
        report["confidence"] = 0.95

    return report

def main():
    parser = argparse.ArgumentParser(description="Animation Profiler")
    parser.add_argument("--mode", choices=["checklist", "interpret"], required=True)
    parser.add_argument("--file", help="Performance JSON file for interpret mode")
    args = parser.parse_args()

    if args.mode == "checklist":
        checklist = generate_checklist()
        print(json.dumps(checklist, indent=2))
    elif args.mode == "interpret":
        if not args.file:
            print("Error: --file required for interpret mode")
            sys.exit(1)
        with open(args.file) as f:
            data = json.load(f)
        report = interpret_performance(data)
        print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
