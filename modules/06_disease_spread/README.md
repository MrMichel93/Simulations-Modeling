# Module 6: Disease Spread

## Epidemic Modeling

How do diseases spread through a population?

This simulation helps us understand:
- Why diseases grow exponentially at first
- How "herd immunity" works
- What interventions actually help
- When epidemics peak and fade

**This is some of the most important simulation work in the world.**

## The SIR Model

A classic framework for epidemic modeling:

### Three States

**S - Susceptible**
- Can catch the disease
- Not yet infected
- Most people start here

**I - Infected**
- Currently sick
- Can spread to others
- Contagious!

**R - Recovered** (or Removed)
- No longer sick
- Can't spread disease
- Immune (in most models)

### Flow

S → I → R

People move through these states as the epidemic progresses.

## Core Concepts

### The Reproduction Number (R₀)

**"R-naught"** - Average number of people one infected person infects.

- **R₀ < 1**: Disease dies out
- **R₀ = 1**: Disease stays constant
- **R₀ > 1**: Epidemic grows!

Critical threshold for pandemic.

### Exponential Growth

Early in an epidemic:
- Day 1: 1 person infected
- Day 2: 2 people infected
- Day 3: 4 people infected
- Day 4: 8 people infected
- ...

Doubling is **scary fast**.

### Herd Immunity

When enough people are immune (recovered or vaccinated):
- Disease can't spread efficiently
- Even susceptible people are protected
- Epidemic stops even with R₀ > 1

Magic threshold: depends on R₀

### Peak and Decline

Every epidemic has a life cycle:
1. Exponential growth
2. Peak (max infections)
3. Decline (running out of susceptible people)
4. End

## Key Insights

### 1. Interventions Matter

Small changes in transmission rate:
- Social distancing
- Masks
- Quarantine

Can have HUGE impacts on epidemic size.

### 2. Timing is Critical

Early intervention much better than late:
- Exponential growth means delays are costly
- "Flatten the curve" = spread cases over time

### 3. Network Structure Matters

Real people aren't randomly mixed:
- Households
- Schools
- Workplaces

Structure affects spread patterns.

## Simulations in This Module

1. **`sir_model.py`** - Classic compartmental SIR
2. **`spatial_epidemic.py`** - Agents moving on a grid
3. **`intervention_study.py`** - Test different interventions
4. **`network_spread.py`** - Disease on social networks

## Learning Objectives

By the end of this module, you should be able to:

- [ ] Explain the SIR model
- [ ] Understand exponential growth
- [ ] Implement a disease spread simulation
- [ ] Visualize epidemic curves
- [ ] Analyze intervention effectiveness
- [ ] Explain herd immunity

## Exercises

### 1. Finding R₀

Run simulations with different transmission rates.
- Find the threshold where R₀ = 1
- Below it: disease dies out
- Above it: epidemic!

### 2. Flatten the Curve

Simulate with and without interventions:
- No intervention: tall, narrow peak
- With intervention: flat, wide curve

Why does "flatten" help healthcare systems?

### 3. Vaccination Strategy

Only have vaccine for 50% of population.
- Vaccinate randomly? Or target approach?
- What strategy minimizes total infections?

### 4. Superspreaders

Most people infect 0-2 others.
Some people infect 10+.

Model this variability - how does it change the epidemic?

## Challenge: COVID-19 Scenario

Try to model a realistic scenario:
- Start with 1 infected person
- Population of 1000
- R₀ around 2.5
- Recovery time ~14 days

Questions:
- How many eventually get infected?
- When does the peak occur?
- How does social distancing help?

## Real-World Impact

Epidemic simulation is used for:
- **Public health planning**: Hospital capacity
- **Policy decisions**: Lockdown timing
- **Vaccine distribution**: Who gets it first?
- **Resource allocation**: Ventilators, beds, staff
- **Communication**: Explaining measures to public

**Simulations literally save lives.**

## Historical Example

The 1918 flu pandemic:
- Cities with early interventions did better
- "Social distancing" worked 100 years ago
- Simulation helps us learn from history

## Ethical Considerations

Disease models affect real policies affecting real people:
- Models have assumptions and limitations
- Results must be communicated carefully
- Uncertainty is important
- Equity matters in interventions

Powerful tool = great responsibility.

## Next Steps

Congratulations! You've completed all core modules!

Now:
- Explore the **sandbox** directory
- Try the **challenge projects**
- Build your own simulations
- Share what you create!

## Final Reflection

You've learned to model:
- Growth and decay
- Randomness and probability
- Individual agents
- Population dynamics
- Spatial patterns
- Network effects

These tools apply to countless real-world systems!

**Keep exploring. Keep simulating. Keep learning.**
