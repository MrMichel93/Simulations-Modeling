# Module 2: Dice & Probability

## Rolling the Dice on Reality

Randomness is everywhere in real life. Think about your day:
- Will it rain tomorrow? (Weather is chaotic and hard to predict)
- Will you hit a green light or red? (Depends on when you arrive)
- Which way will a molecule move? (Quantum randomness!)
- Will a mutation occur in a DNA copy? (Random errors happen)
- Will someone click your ad? (Human behavior is unpredictable)

**Here's the Big Idea:**
We can't predict individual random events, but we CAN predict patterns when we repeat them many times!

*Analogy*: You can't predict which side a single coin flip will land on. But if you flip a coin 1000 times, you can confidently predict you'll get ABOUT 500 heads. The individual is random, the pattern is predictable!

Simulations help us understand **probability** - not by memorizing formulas, but by **experimenting with code**. It's like being a scientist who runs thousands of experiments in seconds!

## Core Ideas

### Expected vs Actual

**Expected**: What math/theory predicts 
- Example: A fair die should roll each number 1/6 of the time (about 16.67%)
- This is the "theoretical probability"

**Actual**: What really happens when you try it
- Example: Roll a die 6 times, you might get: 2, 2, 5, 1, 6, 2 - three 2's and no 3 or 4!
- This is the "experimental probability"

**Key Insight:** They might not match perfectly at first, but the more you try, the closer they get!

*Real-life analogy*: A basketball player might have a 75% free throw average (expected). But on any given night, they might go 3/10 (actual). Over a season with hundreds of attempts, their actual percentage gets closer to 75%.

Simulations let you see how close reality gets to expectations - and understand WHY differences occur.

### The Law of Large Numbers

This is one of the most important ideas in probability!

**The Pattern:**
- Run an experiment once: Could be anything (total randomness!)
- Run it 10 times: Still pretty random, hard to see a pattern
- Run it 1,000 times: Starting to see a clear pattern emerge
- Run it 100,000 times: Very close to the theoretical prediction
- Run it 1,000,000 times: Almost exactly matches theory!

**More trials = closer to the "true" probability**

*Casino analogy*: This is why casinos always make money! On any single bet, you might win or they might win. But over millions of bets, the math ensures they come out ahead. The house edge is small (maybe 2%), but over millions of plays, it's guaranteed profit.

*Coin flip example*:
- Flip 10 times: Might get 7 heads, 3 tails (70% heads!)
- Flip 100 times: Might get 56 heads, 44 tails (56% heads)
- Flip 10,000 times: Might get 5,032 heads, 4,968 tails (50.32% heads)
- Flip 1,000,000 times: Almost certainly around 50% heads

The law doesn't guarantee exact 50/50, but it guarantees you'll get close to it!

### Why This Matters

Understanding randomness helps you in everyday life:

**1. Distinguish luck from skill**
- *Example*: Your friend makes 5 basketball shots in a row. Are they really good, or just lucky? If they usually miss 90% of shots, it's probably luck. If they usually make 60%, it's probably skill.
- *Social media*: Someone's post goes viral. Were they brilliant, or did they get lucky with timing? Hard to tell without seeing their other posts!

**2. Evaluate risks**
- *Example*: "1 in 100 chance of side effects" sounds scary until you realize that's 1%. 99% chance you'll be fine!
- *Driving analogy*: You might feel unsafe flying but comfortable driving. Yet statistically, driving is WAY more dangerous. Our intuition about risk is often wrong!

**3. Design better systems**
- *Example*: How many checkout lanes does a store need? Too few = long waits. Too many = wasted resources. Probability helps find the sweet spot!
- *Tech example*: How many servers does Netflix need for Friday night? They use probability to predict load and prepare.

**4. Not be fooled by coincidences**
- *Example*: You think of a friend, then they text you! Spooky? Or just probability - you think of friends many times a day, eventually it'll align with a text.
- *Birthday paradox*: In a class of 30 students, there's a 70% chance two share a birthday! Feels impossible, but math says it's likely.

**Understanding probability = Understanding reality better**

## Simulations in This Module

### 1. **`roll_dice.py`** - Basic dice experiments
**What it does:**
- Single die vs multiple dice
- See distributions emerge from randomness

**Cool insight:** Rolling one die gives equal chances (1,2,3,4,5,6 all equally likely). But rolling TWO dice and adding them? 7 is way more common than 2 or 12! Why? Because there are more ways to make 7 (1+6, 2+5, 3+4, 4+3, 5+2, 6+1) than to make 2 (only 1+1).

*Board game connection*: This is why games use different numbers of dice - they create different probability patterns!

### 2. **`coin_flips.py`** - Heads vs tails
**What it does:**
- How long until you get 10 heads in a row?
- Understanding streaks and patterns

**Prepare to be shocked:** 10 heads in a row sounds impossible, but it's not as rare as you think! Even in "random" data, streaks appear. This is why people see patterns in randomness (cloud shapes, lucky streaks) - our brains look for patterns even when there aren't any!

*Sports analogy*: Basketball players have "hot hands" - they make several shots in a row. Is it skill or randomness? This simulation helps you understand!

### 3. **`monte_carlo_pi.py`** - Calculate π with randomness!
**What it does:**
- Throw random darts at a square
- Inside the square is a circle inscribed (touching all sides) - the circle's radius is half the square's side length
- Count how many darts land in the circle vs outside
- Use the ratio to estimate π (3.14159...)

**Mind = blown:** You can calculate one of math's most famous constants using RANDOMNESS! This technique is called "Monte Carlo simulation" (named after the famous casino) and is used in physics, finance, and machine learning.

*The magic*: π is exact and deterministic, but we're using random throws to approximate it. The more darts you throw, the closer you get!

### 4. **`probability_game.py`** - Predict then test
**What it does:**
- Interactive learning: You make a prediction, then the simulation tests it
- See if your intuition matches reality

**Why it's valuable:** The best way to learn probability is to make predictions and be wrong! Your brain learns by comparing what you expected vs what actually happened.

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
