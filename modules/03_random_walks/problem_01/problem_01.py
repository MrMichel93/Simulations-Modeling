"""
Problem 1: 1D Random Walk (Easy)

Simulate a random walk in one dimension.
Starting at position 0, move left (-1) or right (+1) randomly at each step.

Your task:
- Implement the random_walk_1d function
- Track position at each time step
"""

import random


def random_walk_1d(num_steps, seed=None):
    """
    Simulate a 1D random walk.
    
    Args:
        num_steps: Number of steps to take
        seed: Random seed for reproducibility (optional)
    
    Returns:
        List of positions at each time step (including initial position 0)
    
    Example:
        >>> walk = random_walk_1d(5, seed=42)
        >>> walk[0]
        0
        >>> len(walk)
        6
    """
    if seed is not None:
        random.seed(seed)
    
    # TODO: Implement this function
    # Start at position 0
    # Each step: randomly move +1 or -1
    pass


if __name__ == "__main__":
    walk = random_walk_1d(10, seed=42)
    print(f"Random walk: {walk}")
    print(f"Final position: {walk[-1]}")
