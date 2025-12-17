"""
Basic Traffic Flow Simulation

Watch how traffic jams emerge from simple driving rules!

Model: Cars on a circular road (no beginning or end)
Rules: Speed up if space ahead, slow down if too close
Result: Spontaneous traffic waves
"""

import sys
sys.path.append('../..')

import random
from utils.visualization import GridAnimation, plot_time_series


class Car:
    """A single car with position and velocity."""
    
    def __init__(self, position, velocity=5):
        self.position = position
        self.velocity = velocity
        self.max_velocity = 5  # Maximum speed
    
    def __repr__(self):
        return f"Car(pos={self.position}, vel={self.velocity})"


def simulate_traffic(num_cars, road_length, time_steps, 
                     slow_probability=0.1):
    """
    Simulate traffic on a circular road.
    
    Args:
        num_cars: Number of cars on the road
        road_length: Length of the road (circular)
        time_steps: How long to simulate
        slow_probability: Chance each car randomly slows down
    
    Returns:
        (positions_over_time, velocities_over_time, grid_history)
    """
    # Initialize cars evenly spaced
    spacing = road_length // num_cars
    cars = [Car(i * spacing) for i in range(num_cars)]
    
    positions_over_time = []
    velocities_over_time = []
    grid_history = []
    
    for step in range(time_steps):
        # Record state
        positions_over_time.append([car.position for car in cars])
        velocities_over_time.append([car.velocity for car in cars])
        
        # Create grid visualization
        # Note: Add 1 to velocity to avoid zero values in visualization
        # (makes stopped cars visible as minimum value, not background)
        grid = [0] * road_length
        for car in cars:
            grid[car.position % road_length] = car.velocity + 1
        grid_history.append(grid)
        
        # Update each car
        for i, car in enumerate(cars):
            # Find car ahead
            next_car = cars[(i + 1) % len(cars)]
            
            # Calculate gap
            if next_car.position > car.position:
                gap = next_car.position - car.position - 1
            else:
                gap = (road_length - car.position) + next_car.position - 1
            
            # Rule 1: Accelerate if possible
            if car.velocity < car.max_velocity:
                car.velocity += 1
            
            # Rule 2: Brake if too close to car ahead
            if car.velocity > gap:
                car.velocity = gap
            
            # Rule 3: Random slowdown (driver distraction, etc.)
            if car.velocity > 0 and random.random() < slow_probability:
                car.velocity -= 1
        
        # Move cars
        for car in cars:
            car.position = (car.position + car.velocity) % road_length
    
    return positions_over_time, velocities_over_time, grid_history


def analyze_traffic_flow(velocities_over_time):
    """
    Calculate average velocity over time.
    Shows how traffic flow changes.
    """
    avg_velocities = []
    for velocities in velocities_over_time:
        avg = sum(velocities) / len(velocities)
        avg_velocities.append(avg)
    return avg_velocities


def main():
    print("=" * 60)
    print("TRAFFIC FLOW SIMULATION")
    print("=" * 60)
    
    print("\nSimulate cars on a circular road.")
    print("\nEach car follows simple rules:")
    print("  1. Speed up if there's space ahead")
    print("  2. Slow down if getting too close")
    print("  3. Occasionally slow down randomly (driver distraction)")
    
    # Parameters (TRY CHANGING THESE!)
    print("\n" + "=" * 60)
    print("SETUP")
    print("=" * 60)
    
    num_cars = 25
    road_length = 100
    time_steps = 200
    slow_probability = 0.1
    
    density = num_cars / road_length
    
    print(f"\nRoad length: {road_length} cells")
    print(f"Number of cars: {num_cars}")
    print(f"Density: {density:.2f} cars per cell")
    print(f"Random slowdown chance: {slow_probability * 100}%")
    
    print("\n🤔 PREDICT:")
    print("   - Will traffic flow smoothly?")
    print("   - Will jams form spontaneously?")
    print("   - Will all cars maintain constant speed?")
    
    input("\nPress Enter to start simulation...")
    
    # Run simulation
    print("\n🚀 Running simulation...")
    positions, velocities, grid_history = simulate_traffic(
        num_cars, road_length, time_steps, slow_probability
    )
    
    # Analyze flow
    avg_velocities = analyze_traffic_flow(velocities)
    
    initial_avg = avg_velocities[0]
    final_avg = avg_velocities[-1]
    min_avg = min(avg_velocities)
    
    print(f"\n📊 Results:")
    print(f"  Initial average velocity: {initial_avg:.2f}")
    print(f"  Final average velocity: {final_avg:.2f}")
    print(f"  Minimum average velocity: {min_avg:.2f}")
    print(f"  Maximum velocity: 5 (speed limit)")
    
    if min_avg < 2:
        print("\n⚠️ Significant jams detected!")
    elif min_avg < 4:
        print("\n⚡ Some slowdowns occurred")
    else:
        print("\n✅ Traffic flowed smoothly!")
    
    # Visualize average velocity over time
    print("\n📈 Generating average velocity graph...")
    plot_time_series(
        [avg_velocities],
        title="Average Traffic Velocity Over Time",
        xlabel="Time Step",
        ylabel="Average Velocity",
        labels=["Average Velocity"],
        colors=["blue"]
    )
    
    # Animate traffic
    print("\n🎬 Generating traffic animation...")
    print("   (This may take a moment...)")
    
    anim = GridAnimation(
        grid_size=(1, road_length),
        interval=50,
        colormap='RdYlGn',
        title="Traffic Flow (Green=Fast, Red=Stopped)"
    )
    
    # Add every 5th frame to keep animation reasonable
    for i in range(0, len(grid_history), 5):
        anim.add_frame([grid_history[i]])
    
    anim.show()
    
    print("\n💡 OBSERVATIONS:")
    print("   - Do you see waves of congestion?")
    print("   - Do jams travel backwards?")
    print("   - Can one slow car trigger a jam?")
    
    print("\n" + "=" * 60)
    print("🧪 EXPERIMENTS TO TRY")
    print("=" * 60)
    
    print("\n1. Change density:")
    print("   - num_cars = 10  (low density)")
    print("   - num_cars = 50  (high density)")
    print("   - Find the critical density where jams start!")
    
    print("\n2. Remove randomness:")
    print("   - slow_probability = 0")
    print("   - Does traffic still jam without random events?")
    
    print("\n3. Increase randomness:")
    print("   - slow_probability = 0.3")
    print("   - More chaos!")
    
    print("\n4. Real-world connection:")
    print("   - This model explains 'phantom' traffic jams")
    print("   - No accident needed - jams emerge spontaneously!")
    print("   - One distracted driver can cause chain reaction")
    
    print("\n📚 Fun Fact:")
    print("   Self-driving cars could eliminate phantom jams by")
    print("   maintaining perfect spacing and smooth acceleration!")


if __name__ == "__main__":
    main()
