"""
Tests for Problem 3: Monte Carlo Estimation
"""

import pytest
from problem_03 import roll_two_dice, estimate_probability_of_seven, simulate_sum_distribution


def test_roll_two_dice_range():
    """Test that both dice are in valid range."""
    for _ in range(20):
        die1, die2 = roll_two_dice()
        assert 1 <= die1 <= 6
        assert 1 <= die2 <= 6


def test_roll_two_dice_reproducibility():
    """Test that same seed gives same result."""
    result1 = roll_two_dice(seed=42)
    result2 = roll_two_dice(seed=42)
    assert result1 == result2


def test_estimate_probability_range():
    """Test that probability is in valid range [0, 1]."""
    prob = estimate_probability_of_seven(100, seed=42)
    assert 0 <= prob <= 1


def test_estimate_probability_convergence():
    """Test that estimate approaches theoretical value with more trials."""
    theoretical = 6/36
    prob = estimate_probability_of_seven(10000, seed=42)
    # Should be within 5% of theoretical with 10k trials
    assert abs(prob - theoretical) < 0.05


def test_estimate_probability_reproducibility():
    """Test that same seed gives same result."""
    prob1 = estimate_probability_of_seven(1000, seed=42)
    prob2 = estimate_probability_of_seven(1000, seed=42)
    assert prob1 == prob2


def test_simulate_sum_distribution_keys():
    """Test that distribution includes all possible sums."""
    dist = simulate_sum_distribution(1000, seed=42)
    # Possible sums are 2 through 12
    for sum_value in range(2, 13):
        assert sum_value in dist


def test_simulate_sum_distribution_counts():
    """Test that distribution counts sum to total trials."""
    num_trials = 500
    dist = simulate_sum_distribution(num_trials, seed=42)
    assert sum(dist.values()) == num_trials


def test_simulate_sum_distribution_seven_most_common():
    """Test that 7 is most common sum (in large sample)."""
    dist = simulate_sum_distribution(10000, seed=42)
    # 7 should have the highest count
    max_count = max(dist.values())
    # 7 should be close to the max (might not always be exact due to randomness)
    assert dist[7] >= max_count * 0.9  # Within 90% of maximum
