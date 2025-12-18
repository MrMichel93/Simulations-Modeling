"""
Problem 1: Single Lane Traffic (Easy)

Simulate cars moving on a single lane road (circular track).
Each car has a position and moves forward each time step.

Your task:
- Implement a simple traffic simulation
- Cars move forward at constant speed
- Track positions over time
"""


def simulate_single_lane(num_cars, road_length, speed, num_steps):
    """
    Simulate cars on a single circular lane.
    
    Args:
        num_cars: Number of cars on the road
        road_length: Length of the circular road
        speed: Distance each car moves per step
        num_steps: Number of time steps
    
    Returns:
        List of lists: positions of all cars at each time step
        Format: [[car0_pos, car1_pos, ...], ...]
    
    Rules:
        - Cars start evenly spaced
        - Each car moves forward by 'speed' each step
        - Position wraps around (circular road)
    
    Example:
        >>> positions = simulate_single_lane(3, 10, 1, 2)
        >>> len(positions) == 3  # initial + 2 steps
        True
    """
    # TODO: Implement this function
    # Hint: Use modulo (%) for circular road
    pass


if __name__ == "__main__":
    positions = simulate_single_lane(5, 20, 2, 10)
    print("Initial positions:", positions[0])
    print("Final positions:", positions[-1])
