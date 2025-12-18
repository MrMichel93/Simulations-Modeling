"""
Problem 4: Multi-Lane Highway (Hard)

Simulate traffic on a multi-lane highway where cars can change lanes.

Your task:
- Implement multi-lane traffic simulation
- Cars change lanes to pass slower vehicles
- Add lane-change rules and safety checks
"""


def simulate_multilane_traffic(num_cars, road_length, num_lanes, max_speed,
                               safe_distance, num_steps, seed=None):
    """
    Simulate multi-lane traffic with lane changes.
    
    Args:
        num_cars: Total number of cars
        road_length: Length of highway
        num_lanes: Number of lanes
        max_speed: Maximum car speed
        safe_distance: Safe following distance
        num_steps: Number of time steps
        seed: Random seed (optional)
    
    Returns:
        Tuple of (positions_history, lanes_history, speeds_history)
        Each is a list of lists tracking all cars at each time step
    
    Rules:
        - Cars start randomly distributed across lanes
        - Each step:
          1. Check if can move faster in another lane
          2. If yes and safe: change lanes
          3. Adjust speed based on car ahead in same lane
          4. Move forward
    
    Lane change conditions (ALL must be true):
        - Car ahead in current lane within 2*safe_distance
        - Target lane has more space (car ahead further)
        - Target lane is safe (no car within safe_distance)
    
    Example:
        >>> pos, lanes, speeds = simulate_multilane_traffic(10, 100, 3, 5, 10, 10, seed=42)
        >>> len(pos) == 11
        True
    """
    import random
    if seed is not None:
        random.seed(seed)
    
    # TODO: Implement this function
    # This is the most complex problem!
    # Break it down:
    # 1. Initialize: assign cars to random lanes and positions
    # 2. Each step:
    #    a. Check lane change opportunities
    #    b. Execute safe lane changes
    #    c. Adjust speeds based on car ahead
    #    d. Move forward
    pass


def calculate_lane_utilization(lanes_history, num_lanes):
    """
    Calculate average utilization of each lane.
    
    Args:
        lanes_history: List of lane assignments from simulation
        num_lanes: Total number of lanes
    
    Returns:
        List of floats: fraction of time each lane is occupied
    
    Example:
        >>> lanes = [[0, 1, 0, 2], [0, 0, 1, 2]]  # 3 lanes
        >>> util = calculate_lane_utilization(lanes, 3)
        >>> len(util) == 3
        True
    """
    # TODO: Implement this function
    pass


if __name__ == "__main__":
    pos, lanes, speeds = simulate_multilane_traffic(15, 200, 3, 6, 12, 50, seed=42)
    
    print(f"Final positions: {[round(p, 1) for p in pos[-1][:5]]}...")
    print(f"Final lanes: {lanes[-1][:5]}...")
    print(f"Final speeds: {[round(s, 1) for s in speeds[-1][:5]]}...")
    
    utilization = calculate_lane_utilization(lanes, 3)
    print(f"\nLane utilization: {[round(u, 2) for u in utilization]}")
