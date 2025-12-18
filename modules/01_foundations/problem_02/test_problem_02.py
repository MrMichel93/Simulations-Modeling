"""
Tests for Problem 2: Linear Growth Simulation
"""

import pytest
from problem_02 import linear_growth


def test_positive_growth():
    """Test with positive growth."""
    result = linear_growth(10, 5, 4)
    assert result == [10, 15, 20, 25]


def test_negative_growth():
    """Test with negative growth (decline)."""
    result = linear_growth(100, -10, 5)
    assert result == [100, 90, 80, 70, 60]


def test_zero_growth():
    """Test with zero growth."""
    result = linear_growth(50, 0, 4)
    assert result == [50, 50, 50, 50]


def test_single_step():
    """Test with single time step."""
    result = linear_growth(10, 5, 1)
    assert result == [10]


def test_from_zero():
    """Test starting from zero."""
    result = linear_growth(0, 10, 3)
    assert result == [0, 10, 20]


def test_decimal_growth():
    """Test with decimal growth rate."""
    result = linear_growth(0, 2.5, 4)
    assert result == [0, 2.5, 5.0, 7.5]


def test_result_length():
    """Test that result has correct length."""
    result = linear_growth(0, 1, 10)
    assert len(result) == 10
