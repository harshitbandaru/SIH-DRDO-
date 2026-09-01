"""
FoveaMap Variable Resolution Grid Engine
Core Adaptive 2.5D Lidar Mapping Module for DRDO / SIH 26053
"""

import sys
import numpy as np
from typing import Dict, List, Tuple, Optional, Union
from dataclasses import dataclass, field


class RingConfig:
    """Configuration for a radial resolution ring in the grid."""
    
    def __init__(
        self,
        ring_id: int,
        resolution: float = 0.1,
        r_min: float = 0.0,
        r_max: Optional[float] = None,
        radius: Optional[float] = None,
        description: str = "",
    ):
        self.ring_id = ring_id
        self.resolution = resolution
        self.r_min = r_min
        if radius is not None:
            self.r_max = radius
        elif r_max is not None:
            self.r_max = r_max
        else:
            self.r_max = 100.0
        self.description = description

    @property
    def radius(self) -> float:
        return self.r_max

    @radius.setter
    def radius(self, val: float):
        self.r_max = val

    @property
    def level_id(self) -> int:
        return self.ring_id

    @level_id.setter
    def level_id(self, val: int):
        self.ring_id = val


# Alias for backward compatibility with earlier prototypes
MultiResLevel = RingConfig


@dataclass
class MapBounds:
    """Spatial bounding box for rendering / compatibility."""
    x_min: float = -100.0
    x_max: float = 100.0
    y_min: float = -100.0
    y_max: float = 100.0

    @property
    def width(self) -> float:
        return self.x_max - self.x_min

    @property
    def height(self) -> float:
        return self.y_max - self.y_min


class VariableResolutionGridEngine:
    """
    Adaptive Variable Resolution 2.5D Lidar Grid Engine.
    
    Features:
    - Radial multi-ring variable spatial resolution (e.g. 0-10m @ 5cm, 10-30m @ 15cm, 30-100m @ 50cm).
    - Sparse hash storage indexed by (ring_id, i, j) tuples.
    - Online accumulation of elevation statistics (mean, min, max, variance).
    - Semantic probability layers (3 classes: terrain=0, static obstacle=1, dynamic obstacle=2).
    - Safe filtering of points out of range.
    - Pure NumPy + Python standard library implementation.
    """

    DEFAULT_RINGS = [
        RingConfig(ring_id=0, r_min=0.0, r_max=10.0, resolution=0.05, description="Fovea High-Res (5cm)"),
        RingConfig(ring_id=1, r_min=10.0, r_max=30.0, resolution=0.15, description="Mid-Res Ring (15cm)"),
        RingConfig(ring_id=2, r_min=30.0, r_max=100.0, resolution=0.50, description="Coarse Outer Ring (50cm)"),
    ]

    SEMANTIC_CLASSES = {0: "terrain", 1: "static", 2: "dynamic"}

    def __init__(
        self,
        rings: Optional[List[RingConfig]] = None,
        origin: Tuple[float, float] = (0.0, 0.0),
        num_classes: int = 3,
    ):
        """
        Initialize the Variable Resolution Grid Engine.

        Parameters:
            rings: List of RingConfig specifying radial resolution bands.
            origin: (x, y) center of the radial grid (e.g., sensor/robot position).
            num_classes: Number of semantic classes (default 3: terrain=0, static=1, dynamic=2).
        """
        if rings is None:
            self.rings = sorted(self.DEFAULT_RINGS, key=lambda r: r.ring_id)
        else:
            self.rings = sorted(rings, key=lambda r: r.ring_id)

        self.origin = np.array(origin, dtype=np.float64)
        self.num_classes = num_classes

        # Calculate max range from outermost ring
        self.max_range = max(r.r_max for r in self.rings)
        self.min_range = min(r.r_min for r in self.rings)

        # Lookup mapping for ring objects by ID
        self.ring_dict: Dict[int, RingConfig] = {r.ring_id: r for r in self.rings}

        # Sparse storage mapping: (ring_id, i, j) -> cell dict
        # cell dict structure:
        # {
        #   'count': int,
        #   'z_sum': float,
        #   'z_sq_sum': float,
        #   'z_min': float,
        #   'z_max': float,
        #   'semantic_counts': np.ndarray (shape: (num_classes,))
        # }
        self.cells: Dict[Tuple[int, int, int], dict] = {}

    def set_origin(self, origin_x: float, origin_y: float):
        """Update the center origin of the radial multi-ring grid."""
        self.origin = np.array([origin_x, origin_y], dtype=np.float64)

    def clear(self):
        """Reset and clear all grid cell data."""
        self.cells.clear()

    def project_points(
        self,
        points: np.ndarray,
        labels: Optional[np.ndarray] = None
    ):
        """
        Project 3D LiDAR point cloud into the sparse variable-resolution 2.5D grid.

        Parameters:
            points: NumPy array of shape (N, 3) or (N, 4) with (x, y, z, [intensity/label]).
            labels: Optional 1D NumPy array of shape (N,) with integer class labels
                    (0: terrain, 1: static, 2: dynamic).
        """
        if points is None or len(points) == 0:
            return

        # Ensure 2D NumPy array
        pts = np.asarray(points, dtype=np.float64)
        if pts.ndim != 2 or pts.shape[1] < 3:
            raise ValueError("points must be a 2D array of shape (N, 3) or (N, 4)")

        xyz = pts[:, :3]

        # Extract semantic labels if provided or embedded in 4th column
        if labels is not None:
            sem_labels = np.asarray(labels, dtype=np.int32)
        elif pts.shape[1] >= 4:
            sem_labels = pts[:, 3].astype(np.int32)
        else:
            sem_labels = np.zeros(len(xyz), dtype=np.int32)  # Default class 0 (terrain)

        # 1. Safe handling & Filtering: drop NaNs, Infs, out of range
        valid_mask = np.isfinite(xyz).all(axis=1) & (sem_labels >= 0) & (sem_labels < self.num_classes)
        xyz = xyz[valid_mask]
        sem_labels = sem_labels[valid_mask]

        if len(xyz) == 0:
            return

        # Compute radial distance from origin
        dx = xyz[:, 0] - self.origin[0]
        dy = xyz[:, 1] - self.origin[1]
        dist = np.hypot(dx, dy)

        # Filter points within [min_range, max_range]
        range_mask = (dist >= self.min_range) & (dist <= self.max_range)
        xyz = xyz[range_mask]
        dx = dx[range_mask]
        dy = dy[range_mask]
        dist = dist[range_mask]
        sem_labels = sem_labels[range_mask]

        if len(xyz) == 0:
            return

        # 2. Assign points to resolution rings
        for ring in self.rings:
            # Points falling into [r_min, r_max) of this ring
            if ring == self.rings[-1]:
                ring_mask = (dist >= ring.r_min) & (dist <= ring.r_max)
            else:
                ring_mask = (dist >= ring.r_min) & (dist < ring.r_max)

            if not np.any(ring_mask):
                continue

            r_dx = dx[ring_mask]
            r_dy = dy[ring_mask]
            r_z = xyz[ring_mask, 2]
            r_labels = sem_labels[ring_mask]
            res = ring.resolution

            # Calculate 2D cell indices relative to origin
            i_indices = np.floor(r_dx / res).astype(np.int32)
            j_indices = np.floor(r_dy / res).astype(np.int32)

            # Ingest points into cells
            for k in range(len(r_z)):
                key = (ring.ring_id, int(i_indices[k]), int(j_indices[k]))
                z_val = r_z[k]
                lbl = int(r_labels[k])

                if key not in self.cells:
                    sem_counts = np.zeros(self.num_classes, dtype=np.int32)
                    sem_counts[lbl] = 1
                    self.cells[key] = {
                        "count": 1,
                        "z_sum": z_val,
                        "z_sq_sum": z_val * z_val,
                        "z_min": z_val,
                        "z_max": z_val,
                        "semantic_counts": sem_counts,
                    }
                else:
                    cell = self.cells[key]
                    cell["count"] += 1
                    cell["z_sum"] += z_val
                    cell["z_sq_sum"] += z_val * z_val
                    if z_val < cell["z_min"]:
                        cell["z_min"] = z_val
                    if z_val > cell["z_max"]:
                        cell["z_max"] = z_val
                    cell["semantic_counts"][lbl] += 1

    def fuse_frame(
        self,
        points: np.ndarray,
        labels: Optional[np.ndarray] = None,
        decay: float = 0.85
    ):
        """
        Temporal Fusion Stub: Accumulate and decay point cloud measurements over 
        consecutive LiDAR sweeps / video frames.

        Parameters:
            points: Array of (N, 3) or (N, 4) points for the current frame.
            labels: Optional (N,) array of integer semantic labels.
            decay: Temporal decay factor for previous observations [0.0 - 1.0].
        """
        # Apply temporal decay to existing cell observation counts and height sums
        for cell in self.cells.values():
            cell["count"] = max(1, int(cell["count"] * decay))
            cell["z_sum"] *= decay
            cell["z_sq_sum"] *= decay
            cell["semantic_counts"] = np.maximum(0, (cell["semantic_counts"] * decay).astype(np.int32))

        # Project current frame points into grid
        self.project_points(points, labels)

    def get_cell_stats(self, ring_id: int, i: int, j: int) -> Optional[dict]:
        """
        Retrieve calculated statistics for a specific sparse cell key (ring_id, i, j).

        Returns None if cell is empty / not occupied.
        """
        key = (ring_id, i, j)
        if key not in self.cells:
            return None

        ring = self.ring_dict.get(ring_id)
        if ring is None:
            return None

        cell = self.cells[key]
        cnt = cell["count"]
        z_mean = cell["z_sum"] / cnt
        z_var = max(0.0, (cell["z_sq_sum"] / cnt) - (z_mean * z_mean))

        # Compute semantic class probabilities
        sem_counts = cell["semantic_counts"]
        sem_probs = sem_counts / cnt
        dominant_class = int(np.argmax(sem_probs))

        # World coordinates of cell center
        res = ring.resolution
        x_center = self.origin[0] + (i + 0.5) * res
        y_center = self.origin[1] + (j + 0.5) * res

        return {
            "ring_id": ring_id,
            "i": i,
            "j": j,
            "x_center": x_center,
            "y_center": y_center,
            "resolution": res,
            "count": cnt,
            "z_mean": z_mean,
            "z_min": cell["z_min"],
            "z_max": cell["z_max"],
            "z_variance": z_var,
            "z_std": np.sqrt(z_var),
            "semantic_counts": sem_counts.copy(),
            "semantic_probs": sem_probs.copy(),
            "dominant_class": dominant_class,
            "dominant_label": self.SEMANTIC_CLASSES.get(dominant_class, "unknown"),
        }

    def get_all_cells(self) -> Dict[Tuple[int, int, int], dict]:
        """
        Return a dictionary of statistics for all non-empty cells in the sparse grid.
        
        Returns:
            Dict mapping (ring_id, i, j) -> cell_stats dict.
        """
        result = {}
        for key in self.cells.keys():
            stats = self.get_cell_stats(key[0], key[1], key[2])
            if stats is not None:
                result[key] = stats
        return result

    def memory_footprint(self) -> dict:
        """
        Calculate actual memory footprint of the sparse grid and compare 
        with an equivalent dense grid spanning max_range at finest resolution.
        """
        num_occupied_cells = len(self.cells)

        # Estimate python object memory footprint in bytes
        # Dict overhead + keys tuple + inner dict + numpy arrays
        bytes_per_cell = (
            sys.getsizeof((0, 0, 0)) +  # Key tuple ~ 64B
            sys.getsizeof({}) +           # Inner dict ~ 232B
            sys.getsizeof(np.zeros(3, dtype=np.int32)) +  # NumPy array ~ 112B
            64                            # Primitive numerical values
        )
        total_memory_bytes = sys.getsizeof(self.cells) + (num_occupied_cells * bytes_per_cell)
        total_memory_kb = total_memory_bytes / 1024.0
        total_memory_mb = total_memory_kb / 1024.0

        # Dense equivalent grid calculation at finest resolution (Ring 0)
        finest_res = self.rings[0].resolution
        dense_dim = int(np.ceil((2.0 * self.max_range) / finest_res))
        total_dense_cells = dense_dim * dense_dim

        # Assuming dense grid float32/64 representation (~64 bytes per cell)
        dense_memory_bytes = total_dense_cells * 64
        dense_memory_mb = dense_memory_bytes / (1024.0 * 1024.0)

        compression_ratio = total_dense_cells / max(1, num_occupied_cells)
        reduction_percent = max(0.0, (1.0 - (num_occupied_cells / total_dense_cells)) * 100.0)

        cells_by_ring = {r.ring_id: 0 for r in self.rings}
        for (r_id, _, _) in self.cells.keys():
            if r_id in cells_by_ring:
                cells_by_ring[r_id] += 1

        return {
            "occupied_cells": num_occupied_cells,
            "equivalent_dense_cells": total_dense_cells,
            "finest_resolution_m": finest_res,
            "max_range_m": self.max_range,
            "memory_bytes": total_memory_bytes,
            "memory_kb": total_memory_kb,
            "memory_mb": total_memory_mb,
            "dense_memory_mb": dense_memory_mb,
            "compression_ratio": compression_ratio,
            "memory_reduction_percent": reduction_percent,
            "cells_by_ring": cells_by_ring,
        }


# Legacy wrapper class for backward compatibility with existing visualization and demo scripts
class FoveaGrid25D(VariableResolutionGridEngine):
    """Compatibility wrapper adapting VariableResolutionGridEngine to legacy interface."""

    def __init__(self, bounds: Optional[MapBounds] = None, fovea_center: Tuple[float, float] = (0.0, 0.0), levels=None):
        rings = None
        if levels is not None:
            rings = [
                RingConfig(ring_id=l.level_id if hasattr(l, 'level_id') else i,
                           r_min=0.0 if i == 0 else levels[i-1].radius if hasattr(levels[i-1], 'radius') else 0.0,
                           r_max=l.radius if hasattr(l, 'radius') else 100.0,
                           resolution=l.resolution if hasattr(l, 'resolution') else 0.1,
                           description=getattr(l, 'description', ''))
                for i, l in enumerate(levels)
            ]
        super().__init__(rings=rings, origin=fovea_center)
        self.bounds = bounds or MapBounds()

    @property
    def fovea_center(self):
        return self.origin

    @fovea_center.setter
    def fovea_center(self, val):
        self.set_origin(val[0], val[1])

    @property
    def levels(self):
        return self.rings

    def add_point_cloud(self, points: np.ndarray):
        self.project_points(points)

    def get_all_cells(self) -> List[dict]:
        """Returns cell list matching legacy output format."""
        cells_dict = super().get_all_cells()
        cell_list = []
        for (r_id, i, j), stats in cells_dict.items():
            cell_list.append({
                "x": stats["x_center"],
                "y": stats["y_center"],
                "cell_x": i,
                "cell_y": j,
                "z_max": stats["z_max"],
                "z_min": stats["z_min"],
                "z_mean": stats["z_mean"],
                "roughness": stats["z_std"],
                "count": stats["count"],
                "resolution": stats["resolution"],
                "level": r_id,
            })
        return cell_list

    def query_point(self, x: float, y: float) -> Optional[dict]:
        """Legacy spatial point query interface."""
        dx = x - self.origin[0]
        dy = y - self.origin[1]
        dist = np.hypot(dx, dy)
        ring = None
        for r in self.rings:
            if dist <= r.r_max:
                ring = r
                break
        if ring is None:
            ring = self.rings[-1]

        i = int(np.floor(dx / ring.resolution))
        j = int(np.floor(dy / ring.resolution))

        stats = self.get_cell_stats(ring.ring_id, i, j)
        if stats is not None:
            return {
                "x": x,
                "y": y,
                "z_max": stats["z_max"],
                "z_min": stats["z_min"],
                "z_mean": stats["z_mean"],
                "roughness": stats["z_std"],
                "resolution": stats["resolution"],
                "level": ring.ring_id,
            }
        return None

    def compute_metrics(self) -> dict:
        m = self.memory_footprint()
        return {
            "total_active_cells": m["occupied_cells"],
            "equivalent_uniform_cells": m["equivalent_dense_cells"],
            "fovea_resolution": m["finest_resolution_m"],
            "cells_per_level": m["cells_by_ring"],
            "memory_reduction_percent": m["memory_reduction_percent"],
            "compression_ratio": m["compression_ratio"],
        }


# =====================================================================
# Full Working __main__ Test Block
# =====================================================================
if __name__ == "__main__":
    print("=" * 70)
    print("      VARIABLE RESOLUTION GRID ENGINE (FOVEAMAP) - TEST")
    print("=" * 70)

    # 1. Instantiate engine with default 3-ring radial resolution configuration
    engine = VariableResolutionGridEngine(origin=(0.0, 0.0))
    
    print("\n[1] Configured Radial Multi-Ring Hierarchy:")
    for ring in engine.rings:
        print(f"    - Ring {ring.ring_id}: [{ring.r_min:5.1f}m -> {ring.r_max:5.1f}m] @ Res = {ring.resolution:.2f}m ({ring.description})")

    # 2. Generate Synthetic 3D Point Cloud with Semantic Labels
    np.random.seed(42)
    num_points = 250_000

    print(f"\n[2] Generating {num_points:,} synthetic 3D LiDAR points with semantic labels...")
    
    # Random polar coordinates up to 120m (some outside max_range 100m to test safe filtering)
    r = np.random.uniform(0.0, 120.0, num_points)
    theta = np.random.uniform(0.0, 2 * np.pi, num_points)

    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    # Elevation: terrain surface + height variation + noise
    z = 0.05 * x - 0.02 * y + np.random.normal(0.0, 0.03, num_points)

    # Synthetic semantic labels (0: terrain, 1: static obstacle, 2: dynamic vehicle)
    labels = np.zeros(num_points, dtype=np.int32)
    
    # Add a static building structure (class 1) around (r=20m, theta=0.5 rad)
    static_mask = (np.abs(x - 18.0) < 3.0) & (np.abs(y - 8.0) < 3.0)
    z[static_mask] += 3.5
    labels[static_mask] = 1

    # Add a moving vehicle (class 2) inside fovea ring around (x=4m, y=3m)
    dynamic_mask = (np.abs(x - 4.0) < 1.2) & (np.abs(y - 3.0) < 1.2)
    z[dynamic_mask] += 1.6
    labels[dynamic_mask] = 2

    # Add out-of-bounds/corrupted points to test safe filtering
    x[0] = np.nan
    y[1] = np.inf
    labels[2] = 999  # invalid label

    points_3d = np.column_stack([x, y, z])

    # 3. Project points into the sparse multi-resolution grid
    print("\n[3] Projecting points into VariableResolutionGridEngine...")
    engine.project_points(points_3d, labels=labels)

    # 4. Measure & Print Memory Footprint and Occupied Cell Statistics
    metrics = engine.memory_footprint()
    
    print("\n[4] Occupied Cells & Memory Usage Report:")
    print("    ---------------------------------------------------")
    print(f"    Total Ingested Points:              {num_points:,}")
    print(f"    Occupied Sparse Cells:              {metrics['occupied_cells']:,}")
    print(f"    Equivalent Dense Cells (5cm Grid):   {metrics['equivalent_dense_cells']:,}")
    print(f"    Compression Ratio:                  {metrics['compression_ratio']:.2f}x")
    print(f"    Memory Reduction Percentage:        {metrics['memory_reduction_percent']:.2f}%")
    print(f"    Estimated Sparse Memory Usage:      {metrics['memory_kb']:.2f} KB ({metrics['memory_mb']:.3f} MB)")
    print(f"    Dense Grid Memory Usage (5cm):      {metrics['dense_memory_mb']:.2f} MB")
    print("    Cells Distribution by Ring:")
    for ring_id, count in metrics["cells_by_ring"].items():
        ring = engine.ring_dict[ring_id]
        print(f"      * Ring {ring_id} ({ring.resolution:.2f}m res, r=[{ring.r_min:.0f}-{ring.r_max:.0f}m]): {count:,} cells")
    print("    ---------------------------------------------------")

    # 5. Query Sample Cells and Verify Elevation + Semantic Probabilities
    print("\n[5] Cell Query & Semantic Probabilities Verification:")

    # Query a cell in Ring 0 (Fovea / Dynamic Vehicle area)
    all_cells = engine.get_all_cells()
    
    fovea_cells = [s for s in all_cells.values() if s["ring_id"] == 0 and s["dominant_class"] == 2]
    if fovea_cells:
        sample = fovea_cells[0]
        print(f"\n    Sample Dynamic Cell in Ring 0 (Fovea): Key=({sample['ring_id']}, {sample['i']}, {sample['j']})")
        print(f"      -> Center: ({sample['x_center']:.2f}m, {sample['y_center']:.2f}m) | Res: {sample['resolution']}m")
        print(f"      -> Point Count: {sample['count']}")
        print(f"      -> Elevation: mean={sample['z_mean']:.3f}m, min={sample['z_min']:.3f}m, max={sample['z_max']:.3f}m, std={sample['z_std']:.3f}m")
        print(f"      -> Semantics: counts={sample['semantic_counts']} | probs={sample['semantic_probs']} | Dominant: {sample['dominant_label']}")

    # Query a cell in Ring 1 (Static Obstacle area)
    static_cells = [s for s in all_cells.values() if s["ring_id"] == 1 and s["dominant_class"] == 1]
    if static_cells:
        sample = static_cells[0]
        print(f"\n    Sample Static Obstacle Cell in Ring 1: Key=({sample['ring_id']}, {sample['i']}, {sample['j']})")
        print(f"      -> Center: ({sample['x_center']:.2f}m, {sample['y_center']:.2f}m) | Res: {sample['resolution']}m")
        print(f"      -> Point Count: {sample['count']}")
        print(f"      -> Elevation: mean={sample['z_mean']:.3f}m, min={sample['z_min']:.3f}m, max={sample['z_max']:.3f}m, std={sample['z_std']:.3f}m")
        print(f"      -> Semantics: counts={sample['semantic_counts']} | probs={sample['semantic_probs']} | Dominant: {sample['dominant_label']}")

    # 6. Test Clear Method
    engine.clear()
    print(f"\n[6] Tested clear() method. Remaining occupied cells: {len(engine.cells)}")
    print("\n[SUCCESS] VariableResolutionGridEngine verification complete!")
    print("=" * 70)
