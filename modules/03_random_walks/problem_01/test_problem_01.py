"""
Tests for Problem 1: 1D Random Walk
"""

import pytest
from problem_01 import random_walk_1d


def test_starts_at_zero():
    """Test that walk starts at position 0."""
    walk = random_walk_1d(10, seed=42)
    assert walk[0] == 0


def test_correct_length():
    """Test that walk has correct length."""
    walk = random_walk_1d(10, seed=42)
    assert len(walk) == 11  # initial position + 10 steps


def test_steps_are_one():
    """Test that each step moves by exactly 1."""
    walk = random_walk_1d(50, seed=42)
    for i in range(1, len(walk)):
        diff = abs(walk[i] - walk[i-1])
        assert diff == 1


def test_reproducibility():
    """Test that same seed gives same walk."""
    walk1 = random_walk_1d(20, seed=42)
    walk2 = random_walk_1d(20, seed=42)
    assert walk1 == walk2


def test_zero_steps():
    """Test with zero steps."""
    walk = random_walk_1d(0, seed=42)
    assert walk == [0]


def test_position_changes():
    """Test that position actually changes (not stuck)."""
    walk = random_walk_1d(100, seed=42)
    # At least one position should be different from start
    assert len(set(walk)) > 1
