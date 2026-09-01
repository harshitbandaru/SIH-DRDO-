# FoveaMap SIH Pitch & Demo Video Narration Script (2.5 – 3 Minutes)

This script provides exact timecoded narration points aligned with generated visual assets for the **DRDO / SIH Problem Statement 26053** demo video.

---

## 🎬 Video Scene Timeline & Voiceover Script

### Scene 1: Introduction & Problem Statement (0:00 – 0:30)
- **Visual Asset**: Project Title Card & SIH Problem Statement 26053 Overview.
- **Voiceover**:
  > *"Welcome. Autonomous tactical unmanned ground vehicles operating in off-road defense environments require dense 3D LiDAR mapping for safe navigation. However, standard uniform high-resolution grids suffer from extreme memory footprints and computational bottlenecks."*
  > *"To solve this, we present **FoveaMap** — an Adaptive Variable-Resolution 2.5D Grid Engine designed for high-speed edge intelligence."*

---

### Scene 2: Live Progressive Point Cloud Animation (0:30 – 1:15)
- **Visual Asset**: [`foveamap_grid_engine.gif`](file:///c:/Users/mail2/OneDrive/Desktop/c/SIH/FoveaMap-Prototype/foveamap_grid_engine.gif) (Live progressive point ingestion animation).
- **Voiceover**:
  > *"Inspired by biological human vision, FoveaMap dynamically partitions spatial terrain into concentric radial resolution rings centered on the vehicle's sensor."*
  > *"In Ring 0, within 10 meters, it allocates 5 cm high-resolution cells for critical obstacle perception. Ring 1 maintains 15 cm resolution up to 30 meters, while Ring 2 uses 50 cm coarse cells across the outer 100-meter periphery."*

---

### Scene 3: Semantic Probability & Temporal Fusion (1:15 – 1:50)
- **Visual Asset**: [`foveamap_semantic_grid.png`](file:///c:/Users/mail2/OneDrive/Desktop/c/SIH/FoveaMap-Prototype/foveamap_semantic_grid.png) (Semantic class map).
- **Voiceover**:
  > *"FoveaMap maintains 2.5D elevation statistics alongside 3-class semantic probability layers. Here, terrain ground is identified in **Green**, static structures in **Red**, and dynamic moving targets in **Blue**."*
  > *"With integrated temporal decay fusion, consecutive LiDAR sweeps are blended seamlessly in real time without unbounded cell growth."*

---

### Scene 4: 2.5D Elevation & Surface Roughness (1:50 – 2:20)
- **Visual Asset**: [`foveamap_elevation_grid.png`](file:///c:/Users/mail2/OneDrive/Desktop/c/SIH/FoveaMap-Prototype/foveamap_elevation_grid.png) (Mean elevation map).
- **Voiceover**:
  > *"For every active cell, FoveaMap maintains $z_{\text{mean}}$, $z_{\text{min}}$, $z_{\text{max}}$, and surface roughness variance. This enables rapid extraction of ground slopes, step hazards, and clearance height required for real-time trajectory planning."*

---

### Scene 5: Memory Efficiency Benchmark & Conclusion (2:20 – 3:00)
- **Visual Asset**: [`foveamap_memory_comparison.png`](file:///c:/Users/mail2/OneDrive/Desktop/c/SIH/FoveaMap-Prototype/foveamap_memory_comparison.png) (Side-by-side memory comparison chart).
- **Voiceover**:
  > *"Let's look at the benchmarks. A uniform 5 cm grid spanning a 200-meter zone requires 16 million cells and nearly 1 Gigabyte of RAM."*
  > *"In contrast, FoveaMap uses a sparse hash architecture operating in under **38 Megabytes** — delivering **over 99.3% memory reduction** and a **150x compression ratio**."*
  > *"FoveaMap is pure Python, zero heavy dependencies, and ready for deployment on defense robotics platforms."*

---

## 📁 Generated Demo Assets Checklist

- [x] [`foveamap_grid_engine.gif`](file:///c:/Users/mail2/OneDrive/Desktop/c/SIH/FoveaMap-Prototype/foveamap_grid_engine.gif) — Progressive projection video asset
- [x] [`foveamap_semantic_grid.png`](file:///c:/Users/mail2/OneDrive/Desktop/c/SIH/FoveaMap-Prototype/foveamap_semantic_grid.png) — Semantic class map PNG
- [x] [`foveamap_elevation_grid.png`](file:///c:/Users/mail2/OneDrive/Desktop/c/SIH/FoveaMap-Prototype/foveamap_elevation_grid.png) — 2.5D Elevation map PNG
- [x] [`foveamap_memory_comparison.png`](file:///c:/Users/mail2/OneDrive/Desktop/c/SIH/FoveaMap-Prototype/foveamap_memory_comparison.png) — Side-by-side memory benchmark PNG
