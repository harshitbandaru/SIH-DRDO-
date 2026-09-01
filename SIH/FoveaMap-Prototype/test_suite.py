"""
Comprehensive Automated Maintenance & Error Verification Suite for FoveaMap-Prototype
"""

import sys
import os
import numpy as np

# Ensure project root is in sys.path
project_root = os.path.abspath(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

print("=" * 70)
print("     FOVEAMAP-PROTOTYPE COMPREHENSIVE AUTOMATED VERIFICATION SUITE")
print("=" * 70)

# Step 1: Import all modules
print("\n[STEP 1] Importing Package Modules...")
try:
    import foveamap
    from foveamap.grid_engine import (
        VariableResolutionGridEngine,
        RingConfig,
        FoveaGrid25D,
        MultiResLevel,
        MapBounds,
    )
    from foveamap.visualization import (
        FoveaVisualizer,
        animate_grid_projection,
        plot_final_grid,
        plot_elevation_map,
        plot_memory_comparison,
    )
    from foveamap.demo import run_demo, generate_synthetic_lidar_data
    print("    [PASS] All modules imported successfully.")
except Exception as e:
    print(f"    [FAIL] Import failed: {e}")
    sys.exit(1)

# Step 2: Instantiate VariableResolutionGridEngine & FoveaGrid25D
print("\n[STEP 2] Instantiating Grid Engines...")
try:
    engine = VariableResolutionGridEngine(origin=(0.0, 0.0))
    legacy_grid = FoveaGrid25D(fovea_center=(2.0, 3.0))
    print(f"    [PASS] Engine instantiated. Default max range = {engine.max_range}m, rings count = {len(engine.rings)}.")
    print(f"    [PASS] Legacy grid instantiated. Origin = {legacy_grid.origin}.")
except Exception as e:
    print(f"    [FAIL] Instantiation failed: {e}")
    sys.exit(1)

# Step 3: Generate synthetic points & labels (including edge cases)
print("\n[STEP 3] Generating Synthetic LiDAR Data & Edge Case Points...")
try:
    num_pts = 10_000
    points, labels = generate_synthetic_lidar_data(num_points=num_pts, seed=42)
    
    # Inject edge cases: NaNs, Infs, out-of-range points, invalid labels
    corrupted_pts = np.vstack([
        points,
        [np.nan, 0.0, 1.0],
        [0.0, np.inf, 2.0],
        [500.0, 500.0, 0.0],  # Out of range (>100m)
        [-200.0, -200.0, -50.0]
    ])
    corrupted_labels = np.append(labels, [0, 1, 2, 999])  # 999 is invalid class
    print(f"    [PASS] Generated {len(corrupted_pts):,} test points with edge case noise.")
except Exception as e:
    print(f"    [FAIL] Point generation failed: {e}")
    sys.exit(1)

# Step 4: Call project_points() and fuse_frame()
print("\n[STEP 4] Testing Point Cloud Ingestion & Temporal Fusion...")
try:
    engine.clear()
    engine.project_points(corrupted_pts, corrupted_labels)
    occupied_count_1 = len(engine.cells)
    
    # Test temporal fusion
    engine.fuse_frame(points[:1000], labels[:1000], decay=0.9)
    occupied_count_2 = len(engine.cells)
    
    # Test 4D array (x, y, z, label)
    pts_4d = np.column_stack([points[:500], labels[:500]])
    engine.project_points(pts_4d)
    
    print(f"    [PASS] Point projection and temporal fusion completed safely.")
    print(f"           Occupied cells after project_points: {occupied_count_1:,}")
    print(f"           Occupied cells after fuse_frame:    {occupied_count_2:,}")
except Exception as e:
    print(f"    [FAIL] Point ingestion failed: {e}")
    sys.exit(1)

# Step 5: Call get_cell_stats(), get_all_cells(), memory_footprint()
print("\n[STEP 5] Testing Query Methods & Memory Footprint...")
try:
    all_cells_dict = engine.get_all_cells()
    sample_key = next(iter(all_cells_dict.keys()))
    sample_stats = engine.get_cell_stats(sample_key[0], sample_key[1], sample_key[2])
    
    assert sample_stats is not None, "get_cell_stats returned None for occupied cell"
    assert "z_mean" in sample_stats and "semantic_probs" in sample_stats
    
    non_existent = engine.get_cell_stats(99, 999, 999)
    assert non_existent is None, "get_cell_stats should return None for empty cell"
    
    metrics = engine.memory_footprint()
    assert "occupied_cells" in metrics and "compression_ratio" in metrics
    
    # Test legacy grid wrapper interface
    legacy_grid.add_point_cloud(points[:5000])
    legacy_cells_list = legacy_grid.get_all_cells()
    assert isinstance(legacy_cells_list, list), "FoveaGrid25D get_all_cells must return list"
    
    print("    [PASS] All query methods & memory footprint metrics evaluated cleanly.")
    print(f"           Sample Query (Ring {sample_stats['ring_id']}): z_mean={sample_stats['z_mean']:.3f}m, Dominant Label={sample_stats['dominant_label']}")
    print(f"           Memory Reduction: {metrics['memory_reduction_percent']:.2f}%, Compression Ratio: {metrics['compression_ratio']:.2f}x")
except Exception as e:
    print(f"    [FAIL] Query methods failed: {e}")
    sys.exit(1)

# Step 6: Test Animation Function (short test)
print("\n[STEP 6] Testing Matplotlib Animation Function (5 frames test)...")
try:
    fig, anim = animate_grid_projection(
        engine, points[:2000], labels[:2000], interval=20, max_frames=5, use_fusion=True
    )
    print("    [PASS] animate_grid_projection generated FuncAnimation successfully.")
    import matplotlib.pyplot as plt
    plt.close(fig)
except Exception as e:
    print(f"    [FAIL] Animation test failed: {e}")
    sys.exit(1)

# Step 7: Test Static Plot Functions
print("\n[STEP 7] Testing Static Rendering Functions...")
try:
    engine.clear()
    engine.project_points(points[:5000], labels[:5000])
    
    plot_final_grid(engine, title="Test Final Grid", show=False)
    plot_elevation_map(engine, title="Test Elevation Map", show=False)
    plot_memory_comparison(engine, show=False)
    print("    [PASS] Static rendering functions (final grid, elevation map, memory benchmark) executed cleanly.")
except Exception as e:
    print(f"    [FAIL] Static rendering failed: {e}")
    sys.exit(1)

# Step 8: Test Clear Method
print("\n[STEP 8] Testing engine clear()...")
try:
    engine.clear()
    assert len(engine.cells) == 0, "clear() did not empty cells dictionary"
    print("    [PASS] Grid clear() reset storage cleanly.")
except Exception as e:
    print(f"    [FAIL] Clear method failed: {e}")
    sys.exit(1)

print("\n" + "=" * 70)
print("     [SUCCESS] ALL VERIFICATION SUITE TESTS PASSED 100% ERROR-FREE!")
print("=" * 70)
