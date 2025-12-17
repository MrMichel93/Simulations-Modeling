"""
Deterministic vs Stochastic: A Direct Comparison

Run the same scenario twice:
1. Deterministic: Everything predictable
2. Stochastic: Randomness included

See how randomness changes everything!
"""

import sys
sys.path.append('../..')

import random
from utils.visualization import side_by_side_comparison


def deterministic_growth(initial, growth_rate, steps):
    """
    Grow population with FIXED growth rate.
    Same inputs = same outputs, always.
    """
    population = initial
    history = []
    
    for _ in range(steps):
        history.append(population)
        population = population * (1 + growth_rate)
    
    return history


def stochastic_growth(initial, growth_rate, steps):
    """
    Grow population with VARIABLE growth rate.
    Each time step has some randomness.
    Same inputs = different outputs each time!
    """
    population = initial
    history = []
    
    for _ in range(steps):
        history.append(population)
        
        # Add randomness: actual growth varies by ±50% of expected
        random_factor = random.uniform(0.5, 1.5)
        actual_growth = growth_rate * random_factor
        
        population = population * (1 + actual_growth)
    
    return history


def main():
    print("=" * 60)
    print("DETERMINISTIC vs STOCHASTIC")
    print("=" * 60)
    
    initial = 100
    growth_rate = 0.05
    steps = 50
    
    print("\nWe'll run two simulations with the SAME starting conditions:")
    print(f"  Initial value: {initial}")
    print(f"  Growth rate: {growth_rate * 100}%")
    print(f"  Time steps: {steps}")
    
    print("\n🎯 DETERMINISTIC:")
    print("   Growth rate is exactly 5% every single time")
    print("   Perfectly predictable")
    
    print("\n🎲 STOCHASTIC:")
    print("   Growth rate varies randomly around 5%")
    print("   Sometimes more, sometimes less")
    print("   Models real-world uncertainty")
    
    input("\nPress Enter to see the comparison...")
    
    # Run both
    det_results = deterministic_growth(initial, growth_rate, steps)
    stoch_results = stochastic_growth(initial, growth_rate, steps)
    
    print(f"\n📊 Final Values:")
    print(f"  Deterministic: {det_results[-1]:.0f}")
    print(f"  Stochastic: {stoch_results[-1]:.0f}")
    print(f"  Difference: {abs(det_results[-1] - stoch_results[-1]):.0f}")
    
    # Visualize
    side_by_side_comparison(
        det_results, 
        stoch_results,
        title1="Deterministic (Predictable)",
        title2="Stochastic (Random)",
        ylabel="Population"
    )
    
    print("\n💡 THINK ABOUT IT:")
    print("   - Which one looks more like the real world?")
    print("   - When would you want deterministic models?")
    print("   - When would you need stochastic models?")
    
    print("\n🧪 TRY THIS:")
    print("   Run this program multiple times.")
    print("   - Does the deterministic graph ever change?")
    print("   - Does the stochastic graph change each time?")


if __name__ == "__main__":
    main()
