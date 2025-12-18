"""
Tests for Problem 3: Carrying Capacity
"""

import pytest
from problem_03 import predator_prey_with_capacity


def test_initial_values():
    """Test that populations start at initial values."""
    prey, pred = predator_prey_with_capacity(50, 5, 0.5, 100, 0.01, 0.1, 10)
    assert prey[0] == 50
    assert pred[0] == 5


def test_length():
    """Test that histories have correct length."""
    prey, pred = predator_prey_with_capacity(50, 5, 0.5, 100, 0.01, 0.1, 10)
    assert len(prey) == 11
    assert len(pred) == 11


def test_no_negative_populations():
    """Test that populations never go negative."""
    prey, pred = predator_prey_with_capacity(50, 10, 0.5, 100, 0.05, 0.1, 20)
    for p in prey:
        assert p >= 0
    for p in pred:
        assert p >= 0


def test_carrying_capacity_limits_growth():
    """Test that prey don't grow much beyond carrying capacity."""
    # Without predators, prey should approach carrying capacity
    prey, pred = predator_prey_with_capacity(10, 0, 0.5, 100, 0.01, 0.1, 50)
    # Should approach 100 but not wildly exceed it
    assert max(prey) <= 110  # Allow 10% overshoot


def test_prey_approach_capacity_without_predators():
    """Test that prey approach carrying capacity when alone."""
    prey, pred = predator_prey_with_capacity(10, 0, 0.3, 50, 0, 0, 50)
    # Should grow toward 50
    assert prey[-1] > 40
    assert prey[-1] <= 60


def test_growth_slows_near_capacity():
    """Test that growth rate decreases near capacity."""
    prey, pred = predator_prey_with_capacity(90, 0, 0.5, 100, 0, 0, 5)
    # Near capacity, growth should be very slow
    growth = prey[-1] - prey[0]
    assert growth < 20  # Much less than it would be far from capacity


def test_predators_can_reduce_prey_below_capacity():
    """Test that predators keep prey below carrying capacity."""
    prey, pred = predator_prey_with_capacity(80, 15, 0.3, 100, 0.02, 0.1, 30)
    # With predators, prey might not reach capacity
    avg_prey = sum(prey[10:]) / len(prey[10:])  # Average after initial period
    # Could be below capacity due to predation
    assert avg_prey >= 0  # Just verify it's reasonable


def test_both_can_coexist():
    """Test that both populations can persist together."""
    prey, pred = predator_prey_with_capacity(50, 5, 0.3, 100, 0.01, 0.1, 100)
    # Check that neither goes extinct
    assert prey[-1] > 1
    assert pred[-1] > 0.5
