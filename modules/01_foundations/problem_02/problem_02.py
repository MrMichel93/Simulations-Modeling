"""
Problem 2: Linear Growth Simulation (Medium)

Create a deterministic simulation of linear growth.
Starting with an initial value, add a constant amount at each time step.

Your task:
- Implement the linear_growth function
- Track the value at each time step
- Return the complete history

This models systems with constant growth like:
- Saving a fixed amount of money each month
- A car traveling at constant speed
"""


def linear_growth(initial_value, growth_per_step, num_steps):
    """
    Simulate linear growth over time.
    
    Args:
        initial_value: Starting value
        growth_per_step: Amount added at each step (can be negative for decline)
        num_steps: Number of time steps to simulate
    
    Returns:
        List of values at each time step
    
    Example:
        >>> linear_growth(10, 5, 4)
        [10, 15, 20, 25]
    """
    # TODO: Implement this function
    pass


if __name__ == "__main__":
    # Test your implementation
    result = linear_growth(0, 10, 5)
    print(f"Starting at 0, adding 10 each step: {result}")
    
    result = linear_growth(100, -5, 6)
    print(f"Starting at 100, subtracting 5 each step: {result}")
