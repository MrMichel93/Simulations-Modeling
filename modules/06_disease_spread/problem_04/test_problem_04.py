"""
Tests for Problem 4: Spatial SEIR Model
"""

import pytest
from problem_04 import (initialize_seir_grid, simulate_spatial_seir, 
                        calculate_epidemic_peak)


def test_initialize_grid_size():
    """Test that grid has correct size."""
    grid = initialize_seir_grid(5, 5, [(2, 2)], seed=42)
    assert len(grid) == 25


def test_initialize_grid_initial_infected():
    """Test that initial infected are set correctly."""
    grid = initialize_seir_grid(5, 5, [(1, 1), (3, 3)], seed=42)
    assert grid[(1, 1)] == 'I'
    assert grid[(3, 3)] == 'I'


def test_initialize_grid_all_susceptible():
    """Test that non-infected cells are susceptible."""
    grid = initialize_seir_grid(5, 5, [(2, 2)], seed=42)
    susceptible_count = sum(1 for status in grid.values() if status == 'S')
    assert susceptible_count == 24  # All except the 1 infected


def test_simulation_length():
    """Test that simulation returns correct length."""
    S, E, I, R = simulate_spatial_seir(10, 10, [(5, 5)], 0.2, 0.3, 0.1, 20, seed=42)
    assert len(S) == 21
    assert len(E) == 21
    assert len(I) == 21
    assert len(R) == 21


def test_simulation_initial_conditions():
    """Test initial state of simulation."""
    S, E, I, R = simulate_spatial_seir(10, 10, [(5, 5)], 0.2, 0.3, 0.1, 5, seed=42)
    assert S[0] == 99
    assert E[0] == 0
    assert I[0] == 1
    assert R[0] == 0


def test_simulation_population_conservation():
    """Test that total population stays constant."""
    S, E, I, R = simulate_spatial_seir(15, 15, [(7, 7)], 0.2, 0.3, 0.1, 30, seed=42)
    total = 225
    for i in range(len(S)):
        assert S[i] + E[i] + I[i] + R[i] == total


def test_simulation_reproducibility():
    """Test that same seed gives same results."""
    S1, E1, I1, R1 = simulate_spatial_seir(10, 10, [(5, 5)], 0.2, 0.3, 0.1, 20, seed=42)
    S2, E2, I2, R2 = simulate_spatial_seir(10, 10, [(5, 5)], 0.2, 0.3, 0.1, 20, seed=42)
    
    assert S1 == S2
    assert E1 == E2
    assert I1 == I2
    assert R1 == R2


def test_disease_spreads_spatially():
    """Test that disease spreads beyond initial location."""
    S, E, I, R = simulate_spatial_seir(20, 20, [(10, 10)], 0.3, 0.3, 0.1, 50, seed=42)
    # Total affected should be more than initial
    total_affected = E[-1] + I[-1] + R[-1]
    assert total_affected > 1


def test_exposed_state_exists():
    """Test that exposed state appears during simulation."""
    S, E, I, R = simulate_spatial_seir(15, 15, [(7, 7)], 0.3, 0.2, 0.1, 30, seed=42)
    # At some point during simulation, there should be exposed individuals
    max_exposed = max(E)
    assert max_exposed > 0


def test_recovered_increases():
    """Test that recovered population increases over time."""
    S, E, I, R = simulate_spatial_seir(10, 10, [(5, 5)], 0.3, 0.3, 0.2, 50, seed=42)
    assert R[-1] > R[0]


def test_calculate_epidemic_peak():
    """Test epidemic peak calculation."""
    I_counts = [1, 3, 5, 10, 8, 4, 2, 1]
    peak_time, peak_count = calculate_epidemic_peak(I_counts)
    assert peak_time == 3
    assert peak_count == 10


def test_high_transmission_spreads_more():
    """Test that higher transmission leads to more spread."""
    # Low transmission
    _, _, _, R_low = simulate_spatial_seir(15, 15, [(7, 7)], 0.1, 0.3, 0.1, 50, seed=42)
    
    # High transmission
    _, _, _, R_high = simulate_spatial_seir(15, 15, [(7, 7)], 0.4, 0.3, 0.1, 50, seed=43)
    
    # Higher transmission should lead to more recovered
    assert R_high[-1] >= R_low[-1]


def test_spatial_locality():
    """Test that disease spreads locally first."""
    # Start in corner
    S, E, I, R = simulate_spatial_seir(20, 20, [(0, 0)], 0.3, 0.3, 0.1, 10, seed=42)
    # After a few steps, should not have spread to entire grid
    total_affected = E[5] + I[5] + R[5]
    assert total_affected < 400  # Should not reach all 400 cells immediately
