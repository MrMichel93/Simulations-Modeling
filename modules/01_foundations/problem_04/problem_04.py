"""
Problem 4: Resource Competition Simulation (Hard)

Create a simulation of two competing resources (A and B).
At each time step:
- Each resource grows by its growth rate
- Resources compete: if total > capacity, both decrease proportionally
- Track both resources over time

Your task:
- Implement the resource_competition function
- Handle growth for both resources
- Apply competition when total exceeds capacity
- Return history for both resources

This models systems like:
- Two species competing for food
- Two companies competing for market share
- Two technologies competing for adoption
"""


def resource_competition(initial_a, initial_b, growth_rate_a, growth_rate_b, 
                        capacity, num_steps):
    """
    Simulate competition between two resources.
    
    Args:
        initial_a: Starting amount of resource A
        initial_b: Starting amount of resource B
        growth_rate_a: Growth rate for A (e.g., 0.1 = 10% growth)
        growth_rate_b: Growth rate for B (e.g., 0.15 = 15% growth)
        capacity: Maximum total resources (A + B) that can be sustained
        num_steps: Number of time steps to simulate
    
    Returns:
        Tuple of two lists: (history_a, history_b)
        Each list contains values at each time step
    
    Algorithm:
        1. Start with initial values
        2. At each step:
           - Grow each resource: new_value = old_value * (1 + growth_rate)
           - Check if total > capacity
           - If yes: scale both down proportionally so total = capacity
        3. Record both values
    
    Example:
        >>> history_a, history_b = resource_competition(10, 10, 0.1, 0.1, 30, 3)
        >>> len(history_a) == 4  # initial + 3 steps
        True
    """
    # TODO: Implement this function
    pass


if __name__ == "__main__":
    # Test your implementation
    history_a, history_b = resource_competition(10, 10, 0.1, 0.15, 50, 10)
    print(f"Resource A over time: {[round(x, 2) for x in history_a]}")
    print(f"Resource B over time: {[round(x, 2) for x in history_b]}")
    print(f"Total at end: {round(history_a[-1] + history_b[-1], 2)}")
