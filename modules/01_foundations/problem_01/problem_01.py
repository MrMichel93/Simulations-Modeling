"""
Problem 1: Simple Counter Simulation (Easy)

Create a simple simulation that counts from a starting number to an ending number.
This demonstrates the basic structure of a simulation with state and time steps.

Your task:
- Implement the count_simulation function
- It should return a list of all numbers from start to end (inclusive)
- Each number represents one time step in the simulation
"""


def count_simulation(start, end):
    """
    Simulate counting from start to end.
    
    Args:
        start: Starting number (inclusive)
        end: Ending number (inclusive)
    
    Returns:
        List of numbers from start to end
    
    Example:
        >>> count_simulation(1, 5)
        [1, 2, 3, 4, 5]
    """
    # TODO: Implement this function
    pass


if __name__ == "__main__":
    # Test your implementation
    result = count_simulation(1, 10)
    print(f"Counting from 1 to 10: {result}")
    
    result = count_simulation(5, 8)
    print(f"Counting from 5 to 8: {result}")
