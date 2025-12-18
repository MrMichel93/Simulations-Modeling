"""
Tests for Problem 3: Network-Based Disease Spread
"""

import pytest
from problem_03 import create_random_network, simulate_network_disease


def test_create_network_size():
    """Test that network has correct number of people."""
    network = create_random_network(10, 3, seed=42)
    assert len(network) == 10


def test_create_network_has_connections():
    """Test that people have connections."""
    network = create_random_network(10, 3, seed=42)
    # At least some people should have connections
    total_connections = sum(len(connections) for connections in network.values())
    assert total_connections > 0


def test_create_network_bidirectional():
    """Test that connections are bidirectional."""
    network = create_random_network(10, 3, seed=42)
    for person, connections in network.items():
        for neighbor in connections:
            # If person is connected to neighbor, neighbor should be connected to person
            assert person in network[neighbor]


def test_create_network_reproducibility():
    """Test that same seed gives same network."""
    network1 = create_random_network(10, 3, seed=42)
    network2 = create_random_network(10, 3, seed=42)
    assert network1 == network2


def test_simulation_initial_infected():
    """Test that simulation starts with correct number infected."""
    network = create_random_network(20, 4, seed=42)
    S, I, R = simulate_network_disease(network, [0, 1, 2], 0.3, 0.1, 5, seed=42)
    assert I[0] == 3
    assert S[0] == 17
    assert R[0] == 0


def test_simulation_length():
    """Test that simulation returns correct length."""
    network = create_random_network(20, 4, seed=42)
    S, I, R = simulate_network_disease(network, [0], 0.3, 0.1, 10, seed=42)
    assert len(S) == 11
    assert len(I) == 11
    assert len(R) == 11


def test_simulation_population_conservation():
    """Test that total population stays constant."""
    network = create_random_network(30, 5, seed=42)
    S, I, R = simulate_network_disease(network, [0, 1], 0.3, 0.1, 20, seed=42)
    for i in range(len(S)):
        assert S[i] + I[i] + R[i] == 30


def test_simulation_reproducibility():
    """Test that same seed gives same results."""
    network = create_random_network(20, 4, seed=42)
    S1, I1, R1 = simulate_network_disease(network, [0], 0.3, 0.1, 10, seed=42)
    
    network = create_random_network(20, 4, seed=42)
    S2, I2, R2 = simulate_network_disease(network, [0], 0.3, 0.1, 10, seed=42)
    
    assert S1 == S2
    assert I1 == I2
    assert R1 == R2


def test_disease_can_spread():
    """Test that disease spreads beyond initial infected."""
    network = create_random_network(50, 6, seed=42)
    S, I, R = simulate_network_disease(network, [0], 0.5, 0.05, 30, seed=42)
    # Total infected + recovered should be more than initial
    assert (I[-1] + R[-1]) > 1


def test_high_transmission_spreads_more():
    """Test that higher transmission leads to more infections."""
    network = create_random_network(50, 5, seed=42)
    
    # Low transmission
    _, _, R_low = simulate_network_disease(network, [0], 0.1, 0.1, 30, seed=42)
    
    network = create_random_network(50, 5, seed=42)
    # High transmission
    _, _, R_high = simulate_network_disease(network, [0], 0.6, 0.1, 30, seed=43)
    
    # Higher transmission should lead to more recovered
    assert R_high[-1] >= R_low[-1]


def test_recovered_increases():
    """Test that recovered population increases over time."""
    network = create_random_network(30, 5, seed=42)
    S, I, R = simulate_network_disease(network, [0, 1], 0.4, 0.2, 30, seed=42)
    assert R[-1] > R[0]
