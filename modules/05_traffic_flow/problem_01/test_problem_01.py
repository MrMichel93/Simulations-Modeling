"""
Tests for Problem 1: Single Lane Traffic
"""

import pytest
from problem_01 import simulate_single_lane


def test_initial_spacing():
    """Test that cars start evenly spaced."""
    positions = simulate_single_lane(4, 20, 1, 1)
    initial = positions[0]
    # Should be spaced by road_length / num_cars
    assert len(initial) == 4
    spacing = 20 / 4
    expected = [0, 5, 10, 15]
    for i, pos in enumerate(initial):
        assert abs(pos - expected[i]) < 0.01


def test_length():
    """Test that result has correct length."""
    positions = simulate_single_lane(3, 10, 1, 5)
    assert len(positions) == 6  # initial + 5 steps


def test_cars_move_forward():
    """Test that cars move forward by speed."""
    positions = simulate_single_lane(2, 20, 3, 1)
    # After 1 step, each car should move forward by 3
    assert abs(positions[1][0] - 3) < 0.01
    assert abs(positions[1][1] - 13) < 0.01  # 10 + 3


def test_circular_wrapping():
    """Test that positions wrap around the road."""
    positions = simulate_single_lane(1, 10, 3, 4)
    # Start at 0, moves: 3, 6, 9, 12%10=2
    assert abs(positions[-1][0] - 2) < 0.01


def test_all_positions_in_range():
    """Test that all positions stay within road length."""
    positions = simulate_single_lane(5, 15, 2, 10)
    for step in positions:
        for pos in step:
            assert 0 <= pos < 15


def test_number_of_cars_constant():
    """Test that number of cars stays constant."""
    positions = simulate_single_lane(4, 20, 1, 10)
    for step in positions:
        assert len(step) == 4


def test_zero_speed():
    """Test with zero speed (cars don't move)."""
    positions = simulate_single_lane(3, 12, 0, 5)
    # All positions should stay the same
    for i in range(len(positions)):
        assert positions[i] == positions[0]
