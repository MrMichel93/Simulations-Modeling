"""
Problem 3: Biased Random Walk (Medium-Hard)

Simulate a random walk with bias (tendency to move in one direction).
In 1D, there's a higher probability of moving right than left.

Your task:
- Implement biased_random_walk_1d with adjustable bias
- Probability of moving right = bias (e.g., 0.6 = 60% right, 40% left)
- Track and analyze the drift over time
"""

import random


def biased_random_walk_1d(num_steps, bias=0.5, seed=None):
    """
    Simulate a biased 1D random walk.
    
    Args:
        num_steps: Number of steps to take
        bias: Probability of moving right (0 to 1)
              0.5 = unbiased, 0.6 = 60% right, 0.4 = 40% right
        seed: Random seed for reproducibility (optional)
    
    Returns:
        List of positions at each time step
    
    Example:
        >>> walk = biased_random_walk_1d(10, bias=0.6, seed=42)
        >>> walk[0]
        0
    """
    if seed is not None:
        random.seed(seed)
    
    # TODO: Implement this function
    # Use random.random() < bias to decide direction
    # If True: move right (+1), else: move left (-1)
    pass


def calculate_average_final_position(num_trials, num_steps, bias, seed=None):
    """
    Run multiple biased walks and calculate average final position.
    
    Args:
        num_trials: Number of walks to simulate
        num_steps: Steps per walk
        bias: Bias probability
        seed: Random seed for reproducibility (optional)
    
    Returns:
        Float: average final position across all trials
    
    This helps verify that bias creates expected drift.
    With bias > 0.5, average should be positive.
    With bias < 0.5, average should be negative.
    """
    if seed is not None:
        random.seed(seed)
    
    # TODO: Implement this function
    pass


if __name__ == "__main__":
    print("Unbiased walk (50-50):")
    walk = biased_random_walk_1d(100, bias=0.5, seed=42)
    print(f"  Final position: {walk[-1]}")
    
    print("\nBiased walk (70% right):")
    walk = biased_random_walk_1d(100, bias=0.7, seed=42)
    print(f"  Final position: {walk[-1]}")
    
    print("\nAverage over 100 trials (70% right, 100 steps):")
    avg = calculate_average_final_position(100, 100, 0.7, seed=42)
    print(f"  Average final position: {avg:.2f}")
    print(f"  Expected: ~40 (100 steps * (0.7 - 0.3) = 40)")
