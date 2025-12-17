"""
Coin Flip Experiments

Explore probability through the simplest random event: flipping a coin.
Discover surprising patterns in seemingly simple randomness!
"""

import sys
sys.path.append('../..')

import random
from utils.visualization import plot_time_series, plot_histogram


def flip_coin():
    """Flip a fair coin. Returns 'H' for heads or 'T' for tails."""
    return random.choice(['H', 'T'])


def flip_many_coins(num_flips):
    """Flip a coin many times and return the sequence."""
    return [flip_coin() for _ in range(num_flips)]


def count_heads(flips):
    """Count number of heads in a sequence of flips."""
    return sum(1 for flip in flips if flip == 'H')


def longest_streak(flips):
    """
    Find the longest streak of the same result.
    
    Returns: (length, result) - e.g., (5, 'H') means 5 heads in a row
    """
    if not flips:
        return 0, None
    
    max_length = 1
    max_result = flips[0]
    current_length = 1
    current_result = flips[0]
    
    for i in range(1, len(flips)):
        if flips[i] == current_result:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                max_result = current_result
            current_length = 1
            current_result = flips[i]
    
    # Check final streak
    if current_length > max_length:
        max_length = current_length
        max_result = current_result
    
    return max_length, max_result


def cumulative_heads_percentage(flips):
    """Calculate percentage of heads at each point."""
    heads_count = 0
    percentages = []
    
    for i, flip in enumerate(flips, 1):
        if flip == 'H':
            heads_count += 1
        percentages.append((heads_count / i) * 100)
    
    return percentages


def main():
    print("=" * 60)
    print("COIN FLIP EXPERIMENTS")
    print("=" * 60)
    
    print("\nThe coin flip: the simplest random event.")
    print("But even simple randomness has patterns!")
    
    # Experiment 1: Basic flips
    print("\n" + "=" * 60)
    print("EXPERIMENT 1: Heads vs Tails")
    print("=" * 60)
    
    num_flips = 1000
    
    print(f"\nFlipping a coin {num_flips} times...")
    print("\n🤔 PREDICT:")
    print("   - Will we get exactly 50% heads?")
    print("   - How close to 50% will we get?")
    
    input("\nPress Enter to flip...")
    
    flips = flip_many_coins(num_flips)
    heads = count_heads(flips)
    tails = num_flips - heads
    heads_percent = (heads / num_flips) * 100
    
    print(f"\n📊 Results:")
    print(f"   Heads: {heads} ({heads_percent:.2f}%)")
    print(f"   Tails: {tails} ({100 - heads_percent:.2f}%)")
    print(f"   Difference from 50%: {abs(heads_percent - 50):.2f}%")
    
    # Visualize convergence
    percentages = cumulative_heads_percentage(flips)
    
    plot_time_series(
        [percentages, [50] * len(percentages)],
        title="Heads Percentage Over Time",
        xlabel="Number of Flips",
        ylabel="Percentage Heads",
        labels=["Actual %", "Expected (50%)"],
        colors=["blue", "red"]
    )
    
    print("\n💡 Notice how it converges to 50%!")
    
    # Experiment 2: Streaks
    print("\n" + "=" * 60)
    print("EXPERIMENT 2: Streaks and Patterns")
    print("=" * 60)
    
    print(f"\nIn those {num_flips} flips, what's the longest streak?")
    print("(How many heads or tails in a row?)")
    
    print("\n🤔 PREDICT:")
    print("   - Longest streak of 3?")
    print("   - Longest streak of 10?")
    print("   - What do you think?")
    
    input("\nPress Enter to find out...")
    
    streak_length, streak_result = longest_streak(flips)
    
    print(f"\n📊 Result:")
    print(f"   Longest streak: {streak_length} {streak_result}'s in a row!")
    
    if streak_length >= 10:
        print("   🤯 Wow! That's rare but happens!")
    elif streak_length >= 7:
        print("   😮 Pretty impressive streak!")
    else:
        print("   😊 A typical result")
    
    print("\n💡 Even in randomness, streaks happen!")
    print("   Humans often think streaks mean 'non-random'")
    print("   But they're actually expected in random sequences!")
    
    # Experiment 3: Many trials
    print("\n" + "=" * 60)
    print("EXPERIMENT 3: Distribution of Streaks")
    print("=" * 60)
    
    num_trials = 100
    flips_per_trial = 100
    
    print(f"\nRun {num_trials} trials of {flips_per_trial} flips each")
    print("Record the longest streak in each trial")
    
    input("\nPress Enter to run all trials...")
    
    all_streaks = []
    for _ in range(num_trials):
        trial_flips = flip_many_coins(flips_per_trial)
        streak_len, _ = longest_streak(trial_flips)
        all_streaks.append(streak_len)
    
    avg_streak = sum(all_streaks) / len(all_streaks)
    max_streak = max(all_streaks)
    min_streak = min(all_streaks)
    
    print(f"\n📊 Statistics:")
    print(f"   Average longest streak: {avg_streak:.1f}")
    print(f"   Maximum streak seen: {max_streak}")
    print(f"   Minimum streak seen: {min_streak}")
    
    plot_histogram(
        all_streaks,
        title=f"Longest Streaks in {num_trials} Trials",
        xlabel="Longest Streak Length",
        bins=range(min_streak, max_streak + 2),
        color='coral'
    )
    
    print("\n💡 Most trials have streaks of 5-8!")
    print("   Streaks are NOT unusual in randomness")
    
    # Experiment 4: Gambler's fallacy
    print("\n" + "=" * 60)
    print("EXPERIMENT 4: The Gambler's Fallacy")
    print("=" * 60)
    
    print("\nAfter seeing 5 heads in a row...")
    print("Is tails 'due' to appear?")
    print("\nLet's test this!")
    
    print("\nWe'll find sequences with 5 heads in a row,")
    print("then see what comes next.")
    
    input("\nPress Enter to investigate...")
    
    # Generate many flips and find 5-head sequences
    many_flips = flip_many_coins(10000)
    next_after_5_heads = []
    
    for i in range(len(many_flips) - 6):
        # Check for 5 heads in a row
        if all(many_flips[i + j] == 'H' for j in range(5)):
            # Record the next flip
            next_after_5_heads.append(many_flips[i + 5])
    
    if next_after_5_heads:
        heads_after = sum(1 for flip in next_after_5_heads if flip == 'H')
        percent_heads = (heads_after / len(next_after_5_heads)) * 100
        
        print(f"\n📊 Results:")
        print(f"   Found {len(next_after_5_heads)} sequences of 5 heads")
        print(f"   Next flip was heads: {percent_heads:.1f}% of the time")
        print(f"   Next flip was tails: {100 - percent_heads:.1f}% of the time")
        
        print("\n💡 INSIGHT: Still 50/50!")
        print("   The coin has no memory")
        print("   Previous flips don't affect future flips")
        print("   This is the GAMBLER'S FALLACY")
    
    print("\n" + "=" * 60)
    print("🧪 EXPERIMENTS TO TRY")
    print("=" * 60)
    
    print("\n1. Find the first time 10 heads in a row occurs")
    print("   - How many flips does it take?")
    print("   - Run multiple times - varies a lot!")
    
    print("\n2. Unfair coin")
    print("   - 60% heads, 40% tails")
    print("   - How many flips to detect the bias?")
    
    print("\n3. Alternating patterns")
    print("   - Count HTHTHTHT patterns")
    print("   - Compare to HHHHHHHH patterns")
    print("   - Which is more common?")
    
    print("\n4. Real-world connection")
    print("   - Sports: win streaks")
    print("   - Weather: sunny day streaks")
    print("   - Games: lucky/unlucky runs")
    print("   - Are these really random or not?")


if __name__ == "__main__":
    main()
