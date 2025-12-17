# Module 2: Dice & Probability

## Rolling the Dice on Reality

Randomness is everywhere in real life:
- Will it rain tomorrow?
- Which way will a molecule move?
- Will a mutation occur?
- Will someone click your ad?

Simulations help us understand **probability** - not by calculating formulas, but by **experimenting with code**.

## Core Ideas

### Expected vs Actual

**Expected**: What math predicts (e.g., "fair die rolls each number 1/6 of the time")

**Actual**: What really happens when you try it

Simulations let you see how close reality gets to expectations.

### The Law of Large Numbers

Run an experiment once: Could be anything
Run it 10 times: Still pretty random
Run it 1,000 times: Starting to see a pattern
Run it 100,000 times: Very close to expected

**More trials = closer to the "true" probability**

### Why This Matters

Understanding randomness helps you:
- Distinguish luck from skill
- Evaluate risks
- Design better systems
- Not be fooled by coincidences

## Simulations in This Module

1. **`roll_dice.py`** - Basic dice experiments
   - Single die vs multiple dice
   - See distributions emerge

2. **`coin_flips.py`** - Heads vs tails
   - How long until you get 10 heads in a row?
   - Streaks and patterns

3. **`monte_carlo_pi.py`** - Calculate π with randomness!
   - Throw random darts at a circle
   - Amazing example of simulation power

4. **`probability_game.py`** - Predict then test
   - Interactive learning

## Learning Objectives

By the end of this module, you should be able to:

- [ ] Use random numbers in simulations
- [ ] Understand the difference between expected and actual outcomes
- [ ] Explain why more trials give better results
- [ ] Visualize probability distributions
- [ ] Design your own probability experiments

## Exercises

### 1. Dice Investigation

**Question**: What's more likely - rolling 7 or rolling 12 with two dice?

**Your task**:
- First, predict which is more likely
- Then modify `roll_dice.py` to test it
- Explain WHY one is more common

### 2. Birthday Paradox

**Question**: In a room of 30 people, what's the chance two share a birthday?

**Your task**:
- Code a simulation to test this
- The answer will surprise you!

### 3. Streaks

**Question**: Flip a coin 100 times. What's the longest streak of heads you expect?

**Your task**:
- Predict first
- Run `coin_flips.py` many times
- What's the typical longest streak?

## Challenge: Design Your Own

Create a simulation for a real-world probability question you're curious about:
- Sports statistics?
- Game odds?
- Weather patterns?

Share your findings!

## Next Steps

Ready to see randomness in motion? Move on to **Module 3: Random Walks**!
