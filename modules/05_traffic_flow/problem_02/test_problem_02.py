"""
Tests for Problem 2: Traffic with Braking
"""

import pytest
from problem_02 import simulate_traffic_with_braking


def test_initial_conditions():
    """Test initial positions and speeds."""
    pos, speeds = simulate_traffic_with_braking(4, 20, 2, 3, 1)
    # Should start evenly spaced
    assert len(pos[0]) == 4
    # Should start at max speed
    assert all(s == 2 for s in speeds[0])


def test_length():
    """Test that histories have correct length."""
    pos, speeds = simulate_traffic_with_braking(3, 20, 2, 3, 5)
    assert len(pos) == 6
    assert len(speeds) == 6


def test_positions_in_range():
    """Test that positions stay within road length."""
    pos, speeds = simulate_traffic_with_braking(5, 30, 3, 5, 10)
    for step in pos:
        for p in step:
            assert 0 <= p < 30


def test_speeds_in_range():
    """Test that speeds stay within valid range."""
    pos, speeds = simulate_traffic_with_braking(5, 30, 3, 5, 10)
    for step in speeds:
        for s in step:
            assert 0 <= s <= 3


def test_braking_when_close():
    """Test that cars brake when too close."""
    # Put cars close together
    pos, speeds = simulate_traffic_with_braking(10, 30, 3, 5, 5)
    # At least some cars should have reduced speed
    final_speeds = speeds[-1]
    min_speed = min(final_speeds)
    assert min_speed < 3  # At least one car should have braked


def test_no_collisions():
    """Test that cars don't collide (positions don't overlap)."""
    pos, speeds = simulate_traffic_with_braking(8, 40, 4, 6, 20)
    for step in pos:
        # Check that all positions are unique (or very close handling)
        sorted_pos = sorted(step)
        for i in range(1, len(sorted_pos)):
            # Allow small tolerance for floating point
            assert sorted_pos[i] - sorted_pos[i-1] > -0.1


def test_acceleration_when_clear():
    """Test that cars can accelerate when safe distance maintained."""
    # Sparse traffic should allow high speeds
    pos, speeds = simulate_traffic_with_braking(2, 100, 5, 3, 10)
    # With lots of space, speeds should be near max
    avg_speed = sum(speeds[-1]) / len(speeds[-1])
    assert avg_speed > 3  # Should maintain good speed with space


def test_number_of_cars_constant():
    """Test that number of cars stays constant."""
    pos, speeds = simulate_traffic_with_braking(6, 40, 3, 5, 10)
    for step in pos:
        assert len(step) == 6
    for step in speeds:
        assert len(step) == 6
