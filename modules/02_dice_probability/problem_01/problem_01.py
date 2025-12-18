"""
Problem 1: Single Die Roll (Easy)

Simulate rolling a single six-sided die multiple times.

Your task:
- Implement the roll_die function to return a random number from 1 to 6
- Implement the roll_multiple_dice function to roll the die n times
- Use random.randint for generating random numbers
"""

import random


def roll_die(seed=None):
    """
    Roll a single six-sided die.
    
    Args:
        seed: Random seed for reproducibility (optional)
    
    Returns:
        Integer from 1 to 6
    """
    if seed is not None:
        random.seed(seed)
    
    # TODO: Implement this function
    pass


def roll_multiple_dice(num_rolls, seed=None):
    """
    Roll a die multiple times.
    
    Args:
        num_rolls: Number of times to roll
        seed: Random seed for reproducibility (optional)
    
    Returns:
        List of roll results
    """
    if seed is not None:
        random.seed(seed)
    
    # TODO: Implement this function
    pass


if __name__ == "__main__":
    print("Rolling a die once:", roll_die(seed=42))
    print("Rolling a die 10 times:", roll_multiple_dice(10, seed=42))
