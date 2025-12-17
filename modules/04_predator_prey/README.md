# Module 4: Predator-Prey Dynamics

## The Hunt is On

What happens when predators hunt prey in an ecosystem?

This classic simulation reveals one of nature's most beautiful patterns: **cyclic population dynamics** - like a never-ending dance between species.

## The Story

**The Basic Scenario:** 
Imagine a meadow with rabbits and foxes. Rabbits eat grass (which grows back). Foxes eat rabbits (their only food source).

**What do you think will happen?**
Most people guess: "Foxes will eat all the rabbits, then starve." Or: "They'll reach a balance and stay constant."

**What ACTUALLY happens** - The Eternal Dance:

**Act 1: Rabbit Paradise** 🐰🐰🐰
- Lots of rabbits eating grass and multiplying
- Foxes have a feast! Easy prey everywhere
- Fox population starts growing (with a delay, because reproduction takes time)

**Act 2: Fox Explosion** 🦊🦊🦊
- Now there are LOTS of foxes
- Rabbits get eaten faster than they can reproduce
- Rabbit population crashes

**Act 3: The Famine** 🦊💀
- Few rabbits left = foxes can't find food
- Foxes start starving
- Fox population crashes

**Act 4: Rabbit Recovery** 🐰✨
- With few foxes around, rabbits can breed safely
- Rabbit population explodes again
- Back to Act 1!

**This cycle repeats endlessly** (unless something external changes or the system crashes entirely)!

*Real-world observation*: Scientists have tracked this exact pattern in Canadian lynx (predator) and snowshoe hares (prey) for over 100 years using fur trading records. The populations rise and fall in perfect cycles, each about 10 years long!

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

### 1. The Lag Effect (Timing is Everything!)

**The Pattern:** Predator population peaks **after** prey population peaks.

**Why the delay?**
- **Biology takes time**: Foxes don't instantly have babies when they find food
- **Pregnancy and growth**: Even when foxes eat well, baby foxes take weeks to be born and months to grow
- **Reaction time**: By the time fox population responds to abundant rabbits, the rabbits are already declining!

*Analogy*: It's like turning the shower temperature knob. You turn it, but the water doesn't get hot immediately. By the time you feel the hot water, you've already turned it too far and now it's TOO hot. Then you overcorrect to cold. The delay causes oscillation!

*Economic parallel*: Oil prices show similar cycling patterns. High prices → companies drill more → takes years → too much oil → prices crash → companies stop drilling → takes years → shortage → prices rise again. The cycle continues! (Note: Real economic cycles involve many additional factors like geopolitics, storage capacity, and demand changes that aren't captured in simple predator-prey models, but the lag effect and cycling behavior are similar.)

### 2. Sensitivity to Parameters (Butterfly Effect!)

**Small changes = BIG differences**

Tiny changes in birth/death rates can:
- **Stabilize the system** - smooth, predictable cycles
- **Make cycles bigger** - dramatic booms and busts  
- **Cause extinction!** - one or both species dies out completely

*Example changes:*
- Increase rabbit birth rate by 10%: Rabbits might boom so much that foxes boom even more, causing wild swings
- Increase fox death rate by 10%: System might stabilize because foxes can't overbuild population

**Why does this matter?**
Small environmental changes (climate, habitat, disease) can drastically affect ecosystems. A 5°C temperature change might seem small, but it could destabilize entire predator-prey relationships!

*Real impact*: This is why conservation is hard. You can't just "add more predators" or "remove some prey" without carefully modeling what happens.

### 3. No Equilibrium (The Perpetual Motion Machine)

**In basic models, populations never settle to fixed values.**
They oscillate forever, like a pendulum that never stops swinging!

**Why no balance?**
- When populations are "just right," tiny random fluctuations tip the balance
- The lag effect prevents settling down
- It's mathematically impossible in the basic model

*Pendulum analogy*: The bottom of a pendulum swing is "equilibrium" but it never stops there - momentum carries it past. Same with populations - the lag and inertia keep them moving past equilibrium.

**(Real ecosystems have more complexity that can create stability)**
- Multiple prey species (if rabbits decline, foxes eat mice)
- Multiple predators (competition limits fox growth)
- Geographic refuges (some rabbits hide where foxes can't reach)
- These factors can dampen the cycles

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
