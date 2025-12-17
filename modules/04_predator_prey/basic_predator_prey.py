"""
Classic Predator-Prey Simulation (Lotka-Volterra Model)

Watch two populations cycle as they interact:
- Rabbits (prey) reproduce and get eaten
- Foxes (predators) eat rabbits and starve

Simple rules → Beautiful cyclic behavior
"""

import sys
sys.path.append('../..')

from utils.visualization import plot_time_series


def simulate_predator_prey(initial_prey, initial_predators, 
                           prey_birth_rate, prey_death_rate,
                           predator_birth_rate, predator_death_rate,
                           time_steps):
    """
    Simulate predator-prey dynamics using the Lotka-Volterra model.
    
    Args:
        initial_prey: Starting number of prey (rabbits)
        initial_predators: Starting number of predators (foxes)
        prey_birth_rate: How fast prey reproduce (when safe)
        prey_death_rate: Rate of prey eaten per predator encounter
        predator_birth_rate: How efficiently predators convert prey to offspring
        predator_death_rate: Natural death rate of predators
        time_steps: How long to simulate
    
    Returns:
        (prey_history, predator_history) - population over time
    """
    prey = initial_prey
    predators = initial_predators
    
    prey_history = []
    predator_history = []
    
    for step in range(time_steps):
        # Record current state
        prey_history.append(prey)
        predator_history.append(predators)
        
        # Calculate changes
        # Prey: grow naturally, decrease when eaten
        prey_growth = prey_birth_rate * prey
        prey_eaten = prey_death_rate * prey * predators
        prey_change = prey_growth - prey_eaten
        
        # Predators: grow by eating prey, die naturally
        predator_growth = predator_birth_rate * prey * predators
        predator_deaths = predator_death_rate * predators
        predator_change = predator_growth - predator_deaths
        
        # Update populations
        prey = prey + prey_change
        predators = predators + predator_change
        
        # Prevent negative populations (extinction)
        prey = max(0, prey)
        predators = max(0, predators)
        
        # Check for extinction
        if prey < 0.1 or predators < 0.1:
            print(f"\n⚠️ Extinction at step {step}!")
            if prey < 0.1:
                print("   Prey went extinct!")
            if predators < 0.1:
                print("   Predators went extinct!")
            break
    
    return prey_history, predator_history


def main():
    print("=" * 60)
    print("PREDATOR-PREY SIMULATION")
    print("=" * 60)
    
    print("\nThe Classic Lotka-Volterra Model")
    print("\nRabbits eat grass. Foxes eat rabbits.")
    print("What happens to their populations over time?")
    
    # Parameters (TRY CHANGING THESE!)
    print("\n" + "=" * 60)
    print("STARTING CONDITIONS")
    print("=" * 60)
    
    initial_prey = 40.0
    initial_predators = 9.0
    
    prey_birth_rate = 0.1      # Rabbits reproduce
    prey_death_rate = 0.02     # Rate eaten by foxes
    
    predator_birth_rate = 0.01 # Foxes reproduce by eating
    predator_death_rate = 0.1  # Foxes die naturally
    
    time_steps = 300
    
    print(f"\nPopulations:")
    print(f"  Rabbits (prey): {initial_prey:.0f}")
    print(f"  Foxes (predators): {initial_predators:.0f}")
    
    print(f"\nRates:")
    print(f"  Rabbit birth rate: {prey_birth_rate}")
    print(f"  Rabbit death rate (per fox): {prey_death_rate}")
    print(f"  Fox birth rate (per rabbit eaten): {predator_birth_rate}")
    print(f"  Fox death rate: {predator_death_rate}")
    
    print("\n🤔 PREDICT:")
    print("   - Will populations stay constant?")
    print("   - Will one species dominate?")
    print("   - Will they cycle up and down?")
    print("   - Will extinction occur?")
    
    input("\nPress Enter to run simulation...")
    
    # Run simulation
    print("\n🚀 Running simulation...")
    prey_history, predator_history = simulate_predator_prey(
        initial_prey, initial_predators,
        prey_birth_rate, prey_death_rate,
        predator_birth_rate, predator_death_rate,
        time_steps
    )
    
    # Results
    print(f"\n📊 Results after {len(prey_history)} steps:")
    print(f"  Final rabbits: {prey_history[-1]:.1f}")
    print(f"  Final foxes: {predator_history[-1]:.1f}")
    
    # Find peaks and valleys
    max_prey = max(prey_history)
    min_prey = min(prey_history)
    max_predator = max(predator_history)
    min_predator = min(predator_history)
    
    print(f"\n  Rabbit population ranged: {min_prey:.1f} to {max_prey:.1f}")
    print(f"  Fox population ranged: {min_predator:.1f} to {max_predator:.1f}")
    
    # Visualize
    plot_time_series(
        [prey_history, predator_history],
        title="Predator-Prey Population Dynamics",
        xlabel="Time Steps",
        ylabel="Population",
        labels=["Rabbits (Prey)", "Foxes (Predators)"],
        colors=["green", "red"]
    )
    
    print("\n💡 OBSERVATIONS:")
    print("   - Do you see cycles?")
    print("   - When rabbits peak, where are foxes?")
    print("   - When rabbits are low, where are foxes?")
    print("   - Is there a lag between the peaks?")
    
    print("\n🔍 THE STORY:")
    print("   1. Lots of rabbits → Foxes eat well → Fox population grows")
    print("   2. Lots of foxes → Rabbits get eaten → Rabbit population drops")
    print("   3. Few rabbits → Foxes starve → Fox population drops")
    print("   4. Few foxes → Rabbits thrive → Rabbit population grows")
    print("   5. Repeat!")
    
    print("\n" + "=" * 60)
    print("🧪 EXPERIMENTS TO TRY")
    print("=" * 60)
    
    print("\n1. Change initial populations")
    print("   - Start with 80 rabbits and 5 foxes")
    print("   - How does this affect the cycles?")
    
    print("\n2. Change prey_birth_rate to 0.15")
    print("   - Rabbits reproduce faster")
    print("   - What happens?")
    
    print("\n3. Change predator_death_rate to 0.15")
    print("   - Foxes die faster")
    print("   - Does this help rabbits?")
    
    print("\n4. Try to find parameters that cause extinction")
    print("   - Hint: Make foxes too efficient!")
    
    print("\n5. Try to find the most stable parameters")
    print("   - Smallest cycles = most stable")
    
    print("\n📚 Fun Fact:")
    print("   The lynx-hare cycle in Canada follows this exact pattern!")
    print("   We have 200 years of fur trading data proving it.")


if __name__ == "__main__":
    main()
