"""
Tests for Problem 3: Biased Random Walk
"""

import pytest
from problem_03 import biased_random_walk_1d, calculate_average_final_position


def test_starts_at_zero():
    """Test that walk starts at 0."""
    walk = biased_random_walk_1d(10, bias=0.5, seed=42)
    assert walk[0] == 0


def test_correct_length():
    """Test that walk has correct length."""
    walk = biased_random_walk_1d(10, bias=0.5, seed=42)
    assert len(walk) == 11


def test_steps_are_one():
    """Test that each step moves by exactly 1."""
    walk = biased_random_walk_1d(50, bias=0.5, seed=42)
    for i in range(1, len(walk)):
        diff = abs(walk[i] - walk[i-1])
        assert diff == 1


def test_reproducibility():
    """Test that same seed gives same walk."""
    walk1 = biased_random_walk_1d(20, bias=0.6, seed=42)
    walk2 = biased_random_walk_1d(20, bias=0.6, seed=42)
    assert walk1 == walk2


def test_full_right_bias():
    """Test with 100% right bias."""
    walk = biased_random_walk_1d(10, bias=1.0, seed=42)
    # Should always move right
    for i in range(1, len(walk)):
        assert walk[i] == walk[i-1] + 1
    assert walk[-1] == 10


def test_full_left_bias():
    """Test with 0% right bias (100% left)."""
    walk = biased_random_walk_1d(10, bias=0.0, seed=42)
    # Should always move left
    for i in range(1, len(walk)):
        assert walk[i] == walk[i-1] - 1
    assert walk[-1] == -10


def test_average_positive_with_right_bias():
    """Test that average is positive with right bias."""
    avg = calculate_average_final_position(100, 50, bias=0.7, seed=42)
    assert avg > 0


def test_average_negative_with_left_bias():
    """Test that average is negative with left bias."""
    avg = calculate_average_final_position(100, 50, bias=0.3, seed=42)
    assert avg < 0


def test_average_near_zero_unbiased():
    """Test that average is near zero for unbiased walk."""
    avg = calculate_average_final_position(100, 50, bias=0.5, seed=42)
    # Should be close to 0, but allow some variance
    assert abs(avg) < 10


def test_average_scales_with_steps():
    """Test that drift increases with more steps."""
    avg_10 = abs(calculate_average_final_position(100, 10, bias=0.7, seed=42))
    avg_100 = abs(calculate_average_final_position(100, 100, bias=0.7, seed=42))
    assert avg_100 > avg_10
