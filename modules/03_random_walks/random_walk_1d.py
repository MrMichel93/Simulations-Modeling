"""
1D Random Walk: Walk on a Number Line

The simplest random walk - just left or right.
Still reveals surprising patterns!
"""

import sys
sys.path.append('../..')

import random
import math
from utils.visualization import plot_time_series, plot_histogram


def random_walk_1d(num_steps, start_position=0):
    """
    Perform a 1D random walk on a number line.
    
    Args:
        num_steps: Number of steps to take
        start_position: Starting position
    
    Returns:
        List of positions at each time step
    """
    position = start_position
    positions = [position]
    
    for _ in range(num_steps):
        # Move left (-1) or right (+1) with equal probability
        step = random.choice([-1, 1])
        position += step
        positions.append(position)
    
    return positions


def main():
    print("=" * 60)
    print("1D RANDOM WALK")
    print("=" * 60)
    
    print("\nImagine walking on a number line.")
    print("Each step, you randomly go left or right.")
    print("Where do you end up?")
    
    # Single walk demonstration
    print("\n" + "=" * 60)
    print("SINGLE WALK")
    print("=" * 60)
    
    num_steps = 1000
    
    print(f"\nTaking {num_steps} random steps...")
    print("\n🤔 PREDICT:")
    print("   - Where will we end up?")
    print("   - How far from start?")
    print("   - Will we return to zero?")
    
    input("\nPress Enter to walk...")
    
    positions = random_walk_1d(num_steps)
    final_position = positions[-1]
    max_position = max(positions)
    min_position = min(positions)
    
    print(f"\n📊 Results:")
    print(f"   Started at: 0")
    print(f"   Ended at: {final_position}")
    print(f"   Maximum reached: {max_position}")
    print(f"   Minimum reached: {min_position}")
    print(f"   Total range: {max_position - min_position}")
    print(f"   Distance from origin: {abs(final_position)}")
    
    # Visualize the walk
    plot_time_series(
        [positions],
        title=f"1D Random Walk: {num_steps} Steps",
        xlabel="Step Number",
        ylabel="Position",
        labels=["Position"],
        colors=["blue"]
    )
    
    # Multiple walks to see distribution
    print("\n" + "=" * 60)
    print("MANY WALKS: Where do they end?")
    print("=" * 60)
    
    num_walks = 500
    num_steps = 100
    
    print(f"\nRunning {num_walks} walks of {num_steps} steps each...")
    input("Press Enter to run all walks...")
    
    final_positions = []
    for _ in range(num_walks):
        positions = random_walk_1d(num_steps)
        final_positions.append(positions[-1])
    
    # Statistics
    avg_distance = sum(abs(pos) for pos in final_positions) / len(final_positions)
    expected_distance = math.sqrt(num_steps)
    
    print(f"\n📊 Statistics:")
    print(f"   Average distance from origin: {avg_distance:.2f}")
    print(f"   Expected (√{num_steps}): {expected_distance:.2f}")
    print(f"   Close match? {abs(avg_distance - expected_distance) < 2}")
    
    # Show distribution
    plot_histogram(
        final_positions,
        title=f"Final Positions: {num_walks} Walks of {num_steps} Steps",
        xlabel="Final Position",
        bins=30,
        color='skyblue'
    )
    
    print("\n💡 OBSERVATIONS:")
    print("   - Distribution is bell-shaped (normal distribution)")
    print("   - Centered at zero (no bias)")
    print("   - Spread relates to √n")
    print("   - Some walks end far from zero, but most are near")
    
    # Return to origin investigation
    print("\n" + "=" * 60)
    print("RETURN TO ORIGIN")
    print("=" * 60)
    
    print("\nHow long until we return to zero?")
    print("(This can take a while!)")
    
    input("\nPress Enter to find return time...")
    
    max_steps = 10000
    position = 0
    steps_taken = 0
    
    for step in range(max_steps):
        position += random.choice([-1, 1])
        steps_taken += 1
        if position == 0 and step > 0:
            break
    
    if position == 0:
        print(f"\n✅ Returned to origin after {steps_taken} steps!")
    else:
        print(f"\n⏱️ Didn't return within {max_steps} steps")
        print("   (Would eventually return if we waited long enough)")
    
    print("\n" + "=" * 60)
    print("🧪 EXPERIMENTS TO TRY")
    print("=" * 60)
    
    print("\n1. Vary the number of steps:")
    print("   - 100, 1000, 10000")
    print("   - How does final distance scale?")
    
    print("\n2. Biased walk:")
    print("   - 60% chance right, 40% left")
    print("   - Where do you end up now?")
    
    print("\n3. First passage time:")
    print("   - How long to reach +10?")
    print("   - Run many times, see distribution")
    
    print("\n4. Symmetric vs asymmetric:")
    print("   - Step size: always 1")
    print("   - vs random size: 1, 2, or 3")
    print("   - Does this change behavior?")
    
    print("\n📚 Fun Facts:")
    print("   - In 1D and 2D: Will ALWAYS return to origin eventually")
    print("   - In 3D: Only 34% chance of returning!")
    print("   - This is a fundamental result in probability theory")


if __name__ == "__main__":
    main()
