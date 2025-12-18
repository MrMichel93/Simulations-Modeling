"""
Problem 3: Carrying Capacity (Medium-Hard)

Add carrying capacity to limit prey population growth.
Prey can't exceed the environment's maximum sustainable population.

Your task:
- Modify predator-prey model to include carrying capacity
- Prey growth slows as population approaches capacity
- Implement logistic growth for prey
"""


def predator_prey_with_capacity(initial_prey, initial_predators,
                                prey_growth, carrying_capacity,
                                predation_rate, predator_death,
                                num_steps):
    """
    Simulate predator-prey with carrying capacity.
    
    Args:
        initial_prey: Starting prey population
        initial_predators: Starting predator population
        prey_growth: Maximum prey growth rate
        carrying_capacity: Maximum sustainable prey population
        predation_rate: Rate at which predators eat prey
        predator_death: Predator death rate
        num_steps: Number of time steps
    
    Returns:
        Tuple of (prey_history, predator_history)
    
    Update rules:
        # Logistic growth for prey
        growth_factor = prey_growth * (1 - prey / carrying_capacity)
        new_prey = prey + prey * growth_factor - predation_rate * prey * predators
        
        # Predators benefit from eating prey
        new_predators = predators * (1 - predator_death) + predation_rate * prey * predators * 0.1
    
    Example:
        >>> prey, pred = predator_prey_with_capacity(50, 5, 0.5, 100, 0.01, 0.1, 10)
        >>> max(prey) <= 100 * 1.2  # Allow small overshoot
        True
    """
    # TODO: Implement this function
    pass


if __name__ == "__main__":
    prey, pred = predator_prey_with_capacity(50, 5, 0.5, 100, 0.01, 0.1, 50)
    print(f"Max prey: {max(prey):.1f}")
    print(f"Carrying capacity: 100")
    print(f"Final prey: {prey[-1]:.1f}")
    print(f"Final predators: {pred[-1]:.1f}")
