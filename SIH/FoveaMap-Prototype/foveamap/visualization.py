"""
FoveaMap Visualization Module - 2.5D Grid Rendering, Memory Benchmarking, and Animation
Enhanced for DRDO / SIH Demonstration Video Assets
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
from matplotlib.colors import Normalize
from typing import Optional, Tuple, List, Dict
import sys

from .grid_engine import VariableResolutionGridEngine, RingConfig


# SIH Custom Color Palette
SEMANTIC_COLORS = {
    0: "#2ecc71",  # Terrain: Green
    1: "#e74c3c",  # Static Objects: Grey/Red
    2: "#3498db",  # Dynamic Objects: Blue/Cyan
}

SEMANTIC_NAMES = {
    0: "Terrain (Green)",
    1: "Static Objects (Grey/Red)",
    2: "Dynamic Objects (Blue/Cyan)",
}

RING_COLORS = ["#00ff66", "#ffd700", "#ff8c00", "#ff007f"]  # Lime, Gold, Orange, Magenta


def draw_resolution_rings(ax, engine: VariableResolutionGridEngine, colors: Optional[List[str]] = None):
    """Draw radial multi-ring variable resolution circles on a matplotlib axis."""
    if colors is None:
        colors = RING_COLORS

    for idx, ring in enumerate(engine.rings):
        color = colors[idx % len(colors)]
        circle = patches.Circle(
            engine.origin,
            ring.r_max,
            fill=False,
            linestyle="--",
            linewidth=1.8,
            edgecolor=color,
            alpha=0.85,
            label=f"Ring {ring.ring_id}: {ring.r_min:.0f}-{ring.r_max:.0f}m ({ring.resolution*100:.0f}cm res)"
        )
        ax.add_patch(circle)

    # Origin marker (sensor/robot)
    ax.plot(
        engine.origin[0], engine.origin[1],
        marker="*", markersize=14, color="#ffffff", markeredgecolor="#e74c3c",
        label="Sensor Origin (Fovea)"
    )


def plot_memory_comparison(
    engine: VariableResolutionGridEngine,
    figsize: Tuple[int, int] = (12, 6),
    save_path: Optional[str] = None,
    show: bool = True,
):
    """
    Generate a side-by-side memory footprint comparison plot:
    Uniform 5cm Grid vs. FoveaMap Variable Grid.
    """
    metrics = engine.memory_footprint()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize, facecolor="#181825")
    fig.suptitle("FoveaMap: Memory Efficiency Benchmark Comparison", color="white", fontsize=15, fontweight="bold", y=0.96)

    # Data
    categories = ["Uniform 5cm Grid", "FoveaMap Grid"]
    cell_counts = [metrics["equivalent_dense_cells"] / 1e6, metrics["occupied_cells"] / 1e6]
    memory_mb = [metrics["dense_memory_mb"], metrics["memory_mb"]]
    colors = ["#e74c3c", "#2ecc71"]

    # 1. Bar Chart: Total Active Cells (Millions)
    ax1.set_facecolor("#11111b")
    ax1.set_title("Grid Cell Allocation (Millions of Cells)", color="#cdd6f4", fontsize=12, pad=10)
    bars1 = ax1.bar(categories, cell_counts, color=colors, width=0.55, edgecolor="#313244", linewidth=1.2)
    ax1.set_ylabel("Cells (Millions)", color="#a6adc8")
    ax1.tick_params(colors="#a6adc8")
    ax1.grid(axis="y", linestyle="--", alpha=0.2, color="#a6adc8")

    for bar, val in zip(bars1, cell_counts):
        height = bar.get_height()
        ax1.text(
            bar.get_x() + bar.get_width() / 2.0, height + max(cell_counts) * 0.02,
            f"{val:.2f} M", ha="center", va="bottom", color="white", fontweight="bold", fontsize=11
        )

    # 2. Bar Chart: RAM Memory Footprint (MB)
    ax2.set_facecolor("#11111b")
    ax2.set_title("RAM Memory Footprint (Megabytes)", color="#cdd6f4", fontsize=12, pad=10)
    bars2 = ax2.bar(categories, memory_mb, color=colors, width=0.55, edgecolor="#313244", linewidth=1.2)
    ax2.set_ylabel("RAM Memory (MB)", color="#a6adc8")
    ax2.tick_params(colors="#a6adc8")
    ax2.grid(axis="y", linestyle="--", alpha=0.2, color="#a6adc8")

    for bar, val in zip(bars2, memory_mb):
        height = bar.get_height()
        ax2.text(
            bar.get_x() + bar.get_width() / 2.0, height + max(memory_mb) * 0.02,
            f"{val:.1f} MB", ha="center", va="bottom", color="white", fontweight="bold", fontsize=11
        )

    # Highlight box
    summary_str = (
        f"Memory Reduction: {metrics['memory_reduction_percent']:.2f}%\n"
        f"Compression Ratio: {metrics['compression_ratio']:.1f}x Reduction"
    )
    fig.text(
        0.5, 0.02, summary_str, ha="center", va="bottom",
        color="#2ecc71", fontsize=12, fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.6", facecolor="#1e1e2e", edgecolor="#2ecc71", alpha=0.9)
    )

    plt.tight_layout(rect=[0, 0.08, 1, 0.92])

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight", facecolor=fig.get_facecolor())
        print(f"[FoveaMap] Memory comparison plot saved to: {save_path}")

    if show:
        plt.show()
    else:
        plt.close(fig)


def plot_elevation_map(
    engine: VariableResolutionGridEngine,
    title: str = "FoveaMap: 2.5D Elevation Height Map (Colour by mean elevation)",
    figsize: Tuple[int, int] = (12, 10),
    save_path: Optional[str] = None,
    show: bool = True,
):
    """
    Render a static scatter plot of the final 2.5D map, colored by mean elevation (z_mean).
    """
    fig, ax = plt.subplots(figsize=figsize, facecolor="#181825")
    ax.set_facecolor("#11111b")
    ax.set_title(title, color="white", fontsize=14, fontweight="bold", pad=12)

    r_max = engine.max_range
    ax.set_xlim(engine.origin[0] - r_max * 1.05, engine.origin[0] + r_max * 1.05)
    ax.set_ylim(engine.origin[1] - r_max * 1.05, engine.origin[1] + r_max * 1.05)
    ax.set_xlabel("X (meters)", color="#a6adc8")
    ax.set_ylabel("Y (meters)", color="#a6adc8")
    ax.tick_params(colors="#a6adc8")
    ax.set_aspect('equal')

    # Draw resolution ring boundaries
    draw_resolution_rings(ax, engine)

    all_cells = engine.get_all_cells()
    if all_cells:
        cell_stats = list(all_cells.values()) if isinstance(all_cells, dict) else all_cells
        xs = np.array([c["x_center"] for c in cell_stats])
        ys = np.array([c["y_center"] for c in cell_stats])
        z_means = np.array([c["z_mean"] for c in cell_stats])
        res = np.array([c["resolution"] for c in cell_stats])

        norm_z = Normalize(vmin=np.min(z_means), vmax=np.max(z_means))
        cmap_z = plt.cm.viridis

        # Visually scale marker size inversely with resolution
        sizes = np.clip(70.0 / (res * 10.0), 5.0, 90.0)

        sc = ax.scatter(xs, ys, s=sizes, c=z_means, cmap=cmap_z, norm=norm_z, alpha=0.9, edgecolors="none")
        cbar = fig.colorbar(sc, ax=ax, pad=0.02)
        cbar.set_label("Mean Elevation Z (meters)", color="#a6adc8", fontsize=11)
        cbar.ax.tick_params(colors="#a6adc8")

    ax.legend(loc="upper right", facecolor="#1e1e2e", edgecolor="#45475a", labelcolor="#cdd6f4", fontsize=9)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
        print(f"[FoveaMap] Elevation map saved to: {save_path}")

    if show:
        plt.show()
    else:
        plt.close(fig)


def plot_final_grid(
    engine: VariableResolutionGridEngine,
    title: str = "FoveaMap: Final 2.5D Semantic Map",
    figsize: Tuple[int, int] = (12, 10),
    save_path: Optional[str] = None,
    show: bool = True,
):
    """
    Render a static scatter plot of all occupied grid cells in VariableResolutionGridEngine,
    colored by dominant semantic class with resolution rings.
    """
    fig, ax = plt.subplots(figsize=figsize, facecolor="#181825")
    ax.set_facecolor("#11111b")
    ax.set_title(title, color="white", fontsize=15, fontweight="bold", pad=14)

    r_max = engine.max_range
    ax.set_xlim(engine.origin[0] - r_max * 1.05, engine.origin[0] + r_max * 1.05)
    ax.set_ylim(engine.origin[1] - r_max * 1.05, engine.origin[1] + r_max * 1.05)
    ax.set_xlabel("X (meters)", color="#a6adc8")
    ax.set_ylabel("Y (meters)", color="#a6adc8")
    ax.tick_params(colors="#a6adc8")
    ax.set_aspect('equal')

    # Draw resolution ring boundaries
    draw_resolution_rings(ax, engine)

    all_cells = engine.get_all_cells()
    metrics = engine.memory_footprint()

    if all_cells:
        cell_stats = list(all_cells.values()) if isinstance(all_cells, dict) else all_cells
        xs = np.array([c["x_center"] for c in cell_stats])
        ys = np.array([c["y_center"] for c in cell_stats])
        res = np.array([c["resolution"] for c in cell_stats])
        dom_classes = [c["dominant_class"] for c in cell_stats]
        colors = [SEMANTIC_COLORS.get(cls, "#ffffff") for cls in dom_classes]

        # Visually scale marker size inversely with resolution
        sizes = np.clip(70.0 / (res * 10.0), 5.0, 90.0)

        ax.scatter(xs, ys, s=sizes, c=colors, alpha=0.88, edgecolors="none")

    # Add semantic class legend items
    for cls_id, color in SEMANTIC_COLORS.items():
        ax.scatter([], [], c=color, s=50, label=f"Class {cls_id}: {SEMANTIC_NAMES.get(cls_id, 'Class')}")

    ax.legend(loc="upper right", facecolor="#1e1e2e", edgecolor="#45475a", labelcolor="#cdd6f4", fontsize=9)

    # Metrics annotation box
    metrics_str = (
        f"Sparse Occupied Cells: {metrics['occupied_cells']:,}\n"
        f"Dense 5cm Grid Equiv:  {metrics['equivalent_dense_cells']:,}\n"
        f"Memory Footprint:      {metrics['memory_kb']:.1f} KB ({metrics['memory_mb']:.3f} MB)\n"
        f"Compression Ratio:     {metrics['compression_ratio']:.1f}x\n"
        f"Memory Saved:          {metrics['memory_reduction_percent']:.2f}%"
    )
    ax.text(
        0.02, 0.98, metrics_str, transform=ax.transAxes,
        verticalalignment='top', horizontalalignment='left',
        color="white", fontsize=10, fontfamily="monospace",
        bbox=dict(boxstyle="round,pad=0.5", facecolor="#1e1e2e", edgecolor="#45475a", alpha=0.9)
    )

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
        print(f"[FoveaMap] Static grid map plot saved to: {save_path}")

    if show:
        plt.show()
    else:
        plt.close(fig)


def animate_grid_projection(
    engine: VariableResolutionGridEngine,
    points: np.ndarray,
    labels: Optional[np.ndarray] = None,
    interval: int = 40,
    max_frames: int = 60,
    use_fusion: bool = True,
    figsize: Tuple[int, int] = (12, 10),
) -> Tuple[plt.Figure, FuncAnimation]:
    """
    Create a high-quality, smooth Matplotlib FuncAnimation visualizing the progressive 
    projection of LiDAR points into the VariableResolutionGridEngine.
    """
    engine.clear()

    fig, ax = plt.subplots(figsize=figsize, facecolor="#181825")
    ax.set_facecolor("#11111b")
    ax.set_title("FoveaMap – Variable Resolution 2.5D Grid Engine", color="white", fontsize=15, fontweight="bold", pad=14)

    r_max = engine.max_range
    ax.set_xlim(engine.origin[0] - r_max * 1.05, engine.origin[0] + r_max * 1.05)
    ax.set_ylim(engine.origin[1] - r_max * 1.05, engine.origin[1] + r_max * 1.05)
    ax.set_xlabel("X (meters)", color="#a6adc8")
    ax.set_ylabel("Y (meters)", color="#a6adc8")
    ax.tick_params(colors="#a6adc8")
    ax.set_aspect('equal')

    # Draw static resolution rings
    draw_resolution_rings(ax, engine)

    # Dynamic scatter elements
    raw_points_scatter = ax.scatter([], [], s=3, color="#6c7086", alpha=0.30, label="Raw Point Cloud")
    occupied_cells_scatter = ax.scatter([], [], s=[], c=[], alpha=0.92, edgecolors="none")

    # Metrics text box
    metrics_text = ax.text(
        0.02, 0.98, "", transform=ax.transAxes,
        verticalalignment='top', horizontalalignment='left',
        color="white", fontsize=10, fontfamily="monospace",
        bbox=dict(boxstyle="round,pad=0.5", facecolor="#1e1e2e", edgecolor="#45475a", alpha=0.9)
    )

    # Semantic legend
    for cls_id, color in SEMANTIC_COLORS.items():
        ax.scatter([], [], c=color, s=40, label=f"Class {cls_id}: {SEMANTIC_NAMES.get(cls_id, 'Class')}")

    ax.legend(loc="upper right", facecolor="#1e1e2e", edgecolor="#45475a", labelcolor="#cdd6f4", fontsize=9)

    num_pts = len(points)
    pts_per_frame = max(1, int(np.ceil(num_pts / max_frames)))
    state = {"total_projected": 0}

    def update(frame: int):
        start_idx = frame * pts_per_frame
        end_idx = min(num_pts, (frame + 1) * pts_per_frame)

        if start_idx < end_idx:
            chunk_pts = points[start_idx:end_idx]
            chunk_lbls = labels[start_idx:end_idx] if labels is not None else None
            
            if use_fusion:
                engine.fuse_frame(chunk_pts, chunk_lbls, decay=0.92)
            else:
                engine.project_points(chunk_pts, chunk_lbls)
                
            state["total_projected"] += len(chunk_pts)

        all_cells = engine.get_all_cells()
        metrics = engine.memory_footprint()

        if all_cells:
            cell_stats = list(all_cells.values()) if isinstance(all_cells, dict) else all_cells
            xs = [c["x_center"] for c in cell_stats]
            ys = [c["y_center"] for c in cell_stats]
            res = np.array([c["resolution"] for c in cell_stats])
            dom_classes = [c["dominant_class"] for c in cell_stats]
            colors = [SEMANTIC_COLORS.get(cls, "#ffffff") for cls in dom_classes]

            sizes = np.clip(65.0 / (res * 10.0), 4.0, 80.0)

            occupied_cells_scatter.set_offsets(np.column_stack([xs, ys]))
            occupied_cells_scatter.set_color(colors)
            occupied_cells_scatter.set_sizes(sizes)

            recent_pts = points[:min(num_pts, (frame + 1) * pts_per_frame):3]
            raw_points_scatter.set_offsets(recent_pts[:, :2])

        text = (
            f"Sweep Frame:      {frame + 1}/{max_frames}\n"
            f"Points Projected: {state['total_projected']:,}\n"
            f"Occupied Cells:   {metrics['occupied_cells']:,}\n"
            f"Memory Footprint: {metrics['memory_kb']:.1f} KB ({metrics['memory_mb']:.3f} MB)\n"
            f"Compression:      {metrics['compression_ratio']:.1f}x ({metrics['memory_reduction_percent']:.1f}% saved)"
        )
        metrics_text.set_text(text)

        return raw_points_scatter, occupied_cells_scatter, metrics_text

    anim = FuncAnimation(fig, update, frames=max_frames, interval=interval, blit=False, repeat=False)
    plt.tight_layout()

    return fig, anim


class FoveaVisualizer:
    """Wrapper adapting FoveaVisualizer interface for VariableResolutionGridEngine."""
    def __init__(self, grid):
        self.grid = grid

    def render_overview(self, title="FoveaMap 2.5D Grid", save_path=None, show=True, **kwargs):
        plot_final_grid(self.grid, title=title, save_path=save_path, show=show)
