"""
Problem 4: Gambler's Ruin (Hard)

Simulate a gambling game where a player starts with some money and bets $1 each round.
The player wins with probability p and loses with probability (1-p).
The game ends when the player reaches a target amount or goes broke.

Your task:
- Implement the gambler_game function
- Track the player's money at each step
- Stop when player reaches target or goes broke
- Return the history and outcome

This models real-world scenarios like:
- Risk-taking in finance
- Resource management
- Sequential decision problems
"""

import random


def gambler_game(initial_money, target_money, win_probability, seed=None):
    """
    Simulate a gambling game.
    
    Args:
        initial_money: Starting amount of money
        target_money: Goal amount (game ends if reached)
        win_probability: Probability of winning each round (0 to 1)
        seed: Random seed for reproducibility (optional)
    
    Returns:
        Tuple of (history, outcome):
        - history: List of money amounts at each step
        - outcome: 'won' if reached target, 'lost' if went broke
    
    Rules:
        - Start with initial_money
        - Each round: flip a biased coin
          - If win (probability = win_probability): gain $1
          - If lose: lose $1
        - Stop if money reaches target_money (win) or 0 (lose)
    
    Example:
        >>> history, outcome = gambler_game(10, 20, 0.5, seed=42)
        >>> history[0] == 10
        True
        >>> outcome in ['won', 'lost']
        True
    """
    if seed is not None:
        random.seed(seed)
    
    # TODO: Implement this function
    pass


def simulate_multiple_games(initial_money, target_money, win_probability, 
                           num_games, seed=None):
    """
    Simulate multiple gambling games and return statistics.
    
    Args:
        initial_money: Starting amount for each game
        target_money: Goal amount for each game
        win_probability: Win probability for each round
        num_games: Number of games to simulate
        seed: Random seed for reproducibility (optional)
    
    Returns:
        Dictionary with:
        - 'win_rate': Fraction of games won
        - 'avg_rounds': Average number of rounds per game
        - 'max_rounds': Maximum rounds in any game
    """
    if seed is not None:
        random.seed(seed)
    
    # TODO: Implement this function
    pass


if __name__ == "__main__":
    print("Single game simulation:")
    history, outcome = gambler_game(10, 20, 0.5, seed=42)
    print(f"  Started with: $10")
    print(f"  Target: $20")
    print(f"  Outcome: {outcome}")
    print(f"  Took {len(history)-1} rounds")
    
    print("\nMultiple games statistics:")
    stats = simulate_multiple_games(10, 20, 0.5, 100, seed=42)
    print(f"  Win rate: {stats['win_rate']:.2%}")
    print(f"  Average rounds: {stats['avg_rounds']:.1f}")
    print(f"  Longest game: {stats['max_rounds']} rounds")
