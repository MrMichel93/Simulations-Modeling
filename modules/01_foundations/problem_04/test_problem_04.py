"""
Tests for Problem 4: Resource Competition Simulation
"""

import pytest
from problem_04 import resource_competition


def test_initial_values():
    """Test that first values are the initial values."""
    history_a, history_b = resource_competition(10, 20, 0.1, 0.1, 100, 5)
    assert history_a[0] == 10
    assert history_b[0] == 20


def test_length():
    """Test that histories have correct length."""
    history_a, history_b = resource_competition(10, 10, 0.1, 0.1, 100, 5)
    assert len(history_a) == 6  # initial + 5 steps
    assert len(history_b) == 6


def test_capacity_limit():
    """Test that total never exceeds capacity."""
    history_a, history_b = resource_competition(40, 40, 0.2, 0.2, 100, 10)
    for i in range(len(history_a)):
        total = history_a[i] + history_b[i]
        assert total <= 100 + 0.01  # small tolerance for floating point


def test_growth_without_competition():
    """Test growth when below capacity."""
    history_a, history_b = resource_competition(10, 10, 0.1, 0.1, 1000, 1)
    # After one step with 10% growth: 10 * 1.1 = 11
    assert abs(history_a[1] - 11.0) < 0.01
    assert abs(history_b[1] - 11.0) < 0.01


def test_equal_resources_stay_equal():
    """Test that equal resources with equal growth rates stay equal."""
    history_a, history_b = resource_competition(25, 25, 0.1, 0.1, 100, 5)
    for i in range(len(history_a)):
        assert abs(history_a[i] - history_b[i]) < 0.01


def test_different_growth_rates():
    """Test with different growth rates."""
    history_a, history_b = resource_competition(10, 10, 0.2, 0.1, 1000, 3)
    # Resource A should grow faster than B
    # After step 1: A=12, B=11
    assert history_a[-1] > history_b[-1]


def test_zero_growth():
    """Test with zero growth rates."""
    history_a, history_b = resource_competition(30, 20, 0, 0, 100, 5)
    # Values should remain constant
    for val in history_a:
        assert val == 30
    for val in history_b:
        assert val == 20


def test_competition_reduces_both():
    """Test that competition reduces both resources proportionally."""
    history_a, history_b = resource_competition(60, 60, 0.5, 0.5, 100, 1)
    # Total after growth would be 180, must be reduced to 100
    # Both should be reduced equally: 50 each
    assert abs(history_a[1] - 50) < 0.01
    assert abs(history_b[1] - 50) < 0.01
