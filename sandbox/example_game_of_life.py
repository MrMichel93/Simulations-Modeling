"""
CONWAY'S GAME OF LIFE

A classic cellular automaton that demonstrates emergence.
Simple rules create complex, lifelike patterns!

Description:
  Grid of cells that are alive or dead. Each generation,
  cells live or die based on their neighbors.

Rules (the "laws of life"):
  1. Any live cell with 2-3 neighbors survives
  2. Any dead cell with exactly 3 neighbors becomes alive
  3. All other cells die or stay dead

Question:
  What patterns emerge from these simple rules?

Expected outcomes:
  - Still lifes (stable patterns)
  - Oscillators (repeating patterns)
  - Gliders (moving patterns)
  - Chaos and order together!
"""

import sys
sys.path.append('..')

import random
from utils.visualization import GridAnimation, plot_grid


def create_random_grid(size, density=0.3):
    """
    Create a random initial grid.
    
    Args:
        size: Grid dimension (size x size)
        density: Probability a cell starts alive
    
    Returns:
        2D list (0 = dead, 1 = alive)
    """
    return [[1 if random.random() < density else 0 
             for _ in range(size)] 
            for _ in range(size)]


def create_glider():
    """
    Create a classic 'glider' pattern.
    This pattern moves diagonally across the grid!
    """
    size = 50
    grid = [[0 for _ in range(size)] for _ in range(size)]
    
    # Place glider in top-left
    glider_pattern = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1]
    ]
    
    start_row, start_col = 5, 5
    for i, row in enumerate(glider_pattern):
        for j, val in enumerate(row):
            grid[start_row + i][start_col + j] = val
    
    return grid


def count_alive_neighbors(grid, row, col):
    """Count how many of the 8 neighbors are alive."""
    size = len(grid)
    count = 0
    
    # Check all 8 neighbors
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue  # Skip self
            
            # Wrap around edges (toroidal topology - like a donut)
            # This means the top connects to bottom, left connects to right
            new_row = (row + dr) % size
            new_col = (col + dc) % size
            
            count += grid[new_row][new_col]
    
    return count


def next_generation(grid):
    """
    Compute the next generation based on the rules.
    
    Returns:
        New grid for next generation
    """
    size = len(grid)
    new_grid = [[0 for _ in range(size)] for _ in range(size)]
    
    for i in range(size):
        for j in range(size):
            alive = grid[i][j] == 1
            neighbors = count_alive_neighbors(grid, i, j)
            
            # Apply the rules
            if alive:
                # Live cell with 2-3 neighbors survives
                if neighbors in [2, 3]:
                    new_grid[i][j] = 1
                # Otherwise dies (overpopulation or loneliness)
            else:
                # Dead cell with exactly 3 neighbors becomes alive
                if neighbors == 3:
                    new_grid[i][j] = 1
    
    return new_grid


def count_alive(grid):
    """Count total number of alive cells."""
    return sum(sum(row) for row in grid)


def main():
    print("=" * 60)
    print("CONWAY'S GAME OF LIFE")
    print("=" * 60)
    
    print("\nThe classic cellular automaton!")
    print("\nRules:")
    print("  1. Live cell with 2-3 neighbors → survives")
    print("  2. Dead cell with exactly 3 neighbors → becomes alive")
    print("  3. All other cells → die or stay dead")
    
    print("\n🤔 PREDICT:")
    print("   - Will patterns stabilize?")
    print("   - Will everything die?")
    print("   - Will patterns emerge and persist?")
    
    print("\nChoose starting pattern:")
    print("  1. Random grid")
    print("  2. Classic glider")
    choice = input("Enter 1 or 2: ").strip()
    
    if choice == "2":
        grid = create_glider()
        print("\n🚀 Starting with a glider pattern!")
        print("   Watch it move diagonally across the grid!")
    else:
        size = 50
        density = 0.3
        grid = create_random_grid(size, density)
        print(f"\n🎲 Starting with random grid ({density * 100}% alive)")
    
    generations = 100
    
    print(f"\nRunning {generations} generations...")
    input("Press Enter to start...")
    
    # Track history
    grid_history = []
    population_history = []
    
    # Run simulation
    print("\n⏳ Computing generations...")
    for gen in range(generations):
        grid_history.append([row[:] for row in grid])  # Deep copy
        population = count_alive(grid)
        population_history.append(population)
        
        if gen % 20 == 0:
            print(f"  Generation {gen}: {population} alive")
        
        grid = next_generation(grid)
    
    print("\n✅ Simulation complete!")
    
    # Show initial and final states
    print("\n📊 Initial state:")
    plot_grid(grid_history[0], 
              title="Generation 0", 
              colormap='binary')
    
    print("\n📊 Final state:")
    plot_grid(grid_history[-1], 
              title=f"Generation {generations}", 
              colormap='binary')
    
    # Animate
    print("\n🎬 Generating animation...")
    print("   (This may take a moment...)")
    
    anim = GridAnimation(
        grid_size=(len(grid), len(grid)),
        interval=100,
        colormap='binary',
        title="Conway's Game of Life"
    )
    
    # Add every 2nd frame for smoother viewing
    for i in range(0, len(grid_history), 2):
        anim.add_frame(grid_history[i])
    
    anim.show()
    
    print("\n💡 OBSERVATIONS:")
    print("   - Did you see stable patterns (still lifes)?")
    print("   - Did you see oscillators (blinkers)?")
    print("   - Did patterns move (gliders)?")
    print("   - Did complexity emerge from simple rules?")
    
    print("\n🧪 EXPERIMENTS TO TRY:")
    print("\n1. Different densities:")
    print("   - 0.1 (sparse)")
    print("   - 0.5 (dense)")
    print("   - How does this affect outcomes?")
    
    print("\n2. Different rules:")
    print("   - Change survival conditions")
    print("   - 'HighLife': Also revive with 6 neighbors")
    print("   - Create your own cellular automaton!")
    
    print("\n3. Known patterns to try:")
    print("   - Blinker: 3 cells in a row")
    print("   - Block: 2x2 square (stable)")
    print("   - Toad: 3+3 pattern (oscillates)")
    print("   - Glider gun: Creates infinite gliders!")
    
    print("\n4. Investigations:")
    print("   - What's the longest-lived random configuration?")
    print("   - Can you create a pattern that grows forever?")
    print("   - What's the smallest oscillator?")
    
    print("\n🌟 FUN FACTS:")
    print("   - Game of Life is Turing complete!")
    print("   - People have built computers inside it")
    print("   - It demonstrates emergence perfectly")
    print("   - Simple rules → incredible complexity")
    
    print("\n📚 Real-World Connections:")
    print("   - Biological systems")
    print("   - Crystal growth")
    print("   - Social dynamics")
    print("   - Urban development")
    print("   - Any system where local interactions create global patterns!")


if __name__ == "__main__":
    main()
