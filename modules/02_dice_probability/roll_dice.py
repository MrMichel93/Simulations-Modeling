"""
Dice Rolling Simulation

Explore probability through dice rolls.
See how distributions emerge from randomness!
"""

import sys
sys.path.append('../..')

import random
from utils.visualization import plot_histogram, plot_time_series


def roll_die(sides=6):
    """Roll a single die."""
    return random.randint(1, sides)


def roll_multiple_dice(num_dice, sides=6):
    """Roll multiple dice and return the sum."""
    return sum(roll_die(sides) for _ in range(num_dice))


def experiment_single_die(num_rolls):
    """
    Roll a single die many times.
    See if each outcome happens equally often.
    """
    print("\n" + "=" * 60)
    print("EXPERIMENT 1: Single Die")
    print("=" * 60)
    
    print(f"\nRolling a 6-sided die {num_rolls} times...")
    print("\n🤔 PREDICT: Will each number (1-6) appear the same amount?")
    input("Press Enter to run the experiment...")
    
    results = [roll_die() for _ in range(num_rolls)]
    
    # Count each outcome
    counts = {i: results.count(i) for i in range(1, 7)}
    
    print("\n📊 Results:")
    for number, count in counts.items():
        percentage = (count / num_rolls) * 100
        bar = "█" * int(percentage / 2)
        print(f"  {number}: {count:5d} ({percentage:5.2f}%) {bar}")
    
    print("\n💡 Expected: Each number should appear ~16.67% of the time")
    print("   (That's 1/6 = 0.1667)")
    
    # Visualize
    plot_histogram(results, 
                   title=f"Single Die: {num_rolls} Rolls",
                   xlabel="Die Value",
                   bins=6)
    
    return results


def experiment_two_dice(num_rolls):
    """
    Roll TWO dice and sum them.
    Notice how some sums are more common than others!
    """
    print("\n" + "=" * 60)
    print("EXPERIMENT 2: Two Dice (Sum)")
    print("=" * 60)
    
    print(f"\nRolling 2 dice {num_rolls} times and summing them...")
    print("\n🤔 PREDICT: Will all sums (2-12) be equally likely?")
    print("   Or will some sums appear more often?")
    input("Press Enter to run the experiment...")
    
    results = [roll_multiple_dice(2) for _ in range(num_rolls)]
    
    # Count each outcome
    counts = {i: results.count(i) for i in range(2, 13)}
    
    print("\n📊 Results:")
    for number, count in counts.items():
        percentage = (count / num_rolls) * 100
        bar = "█" * int(percentage)
        print(f"  {number:2d}: {count:5d} ({percentage:5.2f}%) {bar}")
    
    print("\n💡 Notice anything?")
    print("   - Why is 7 most common?")
    print("   - Why are 2 and 12 rare?")
    print("   - Think about how many ways you can make each sum!")
    
    # Visualize
    plot_histogram(results,
                   title=f"Two Dice (Sum): {num_rolls} Rolls",
                   xlabel="Sum of Two Dice",
                   bins=11,
                   color='coral')
    
    return results


def convergence_demo():
    """
    Show how results get closer to expected as you roll more.
    The Law of Large Numbers in action!
    """
    print("\n" + "=" * 60)
    print("EXPERIMENT 3: Law of Large Numbers")
    print("=" * 60)
    
    print("\nWatch how the % of 6's converges to 16.67% as we roll more...")
    input("Press Enter to see convergence...")
    
    target = 1/6  # Expected probability of rolling a 6
    max_rolls = 1000
    
    num_sixes = 0
    percentages = []
    
    for roll_num in range(1, max_rolls + 1):
        if roll_die() == 6:
            num_sixes += 1
        
        current_percentage = num_sixes / roll_num
        percentages.append(current_percentage * 100)
    
    print(f"\n📊 After {max_rolls} rolls:")
    print(f"   Actual % of 6's: {percentages[-1]:.2f}%")
    print(f"   Expected: 16.67%")
    print(f"   Difference: {abs(percentages[-1] - 16.67):.2f}%")
    
    # Visualize
    plot_time_series(
        [percentages, [16.67] * max_rolls],
        title="Convergence to Expected Value",
        xlabel="Number of Rolls",
        ylabel="Percentage of 6's",
        labels=["Actual %", "Expected (16.67%)"],
        colors=["blue", "red"]
    )
    
    print("\n💡 See how it bounces around at first, then stabilizes?")
    print("   That's the Law of Large Numbers!")


def main():
    print("=" * 60)
    print("DICE PROBABILITY EXPERIMENTS")
    print("=" * 60)
    print("\nLearn probability by experimenting with code!")
    
    # Experiment 1: Single die
    experiment_single_die(num_rolls=1000)
    
    # Experiment 2: Two dice
    experiment_two_dice(num_rolls=1000)
    
    # Experiment 3: Convergence
    convergence_demo()
    
    print("\n" + "=" * 60)
    print("🧪 YOUR TURN TO EXPERIMENT")
    print("=" * 60)
    print("\nTry these challenges:")
    print("1. Change num_rolls to 100, 10000, 100000 - what happens?")
    print("2. Roll THREE dice instead of two - what's the distribution?")
    print("3. Create a simulation for rolling until you get three 6's in a row")
    print("4. What if the die was unfair? (Hint: use random.choices with weights)")


if __name__ == "__main__":
    main()
