"""
2D Random Walk: The Drunkard's Walk

Watch as a random walker traces an unpredictable path through 2D space.
Each step goes in a completely random direction!
"""

import sys
sys.path.append('../..')

import random
import math
from utils.visualization import plot_walk, plot_scatter, plot_histogram


def take_random_step():
    """
    Take one step in a random direction.
    
    Returns: (dx, dy) - the change in x and y position
    """
    # Choose one of 4 directions: up, down, left, right
    direction = random.choice(['up', 'down', 'left', 'right'])
    
    if direction == 'up':
        return (0, 1)
    elif direction == 'down':
        return (0, -1)
    elif direction == 'left':
        return (-1, 0)
    else:  # right
        return (1, 0)


def random_walk_2d(num_steps, start_x=0, start_y=0):
    """
    Perform a 2D random walk.
    
    Args:
        num_steps: How many steps to take
        start_x, start_y: Starting position
    
    Returns:
        (x_positions, y_positions) - lists of coordinates at each step
    """
    x, y = start_x, start_y
    x_positions = [x]
    y_positions = [y]
    
    for _ in range(num_steps):
        dx, dy = take_random_step()
        x += dx
        y += dy
        x_positions.append(x)
        y_positions.append(y)
    
    return x_positions, y_positions


def distance_from_origin(x, y):
    """Calculate Euclidean distance from origin."""
    return math.sqrt(x**2 + y**2)


def single_walk_demo(num_steps):
    """
    Watch a single walker's journey.
    """
    print("\n" + "=" * 60)
    print("SINGLE RANDOM WALK")
    print("=" * 60)
    
    print(f"\nA walker takes {num_steps} random steps...")
    print("\n🤔 PREDICT:")
    print("   - Will they end up far from where they started?")
    print("   - Will the path loop back on itself?")
    print("   - What will the path look like?")
    
    input("\nPress Enter to watch the walk...")
    
    x_pos, y_pos = random_walk_2d(num_steps)
    
    final_x, final_y = x_pos[-1], y_pos[-1]
    final_distance = distance_from_origin(final_x, final_y)
    
    print(f"\n📊 Results:")
    print(f"   Started at: (0, 0)")
    print(f"   Ended at: ({final_x}, {final_y})")
    print(f"   Distance from origin: {final_distance:.2f}")
    print(f"   Theoretical expectation: ~{math.sqrt(num_steps):.2f}")
    print(f"      (That's √{num_steps})")
    
    # Visualize the path
    plot_walk(x_pos, y_pos, title=f"Random Walk: {num_steps} Steps")
    
    print("\n💡 Notice:")
    print("   - The path is unpredictable!")
    print("   - Distance from origin is much less than total steps")
    print("   - Random movement is inefficient")


def multiple_walks_demo(num_walks, num_steps):
    """
    Run many walks and see the statistical pattern.
    """
    print("\n" + "=" * 60)
    print("MULTIPLE RANDOM WALKS")
    print("=" * 60)
    
    print(f"\nRunning {num_walks} different walks, each with {num_steps} steps...")
    print("\n🤔 PREDICT:")
    print("   - Where will most walkers end up?")
    print("   - Will they cluster somewhere?")
    
    input("\nPress Enter to run all walks...")
    
    final_x_positions = []
    final_y_positions = []
    distances = []
    
    for _ in range(num_walks):
        x_pos, y_pos = random_walk_2d(num_steps)
        final_x = x_pos[-1]
        final_y = y_pos[-1]
        
        final_x_positions.append(final_x)
        final_y_positions.append(final_y)
        distances.append(distance_from_origin(final_x, final_y))
    
    # Statistics
    avg_distance = sum(distances) / len(distances)
    expected_distance = math.sqrt(num_steps)
    
    print(f"\n📊 Statistics:")
    print(f"   Average distance from origin: {avg_distance:.2f}")
    print(f"   Expected (√{num_steps}): {expected_distance:.2f}")
    print(f"   Match? {abs(avg_distance - expected_distance) < 2}")
    
    # Show where walkers ended up
    plot_scatter(
        final_x_positions,
        final_y_positions,
        title=f"Final Positions: {num_walks} Walks of {num_steps} Steps",
        xlabel="X Position",
        ylabel="Y Position",
        color='purple',
        alpha=0.5
    )
    
    # Show distribution of distances
    plot_histogram(
        distances,
        title=f"Distance from Origin: {num_walks} Walks",
        xlabel="Distance",
        bins=30,
        color='green'
    )
    
    print("\n💡 Notice:")
    print("   - Final positions form a circular pattern!")
    print("   - Most distances cluster around √n")
    print("   - This is a fundamental property of random walks")


def main():
    print("=" * 60)
    print("2D RANDOM WALK SIMULATION")
    print("=" * 60)
    
    print("\nRandom walks model many real-world phenomena:")
    print("  • Molecules diffusing through air")
    print("  • Stock prices changing over time")
    print("  • Animals searching for food")
    print("  • Brownian motion of particles")
    
    # Single walk
    single_walk_demo(num_steps=500)
    
    # Multiple walks
    multiple_walks_demo(num_walks=200, num_steps=500)
    
    print("\n" + "=" * 60)
    print("🧪 EXPERIMENTS TO TRY")
    print("=" * 60)
    print("\n1. Change num_steps to 100, 1000, 10000")
    print("   - How does this affect the distance?")
    print("   - Does the √n rule still hold?")
    
    print("\n2. Allow diagonal steps (8 directions instead of 4)")
    print("   - Does this change the behavior?")
    
    print("\n3. Track how long until the walker returns to origin")
    print("   - In 1D and 2D, it WILL return eventually")
    print("   - But it might take a very long time!")
    
    print("\n4. Add 'walls' that the walker can't cross")
    print("   - How does confinement change the behavior?")


if __name__ == "__main__":
    main()
