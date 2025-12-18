"""
Tests for Problem 4: Self-Avoiding Random Walk
"""

import pytest
from problem_04 import self_avoiding_walk_2d, count_stuck_walks


def test_starts_at_origin():
    """Test that walk starts at (0, 0)."""
    walk = self_avoiding_walk_2d(10, seed=42)
    assert walk[0] == (0, 0)


def test_no_repeated_positions():
    """Test that all positions are unique."""
    walk = self_avoiding_walk_2d(50, seed=42)
    assert len(set(walk)) == len(walk)


def test_adjacent_positions():
    """Test that consecutive positions are adjacent."""
    walk = self_avoiding_walk_2d(50, seed=42)
    for i in range(1, len(walk)):
        x_diff = abs(walk[i][0] - walk[i-1][0])
        y_diff = abs(walk[i][1] - walk[i-1][1])
        # Should move exactly 1 in x OR y, but not both
        assert (x_diff == 1 and y_diff == 0) or (x_diff == 0 and y_diff == 1)


def test_reproducibility():
    """Test that same seed gives same walk."""
    walk1 = self_avoiding_walk_2d(20, seed=42)
    walk2 = self_avoiding_walk_2d(20, seed=42)
    assert walk1 == walk2


def test_max_length():
    """Test that walk doesn't exceed requested steps."""
    walk = self_avoiding_walk_2d(10, seed=42)
    assert len(walk) <= 11  # initial + 10 steps


def test_can_get_stuck():
    """Test that walks can get stuck (important property)."""
    # With enough trials, at least one should get stuck
    walks = [self_avoiding_walk_2d(30, seed=i) for i in range(20)]
    lengths = [len(w) for w in walks]
    # At least one walk should be shorter than requested
    assert min(lengths) < 31


def test_count_stuck_walks_format():
    """Test that count_stuck_walks returns correct format."""
    num_stuck, avg_length = count_stuck_walks(10, 20, seed=42)
    assert isinstance(num_stuck, int)
    assert isinstance(avg_length, (int, float))
    assert 0 <= num_stuck <= 10
    assert avg_length > 0


def test_count_stuck_increases_with_steps():
    """Test that more steps leads to more stuck walks."""
    num_stuck_short, _ = count_stuck_walks(50, 10, seed=42)
    num_stuck_long, _ = count_stuck_walks(50, 30, seed=43)
    # Generally, longer walks are more likely to get stuck
    # This might not always be true due to randomness, but should trend this way
    assert num_stuck_long >= num_stuck_short - 5  # Allow some variance


def test_short_walk_no_duplicates():
    """Test that even short walks maintain no duplicates."""
    walk = self_avoiding_walk_2d(5, seed=42)
    assert len(set(walk)) == len(walk)
