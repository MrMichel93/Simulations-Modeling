"""
Tests for Problem 2: 2D Random Walk
"""

import pytest
from problem_02 import random_walk_2d, calculate_distance_from_origin


def test_starts_at_origin():
    """Test that walk starts at (0, 0)."""
    walk = random_walk_2d(10, seed=42)
    assert walk[0] == (0, 0)


def test_correct_length():
    """Test that walk has correct length."""
    walk = random_walk_2d(10, seed=42)
    assert len(walk) == 11  # initial position + 10 steps


def test_steps_are_one():
    """Test that each step moves by exactly 1 in one direction."""
    walk = random_walk_2d(50, seed=42)
    for i in range(1, len(walk)):
        x_diff = abs(walk[i][0] - walk[i-1][0])
        y_diff = abs(walk[i][1] - walk[i-1][1])
        # Should move exactly 1 in x OR y, but not both
        assert (x_diff == 1 and y_diff == 0) or (x_diff == 0 and y_diff == 1)


def test_reproducibility():
    """Test that same seed gives same walk."""
    walk1 = random_walk_2d(20, seed=42)
    walk2 = random_walk_2d(20, seed=42)
    assert walk1 == walk2


def test_zero_steps():
    """Test with zero steps."""
    walk = random_walk_2d(0, seed=42)
    assert walk == [(0, 0)]


def test_distance_at_origin():
    """Test distance calculation at origin."""
    dist = calculate_distance_from_origin((0, 0))
    assert dist == 0


def test_distance_calculation():
    """Test distance calculation."""
    dist = calculate_distance_from_origin((3, 4))
    assert abs(dist - 5.0) < 0.01  # 3-4-5 triangle


def test_distance_negative_coordinates():
    """Test distance with negative coordinates."""
    dist = calculate_distance_from_origin((-3, -4))
    assert abs(dist - 5.0) < 0.01


def test_position_changes():
    """Test that position actually changes."""
    walk = random_walk_2d(100, seed=42)
    # At least one position should be different from start
    assert len(set(walk)) > 1
