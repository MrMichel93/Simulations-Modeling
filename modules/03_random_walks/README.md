# Module 3: Random Walks

## The Drunkard's Walk

Imagine someone taking steps in random directions. Where do they end up?

This simple concept appears EVERYWHERE in nature:
- Molecules diffusing through air
- Stock prices fluctuating
- Animals foraging for food
- Light scattering in materials
- Internet packets finding routes

## Core Concepts

### What is a Random Walk?

1. Start at a position
2. Each time step, move in a random direction
3. Repeat many times
4. Observe the path and final position

### 1D vs 2D Walks

**1D (number line)**: Move left or right
- Simple but insightful
- Models many real phenomena

**2D (plane)**: Move in any direction
- More realistic for spatial movement
- Beautiful, unpredictable paths

### Key Questions

- How far from start do you expect to end up?
- Is the walk more likely to return to the start or wander away?
- What does the path look like?
- What if you run 1000 walkers - what patterns emerge?

## Surprising Results

### The √n Rule

After n steps, on average you're about √n distance from start.

- 100 steps → ~10 units away (not 100!)
- 10,000 steps → ~100 units away (not 10,000!)

Random walks are less efficient than directed movement!

### Eventual Return (in 1D and 2D)

In 1D and 2D, a random walker will EVENTUALLY return to the start (with probability 1)!

In 3D? Only 34% chance of returning. Mind-blowing!

## Simulations in This Module

1. **`random_walk_1d.py`** - Walk on a number line
2. **`random_walk_2d.py`** - Walk on a plane
3. **`multiple_walkers.py`** - See statistical patterns
4. **`biased_walk.py`** - What if there's a preferred direction?

## Learning Objectives

By the end of this module, you should be able to:

- [ ] Implement 1D and 2D random walks
- [ ] Visualize paths and final positions
- [ ] Understand the √n distance relationship
- [ ] Run multiple trials to see distributions
- [ ] Explain real-world applications

## Exercises

### 1. Distance from Origin

Run `random_walk_2d.py` 100 times with 1000 steps each.
- Record the final distance from origin each time
- Plot a histogram
- Does it match the √1000 ≈ 31.6 prediction?

### 2. Biased Walk

Modify a walk to have a 60% chance of moving right (instead of 50/50).
- How does this change the behavior?
- What real-world scenarios have biased walks?

### 3. First Return Time

Start at position 0. Walk randomly.
- How long until you return to 0?
- Run this 100 times and plot the distribution
- Some take a LONG time!

### 4. Treasure Hunt

Place "treasure" at position (10, 10).
Random walker starts at (0, 0).
- How long to reach the treasure?
- Is random walking a good search strategy?

## Challenge: Real-World Application

Pick one real-world phenomenon that involves random walks:
- Model it with code
- Visualize it
- Explain what you learned

Ideas:
- Stock price simulation
- Animal movement patterns
- Particle diffusion
- Brownian motion

## Next Steps

Ready to model interacting agents? Move on to **Module 4: Predator-Prey**!
