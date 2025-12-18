"""
Tests for Problem 1: Simple Prey Population
"""

import pytest
from problem_01 import prey_population_growth


def test_initial_value():
    """Test that population starts at initial value."""
    pop = prey_population_growth(100, 0.1, 0.05, 5)
    assert pop[0] == 100


def test_length():
    """Test that result has correct length."""
    pop = prey_population_growth(100, 0.1, 0.05, 10)
    assert len(pop) == 11  # initial + 10 steps


def test_growth_when_birth_exceeds_death():
    """Test that population grows when birth > death."""
    pop = prey_population_growth(100, 0.2, 0.1, 5)
    assert pop[-1] > pop[0]


def test_decline_when_death_exceeds_birth():
    """Test that population declines when death > birth."""
    pop = prey_population_growth(100, 0.1, 0.2, 5)
    assert pop[-1] < pop[0]


def test_stable_when_rates_equal():
    """Test that population stays constant when birth = death."""
    pop = prey_population_growth(100, 0.1, 0.1, 5)
    for p in pop:
        assert abs(p - 100) < 0.01


def test_exponential_growth():
    """Test exponential growth behavior."""
    pop = prey_population_growth(10, 0.5, 0, 3)
    # Should be: 10, 15, 22.5, 33.75
    assert abs(pop[1] - 15) < 0.01
    assert abs(pop[2] - 22.5) < 0.01


def test_zero_rates():
    """Test with zero birth and death rates."""
    pop = prey_population_growth(50, 0, 0, 5)
    for p in pop:
        assert p == 50
