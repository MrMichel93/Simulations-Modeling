"""
Problem 1: Simple Prey Population (Easy)

Simulate a prey population with birth and death rates (no predators yet).

Your task:
- Implement prey_population_growth
- Birth rate increases population
- Death rate decreases population
- Track population over time
"""


def prey_population_growth(initial_prey, birth_rate, death_rate, num_steps):
    """
    Simulate prey population with birth and death.
    
    Args:
        initial_prey: Starting number of prey
        birth_rate: Fraction of new prey per step (e.g., 0.1 = 10% growth)
        death_rate: Fraction of prey that die per step
        num_steps: Number of time steps
    
    Returns:
        List of prey populations at each time step
    
    Formula:
        new_prey = old_prey * (1 + birth_rate - death_rate)
    
    Example:
        >>> pop = prey_population_growth(100, 0.1, 0.05, 3)
        >>> pop[0]
        100
    """
    # TODO: Implement this function
    pass


if __name__ == "__main__":
    population = prey_population_growth(100, 0.1, 0.05, 10)
    print(f"Population growth: {[round(p, 1) for p in population]}")
