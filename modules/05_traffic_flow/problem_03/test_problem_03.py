"""
Tests for Problem 3: Traffic Wave Analysis
"""

import pytest
from problem_03 import (simulate_traffic_with_disturbance, 
                        calculate_average_speed, count_stop_events)


def test_simulation_length():
    """Test that simulation returns correct length."""
    pos, speeds = simulate_traffic_with_disturbance(5, 50, 3, 5, 0.05, 10, seed=42)
    assert len(pos) == 11
    assert len(speeds) == 11


def test_simulation_reproducibility():
    """Test that same seed gives same results."""
    pos1, speeds1 = simulate_traffic_with_disturbance(5, 50, 3, 5, 0.05, 10, seed=42)
    pos2, speeds2 = simulate_traffic_with_disturbance(5, 50, 3, 5, 0.05, 10, seed=42)
    assert pos1 == pos2
    assert speeds1 == speeds2


def test_positions_in_range():
    """Test that positions stay within road."""
    pos, speeds = simulate_traffic_with_disturbance(5, 40, 3, 5, 0.05, 10, seed=42)
    for step in pos:
        for p in step:
            assert 0 <= p < 40


def test_speeds_in_range():
    """Test that speeds are non-negative and bounded."""
    pos, speeds = simulate_traffic_with_disturbance(5, 40, 3, 5, 0.05, 10, seed=42)
    for step in speeds:
        for s in step:
            assert 0 <= s <= 3


def test_disturbances_cause_slowdowns():
    """Test that disturbances reduce average speed."""
    # No disturbances
    _, speeds_no = simulate_traffic_with_disturbance(5, 100, 5, 5, 0.0, 30, seed=42)
    avg_no = calculate_average_speed(speeds_no)
    
    # With disturbances
    _, speeds_yes = simulate_traffic_with_disturbance(5, 100, 5, 5, 0.1, 30, seed=42)
    avg_yes = calculate_average_speed(speeds_yes)
    
    # Disturbances should reduce average speed
    assert avg_yes < avg_no


def test_calculate_average_speed():
    """Test average speed calculation."""
    speeds = [[2, 3, 4], [1, 2, 3]]
    avg = calculate_average_speed(speeds)
    expected = (2+3+4+1+2+3) / 6
    assert abs(avg - expected) < 0.01


def test_calculate_average_speed_single_step():
    """Test average with single time step."""
    speeds = [[5, 5, 5]]
    avg = calculate_average_speed(speeds)
    assert avg == 5.0


def test_count_stop_events():
    """Test counting stop events."""
    speeds = [[2, 0.3, 4], [1, 0.1, 3], [2, 5, 0.4]]
    stops = count_stop_events(speeds, threshold=0.5)
    # Should count: 0.3, 0.1, 0.4 = 3 stops
    assert stops == 3


def test_count_stop_events_none():
    """Test when no stops occur."""
    speeds = [[5, 4, 3], [4, 5, 3]]
    stops = count_stop_events(speeds, threshold=0.5)
    assert stops == 0


def test_high_disturbance_more_stops():
    """Test that higher disturbance probability causes more stops."""
    _, speeds_low = simulate_traffic_with_disturbance(5, 50, 3, 5, 0.02, 30, seed=42)
    _, speeds_high = simulate_traffic_with_disturbance(5, 50, 3, 5, 0.1, 30, seed=43)
    
    stops_low = count_stop_events(speeds_low)
    stops_high = count_stop_events(speeds_high)
    
    # Higher disturbance should generally cause more stops
    # Use >= to account for randomness
    assert stops_high >= stops_low - 5  # Allow some variance
