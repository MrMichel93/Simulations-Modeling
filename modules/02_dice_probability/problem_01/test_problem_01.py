"""
Tests for Problem 1: Single Die Roll
"""

import pytest
from problem_01 import roll_die, roll_multiple_dice


def test_roll_die_in_range():
    """Test that die roll is in valid range."""
    for _ in range(20):
        result = roll_die()
        assert 1 <= result <= 6


def test_roll_die_reproducibility():
    """Test that same seed gives same result."""
    result1 = roll_die(seed=42)
    result2 = roll_die(seed=42)
    assert result1 == result2


def test_roll_multiple_dice_length():
    """Test that we get correct number of rolls."""
    result = roll_multiple_dice(10, seed=42)
    assert len(result) == 10


def test_roll_multiple_dice_all_valid():
    """Test that all rolls are in valid range."""
    result = roll_multiple_dice(50, seed=42)
    for roll in result:
        assert 1 <= roll <= 6


def test_roll_multiple_dice_reproducibility():
    """Test that same seed gives same results."""
    result1 = roll_multiple_dice(20, seed=42)
    result2 = roll_multiple_dice(20, seed=42)
    assert result1 == result2


def test_roll_multiple_dice_has_variety():
    """Test that multiple rolls produce different values."""
    result = roll_multiple_dice(100, seed=42)
    unique_values = set(result)
    assert len(unique_values) > 1  # Should have more than one unique value
