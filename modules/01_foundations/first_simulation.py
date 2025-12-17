"""
Your First Simulation: Population Growth

This demonstrates the key components of any simulation:
- State (current population)
- Rules (how population changes)
- Time steps (updating over time)
- Visualization (seeing the results)

This is a DETERMINISTIC simulation - same input always gives same output.
"""

import sys
sys.path.append('../..')

from utils.visualization import plot_time_series


def simulate_population(initial_population, growth_rate, num_steps):
    """
    Simulate population growth over time.
    
    Args:
        initial_population: Starting number of organisms
        growth_rate: Fraction of population added each step (e.g., 0.05 = 5% growth)
        num_steps: How many time steps to simulate
    
    Returns:
        List of population values at each time step
    """
    # State: track the population over time
    population_history = []
    current_population = initial_population
    
    # Time steps: loop through each moment in time
    for step in range(num_steps):
        # Record current state
        population_history.append(current_population)
        
        # Rules: how does population change?
        # New population = old population + (growth_rate * old population)
        growth = growth_rate * current_population
        current_population = current_population + growth
    
    return population_history


def main():
    print("=" * 60)
    print("POPULATION GROWTH SIMULATION")
    print("=" * 60)
    
    # Parameters (try changing these!)
    initial_population = 100
    growth_rate = 0.05  # 5% growth each step
    num_steps = 100
    
    print(f"\nStarting conditions:")
    print(f"  Initial population: {initial_population}")
    print(f"  Growth rate: {growth_rate * 100}% per time step")
    print(f"  Time steps: {num_steps}")
    
    print("\n🤔 PREDICT: Before running, guess...")
    print("   - Will population grow faster or slower as time goes on?")
    print("   - What shape will the graph be?")
    input("\nPress Enter when you've made your prediction...")
    
    # Run the simulation
    print("\n🚀 Running simulation...")
    results = simulate_population(initial_population, growth_rate, num_steps)
    
    # Show results
    final_population = results[-1]
    print(f"\n📊 Results:")
    print(f"  Final population: {final_population:.0f}")
    print(f"  Total growth: {final_population - initial_population:.0f}")
    print(f"  Growth factor: {final_population / initial_population:.2f}x")
    
    # Visualize
    print("\n📈 Generating graph...")
    plot_time_series(
        [results],
        title="Population Growth Over Time",
        xlabel="Time Step",
        ylabel="Population",
        labels=["Population"],
        colors=["green"]
    )
    
    print("\n💡 REFLECT:")
    print("   - Did the graph match your prediction?")
    print("   - Why does it curve upward instead of being a straight line?")
    print("   - What does this tell you about 'exponential growth'?")
    
    print("\n🧪 EXPERIMENT:")
    print("   Try changing the parameters at the top of main():")
    print("   - growth_rate = 0.10  (what happens?)")
    print("   - growth_rate = -0.05 (what does this model?)")
    print("   - initial_population = 1000 (does shape change?)")


if __name__ == "__main__":
    main()
