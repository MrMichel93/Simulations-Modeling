"""
FOREST FIRE SIMULATION

A sandbox example to inspire your own creations!

Description:
  Simulate how fire spreads through a forest with trees, empty spaces, and burning trees.

Question:
  What density of trees leads to forest-wide fires vs small contained burns?

Rules:
  1. Trees have a small chance to catch fire from lightning
  2. Fire spreads to adjacent trees
  3. Burning trees become empty spaces
  4. Empty spaces slowly regrow into trees

Parameters to explore:
  - tree_density: How packed is the forest?
  - spread_probability: How easily does fire spread?
  - regrowth_rate: How fast do trees grow back?
  - lightning_probability: How often do fires start?

Expected outcomes:
  - Low density → fires don't spread far
  - High density → catastrophic fires
  - There's probably a critical threshold!
"""

import sys
sys.path.append('..')

import random
from utils.visualization import GridAnimation, plot_time_series


# Cell states
EMPTY = 0
TREE = 1
FIRE = 2


def initialize_forest(size, tree_density):
    """
    Create initial forest grid.
    
    Args:
        size: Grid dimension (size x size)
        tree_density: Probability a cell starts as a tree (0.0 to 1.0)
    
    Returns:
        2D list representing the forest
    """
    forest = []
    for i in range(size):
        row = []
        for j in range(size):
            if random.random() < tree_density:
                row.append(TREE)
            else:
                row.append(EMPTY)
        forest.append(row)
    return forest


def count_neighbors_on_fire(forest, row, col):
    """Count how many adjacent cells are on fire."""
    size = len(forest)
    count = 0
    
    # Check all 4 adjacent cells (up, down, left, right)
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_row = row + dr
        new_col = col + dc
        
        # Check bounds
        if 0 <= new_row < size and 0 <= new_col < size:
            if forest[new_row][new_col] == FIRE:
                count += 1
    
    return count


def simulate_step(forest, lightning_prob, spread_prob, regrowth_rate):
    """
    Simulate one time step.
    
    Returns:
        Updated forest grid
    """
    size = len(forest)
    new_forest = [[EMPTY for _ in range(size)] for _ in range(size)]
    
    for i in range(size):
        for j in range(size):
            current_state = forest[i][j]
            
            if current_state == EMPTY:
                # Empty space might regrow
                if random.random() < regrowth_rate:
                    new_forest[i][j] = TREE
                else:
                    new_forest[i][j] = EMPTY
            
            elif current_state == TREE:
                # Tree might catch fire from lightning
                if random.random() < lightning_prob:
                    new_forest[i][j] = FIRE
                # Or from nearby burning trees
                elif count_neighbors_on_fire(forest, i, j) > 0:
                    if random.random() < spread_prob:
                        new_forest[i][j] = FIRE
                    else:
                        new_forest[i][j] = TREE
                else:
                    new_forest[i][j] = TREE
            
            elif current_state == FIRE:
                # Fire burns out, leaving empty space
                new_forest[i][j] = EMPTY
    
    return new_forest


def count_cells(forest):
    """Count number of each cell type."""
    empty = 0
    trees = 0
    fire = 0
    
    for row in forest:
        for cell in row:
            if cell == EMPTY:
                empty += 1
            elif cell == TREE:
                trees += 1
            elif cell == FIRE:
                fire += 1
    
    return empty, trees, fire


def main():
    print("=" * 60)
    print("FOREST FIRE SIMULATION")
    print("=" * 60)
    
    print("\nA simple model of forest dynamics:")
    print("  🟢 Green = Trees")
    print("  🔴 Red = Fire")
    print("  ⚫ Black = Empty")
    
    # Parameters - TRY CHANGING THESE!
    size = 50
    tree_density = 0.6
    lightning_prob = 0.00001
    spread_prob = 0.5
    regrowth_rate = 0.01
    steps = 200
    
    print(f"\nParameters:")
    print(f"  Grid size: {size}x{size}")
    print(f"  Initial tree density: {tree_density * 100}%")
    print(f"  Lightning probability: {lightning_prob}")
    print(f"  Fire spread probability: {spread_prob * 100}%")
    print(f"  Regrowth rate: {regrowth_rate * 100}%")
    
    print("\n🤔 PREDICT:")
    print("   - Will fire spread across the entire forest?")
    print("   - Will the system reach an equilibrium?")
    print("   - What patterns will emerge?")
    
    input("\nPress Enter to start simulation...")
    
    # Initialize
    forest = initialize_forest(size, tree_density)
    
    # Tracking
    empty_history = []
    tree_history = []
    fire_history = []
    grid_history = []
    
    # Run simulation
    print("\n🔥 Running simulation...")
    
    for step in range(steps):
        # Count current state
        empty, trees, fire = count_cells(forest)
        empty_history.append(empty)
        tree_history.append(trees)
        fire_history.append(fire)
        grid_history.append([row[:] for row in forest])  # Deep copy
        
        # Update
        forest = simulate_step(forest, lightning_prob, spread_prob, regrowth_rate)
        
        # Progress indicator
        if step % 50 == 0:
            print(f"  Step {step}/{steps} - Trees: {trees}, Fire: {fire}")
    
    print("\n📊 Simulation complete!")
    
    # Show population over time
    print("\n📈 Generating population graph...")
    plot_time_series(
        [tree_history, fire_history, empty_history],
        title="Forest Dynamics Over Time",
        xlabel="Time Steps",
        ylabel="Number of Cells",
        labels=["Trees", "Fire", "Empty"],
        colors=["green", "red", "black"]
    )
    
    # Animate the forest
    print("\n🎬 Generating forest animation...")
    print("   (This may take a moment...)")
    
    anim = GridAnimation(
        grid_size=(size, size),
        interval=100,
        colormap='RdYlGn',  # Red-Yellow-Green
        title="Forest Fire Spread"
    )
    
    # Add every 5th frame
    for i in range(0, len(grid_history), 5):
        anim.add_frame(grid_history[i])
    
    anim.show()
    
    print("\n💡 OBSERVATIONS:")
    print("   - Did large fires occur?")
    print("   - Did the forest recover?")
    print("   - What patterns emerged?")
    
    print("\n🧪 EXPERIMENTS TO TRY:")
    print("\n1. Vary tree density:")
    print("   - 0.3 (sparse forest)")
    print("   - 0.9 (dense forest)")
    print("   - Find the critical threshold!")
    
    print("\n2. Change spread probability:")
    print("   - 0.2 (fire spreads slowly)")
    print("   - 0.8 (fire spreads easily)")
    
    print("\n3. Adjust regrowth rate:")
    print("   - 0.001 (slow regrowth)")
    print("   - 0.05 (fast regrowth)")
    
    print("\n4. Real-world connections:")
    print("   - Forest management strategies")
    print("   - Controlled burns")
    print("   - Fire breaks (modify to add non-flammable cells)")
    
    print("\n🎨 CREATIVE EXTENSIONS:")
    print("   - Add wind (fire spreads more in one direction)")
    print("   - Add fire breaks")
    print("   - Different tree types (some more flammable)")
    print("   - Water cells that stop fire")
    print("   - Firefighters that extinguish fire")


if __name__ == "__main__":
    main()
