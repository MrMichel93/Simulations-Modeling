"""
Tests for Problem 2: Dice Statistics
"""

import pytest
from problem_02 import calculate_mean, calculate_mode, calculate_distribution


def test_calculate_mean_uniform():
    """Test mean of uniform distribution."""
    rolls = [1, 2, 3, 4, 5, 6]
    assert abs(calculate_mean(rolls) - 3.5) < 0.01


def test_calculate_mean_repeated():
    """Test mean with repeated values."""
    rolls = [3, 3, 3, 3]
    assert calculate_mean(rolls) == 3.0


def test_calculate_mode_clear_winner():
    """Test mode when one value is most common."""
    rolls = [1, 2, 3, 3, 3, 4, 5]
    assert calculate_mode(rolls) == 3


def test_calculate_mode_tie():
    """Test mode when there's a tie (return smallest)."""
    rolls = [1, 1, 2, 2, 3]
    result = calculate_mode(rolls)
    assert result in [1, 2]  # Either is acceptable, but prefer smallest


def test_calculate_distribution_complete():
    """Test distribution includes all values."""
    rolls = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
    dist = calculate_distribution(rolls)
    assert dist == {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2}


def test_calculate_distribution_missing_values():
    """Test distribution with missing values."""
    rolls = [1, 1, 1, 6, 6, 6]
    dist = calculate_distribution(rolls)
    assert dist[1] == 3
    assert dist[6] == 3
    assert dist.get(2, 0) == 0
    assert dist.get(3, 0) == 0


def test_calculate_distribution_sum():
    """Test that distribution counts sum to total rolls."""
    rolls = [1, 2, 3, 4, 5, 6, 1, 2, 3]
    dist = calculate_distribution(rolls)
    assert sum(dist.values()) == len(rolls)
