"""
Tests for Problem 2: SIR with Interventions
"""

import pytest
from problem_02 import simulate_sir_with_intervention, calculate_total_infections


def test_initial_values():
    """Test that populations start correctly."""
    S, I, R = simulate_sir_with_intervention(990, 10, 0, 0.0005, 0.1, 20, 0.5, 10)
    assert S[0] == 990
    assert I[0] == 10
    assert R[0] == 0


def test_length():
    """Test correct history length."""
    S, I, R = simulate_sir_with_intervention(990, 10, 0, 0.0005, 0.1, 20, 0.5, 50)
    assert len(S) == 51
    assert len(I) == 51
    assert len(R) == 51


def test_population_conservation():
    """Test that total population is conserved."""
    S, I, R = simulate_sir_with_intervention(1000, 10, 0, 0.0005, 0.1, 20, 0.5, 30)
    total = 1010
    for i in range(len(S)):
        current_total = S[i] + I[i] + R[i]
        assert abs(current_total - total) < 0.1


def test_intervention_reduces_infections():
    """Test that intervention reduces total infections."""
    # No intervention
    S_no, _, _ = simulate_sir_with_intervention(990, 10, 0, 0.0005, 0.1, 999, 0, 100)
    infections_no = calculate_total_infections(S_no)
    
    # With intervention
    S_yes, _, _ = simulate_sir_with_intervention(990, 10, 0, 0.0005, 0.1, 20, 0.7, 100)
    infections_yes = calculate_total_infections(S_yes)
    
    # Intervention should reduce infections
    assert infections_yes < infections_no


def test_intervention_reduces_peak():
    """Test that intervention reduces peak infections."""
    # No intervention
    _, I_no, _ = simulate_sir_with_intervention(990, 10, 0, 0.0005, 0.1, 999, 0, 100)
    
    # With intervention
    _, I_yes, _ = simulate_sir_with_intervention(990, 10, 0, 0.0005, 0.1, 20, 0.7, 100)
    
    # Intervention should reduce peak
    assert max(I_yes) < max(I_no)


def test_early_intervention_more_effective():
    """Test that earlier intervention is more effective."""
    # Late intervention
    S_late, _, _ = simulate_sir_with_intervention(990, 10, 0, 0.0005, 0.1, 40, 0.7, 100)
    
    # Early intervention
    S_early, _, _ = simulate_sir_with_intervention(990, 10, 0, 0.0005, 0.1, 15, 0.7, 100)
    
    # Earlier intervention should reduce infections more
    assert calculate_total_infections(S_early) < calculate_total_infections(S_late)


def test_calculate_total_infections():
    """Test calculation of total infections."""
    S = [1000, 950, 900, 850]
    total = calculate_total_infections(S)
    assert total == 150  # 1000 - 850


def test_no_intervention_same_as_base():
    """Test that 0% reduction is same as no intervention."""
    S1, I1, R1 = simulate_sir_with_intervention(990, 10, 0, 0.0005, 0.1, 999, 0, 50)
    S2, I2, R2 = simulate_sir_with_intervention(990, 10, 0, 0.0005, 0.1, 10, 0, 50)
    
    # Should be similar (slight differences due to exact timing)
    assert abs(calculate_total_infections(S1) - calculate_total_infections(S2)) < 10
