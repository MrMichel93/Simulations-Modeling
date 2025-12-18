"""
Problem 2: Basic Predator-Prey Interaction (Medium)

Simulate both predator and prey populations with simple interactions.

Your task:
- Implement predator_prey_simulation
- Prey grow on their own
- Predators eat prey (reduces prey, increases predators)
- Predators die without food
"""


def predator_prey_simulation(initial_prey, initial_predators, 
                             prey_growth, predation_rate, 
                             predator_death, num_steps):
    """
    Simulate predator-prey dynamics.
    
    Args:
        initial_prey: Starting prey population
        initial_predators: Starting predator population
        prey_growth: Prey birth rate per step
        predation_rate: Rate at which predators eat prey
        predator_death: Predator death rate per step
        num_steps: Number of time steps
    
    Returns:
        Tuple of (prey_history, predator_history)
        Each is a list of populations at each time step
    
    Update rules:
        new_prey = prey * (1 + prey_growth) - predation_rate * prey * predators
        new_predators = predators * (1 - predator_death) + predation_rate * prey * predators * 0.1
    
    Example:
        >>> prey, pred = predator_prey_simulation(100, 10, 0.1, 0.01, 0.1, 5)
        >>> len(prey) == 6
        True
    """
    # TODO: Implement this function
    # Make sure populations don't go negative
    pass


if __name__ == "__main__":
    prey, predators = predator_prey_simulation(100, 10, 0.1, 0.01, 0.1, 20)
    print(f"Prey: {[round(p, 1) for p in prey]}")
    print(f"Predators: {[round(p, 1) for p in predators]}")
