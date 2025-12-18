"""
Problem 2: Traffic with Braking (Medium)

Add collision avoidance - cars slow down when too close to car ahead.

Your task:
- Cars brake when they get too close to the car in front
- Implement safe distance logic
- Cars accelerate back to max speed when safe
"""


def simulate_traffic_with_braking(num_cars, road_length, max_speed, 
                                  safe_distance, num_steps):
    """
    Simulate traffic with collision avoidance.
    
    Args:
        num_cars: Number of cars on the road
        road_length: Length of the circular road
        max_speed: Maximum speed of cars
        safe_distance: Minimum distance to maintain from car ahead
        num_steps: Number of time steps
    
    Returns:
        Tuple of (positions_history, speeds_history)
        Each is a list of lists showing state at each time step
    
    Rules:
        - Cars start evenly spaced at max speed
        - Each step:
          * Check distance to car ahead
          * If distance < safe_distance: reduce speed to half
          * If distance >= safe_distance: accelerate toward max_speed
          * Move forward by current speed
    
    Example:
        >>> pos, speeds = simulate_traffic_with_braking(3, 30, 2, 5, 5)
        >>> len(pos) == 6
        True
    """
    # TODO: Implement this function
    # Hint: Track both position and speed for each car
    # Hint: Calculate distance considering circular road
    pass


if __name__ == "__main__":
    positions, speeds = simulate_traffic_with_braking(5, 50, 3, 8, 20)
    print("Final positions:", [round(p, 1) for p in positions[-1]])
    print("Final speeds:", [round(s, 1) for s in speeds[-1]])
