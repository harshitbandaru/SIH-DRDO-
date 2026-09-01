"""
FoveaMap Prototype Professional Demo Dashboard Generator
DRDO / SIH Problem Statement 26053

Renders a unified multi-panel dashboard displaying:
1. 2.5D Semantic Class Map (Terrain, Static, Dynamic)
2. 2.5D Elevation Height Map (Mean Elevation Z)
3. Memory Efficiency Benchmark Bar Chart
4. Grid Engine System Metrics & Resolution Schedule Summary
"""

import os
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.colors import Normalize
from typing import Optional

# Ensure project root is in sys.path
project_root = os.path.abspath(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from foveamap.grid_engine import VariableResolutionGridEngine
from foveamap.visualization import (
    draw_resolution_rings,
    SEMANTIC_COLORS,
    SEMANTIC_NAMES,
)
from foveamap.demo import generate_synthetic_lidar_data


def render_dashboard(
    engine: VariableResolutionGridEngine,
    points: np.ndarray,
    save_path: Optional[str] = None,
    show: bool = False,
):
    """
    Renders the complete FoveaMap Demo Dashboard figure with 4 visual panels.
    """
    fig = plt.figure(figsize=(18, 14), facecolor="#181825")
    fig.suptitle(
        "FoveaMap – Adaptive Variable Resolution 2.5D LiDAR Mapping | SIH 26053",
        color="white", fontsize=18, fontweight="bold", y=0.96
    )

    all_cells = engine.get_all_cells()
    metrics = engine.memory_footprint()
    cell_stats = list(all_cells.values()) if isinstance(all_cells, dict) else all_cells

    xs = np.array([c["x_center"] for c in cell_stats])
    ys = np.array([c["y_center"] for c in cell_stats])
    z_means = np.array([c["z_mean"] for c in cell_stats])
    res = np.array([c["resolution"] for c in cell_stats])
    dom_classes = [c["dominant_class"] for c in cell_stats]
    colors_sem = [SEMANTIC_COLORS.get(cls, "#ffffff") for cls in dom_classes]

    r_max = engine.max_range

    # =========================================================================
    # Panel 1: 2.5D Semantic Map (Top-Left)
    # =========================================================================
    ax1 = fig.add_subplot(221, facecolor="#11111b")
    ax1.set_title("1. 2.5D Semantic Map (Terrain / Static / Dynamic)", color="#cdd6f4", fontsize=13, pad=10)
    ax1.set_xlim(engine.origin[0] - r_max * 1.05, engine.origin[0] + r_max * 1.05)
    ax1.set_ylim(engine.origin[1] - r_max * 1.05, engine.origin[1] + r_max * 1.05)
    ax1.set_xlabel("X (meters)", color="#a6adc8")
    ax1.set_ylabel("Y (meters)", color="#a6adc8")
    ax1.tick_params(colors="#a6adc8")
    ax1.set_aspect('equal')

    draw_resolution_rings(ax1, engine)

    sizes_sem = np.clip(65.0 / (res * 10.0), 4.0, 80.0)
    ax1.scatter(xs, ys, s=sizes_sem, c=colors_sem, alpha=0.88, edgecolors="none")

    for cls_id, color in SEMANTIC_COLORS.items():
        ax1.scatter([], [], c=color, s=40, label=f"Class {cls_id}: {SEMANTIC_NAMES.get(cls_id, 'Class')}")

    ax1.legend(loc="upper right", facecolor="#1e1e2e", edgecolor="#45475a", labelcolor="#cdd6f4", fontsize=8.5)

    # =========================================================================
    # Panel 2: 2.5D Elevation Map (Top-Right)
    # =========================================================================
    ax2 = fig.add_subplot(222, facecolor="#11111b")
    ax2.set_title("2. 2.5D Elevation Height Map (Mean Elevation Z)", color="#cdd6f4", fontsize=13, pad=10)
    ax2.set_xlim(engine.origin[0] - r_max * 1.05, engine.origin[0] + r_max * 1.05)
    ax2.set_ylim(engine.origin[1] - r_max * 1.05, engine.origin[1] + r_max * 1.05)
    ax2.set_xlabel("X (meters)", color="#a6adc8")
    ax2.set_ylabel("Y (meters)", color="#a6adc8")
    ax2.tick_params(colors="#a6adc8")
    ax2.set_aspect('equal')

    draw_resolution_rings(ax2, engine)

    norm_z = Normalize(vmin=np.min(z_means), vmax=np.max(z_means))
    cmap_z = plt.cm.viridis

    sc2 = ax2.scatter(xs, ys, s=sizes_sem, c=z_means, cmap=cmap_z, norm=norm_z, alpha=0.9, edgecolors="none")
    cbar2 = fig.colorbar(sc2, ax=ax2, pad=0.02)
    cbar2.set_label("Mean Elevation Z (meters)", color="#a6adc8", fontsize=10)
    cbar2.ax.tick_params(colors="#a6adc8")

    ax2.legend(loc="upper right", facecolor="#1e1e2e", edgecolor="#45475a", labelcolor="#cdd6f4", fontsize=8.5)

    # =========================================================================
    # Panel 3: Memory Efficiency Benchmark (Bottom-Left)
    # =========================================================================
    ax3_1 = fig.add_subplot(245, facecolor="#11111b")
    ax3_2 = fig.add_subplot(246, facecolor="#11111b")

    categories = ["Uniform 5cm", "FoveaMap"]
    cell_counts = [metrics["equivalent_dense_cells"] / 1e6, metrics["occupied_cells"] / 1e6]
    memory_mb = [metrics["dense_memory_mb"], metrics["memory_mb"]]
    colors_bar = ["#e74c3c", "#2ecc71"]

    # Bar 1: Cell Allocation
    ax3_1.set_title("Grid Cells (Millions)", color="#cdd6f4", fontsize=11, pad=8)
    bars1 = ax3_1.bar(categories, cell_counts, color=colors_bar, width=0.55, edgecolor="#313244", linewidth=1.2)
    ax3_1.set_ylabel("Cells (M)", color="#a6adc8")
    ax3_1.tick_params(colors="#a6adc8")
    ax3_1.grid(axis="y", linestyle="--", alpha=0.2, color="#a6adc8")
    for bar, val in zip(bars1, cell_counts):
        height = bar.get_height()
        ax3_1.text(bar.get_x() + bar.get_width() / 2.0, height + max(cell_counts) * 0.02,
                   f"{val:.2f} M", ha="center", va="bottom", color="white", fontweight="bold", fontsize=9.5)

    # Bar 2: Memory Footprint
    ax3_2.set_title("RAM Footprint (MB)", color="#cdd6f4", fontsize=11, pad=8)
    bars2 = ax3_2.bar(categories, memory_mb, color=colors_bar, width=0.55, edgecolor="#313244", linewidth=1.2)
    ax3_2.set_ylabel("RAM (MB)", color="#a6adc8")
    ax3_2.tick_params(colors="#a6adc8")
    ax3_2.grid(axis="y", linestyle="--", alpha=0.2, color="#a6adc8")
    for bar, val in zip(bars2, memory_mb):
        height = bar.get_height()
        ax3_2.text(bar.get_x() + bar.get_width() / 2.0, height + max(memory_mb) * 0.02,
                   f"{val:.1f} MB", ha="center", va="bottom", color="white", fontweight="bold", fontsize=9.5)

    # =========================================================================
    # Panel 4: System Metrics & Resolution Schedule Card (Bottom-Right)
    # =========================================================================
    ax4 = fig.add_subplot(224, facecolor="#11111b")
    ax4.axis("off")

    card_text = (
        "[METRICS] SYSTEM METRICS & RESOLUTION SCHEDULE\n"
        "────────────────────────────────────────────────────────────\n"
        f"• Ingested LiDAR Point Cloud:     {len(points):,} points\n"
        f"• Fovea Sensor Center:            {tuple(engine.origin)} m\n"
        f"• Max Perception Boundary:        {engine.max_range:.0f} meters\n\n"
        "RADIAL MULTI-RING RESOLUTION SCHEDULE:\n"
        f"  - Ring 0 (Fovea High-Res):      0.0m - 10.0m  @  5 cm cell res ({metrics['cells_by_ring'].get(0, 0):,} cells)\n"
        f"  - Ring 1 (Mid-Res Inner):       10.0m - 30.0m @ 15 cm cell res ({metrics['cells_by_ring'].get(1, 0):,} cells)\n"
        f"  - Ring 2 (Coarse Outer):        30.0m - 100m  @ 50 cm cell res ({metrics['cells_by_ring'].get(2, 0):,} cells)\n\n"
        "PERFORMANCE BENCHMARK SUMMARY:\n"
        f"  - Sparse Occupied Cells:        {metrics['occupied_cells']:,} cells\n"
        f"  - Equivalent Dense 5cm Cells:   {metrics['equivalent_dense_cells']:,} cells\n"
        f"  - Memory Compression Ratio:     {metrics['compression_ratio']:.2f}x Reduction\n"
        f"  - Memory Footprint Saved:       {metrics['memory_reduction_percent']:.2f}%\n"
        f"  - Actual Sparse RAM Usage:      {metrics['memory_mb']:.2f} MB (vs {metrics['dense_memory_mb']:.2f} MB dense)\n"
        "────────────────────────────────────────────────────────────\n"
        "Target Platform: Off-Road Tactical UGV Edge Intelligence (Pure NumPy)"
    )

    ax4.text(
        0.05, 0.95, card_text, transform=ax4.transAxes,
        verticalalignment='top', horizontalalignment='left',
        color="#cdd6f4", fontsize=10, fontfamily="monospace",
        bbox=dict(boxstyle="round,pad=0.8", facecolor="#1e1e2e", edgecolor="#3498db", linewidth=1.5, alpha=0.95)
    )

    plt.tight_layout(rect=[0, 0.02, 1, 0.94])

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
        print(f"[FoveaMap] Saved Demo Dashboard image to: {save_path}")

    if show:
        plt.show()
    else:
        plt.close(fig)


def run_dashboard_demo():
    print("=" * 75)
    print("    FOVEAMAP DEMO DASHBOARD GENERATOR | SIH 26053")
    print("=========================================================================")

    # 1. Instantiate VariableResolutionGridEngine
    print("\n[1] Instantiating VariableResolutionGridEngine...")
    engine = VariableResolutionGridEngine(origin=(0.0, 0.0))

    # 2. Generate Synthetic Point Cloud
    print("\n[2] Ingesting Synthetic 3D LiDAR Point Cloud (150,000 points)...")
    points, labels = generate_synthetic_lidar_data(num_points=150_000, seed=42)
    engine.project_points(points, labels)

    # 3. Render Dashboard with Atomic In-Place Swap
    print("\n[3] Rendering Multi-Panel Demo Dashboard (Atomic In-Place Swap)...")
    from foveamap.demo import safe_atomic_save
    dashboard_path = os.path.join(project_root, "foveamap_demo_dashboard.png")
    safe_atomic_save(
        dashboard_path,
        lambda path: render_dashboard(engine, points, save_path=path, show=False)
    )

    # 4. Verify Output File
    print("\n[4] Verifying Output File...")
    if os.path.exists(dashboard_path):
        size_bytes = os.path.getsize(dashboard_path)
        size_mb = size_bytes / (1024.0 * 1024.0)
        print(f"  [SWAPPED IN-PLACE] Generated: foveamap_demo_dashboard.png ({size_mb:.2f} MB / {size_bytes:,} bytes)")
    else:
        print("  [ERROR] Dashboard file was not created!")
        sys.exit(1)

    print("\n[SUCCESS] FoveaMap Demo Dashboard Execution Complete!")
    print("=" * 75)


if __name__ == "__main__":
    run_dashboard_demo()
