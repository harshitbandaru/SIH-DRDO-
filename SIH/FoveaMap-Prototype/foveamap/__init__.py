"""
FoveaMap: Adaptive Variable Resolution 2.5D Lidar Mapping Engine
Prototype for DRDO / SIH Problem Statement 26053
"""

from .grid_engine import (
    VariableResolutionGridEngine,
    RingConfig,
    FoveaGrid25D,
    MultiResLevel,
    MapBounds,
)
from .visualization import (
    FoveaVisualizer,
    animate_grid_projection,
    plot_final_grid,
    plot_elevation_map,
    plot_memory_comparison,
)

__all__ = [
    "VariableResolutionGridEngine",
    "RingConfig",
    "FoveaGrid25D",
    "MultiResLevel",
    "MapBounds",
    "FoveaVisualizer",
    "animate_grid_projection",
    "plot_final_grid",
    "plot_elevation_map",
    "plot_memory_comparison",
]
__version__ = "0.3.0"
