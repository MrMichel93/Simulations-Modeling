"""
Problem 4: Self-Avoiding Random Walk (Hard)

Simulate a random walk that cannot visit the same position twice.
This is more complex because we need to track visited positions
and only choose valid moves.

Your task:
- Implement self_avoiding_walk_2d
- Track visited positions
- Only allow moves to unvisited positions
- Handle the case where the walk gets "stuck"

This models real-world scenarios like:
- Polymer chains in chemistry
- Maze exploration
- Path finding without backtracking
"""

import random


def self_avoiding_walk_2d(num_steps, seed=None):
    """
    Simulate a 2D self-avoiding random walk.
    
    Args:
        num_steps: Maximum number of steps to attempt
        seed: Random seed for reproducibility (optional)
    
    Returns:
        List of (x, y) tuples representing the path
        Walk may be shorter than num_steps if it gets stuck
    
    Algorithm:
        1. Start at (0, 0)
        2. Track visited positions in a set
        3. At each step:
           - Find valid moves (neighbors not yet visited)
           - If no valid moves: walk is stuck, return
           - Otherwise: randomly choose a valid move
    
    Example:
        >>> walk = self_avoiding_walk_2d(10, seed=42)
        >>> walk[0]
        (0, 0)
        >>> len(set(walk)) == len(walk)  # All positions unique
        True
    """
    if seed is not None:
        random.seed(seed)
    
    # TODO: Implement this function
    # Hint: Use a set to track visited positions
    # Hint: Check all 4 neighbors: (x+1,y), (x-1,y), (x,y+1), (x,y-1)
    pass


def count_stuck_walks(num_trials, num_steps, seed=None):
    """
    Count how many walks get stuck before completing all steps.
    
    Args:
        num_trials: Number of walks to simulate
        num_steps: Target number of steps
        seed: Random seed for reproducibility (optional)
    
    Returns:
        Tuple of (num_stuck, avg_length):
        - num_stuck: number of walks that got stuck
        - avg_length: average length of all walks
    """
    if seed is not None:
        random.seed(seed)
    
    # TODO: Implement this function
    pass


if __name__ == "__main__":
    print("Self-avoiding walk:")
    walk = self_avoiding_walk_2d(50, seed=42)
    print(f"  Attempted: 50 steps")
    print(f"  Completed: {len(walk)-1} steps")
    print(f"  Final position: {walk[-1]}")
    
    print("\nAnalyzing 100 walks of 50 steps:")
    num_stuck, avg_length = count_stuck_walks(100, 50, seed=42)
    print(f"  Walks that got stuck: {num_stuck}")
    print(f"  Average length: {avg_length:.1f}")
