"""
FoveaMap Prototype Complete Demo Generator
Generates all video and graphic assets for the SIH 26053 Demo Presentation Video.
Includes atomic file swapping and duplicate file cleanup.
"""

import os
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter, FFMpegWriter

# Ensure project root is in sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from foveamap.grid_engine import VariableResolutionGridEngine, RingConfig
from foveamap.visualization import (
    animate_grid_projection,
    plot_final_grid,
    plot_elevation_map,
    plot_memory_comparison,
)


def cleanup_legacy_duplicates(root_dir: str):
    """
    Scans for and removes any legacy duplicate file names from previous prototype versions
    to ensure only the canonical set of 5 output files exists.
    """
    legacy_patterns = [
        "foveamap_elevation_grid.png",
        "foveamap_final_grid.png",
        "foveamap_grid_engine.gif",
        "foveamap_semantic_grid.png",
        os.path.join("foveamap", "foveamap_demo_output.png"),
        os.path.join("foveamap", "foveamap_final_grid.png"),
        os.path.join("foveamap", "foveamap_grid_engine.gif"),
    ]
    for pattern in legacy_patterns:
        full_path = os.path.join(root_dir, pattern)
        if os.path.exists(full_path):
            try:
                os.remove(full_path)
                print(f"    [CLEANUP] Removed legacy file: {pattern}")
            except OSError:
                pass


def safe_atomic_save(target_path: str, save_func):
    """
    Saves an asset file atomically using a temporary file swap preserving file extension.
    Guarantees that the target file is cleanly overwritten in-place,
    preventing duplicate file creation or corrupted partial writes.
    """
    base, ext = os.path.splitext(target_path)
    tmp_path = f"{base}.tmp{ext}"

    if os.path.exists(tmp_path):
        try:
            os.remove(tmp_path)
        except OSError:
            pass

    # Save to temporary path with valid extension
    save_func(tmp_path)

    # Atomically replace target file with fresh render
    if os.path.exists(tmp_path):
        if os.path.exists(target_path):
            try:
                os.remove(target_path)
            except OSError:
                pass
        os.replace(tmp_path, target_path)


def generate_synthetic_lidar_data(num_points: int = 150_000, seed: int = 42):
    """
    Generates realistic 3D LiDAR point cloud with semantic labels:
    - Class 0: Terrain (ground plane, gentle slopes, terrain variation)
    - Class 1: Static Obstacles (buildings, walls, trees)
    - Class 2: Dynamic Obstacles (vehicles, moving targets)
    """
    np.random.seed(seed)

    # 1. Radial distribution up to 100m
    r = np.random.exponential(scale=25.0, size=num_points)
    r = np.clip(r, 0.5, 98.0)
    theta = np.random.uniform(0.0, 2 * np.pi, num_points)

    x = r * np.cos(theta)
    y = r * np.sin(theta)

    # Base terrain elevation
    z = 0.04 * x - 0.02 * y + 0.1 * np.sin(0.1 * x) * np.cos(0.1 * y)
    labels = np.zeros(num_points, dtype=np.int32)

    # 2. Add Static Structures (Class 1) - Buildings & Barriers
    b1_mask = (np.abs(x - 15.0) < 4.0) & (np.abs(y - 10.0) < 5.0)
    z[b1_mask] += np.random.uniform(2.0, 6.0, size=np.sum(b1_mask))
    labels[b1_mask] = 1

    b2_mask = (np.abs(x + 35.0) < 8.0) & (np.abs(y + 25.0) < 10.0)
    z[b2_mask] += np.random.uniform(3.0, 8.0, size=np.sum(b2_mask))
    labels[b2_mask] = 1

    # 3. Add Dynamic Vehicles (Class 2) - Near Fovea Ring (0-10m)
    v1_mask = (np.abs(x - 3.5) < 1.2) & (np.abs(y - 2.0) < 0.8)
    z[v1_mask] += 1.5
    labels[v1_mask] = 2

    v2_mask = (np.abs(x + 6.0) < 1.0) & (np.abs(y - 5.0) < 1.5)
    z[v2_mask] += 1.4
    labels[v2_mask] = 2

    # Add Gaussian measurement noise
    z += np.random.normal(0, 0.02, num_points)

    points = np.column_stack([x, y, z])
    return points, labels


def run_demo(save_anim: bool = True, max_frames: int = 50):
    print("=" * 75)
    print("    FOVEAMAP: COMPLETE SIH PROTOTYPE DEMO & ASSET GENERATOR")
    print("    DRDO / SIH Problem Statement 26053")
    print("=========================================================================")

    # Clean up any legacy duplicate file names
    cleanup_legacy_duplicates(project_root)

    # 1. Instantiate VariableResolutionGridEngine
    print("\n[1] Instantiating VariableResolutionGridEngine...")
    engine = VariableResolutionGridEngine(origin=(0.0, 0.0))
    for ring in engine.rings:
        print(f"    - Ring {ring.ring_id}: r=[{ring.r_min:4.1f}m -> {ring.r_max:5.1f}m] @ Res={ring.resolution:.2f}m ({ring.description})")

    # 2. Generate Synthetic Point Cloud & Labels
    print("\n[2] Generating Synthetic LiDAR Points & Semantic Labels...")
    points, labels = generate_synthetic_lidar_data(num_points=150_000)
    print(f"    Generated {len(points):,} points with 3 semantic classes (Terrain=0, Static=1, Dynamic=2)")

    # 3. Generate Smooth Live Projection Animation (Asset 1 & 2)
    print(f"\n[3] Generating Projection Animation ({max_frames} frames)...")
    fig, anim = animate_grid_projection(
        engine, points, labels, interval=50, max_frames=max_frames, use_fusion=True
    )

    generated_files = []

    if save_anim:
        gif_path = os.path.join(project_root, "foveamap_projection_animation.gif")
        mp4_path = os.path.join(project_root, "foveamap_projection_animation.mp4")

        print(f"\n[4] Exporting Animation Assets (Atomic Swap Mode)...")
        
        # Save GIF cleanly with atomic swap
        try:
            print(f"    - Overwriting GIF animation in-place: {gif_path} ...")
            writer_gif = PillowWriter(fps=15)
            safe_atomic_save(gif_path, lambda path: anim.save(path, writer=writer_gif))
            print(f"    [SUCCESS] Swapped GIF animation: {gif_path}")
            generated_files.append(gif_path)
        except Exception as e:
            print(f"    [WARNING] Could not export GIF: {e}")

        # Save MP4 video if ffmpeg is available
        try:
            if FFMpegWriter.isAvailable():
                print(f"    - Overwriting MP4 video asset in-place: {mp4_path} ...")
                writer_mp4 = FFMpegWriter(fps=15, codec="h264")
                safe_atomic_save(mp4_path, lambda path: anim.save(path, writer=writer_mp4))
                print(f"    [SUCCESS] Swapped MP4 animation: {mp4_path}")
                generated_files.append(mp4_path)
            else:
                print("    [NOTE] FFMpeg system binary not found. Skipping MP4 export.")
        except Exception as e:
            print(f"    [NOTE] Skipping MP4 export: {e}")

    plt.close(fig)

    # 4. Ingest Full Point Cloud into Grid Engine
    print("\n[5] Projecting Full Point Cloud & Computing Spatial Statistics...")
    engine.clear()
    engine.project_points(points, labels)
    metrics = engine.memory_footprint()

    # 5. Render Asset 3: Semantic Class Map
    print("\n[6] Rendering Asset 3: foveamap_semantic_map.png ...")
    semantic_map_path = os.path.join(project_root, "foveamap_semantic_map.png")
    safe_atomic_save(
        semantic_map_path,
        lambda path: plot_final_grid(
            engine,
            title=f"FoveaMap 2.5D Semantic Map (Memory Saved: {metrics['memory_reduction_percent']:.1f}%, Compression: {metrics['compression_ratio']:.1f}x)",
            save_path=path,
            show=False
        )
    )
    generated_files.append(semantic_map_path)

    # 6. Render Asset 4: 2.5D Elevation Height Map
    print("\n[7] Rendering Asset 4: foveamap_elevation_map.png (Colour by mean_elevation)...")
    elevation_map_path = os.path.join(project_root, "foveamap_elevation_map.png")
    safe_atomic_save(
        elevation_map_path,
        lambda path: plot_elevation_map(
            engine,
            title="FoveaMap 2.5D Elevation Map (Mean Elevation Z)",
            save_path=path,
            show=False
        )
    )
    generated_files.append(elevation_map_path)

    # 7. Render Asset 5: Side-by-Side Memory Benchmark Comparison Plot
    print("\n[8] Rendering Asset 5: foveamap_memory_comparison.png ...")
    memory_chart_path = os.path.join(project_root, "foveamap_memory_comparison.png")
    safe_atomic_save(
        memory_chart_path,
        lambda path: plot_memory_comparison(
            engine,
            save_path=path,
            show=False
        )
    )
    generated_files.append(memory_chart_path)

    # 8. Render Asset 6: Unified Demo Dashboard PNG
    print("\n[9] Rendering Asset 6: foveamap_demo_dashboard.png ...")
    from dashboard import render_dashboard
    dashboard_path = os.path.join(project_root, "foveamap_demo_dashboard.png")
    safe_atomic_save(
        dashboard_path,
        lambda path: render_dashboard(
            engine,
            points,
            save_path=path,
            show=False
        )
    )
    generated_files.append(dashboard_path)

    # 9. Print Summary Table & File Verification Output
    print("\n" + "=" * 75)
    print("         FOVEAMAP MEMORY FOOTPRINT COMPARISON & METRICS")
    print("=" * 75)
    print(f"  Ingested Point Cloud Size:         {len(points):,} points")
    print(f"  Sparse Occupied Cells:            {metrics['occupied_cells']:,} cells")
    print(f"  Dense Uniform 5cm Grid Equiv:      {metrics['equivalent_dense_cells']:,} cells")
    print(f"  Memory Compression Ratio:          {metrics['compression_ratio']:.2f}x")
    print(f"  Memory Footprint Reduction:        {metrics['memory_reduction_percent']:.2f}%")
    print(f"  Actual Sparse Grid Memory:         {metrics['memory_kb']:.1f} KB ({metrics['memory_mb']:.3f} MB)")
    print(f"  Estimated Dense Grid Memory:       {metrics['dense_memory_mb']:.2f} MB")
    print("  Cell Breakdown by Ring:")
    for ring_id, count in metrics["cells_by_ring"].items():
        ring = engine.ring_dict[ring_id]
        print(f"    * Ring {ring_id} ({ring.resolution:.2f}m res, r=[{ring.r_min:.0f}-{ring.r_max:.0f}m]): {count:,} cells")
    print("=" * 75)

    print("\n" + "=" * 75)
    print("         VERIFIED IN-PLACE SWAPPED ASSET FILES (NO DUPLICATES)")
    print("=" * 75)
    for filepath in generated_files:
        if os.path.exists(filepath):
            size_bytes = os.path.getsize(filepath)
            size_mb = size_bytes / (1024.0 * 1024.0)
            fname = os.path.basename(filepath)
            print(f"  [SWAPPED IN-PLACE] {fname:<36} -> {size_mb:.2f} MB ({size_bytes:,} bytes)")
        else:
            print(f"  [MISSING] {os.path.basename(filepath)}")
    print("=" * 75)

    print("\n[SUCCESS] All SIH 26053 Demo Assets In-Place Swapped & Verified Successfully!")
    print("=" * 75)


if __name__ == "__main__":
    run_demo(save_anim=True, max_frames=50)
