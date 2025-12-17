# Module 1: Foundations

## What Are Simulations?

A **simulation** is a program that mimics how something works in the real world. Instead of watching the real thing, you create a simplified model in code and see what happens.

### Why Simulate?

- **Too expensive**: Crash testing cars costs millions
- **Too dangerous**: Can't experiment with disease outbreaks on real people
- **Too slow**: Evolution takes millions of years
- **Too fast**: Chemical reactions happen in nanoseconds
- **Impossible**: Can't rewind time to see "what if?"

Simulations let us **explore, predict, and understand** complex systems safely and quickly.

## Core Concepts

### 1. Deterministic vs Stochastic

**Deterministic**: Same input → same output, every time
- Example: Bouncing ball with no air resistance
- Like a calculator - predictable

**Stochastic**: Randomness involved
- Example: Flipping a coin, rolling dice
- Different result each time
- More realistic for most real-world systems

### 2. The Four Pillars

Every simulation needs these:

1. **State**: What's the current situation?
   - Position of objects
   - Values of variables
   - "Take a snapshot right now"

2. **Rules**: How does the state change?
   - If A happens, then do B
   - "The laws of your mini-universe"

3. **Time Steps**: How do we move forward?
   - Tick... tick... tick...
   - Each step updates the state
   - "Press fast-forward, frame by frame"

4. **Randomness** (optional): Introduce uncertainty
   - Real life isn't perfectly predictable
   - Use random numbers to model chance events

### 3. Emergent Behavior

This is the **magic** of simulations! 

Simple rules → Complex patterns

- Flocking birds (just 3 simple rules)
- Traffic jams (no central planner)
- Markets (millions of individual choices)

The whole becomes greater than the sum of its parts.

## Your First Simulation

Let's start simple: **growing a population**

### The Rules:
1. Start with some number of organisms
2. Each time step, population increases by a percentage
3. Run for many time steps

See `first_simulation.py` to run it!

## Learning Objectives

By the end of this module, you should be able to:

- [ ] Explain what a simulation is in your own words
- [ ] Distinguish between deterministic and stochastic models
- [ ] Identify the state, rules, and time steps in a simulation
- [ ] Run and modify your first simulation
- [ ] Predict how changing parameters affects outcomes

## Exercises

1. **Predict First**: Before running `first_simulation.py`, predict:
   - Will the population grow faster or slower over time?
   - What will the graph look like?

2. **Run It**: Execute the simulation and compare to your prediction

3. **Experiment**:
   - Change the growth rate from 0.05 to 0.10 - what happens?
   - Change it to -0.05 (negative growth) - what does this model?
   - Start with 1000 organisms instead of 100 - does the shape change?

4. **Explain**: In plain English, why does the graph curve upward?

## Next Steps

Ready to add randomness? Move on to **Module 2: Dice & Probability**!
