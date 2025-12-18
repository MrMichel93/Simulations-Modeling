"""
Problem 2: Dice Statistics (Medium)

Calculate statistics from multiple die rolls.

Your task:
- Implement functions to calculate mean, mode, and distribution
- Count frequency of each outcome
- Find the most common roll
"""

import random
from collections import Counter


def calculate_mean(rolls):
    """
    Calculate the average value of rolls.
    
    Args:
        rolls: List of die roll results
    
    Returns:
        Float: mean value
    """
    # TODO: Implement this function
    pass


def calculate_mode(rolls):
    """
    Find the most common roll result.
    
    Args:
        rolls: List of die roll results
    
    Returns:
        Integer: most frequent value (if tie, return the smallest)
    """
    # TODO: Implement this function
    pass


def calculate_distribution(rolls):
    """
    Calculate the frequency distribution of rolls.
    
    Args:
        rolls: List of die roll results
    
    Returns:
        Dictionary mapping each value (1-6) to its count
        Example: {1: 15, 2: 18, 3: 14, 4: 17, 5: 19, 6: 17}
    """
    # TODO: Implement this function
    pass


if __name__ == "__main__":
    # Test with sample data
    rolls = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 3, 3, 3]
    print(f"Rolls: {rolls}")
    print(f"Mean: {calculate_mean(rolls)}")
    print(f"Mode: {calculate_mode(rolls)}")
    print(f"Distribution: {calculate_distribution(rolls)}")
