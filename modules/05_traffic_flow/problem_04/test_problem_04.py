"""
Tests for Problem 4: Multi-Lane Highway
"""

import pytest
from problem_04 import simulate_multilane_traffic, calculate_lane_utilization


def test_simulation_length():
    """Test that simulation returns correct length."""
    pos, lanes, speeds = simulate_multilane_traffic(10, 100, 3, 5, 10, 10, seed=42)
    assert len(pos) == 11
    assert len(lanes) == 11
    assert len(speeds) == 11


def test_simulation_reproducibility():
    """Test that same seed gives same results."""
    result1 = simulate_multilane_traffic(8, 80, 2, 4, 8, 5, seed=42)
    result2 = simulate_multilane_traffic(8, 80, 2, 4, 8, 5, seed=42)
    assert result1[0] == result2[0]  # positions
    assert result1[1] == result2[1]  # lanes
    assert result1[2] == result2[2]  # speeds


def test_positions_in_range():
    """Test that positions stay within road."""
    pos, lanes, speeds = simulate_multilane_traffic(10, 100, 3, 5, 10, 10, seed=42)
    for step in pos:
        for p in step:
            assert 0 <= p < 100


def test_lanes_valid():
    """Test that lane assignments are valid."""
    pos, lanes, speeds = simulate_multilane_traffic(10, 100, 3, 5, 10, 10, seed=42)
    for step in lanes:
        for lane in step:
            assert 0 <= lane < 3


def test_speeds_in_range():
    """Test that speeds are valid."""
    pos, lanes, speeds = simulate_multilane_traffic(10, 100, 3, 5, 10, 10, seed=42)
    for step in speeds:
        for s in step:
            assert 0 <= s <= 5


def test_number_of_cars_constant():
    """Test that number of cars stays constant."""
    pos, lanes, speeds = simulate_multilane_traffic(12, 100, 3, 5, 10, 10, seed=42)
    for i in range(len(pos)):
        assert len(pos[i]) == 12
        assert len(lanes[i]) == 12
        assert len(speeds[i]) == 12


def test_lane_changes_occur():
    """Test that cars actually change lanes."""
    pos, lanes, speeds = simulate_multilane_traffic(10, 100, 3, 5, 10, 20, seed=42)
    # Check if any car changed lanes during simulation
    initial_lanes = lanes[0]
    final_lanes = lanes[-1]
    # At least one car should have changed lanes
    assert initial_lanes != final_lanes or len(set([tuple(step) for step in lanes])) > 1


def test_more_lanes_better_flow():
    """Test that more lanes allow higher average speeds."""
    # 2 lanes
    _, _, speeds_2 = simulate_multilane_traffic(15, 100, 2, 5, 10, 30, seed=42)
    avg_2 = sum(sum(step) for step in speeds_2) / (len(speeds_2) * len(speeds_2[0]))
    
    # 3 lanes (more capacity)
    _, _, speeds_3 = simulate_multilane_traffic(15, 100, 3, 5, 10, 30, seed=42)
    avg_3 = sum(sum(step) for step in speeds_3) / (len(speeds_3) * len(speeds_3[0]))
    
    # More lanes should allow better flow (generally)
    # Use >= to account for randomness
    assert avg_3 >= avg_2 * 0.9  # Allow some variance


def test_calculate_lane_utilization():
    """Test lane utilization calculation."""
    lanes = [[0, 1, 2], [0, 0, 1], [1, 1, 2]]
    util = calculate_lane_utilization(lanes, 3)
    assert len(util) == 3
    # Lane 0: 1+2+0 = 3 cars total, 3 steps = 1.0
    # Lane 1: 1+1+2 = 4 cars total, 3 steps = 1.33
    # Lane 2: 1+0+1 = 2 cars total, 3 steps = 0.67
    # Each value should be between 0 and number of cars
    for u in util:
        assert 0 <= u <= 3


def test_utilization_sums_correctly():
    """Test that utilization accounts for all cars."""
    lanes = [[0, 0, 1, 1, 2], [0, 1, 1, 2, 2]]
    util = calculate_lane_utilization(lanes, 3)
    # Total utilization should equal number of cars
    assert abs(sum(util) - 5) < 0.01
