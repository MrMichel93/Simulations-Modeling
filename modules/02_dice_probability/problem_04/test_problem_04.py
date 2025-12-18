"""
Tests for Problem 4: Gambler's Ruin
"""

import pytest
from problem_04 import gambler_game, simulate_multiple_games


def test_gambler_game_initial_value():
    """Test that game starts with initial money."""
    history, outcome = gambler_game(10, 20, 0.5, seed=42)
    assert history[0] == 10


def test_gambler_game_outcome():
    """Test that outcome is either won or lost."""
    history, outcome = gambler_game(10, 20, 0.5, seed=42)
    assert outcome in ['won', 'lost']


def test_gambler_game_win_condition():
    """Test that game ends at target when won."""
    history, outcome = gambler_game(10, 20, 0.5, seed=42)
    if outcome == 'won':
        assert history[-1] == 20


def test_gambler_game_lose_condition():
    """Test that game ends at 0 when lost."""
    history, outcome = gambler_game(10, 20, 0.5, seed=42)
    if outcome == 'lost':
        assert history[-1] == 0


def test_gambler_game_steps():
    """Test that money changes by 1 each step."""
    history, outcome = gambler_game(10, 20, 0.5, seed=42)
    for i in range(1, len(history)):
        diff = abs(history[i] - history[i-1])
        assert diff == 1


def test_gambler_game_reproducibility():
    """Test that same seed gives same result."""
    history1, outcome1 = gambler_game(10, 20, 0.5, seed=42)
    history2, outcome2 = gambler_game(10, 20, 0.5, seed=42)
    assert history1 == history2
    assert outcome1 == outcome2


def test_gambler_game_certain_win():
    """Test with probability 1.0 (always wins)."""
    history, outcome = gambler_game(10, 15, 1.0, seed=42)
    assert outcome == 'won'
    assert history[-1] == 15


def test_gambler_game_certain_loss():
    """Test with probability 0.0 (always loses)."""
    history, outcome = gambler_game(10, 15, 0.0, seed=42)
    assert outcome == 'lost'
    assert history[-1] == 0


def test_simulate_multiple_games_win_rate():
    """Test that win rate is in valid range."""
    stats = simulate_multiple_games(10, 20, 0.5, 100, seed=42)
    assert 0 <= stats['win_rate'] <= 1


def test_simulate_multiple_games_with_high_probability():
    """Test that high win probability leads to high win rate."""
    stats = simulate_multiple_games(10, 15, 0.7, 100, seed=42)
    assert stats['win_rate'] > 0.5


def test_simulate_multiple_games_avg_rounds():
    """Test that average rounds is positive."""
    stats = simulate_multiple_games(10, 20, 0.5, 100, seed=42)
    assert stats['avg_rounds'] > 0


def test_simulate_multiple_games_max_rounds():
    """Test that max rounds >= avg rounds."""
    stats = simulate_multiple_games(10, 20, 0.5, 100, seed=42)
    assert stats['max_rounds'] >= stats['avg_rounds']
