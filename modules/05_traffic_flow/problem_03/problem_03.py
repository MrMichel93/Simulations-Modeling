"""
Problem 3: Traffic Wave Analysis (Medium-Hard)

Analyze traffic waves (phantom jams) that emerge from interactions.
Measure how disturbances propagate through traffic.

Your task:
- Simulate traffic with occasional random braking
- Detect and measure traffic waves
- Calculate wave speed and impact
"""


def simulate_traffic_with_disturbance(num_cars, road_length, max_speed,
                                      safe_distance, disturbance_prob,
                                      num_steps, seed=None):
    """
    Simulate traffic with random disturbances.
    
    Args:
        num_cars: Number of cars
        road_length: Length of circular road
        max_speed: Maximum car speed
        safe_distance: Safe following distance
        disturbance_prob: Probability of random braking per car per step
        num_steps: Number of time steps
        seed: Random seed (optional)
    
    Returns:
        Tuple of (positions_history, speeds_history)
    
    Rules:
        - Normal traffic with braking rules
        - Each step: each car has disturbance_prob chance to brake suddenly
        - Sudden brake: speed becomes 0 for that step
        - This creates waves that propagate backward
    
    Example:
        >>> pos, speeds = simulate_traffic_with_disturbance(5, 50, 3, 5, 0.05, 10, seed=42)
        >>> len(pos) == 11
        True
    """
    import random
    if seed is not None:
        random.seed(seed)
    
    # TODO: Implement this function
    pass


def calculate_average_speed(speeds_history):
    """
    Calculate average speed across all cars and time steps.
    
    Args:
        speeds_history: List of speed lists from simulation
    
    Returns:
        Float: average speed
    """
    # TODO: Implement this function
    pass


def count_stop_events(speeds_history, threshold=0.5):
    """
    Count how many times cars come to near-stop.
    
    Args:
        speeds_history: List of speed lists
        threshold: Speed below which counts as "stopped"
    
    Returns:
        Integer: total number of stop events
    """
    # TODO: Implement this function
    pass


if __name__ == "__main__":
    pos, speeds = simulate_traffic_with_disturbance(10, 100, 5, 10, 0.02, 50, seed=42)
    avg_speed = calculate_average_speed(speeds)
    stops = count_stop_events(speeds)
    print(f"Average speed: {avg_speed:.2f}")
    print(f"Stop events: {stops}")
    print(f"Impact of disturbances visible in reduced average speed")
