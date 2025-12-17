"""
SIR Model: Susceptible-Infected-Recovered

The classic epidemic model that shows how diseases spread through populations.

Watch the three curves interact as the epidemic progresses!
"""

import sys
sys.path.append('../..')

from utils.visualization import plot_time_series


def simulate_sir(population, initial_infected, 
                 transmission_rate, recovery_rate, time_steps):
    """
    Simulate disease spread using the SIR model.
    
    Args:
        population: Total population size
        initial_infected: Number infected at start
        transmission_rate: Probability of transmission per contact
        recovery_rate: Fraction of infected who recover each step
        time_steps: How long to simulate
    
    Returns:
        (susceptible_history, infected_history, recovered_history)
    """
    # Initial state
    susceptible = population - initial_infected
    infected = initial_infected
    recovered = 0
    
    # History tracking
    S_history = []
    I_history = []
    R_history = []
    
    for step in range(time_steps):
        # Record current state
        S_history.append(susceptible)
        I_history.append(infected)
        R_history.append(recovered)
        
        # Calculate changes
        # New infections: susceptible people meeting infected people
        # Simplified: rate × (S/N) × I
        # This assumes random mixing of population
        contact_rate = transmission_rate * (susceptible / population) * infected
        new_infections = contact_rate
        
        # Recoveries: fraction of infected recover each step
        new_recoveries = recovery_rate * infected
        
        # Update populations
        susceptible -= new_infections
        infected += new_infections - new_recoveries
        recovered += new_recoveries
        
        # Prevent negative values
        susceptible = max(0, susceptible)
        infected = max(0, infected)
        recovered = min(population, recovered)
        
        # Stop if no more infected
        if infected < 0.1:
            print(f"\n✅ Epidemic ended at step {step}")
            break
    
    return S_history, I_history, R_history


def calculate_r0(transmission_rate, recovery_rate, population):
    """
    Estimate the basic reproduction number R₀.
    
    R₀ = average number of people one infected person infects
    
    Simplified calculation: transmission_rate / recovery_rate
    """
    return transmission_rate / recovery_rate


def main():
    print("=" * 60)
    print("SIR EPIDEMIC MODEL")
    print("=" * 60)
    
    print("\nThe SIR Model tracks three groups:")
    print("  S - Susceptible (can catch disease)")
    print("  I - Infected (currently sick, spreading)")
    print("  R - Recovered (immune, can't spread)")
    
    print("\nFlow: S → I → R")
    
    # Parameters (TRY CHANGING THESE!)
    print("\n" + "=" * 60)
    print("EPIDEMIC PARAMETERS")
    print("=" * 60)
    
    population = 1000
    initial_infected = 1
    transmission_rate = 0.5  # How easily disease spreads
    recovery_rate = 0.1      # How quickly people recover
    time_steps = 200
    
    r0 = calculate_r0(transmission_rate, recovery_rate, population)
    
    print(f"\nPopulation: {population}")
    print(f"Initially infected: {initial_infected}")
    print(f"Transmission rate: {transmission_rate}")
    print(f"Recovery rate: {recovery_rate}")
    print(f"\n📊 Basic Reproduction Number (R₀): {r0:.2f}")
    
    if r0 > 1:
        print("   ⚠️ R₀ > 1: EPIDEMIC will occur!")
    elif r0 == 1:
        print("   ⚖️ R₀ = 1: Endemic (disease persists)")
    else:
        print("   ✅ R₀ < 1: Disease will die out")
    
    print("\n🤔 PREDICT:")
    print("   - How many people will eventually get infected?")
    print("   - When will the infection peak?")
    print("   - Will everyone get infected?")
    print("   - What will the curves look like?")
    
    input("\nPress Enter to run simulation...")
    
    # Run simulation
    print("\n🚀 Running epidemic simulation...")
    S_history, I_history, R_history = simulate_sir(
        population, initial_infected,
        transmission_rate, recovery_rate, time_steps
    )
    
    # Analyze results
    peak_infected = max(I_history)
    peak_time = I_history.index(peak_infected)
    final_recovered = R_history[-1]
    attack_rate = (final_recovered / population) * 100
    
    print(f"\n📊 RESULTS:")
    print(f"  Peak infections: {peak_infected:.0f} people")
    print(f"  Peak occurred at: step {peak_time}")
    print(f"  Total infected (ever): {final_recovered:.0f}")
    print(f"  Attack rate: {attack_rate:.1f}% of population")
    print(f"  Never infected: {population - final_recovered:.0f} people")
    
    # Visualize
    plot_time_series(
        [S_history, I_history, R_history],
        title=f"SIR Epidemic Model (R₀={r0:.2f})",
        xlabel="Time Steps",
        ylabel="Number of People",
        labels=["Susceptible", "Infected", "Recovered"],
        colors=["blue", "red", "green"]
    )
    
    print("\n💡 OBSERVE THE CURVES:")
    print("   - Susceptible (blue): Starts high, decreases")
    print("   - Infected (red): Rises, peaks, falls to zero")
    print("   - Recovered (green): Starts zero, increases")
    print("   - All three sum to total population")
    
    print("\n🔍 KEY INSIGHTS:")
    print("   1. Exponential growth at first (scary!)")
    print("   2. Peak when susceptible becomes scarce")
    print("   3. Epidemic ends before everyone infected (herd immunity)")
    
    print("\n" + "=" * 60)
    print("🧪 EXPERIMENTS TO TRY")
    print("=" * 60)
    
    print("\n1. VARY TRANSMISSION RATE:")
    print("   - transmission_rate = 0.3 (less contagious)")
    print("   - transmission_rate = 0.7 (more contagious)")
    print("   - How does R₀ and peak change?")
    
    print("\n2. INTERVENTION SIMULATION:")
    print("   - Start with transmission_rate = 0.5")
    print("   - Run simulation")
    print("   - Now try transmission_rate = 0.25")
    print("   - That's 'social distancing' - see the difference?")
    
    print("\n3. FAST vs SLOW RECOVERY:")
    print("   - recovery_rate = 0.05 (long illness)")
    print("   - recovery_rate = 0.2 (quick recovery)")
    print("   - How does this affect the epidemic?")
    
    print("\n4. FIND THE THRESHOLD:")
    print("   - Adjust parameters to get R₀ close to 1.0")
    print("   - See how the epidemic barely happens")
    
    print("\n5. SUPERSPREADER EVENT:")
    print("   - initial_infected = 50 (conference, concert, etc.)")
    print("   - How does this change the outcome?")
    
    print("\n📚 Real-World Applications:")
    print("   - COVID-19 policy decisions")
    print("   - Flu vaccination strategies")
    print("   - Hospital capacity planning")
    print("   - Quarantine effectiveness")
    
    print("\n⚠️ Important Note:")
    print("   Real epidemics are more complex than this model!")
    print("   But the basic principles hold true.")
    print("   This helps us understand the fundamentals.")


if __name__ == "__main__":
    main()
