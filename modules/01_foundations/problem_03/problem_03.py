"""
Problem 3: Random Walk Accumulator (Medium-Hard)

Create a stochastic simulation where a value randomly increases or decreases.
At each time step, add either +1 or -1 randomly.

Your task:
- Implement the random_accumulator function
- Use random.choice to pick between +1 and -1
- Track the accumulated value at each step
- Return the complete history

This models systems with random fluctuations like:
- Stock prices (simplified)
- Temperature changes
- Random particle movement
"""

import random


def random_accumulator(initial_value, num_steps, seed=None):
    """
    Simulate random accumulation over time.
    
    Args:
        initial_value: Starting value
        num_steps: Number of time steps to simulate
        seed: Random seed for reproducibility (optional)
    
    Returns:
        List of values at each time step
    
    Example (with seed=42):
        >>> random_accumulator(0, 5, seed=42)
        [0, -1, 0, 1, 2, 1]
    """
    if seed is not None:
        random.seed(seed)
    
    # TODO: Implement this function
    pass


if __name__ == "__main__":
    # Test your implementation
    result = random_accumulator(0, 10, seed=42)
    print(f"Random walk from 0 for 10 steps: {result}")
    
    result = random_accumulator(100, 20, seed=123)
    print(f"Random walk from 100 for 20 steps: {result}")
