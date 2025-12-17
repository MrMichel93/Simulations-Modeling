"""
Monte Carlo Estimation of Pi

Use RANDOMNESS to calculate a mathematical constant!
This shows the power of simulation.

The Idea:
- Throw random darts at a square
- Count how many land inside an inscribed circle
- The ratio tells us about π!
"""

import sys
sys.path.append('../..')

import random
import math
import matplotlib.pyplot as plt
from utils.visualization import plot_time_series


def throw_dart():
    """
    Throw a random dart at a 1x1 square.
    Returns (x, y) coordinates.
    """
    x = random.random()  # Random number between 0 and 1
    y = random.random()
    return x, y


def is_inside_circle(x, y):
    """
    Check if point (x, y) is inside the quarter circle.
    
    Circle equation: x² + y² = r²
    For a circle of radius 1 centered at origin,
    a point is inside if x² + y² < 1
    """
    distance_from_origin = x**2 + y**2
    return distance_from_origin <= 1.0


def estimate_pi(num_darts):
    """
    Estimate pi by throwing random darts.
    
    Math: The ratio of circle area to square area is π/4
    So: π ≈ 4 * (points in circle) / (total points)
    """
    inside_circle = 0
    
    for _ in range(num_darts):
        x, y = throw_dart()
        if is_inside_circle(x, y):
            inside_circle += 1
    
    pi_estimate = 4 * inside_circle / num_darts
    return pi_estimate


def visualize_darts(num_darts):
    """
    Show where the darts land.
    Visual proof of why this works!
    """
    inside_x, inside_y = [], []
    outside_x, outside_y = [], []
    
    for _ in range(num_darts):
        x, y = throw_dart()
        if is_inside_circle(x, y):
            inside_x.append(x)
            inside_y.append(y)
        else:
            outside_x.append(x)
            outside_y.append(y)
    
    # Plot
    plt.figure(figsize=(10, 10))
    plt.scatter(inside_x, inside_y, color='red', s=1, alpha=0.5, label='Inside circle')
    plt.scatter(outside_x, outside_y, color='blue', s=1, alpha=0.5, label='Outside circle')
    
    # Draw the circle
    circle = plt.Circle((0, 0), 1, fill=False, color='black', linewidth=2)
    plt.gca().add_patch(circle)
    
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.gca().set_aspect('equal')
    plt.xlabel('X', fontsize=12)
    plt.ylabel('Y', fontsize=12)
    plt.title(f'Monte Carlo Pi: {num_darts} Darts', fontsize=14, fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def convergence_to_pi():
    """
    Watch our estimate get closer to π as we throw more darts.
    """
    max_darts = 5000
    estimates = []
    
    inside = 0
    for i in range(1, max_darts + 1):
        x, y = throw_dart()
        if is_inside_circle(x, y):
            inside += 1
        
        current_estimate = 4 * inside / i
        estimates.append(current_estimate)
    
    # Plot
    import math
    actual_pi = [math.pi] * max_darts
    
    plot_time_series(
        [estimates, actual_pi],
        title="Monte Carlo Estimation of π",
        xlabel="Number of Darts Thrown",
        ylabel="Estimated Value of π",
        labels=["Our Estimate", f"Actual π ({math.pi:.6f})"],
        colors=["blue", "red"]
    )


def main():
    print("=" * 60)
    print("MONTE CARLO ESTIMATION OF π")
    print("=" * 60)
    
    print("\n🎯 The Challenge: Calculate π using RANDOM numbers!")
    print("\nThe Method:")
    print("  1. Imagine a quarter circle inside a square")
    print("  2. Throw random 'darts' at the square")
    print("  3. Count how many land in the circle")
    print("  4. The ratio tells us about π!")
    
    print(f"\n📐 Actual value of π: {math.pi}")
    
    input("\nPress Enter to start throwing darts...")
    
    # Experiment with different numbers of darts
    trials = [100, 1000, 10000, 100000]
    
    print("\n" + "=" * 60)
    print("ACCURACY vs NUMBER OF DARTS")
    print("=" * 60)
    
    for num_darts in trials:
        estimate = estimate_pi(num_darts)
        error = abs(estimate - math.pi)
        error_percent = (error / math.pi) * 100
        
        print(f"\n{num_darts:6d} darts: π ≈ {estimate:.6f}")
        print(f"         Error: {error:.6f} ({error_percent:.2f}%)")
    
    print("\n💡 Notice: More darts → better estimate!")
    
    # Visualize where darts land
    print("\n📊 Let's see where 2000 darts land...")
    input("Press Enter to visualize...")
    visualize_darts(2000)
    
    # Show convergence
    print("\n📈 Watch the estimate converge to π...")
    input("Press Enter to see convergence...")
    convergence_to_pi()
    
    print("\n" + "=" * 60)
    print("🤯 MIND = BLOWN")
    print("=" * 60)
    print("\nWe just calculated a mathematical constant using RANDOMNESS!")
    print("This is the power of Monte Carlo methods.")
    print("\nReal-world uses:")
    print("  - Physics simulations")
    print("  - Financial risk analysis")
    print("  - Machine learning")
    print("  - Computer graphics")
    
    print("\n🧪 EXPERIMENT:")
    print("  Can you use this method to estimate the area under a curve?")
    print("  What about estimating integrals?")


if __name__ == "__main__":
    main()
