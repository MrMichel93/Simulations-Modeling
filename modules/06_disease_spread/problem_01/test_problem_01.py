"""
Tests for Problem 1: Simple SIR Model
"""

import pytest
from problem_01 import simulate_sir


def test_initial_values():
    """Test that populations start at initial values."""
    S, I, R = simulate_sir(990, 10, 0, 0.0003, 0.1, 5)
    assert S[0] == 990
    assert I[0] == 10
    assert R[0] == 0


def test_length():
    """Test that histories have correct length."""
    S, I, R = simulate_sir(990, 10, 0, 0.0003, 0.1, 10)
    assert len(S) == 11
    assert len(I) == 11
    assert len(R) == 11


def test_population_conservation():
    """Test that total population stays constant."""
    S, I, R = simulate_sir(1000, 10, 0, 0.0003, 0.1, 20)
    total = 1010
    for i in range(len(S)):
        current_total = S[i] + I[i] + R[i]
        assert abs(current_total - total) < 0.1


def test_susceptible_decreases():
    """Test that susceptible population decreases over time."""
    S, I, R = simulate_sir(990, 10, 0, 0.0005, 0.1, 50)
    assert S[-1] < S[0]


def test_recovered_increases():
    """Test that recovered population increases."""
    S, I, R = simulate_sir(990, 10, 0, 0.0003, 0.1, 50)
    assert R[-1] > R[0]


def test_no_negative_populations():
    """Test that populations never go negative."""
    S, I, R = simulate_sir(100, 10, 0, 0.001, 0.2, 100)
    for i in range(len(S)):
        assert S[i] >= 0
        assert I[i] >= 0
        assert R[i] >= 0


def test_infection_peaks_and_declines():
    """Test that infection peaks and then declines."""
    S, I, R = simulate_sir(990, 10, 0, 0.0005, 0.1, 100)
    max_infected = max(I)
    # Peak should be higher than start
    assert max_infected > I[0]
    # Final should be lower than peak
    assert I[-1] < max_infected


def test_high_recovery_limits_spread():
    """Test that high recovery rate limits spread."""
    # Low recovery
    _, I_low, _ = simulate_sir(990, 10, 0, 0.0003, 0.05, 100)
    # High recovery
    _, I_high, _ = simulate_sir(990, 10, 0, 0.0003, 0.3, 100)
    
    # High recovery should lead to lower peak
    assert max(I_high) < max(I_low)
