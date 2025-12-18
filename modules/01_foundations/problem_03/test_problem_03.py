"""
Tests for Problem 3: Random Walk Accumulator
"""

import pytest
from problem_03 import random_accumulator


def test_initial_value():
    """Test that first value is the initial value."""
    result = random_accumulator(10, 5, seed=42)
    assert result[0] == 10


def test_length():
    """Test that result has correct length."""
    result = random_accumulator(0, 10, seed=42)
    assert len(result) == 11  # initial value + 10 steps


def test_reproducibility_with_seed():
    """Test that same seed gives same results."""
    result1 = random_accumulator(0, 20, seed=42)
    result2 = random_accumulator(0, 20, seed=42)
    assert result1 == result2


def test_steps_are_plus_or_minus_one():
    """Test that each step changes by exactly 1."""
    result = random_accumulator(0, 100, seed=42)
    for i in range(1, len(result)):
        diff = abs(result[i] - result[i-1])
        assert diff == 1


def test_different_initial_values():
    """Test with different initial values."""
    result = random_accumulator(50, 10, seed=42)
    assert result[0] == 50


def test_single_step():
    """Test with single step."""
    result = random_accumulator(0, 1, seed=42)
    assert len(result) == 2
    assert abs(result[1] - result[0]) == 1


def test_zero_steps():
    """Test with zero steps."""
    result = random_accumulator(5, 0, seed=42)
    assert result == [5]
