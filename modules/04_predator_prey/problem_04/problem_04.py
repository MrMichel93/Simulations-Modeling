"""
Problem 4: Spatial Predator-Prey (Hard)

Simulate predator-prey on a 2D grid where organisms can only interact
with neighbors. This adds spatial dynamics to the model.

Your task:
- Implement a grid-based predator-prey simulation
- Organisms move randomly to neighboring cells
- Predators eat prey in the same cell
- Track total populations over time
"""

import random


def initialize_grid(width, height, num_prey, num_predators, seed=None):
    """
    Create a grid with randomly placed organisms.
    
    Args:
        width: Grid width
        height: Grid height
        num_prey: Number of prey to place
        num_predators: Number of predators to place
        seed: Random seed (optional)
    
    Returns:
        Dictionary: {(x, y): 'prey' or 'predator' or 'empty'}
    
    Grid cells can contain: 'prey', 'predator', or 'empty'
    """
    if seed is not None:
        random.seed(seed)
    
    # TODO: Implement this function
    pass


def simulate_spatial_predator_prey(width, height, initial_prey, initial_predators,
                                   num_steps, seed=None):
    """
    Simulate spatial predator-prey dynamics.
    
    Args:
        width: Grid width
        height: Grid height
        initial_prey: Initial number of prey
        initial_predators: Initial number of predators
        num_steps: Number of simulation steps
        seed: Random seed (optional)
    
    Returns:
        Tuple of (prey_counts, predator_counts)
        Each is a list of population counts at each time step
    
    Rules per time step:
        1. Each organism tries to move to a random adjacent cell (up/down/left/right)
        2. If a predator moves to a cell with prey:
           - Prey is eaten (removed)
           - Predator stays
        3. Prey reproduce: 10% chance to create offspring in adjacent empty cell
        4. Predators die: 5% chance to die if no prey in adjacent cells
    
    Example:
        >>> prey, pred = simulate_spatial_predator_prey(10, 10, 20, 5, 10, seed=42)
        >>> len(prey) == 11
        True
    """
    if seed is not None:
        random.seed(seed)
    
    # TODO: Implement this function
    # This is complex! Break it down:
    # 1. Initialize grid
    # 2. For each step:
    #    - Count current populations
    #    - Process movement
    #    - Process interactions
    #    - Process reproduction/death
    pass


if __name__ == "__main__":
    prey_hist, pred_hist = simulate_spatial_predator_prey(15, 15, 30, 10, 50, seed=42)
    print(f"Initial - Prey: {prey_hist[0]}, Predators: {pred_hist[0]}")
    print(f"Final - Prey: {prey_hist[-1]}, Predators: {pred_hist[-1]}")
    print(f"Max prey: {max(prey_hist)}")
    print(f"Max predators: {max(pred_hist)}")
