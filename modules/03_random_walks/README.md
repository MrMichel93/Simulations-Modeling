# Module 3: Random Walks

## The Drunkard's Walk

**The Classic Scenario:**
Imagine someone who's had too much to drink standing on a sidewalk. Each step, they randomly stumble left or right (or in 2D: north, south, east, or west). Where do they end up after 100 steps? 1000 steps?

**Your gut feeling might say:** "They'll wander far away, maybe 1000 steps away!"

**The surprising truth:** They'll typically end up much closer to where they started - maybe only 30 steps away after 1000 steps!

This simple concept appears EVERYWHERE in nature and technology:

**Physical Science:**
- **Molecules diffusing through air** - smell from kitchen spreads via random molecular motion
- **Light scattering in materials** - why clouds are white (photons bouncing randomly)
- **Brownian motion** - pollen grains jiggling in water (Einstein's proof atoms exist!)

**Biology:**
- **Animals foraging for food** - when you don't know where food is, random search isn't bad!
- **Immune cells patrolling** - white blood cells wander randomly looking for invaders
- **Bacterial movement** - bacteria "tumble" randomly to explore their environment

**Economics & Technology:**
- **Stock prices fluctuating** - short-term price changes behave like random walks
- **Internet packets finding routes** - some routing algorithms use random paths
- **Google search** - PageRank algorithm based on random web surfing!

**Your daily life:**
- **Looking for lost keys** - you probably search somewhat randomly!
- **Zombie game AI** - many games use random walks for enemy movement

The math is the same across all these situations. Learn it once, apply it everywhere!

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

### The √n Rule (Square Root Rule)

**The Shocking Result:**
After n steps, on average you're about √n distance from start.

Let's see what this means:
- **100 steps** → ~10 units away (not 100!)
  - You took 100 steps but only got 10 units from home!
- **10,000 steps** → ~100 units away (not 10,000!)
  - You took 10,000 steps but only got 100 units from home!

**Why is this so weird?**
If you walked 100 steps in a straight line, you'd be 100 units away. But random walking? You end up going back and forth, canceling out your progress!

*Analogy*: It's like trying to get somewhere by flipping a coin at every intersection. Sometimes you go toward your goal, sometimes away. You make progress, but very slowly!

**Real-world impact:**
- **Diffusion is slow** - this is why it takes time for perfume to spread across a room
- **Random search is inefficient** - if you're looking for something, having a strategy beats random search!
- **Lost in the woods?** Random walking won't get you far. Better to walk in one direction!

### Eventual Return (in 1D and 2D)

**Mind-blowing mathematical fact:**

In **1D (a line)** and **2D (a plane)**, a random walker will EVENTUALLY return to the start with probability 1 (certainty)!

It might take a while - maybe 1000 steps, maybe a million - but mathematically, you're guaranteed to come back.

**But here's the twist:** In **3D (space)**, only 34% chance of returning!

**Why does dimension matter?**
- **1D**: Only 2 directions (left/right), so you keep revisiting the same spots
- **2D**: 4 directions (up/down/left/right), more space but still likely to return
- **3D**: 6 directions (add forward/back), so much space you'll likely wander off forever!

*Space analogy*: 
- 1D: Walking on a tightrope - nowhere else to go
- 2D: Walking on flat ground - eventually you'll cross your path
- 3D: Floating in space - infinite room to wander away!

**Physics connection:** This is why molecules in 2D surfaces behave differently than molecules in 3D space!

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
