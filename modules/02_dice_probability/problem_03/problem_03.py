"""
Problem 3: Monte Carlo Estimation (Medium-Hard)

Use random sampling to estimate probabilities.

Your task:
- Simulate rolling two dice many times
- Calculate the probability of getting a sum of 7
- Estimate probability through simulation (Monte Carlo method)

The theoretical probability of rolling a 7 with two dice is 6/36 = 1/6 ≈ 0.1667
Your simulation should approach this value with more trials.
"""

import random


def roll_two_dice(seed=None):
    """
    Roll two six-sided dice.
    
    Args:
        seed: Random seed for reproducibility (optional)
    
    Returns:
        Tuple of (die1, die2)
    """
    if seed is not None:
        random.seed(seed)
    
    # TODO: Implement this function
    pass


def estimate_probability_of_seven(num_trials, seed=None):
    """
    Estimate the probability of rolling a sum of 7 with two dice.
    
    Args:
        num_trials: Number of times to roll two dice
        seed: Random seed for reproducibility (optional)
    
    Returns:
        Float: estimated probability (number of 7s / total trials)
    
    Example:
        With many trials, this should approach 0.1667 (which is 6/36)
    """
    if seed is not None:
        random.seed(seed)
    
    # TODO: Implement this function
    # Hint: Count how many times the sum of two dice equals 7
    pass


def simulate_sum_distribution(num_trials, seed=None):
    """
    Simulate rolling two dice and return distribution of sums.
    
    Args:
        num_trials: Number of trials
        seed: Random seed for reproducibility (optional)
    
    Returns:
        Dictionary mapping each sum (2-12) to its frequency
    """
    if seed is not None:
        random.seed(seed)
    
    # TODO: Implement this function
    pass


if __name__ == "__main__":
    print("Rolling two dice:", roll_two_dice(seed=42))
    print("\nEstimating P(sum=7) with different trial counts:")
    print(f"  1,000 trials: {estimate_probability_of_seven(1000, seed=42):.4f}")
    print(f" 10,000 trials: {estimate_probability_of_seven(10000, seed=42):.4f}")
    print(f"100,000 trials: {estimate_probability_of_seven(100000, seed=42):.4f}")
    print(f"\nTheoretical probability: {6/36:.4f}")
