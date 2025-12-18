"""
Problem 3: Network-Based Disease Spread (Medium-Hard)

Simulate disease spread on a social network.
People are connected by relationships, and disease spreads along connections.

Your task:
- Implement network-based disease simulation
- Disease spreads from infected to susceptible neighbors
- Track infection spread through the network
"""

import random


def create_random_network(num_people, connections_per_person, seed=None):
    """
    Create a random social network.
    
    Args:
        num_people: Number of people in the network
        connections_per_person: Average connections per person
        seed: Random seed (optional)
    
    Returns:
        Dictionary: {person_id: [list of connected person_ids]}
    
    Example:
        >>> network = create_random_network(5, 2, seed=42)
        >>> len(network) == 5
        True
    """
    if seed is not None:
        random.seed(seed)
    
    # TODO: Implement this function
    # Hint: Make sure connections are bidirectional
    pass


def simulate_network_disease(network, initial_infected, transmission_prob,
                             recovery_prob, num_steps, seed=None):
    """
    Simulate disease spread on a network.
    
    Args:
        network: Dictionary of connections from create_random_network
        initial_infected: List of person_ids initially infected
        transmission_prob: Probability of transmission per contact
        recovery_prob: Probability of recovery per step
        num_steps: Number of time steps
        seed: Random seed (optional)
    
    Returns:
        Tuple of (S_history, I_history, R_history)
        Each is a count at each time step
    
    Rules per time step:
        1. For each infected person:
           - Try to infect each susceptible neighbor (prob = transmission_prob)
        2. For each infected person:
           - Try to recover (prob = recovery_prob)
    
    Example:
        >>> network = create_random_network(10, 3, seed=42)
        >>> S, I, R = simulate_network_disease(network, [0], 0.3, 0.1, 10, seed=42)
        >>> len(S) == 11
        True
    """
    if seed is not None:
        random.seed(seed)
    
    # TODO: Implement this function
    # Track status of each person: 'S', 'I', or 'R'
    pass


if __name__ == "__main__":
    network = create_random_network(100, 5, seed=42)
    S, I, R = simulate_network_disease(network, [0, 1], 0.3, 0.1, 50, seed=42)
    
    print(f"Network: 100 people, avg 5 connections each")
    print(f"Initial infected: 2 people")
    print(f"\nResults:")
    print(f"  Final S: {S[-1]}")
    print(f"  Final I: {I[-1]}")
    print(f"  Final R: {R[-1]}")
    print(f"  Peak infected: {max(I)}")
