# Module 4: Predator-Prey Dynamics

## The Hunt is On

What happens when predators hunt prey in an ecosystem?

This classic simulation reveals one of nature's most beautiful patterns: **cyclic population dynamics**.

## The Story

**Scenario**: Rabbits eat grass. Foxes eat rabbits.

**What happens?**
1. Lots of rabbits → Foxes have plenty to eat → Fox population grows
2. Lots of foxes → Rabbits get eaten → Rabbit population drops
3. Few rabbits → Foxes starve → Fox population drops
4. Few foxes → Rabbits thrive → Rabbit population grows
5. Back to step 1!

This cycle repeats endlessly (unless the system crashes).

## Core Concepts

### Population Dynamics

Living populations don't grow at fixed rates - they **interact**:
- Prey grow when left alone
- Predators need prey to survive
- More predators → fewer prey
- Fewer prey → fewer predators

### The Lotka-Volterra Model

Simple rules that create complex behavior:

**Prey (Rabbits)**:
- Birth rate (natural growth)
- Death rate (when caught by predators)

**Predators (Foxes)**:
- Birth rate (depends on catching prey)
- Death rate (starvation)

### Emergent Behavior

The **cycles** aren't programmed - they emerge from the interaction!

This is a key insight: Complex patterns from simple rules.

## Key Insights

### 1. Lag Effect

Predator population peaks **after** prey population peaks.

Why? Takes time for:
- Predators to reproduce
- Effects of abundant food to show

### 2. Sensitivity to Parameters

Tiny changes in birth/death rates can:
- Stabilize the system
- Make cycles bigger
- Cause extinction!

### 3. No Equilibrium

In basic models, populations never settle to fixed values.
They oscillate forever!

(Real ecosystems have more complexity that can create stability)

## Simulations in This Module

1. **`basic_predator_prey.py`** - Classic Lotka-Volterra model
2. **`spatial_predator_prey.py`** - Agents moving on a grid
3. **`parameter_explorer.py`** - See how parameters affect outcomes

## Learning Objectives

By the end of this module, you should be able to:

- [ ] Explain why populations cycle
- [ ] Implement a basic predator-prey simulation
- [ ] Visualize population changes over time
- [ ] Predict how parameter changes affect stability
- [ ] Connect this to real ecosystems

## Exercises

### 1. Stability Analysis

Run `basic_predator_prey.py` with different parameters:
- What makes cycles bigger or smaller?
- Can you find parameters that cause extinction?
- What makes the system most stable?

### 2. Three Species

Add a third species to the model:
- Grass → Rabbits → Foxes
- Now rabbits are limited by food too
- How does this change the dynamics?

### 3. Safe Haven

In the spatial model, add a region where predators can't go.
- How does this affect prey survival?
- Does it stabilize the system?

### 4. Real Ecosystem

Research a real predator-prey relationship:
- Lynx and hares in Canada (famous example!)
- Wolves and deer
- Ladybugs and aphids

Try to match the model to real data.

## Challenge: Design a Balanced Ecosystem

Create a simulation with multiple species that:
- Doesn't lead to extinction
- Has interesting dynamics
- Could plausibly exist in nature

This is harder than it sounds!

## Real-World Applications

This model framework applies to:
- **Ecology**: Managing wildlife populations
- **Epidemiology**: Disease and immune system
- **Economics**: Supply and demand cycles
- **Chemistry**: Oscillating reactions
- **Social Systems**: Competing trends

## Next Steps

Ready to see emergent traffic jams? Move on to **Module 5: Traffic Flow**!
