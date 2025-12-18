"""
Problem 2: 2D Random Walk (Medium)

Simulate a random walk in two dimensions.
Starting at (0, 0), move up, down, left, or right randomly at each step.

Your task:
- Implement the random_walk_2d function
- Track (x, y) position at each time step
- Return list of tuples
"""

import random


def random_walk_2d(num_steps, seed=None):
    """
    Simulate a 2D random walk.
    
    Args:
        num_steps: Number of steps to take
        seed: Random seed for reproducibility (optional)
    
    Returns:
        List of (x, y) tuples representing position at each time step
    
    Example:
        >>> walk = random_walk_2d(5, seed=42)
        >>> walk[0]
        (0, 0)
        >>> len(walk)
        6
    """
    if seed is not None:
        random.seed(seed)
    
    # TODO: Implement this function
    # Start at (0, 0)
    # Each step: randomly choose one of: (+1,0), (-1,0), (0,+1), (0,-1)
    pass


def calculate_distance_from_origin(position):
    """
    Calculate Euclidean distance from origin.
    
    Args:
        position: Tuple of (x, y)
    
    Returns:
        Float: distance from (0, 0)
    """
    # TODO: Implement this function
    # Use formula: sqrt(x^2 + y^2)
    pass


if __name__ == "__main__":
    walk = random_walk_2d(20, seed=42)
    print(f"Random walk: {walk}")
    print(f"Final position: {walk[-1]}")
    print(f"Distance from origin: {calculate_distance_from_origin(walk[-1]):.2f}")
