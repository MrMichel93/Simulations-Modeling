"""
Tests for Problem 2: Basic Predator-Prey Interaction
"""

import pytest
from problem_02 import predator_prey_simulation


def test_initial_values():
    """Test that populations start at initial values."""
    prey, pred = predator_prey_simulation(100, 10, 0.1, 0.01, 0.1, 5)
    assert prey[0] == 100
    assert pred[0] == 10


def test_length():
    """Test that histories have correct length."""
    prey, pred = predator_prey_simulation(100, 10, 0.1, 0.01, 0.1, 10)
    assert len(prey) == 11
    assert len(pred) == 11


def test_no_negative_populations():
    """Test that populations never go negative."""
    prey, pred = predator_prey_simulation(10, 50, 0.1, 0.1, 0.1, 20)
    for p in prey:
        assert p >= 0
    for p in pred:
        assert p >= 0


def test_prey_growth_without_predators():
    """Test that prey grow when no predators."""
    prey, pred = predator_prey_simulation(100, 0, 0.1, 0.01, 0.1, 5)
    assert prey[-1] > prey[0]


def test_predators_decline_without_prey():
    """Test that predators decline without prey."""
    prey, pred = predator_prey_simulation(0, 10, 0.1, 0.01, 0.5, 5)
    assert pred[-1] < pred[0]


def test_both_populations_change():
    """Test that both populations can change over time."""
    prey, pred = predator_prey_simulation(100, 10, 0.1, 0.01, 0.1, 20)
    # At least one should change
    prey_changed = prey[0] != prey[-1]
    pred_changed = pred[0] != pred[-1]
    assert prey_changed or pred_changed


def test_high_predation_reduces_prey():
    """Test that high predation rate reduces prey."""
    prey, pred = predator_prey_simulation(100, 20, 0.1, 0.05, 0.1, 10)
    # Prey should decline with high predation
    assert prey[-1] < prey[0] or prey[-1] < 50
