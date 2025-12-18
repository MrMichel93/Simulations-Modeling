"""
Problem 4: Spatial SEIR Model (Hard)

Implement a spatial SEIR model (Susceptible-Exposed-Infected-Recovered).
Disease spreads geographically with an incubation period.

Your task:
- Implement SEIR on a 2D grid
- Add exposed state (infected but not yet contagious)
- Disease spreads to neighboring cells
- Track all four populations
"""

import random


def initialize_seir_grid(width, height, initial_infected_positions, seed=None):
    """
    Create a grid with SEIR status for each cell.
    
    Args:
        width: Grid width
        height: Grid height
        initial_infected_positions: List of (x, y) tuples for initial infected
        seed: Random seed (optional)
    
    Returns:
        Dictionary: {(x, y): status} where status is 'S', 'E', 'I', or 'R'
    """
    if seed is not None:
        random.seed(seed)
    
    # TODO: Implement this function
    # All cells start as 'S' except initial_infected_positions which are 'I'
    pass


def simulate_spatial_seir(width, height, initial_infected_positions,
                          transmission_rate, incubation_rate, recovery_rate,
                          num_steps, seed=None):
    """
    Simulate SEIR disease spread on a spatial grid.
    
    Args:
        width: Grid width
        height: Grid height
        initial_infected_positions: List of (x, y) for initially infected
        transmission_rate: Probability of S->E transmission per infected neighbor
        incubation_rate: Probability of E->I progression per step
        recovery_rate: Probability of I->R progression per step
        num_steps: Number of time steps
        seed: Random seed (optional)
    
    Returns:
        Tuple of (S_counts, E_counts, I_counts, R_counts)
        Each is a list of counts at each time step
    
    Rules per time step:
        1. For each 'S' cell with infected neighbors (status 'I'):
           - Becomes 'E' with prob = transmission_rate * num_infected_neighbors
        2. For each 'E' cell:
           - Becomes 'I' with prob = incubation_rate
        3. For each 'I' cell:
           - Becomes 'R' with prob = recovery_rate
    
    Neighbors are up, down, left, right (4 neighbors).
    
    Example:
        >>> S, E, I, R = simulate_spatial_seir(10, 10, [(5,5)], 0.2, 0.3, 0.1, 10, seed=42)
        >>> len(S) == 11
        True
    """
    if seed is not None:
        random.seed(seed)
    
    # TODO: Implement this function
    # This is complex - break it down:
    # 1. Initialize grid
    # 2. For each step:
    #    a. Count current S, E, I, R
    #    b. Process S->E transitions
    #    c. Process E->I transitions
    #    d. Process I->R transitions
    pass


def calculate_epidemic_peak(I_counts):
    """
    Calculate when and what the peak infection was.
    
    Args:
        I_counts: List of infected counts over time
    
    Returns:
        Tuple of (peak_time, peak_count)
    """
    # TODO: Implement this function
    pass


if __name__ == "__main__":
    S, E, I, R = simulate_spatial_seir(20, 20, [(10, 10)], 0.15, 0.2, 0.1, 100, seed=42)
    
    peak_time, peak_count = calculate_epidemic_peak(I)
    
    print(f"Grid: 20x20 = 400 cells")
    print(f"Initial infected: 1 cell at center")
    print(f"\nResults:")
    print(f"  Final S: {S[-1]}")
    print(f"  Final E: {E[-1]}")
    print(f"  Final I: {I[-1]}")
    print(f"  Final R: {R[-1]}")
    print(f"\n  Peak infections: {peak_count} at time step {peak_time}")
    print(f"  Total affected: {E[-1] + I[-1] + R[-1]}")
