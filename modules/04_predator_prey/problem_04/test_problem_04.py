"""
Tests for Problem 4: Spatial Predator-Prey
"""

import pytest
from problem_04 import initialize_grid, simulate_spatial_predator_prey


def test_initialize_grid_size():
    """Test that grid has correct dimensions."""
    grid = initialize_grid(5, 5, 10, 5, seed=42)
    # Should have entries for all cells
    assert len(grid) <= 25  # At most all cells


def test_initialize_grid_counts():
    """Test that grid has correct number of organisms."""
    grid = initialize_grid(10, 10, 20, 10, seed=42)
    prey_count = sum(1 for v in grid.values() if v == 'prey')
    pred_count = sum(1 for v in grid.values() if v == 'predator')
    assert prey_count == 20
    assert pred_count == 10


def test_initialize_grid_valid_coordinates():
    """Test that all coordinates are valid."""
    grid = initialize_grid(5, 5, 10, 5, seed=42)
    for (x, y) in grid.keys():
        assert 0 <= x < 5
        assert 0 <= y < 5


def test_initialize_grid_reproducibility():
    """Test that same seed gives same grid."""
    grid1 = initialize_grid(10, 10, 15, 8, seed=42)
    grid2 = initialize_grid(10, 10, 15, 8, seed=42)
    assert grid1 == grid2


def test_simulation_initial_counts():
    """Test that simulation starts with correct counts."""
    prey, pred = simulate_spatial_predator_prey(10, 10, 20, 10, 5, seed=42)
    assert prey[0] == 20
    assert pred[0] == 10


def test_simulation_length():
    """Test that simulation returns correct length."""
    prey, pred = simulate_spatial_predator_prey(10, 10, 20, 10, 10, seed=42)
    assert len(prey) == 11
    assert len(pred) == 11


def test_simulation_no_negative_counts():
    """Test that populations never go negative."""
    prey, pred = simulate_spatial_predator_prey(10, 10, 20, 10, 20, seed=42)
    for p in prey:
        assert p >= 0
    for p in pred:
        assert p >= 0


def test_simulation_reproducibility():
    """Test that same seed gives same results."""
    prey1, pred1 = simulate_spatial_predator_prey(10, 10, 15, 8, 10, seed=42)
    prey2, pred2 = simulate_spatial_predator_prey(10, 10, 15, 8, 10, seed=42)
    assert prey1 == prey2
    assert pred1 == pred2


def test_simulation_populations_bounded():
    """Test that populations stay within reasonable bounds."""
    prey, pred = simulate_spatial_predator_prey(10, 10, 20, 10, 30, seed=42)
    # Can't exceed grid size
    assert all(p <= 100 for p in prey)
    assert all(p <= 100 for p in pred)


def test_simulation_dynamics():
    """Test that populations can change over time."""
    prey, pred = simulate_spatial_predator_prey(15, 15, 30, 10, 50, seed=42)
    # At least one population should change
    prey_changed = prey[0] != prey[-1]
    pred_changed = pred[0] != pred[-1]
    assert prey_changed or pred_changed
