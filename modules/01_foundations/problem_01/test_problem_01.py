"""
Tests for Problem 1: Simple Counter Simulation
"""

import pytest
from problem_01 import count_simulation


def test_count_small_range():
    """Test counting a small range."""
    result = count_simulation(1, 5)
    assert result == [1, 2, 3, 4, 5]


def test_count_single_number():
    """Test counting when start equals end."""
    result = count_simulation(7, 7)
    assert result == [7]


def test_count_larger_range():
    """Test counting a larger range."""
    result = count_simulation(0, 10)
    assert result == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_count_negative_numbers():
    """Test counting with negative numbers."""
    result = count_simulation(-3, 2)
    assert result == [-3, -2, -1, 0, 1, 2]


def test_count_return_type():
    """Test that return type is a list."""
    result = count_simulation(1, 3)
    assert isinstance(result, list)


def test_count_length():
    """Test that the length is correct."""
    result = count_simulation(1, 10)
    assert len(result) == 10
