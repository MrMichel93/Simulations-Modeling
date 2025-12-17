# Module 6: Disease Spread

## Epidemic Modeling

How do diseases spread through a population?

**Why this matters more than ever:**
You've lived through COVID-19. You've heard terms like "flatten the curve," "herd immunity," and "R-naught." This module explains the math behind those concepts - the same math that public health officials use to make real decisions affecting millions of lives.

This simulation helps us understand:
- Why diseases grow exponentially at first (1 → 2 → 4 → 8 → scary fast!)
- How "herd immunity" works (and why it's a percentage, not a yes/no)
- What interventions actually help (and which are just theater)
- When epidemics peak and fade (and why timing matters SO much)

**This is some of the most important simulation work in the world.**

These models:
- Guide government policy during pandemics
- Determine hospital capacity planning
- Inform vaccine distribution strategies
- Help predict and prevent outbreaks
- **Literally save millions of lives**

*Historical note*: During COVID-19, epidemic models helped countries decide when to lock down, when to reopen, and how to allocate resources. The difference between good models and bad models was measured in lives saved or lost.

## The SIR Model

A classic framework for epidemic modeling used by public health agencies worldwide!

**SIR = three boxes that people move through**

### Three States (Everyone is in exactly ONE box)

**S - Susceptible** 🧍
- Can catch the disease
- Not yet infected  
- Hasn't been vaccinated or had it before
- Most people start here
- *Think of it as*: "Sitting ducks" - vulnerable to infection

**I - Infected** 🤒
- Currently sick
- Can spread to others
- Contagious!
- *Think of it as*: "Active cases" - the people actually spreading disease right now
- *Key point*: This is where the action happens - infected people create more infected people!

**R - Recovered** (or Removed) ✅
- No longer sick
- Can't spread disease (not contagious anymore)
- Usually immune (can't get it again, in basic models)
- *Think of it as*: "Out of the game" - they're done with this disease
- *Note*: "Removed" can mean recovered OR died. It's any way of leaving the infected state

### Flow (The One-Way Street)

**S → I → R**

People move through these states as the epidemic progresses. In the basic model, you can't go backward!

*Video game analogy*: Think of it like levels in a game:
- Level 1 (S): Not infected yet
- Level 2 (I): Infected and infectious  
- Level 3 (R): Recovered/immune
- You can't go back to level 1!

**The key questions:**
- How fast do people move from S to I? (Transmission rate - depends on contagiousness)
- How fast do people move from I to R? (Recovery rate - depends on disease duration)

These two rates determine everything about how the epidemic plays out!

## Core Concepts

### The Reproduction Number (R₀)

**Pronounced "R-naught"** - The most important number in epidemiology!

**Simple definition:** Average number of people one infected person infects (before they recover or die).

**Example interpretations:**
- **R₀ = 2**: Each infected person infects 2 others on average
- **R₀ = 0.5**: Each infected person infects 0.5 others (half the people infect one person, half infect nobody)

**The Three Critical Zones:**

- **R₀ < 1**: Disease dies out (each person infects less than 1 → shrinking)
  - *Example*: R₀ = 0.8 means 10 infected people create only 8 new infections
  - Epidemic fizzles out naturally
  - *This is the goal!*

- **R₀ = 1**: Disease stays constant (teetering on the edge)
  - Each person infects exactly 1 replacement
  - Endemic - disease sticks around but doesn't grow
  - *Rare equilibrium point*

- **R₀ > 1**: Epidemic grows! (each person infects more than 1 → expanding)
  - *Example*: R₀ = 2 means 10 infected people create 20 new infections
  - This is when you get a full-blown epidemic
  - *This is what we're trying to prevent!*

**Real diseases:**
- Measles: R₀ ≈ 12-18 (super contagious!)
- COVID-19 (original): R₀ ≈ 2-3 (moderately contagious)
- Seasonal flu: R₀ ≈ 1-2 (mildly contagious)
- SARS: R₀ ≈ 2-4 (moderately contagious)

**Why this number is powerful:**
Every intervention (masks, social distancing, vaccines) is trying to push R₀ below 1!
- Masks reduce transmission → lower R₀
- Social distancing reduces contacts → lower R₀  
- Vaccines remove susceptible people → lower effective R₀

### Exponential Growth (The Sneaky Danger)

**Why epidemics catch us off guard:**

Early in an epidemic, numbers seem small and manageable. Then suddenly they explode!

**Example timeline (R₀ = 2, doubling every 3 days):**
- Day 0: 1 person infected ("No big deal")
- Day 3: 2 people infected ("Still fine")
- Day 6: 4 people infected ("Under control")
- Day 9: 8 people infected ("We've got this")
- Day 12: 16 people infected ("Hmm, growing")
- Day 15: 32 people infected ("Getting concerning")
- Day 18: 64 people infected ("Problem!")
- Day 21: 128 people infected ("Crisis!")
- Day 24: 256 people infected ("Emergency!")
- Day 30: 1,024 people infected ("Overwhelmed!")

**The danger:** For the first 15 days, it seems manageable. Then it suddenly explodes!

**Doubling is scary fast.** Exponential growth is deceptive - it lulls you into thinking you have time, then overwhelms you.

*Rice on chessboard story*: Ancient tale - king agrees to put 1 grain of rice on first square of chessboard, 2 on second, 4 on third, doubling each time. Seems reasonable. But by square 64, it's 18 quintillion grains - more rice than exists on Earth! That's exponential growth.

*The key lesson*: With exponential growth, early action matters IMMENSELY. Waiting "just a few days" can mean 10x more cases!

### Herd Immunity (The Shield of the Many)

**The Beautiful Concept:**
When enough people are immune (recovered or vaccinated), the disease can't spread efficiently - even susceptible people are protected!

**How it works - The Social Shield:**

Imagine 100 people in a room. 1 is infected.

**Scenario 1: No immunity**
- Infected person encounters 99 susceptible people
- If R₀ = 3, they infect 3 people
- Those 3 infect 9 more
- Epidemic grows!

**Scenario 2: 70% immune**
- Infected person encounters 99 people
- But 69 are immune (bounces off them)
- Only 30 are susceptible
- Even if they try to infect 3 people (R₀ = 3), they probably only encounter 1 susceptible person
- Epidemic slows or stops!

**Key insight:** Immune people act as "buffers" or "circuit breakers." They break the chain of transmission!

*Forest fire analogy*: 
- Forest with dry trees everywhere = fire spreads fast
- Forest with firebreaks (gaps, wet areas) = fire stops spreading
- Immune people are like firebreaks in disease transmission!

**The Magic Threshold (Herd Immunity Threshold):**

The percentage needed depends on R₀!

**Formula:** Threshold ≈ (1 - 1/R₀) × 100%

**Examples:**
- R₀ = 2: Need 50% immune (1 - 1/2 = 0.5 = 50%)
- R₀ = 3: Need 67% immune (1 - 1/3 = 0.67 = 67%)
- R₀ = 10: Need 90% immune (1 - 1/10 = 0.9 = 90%)

**Why this matters:**
- More contagious disease = need higher immunity percentage
- Measles (R₀ ≈ 15) needs ~95% vaccination rate!
- COVID-19 (R₀ ≈ 3) needs ~67% vaccination rate
- This is why "most people" isn't enough - need a specific percentage!

**The Ethical Dimension:**
Vaccines protect TWO groups:
1. The person vaccinated (direct protection)
2. Vulnerable people who CAN'T be vaccinated (babies, immune-compromised) via herd immunity (indirect protection)

*That's why vaccinating your healthy teenager protects someone's elderly grandparent!*

### Peak and Decline

Every epidemic has a life cycle:
1. Exponential growth
2. Peak (max infections)
3. Decline (running out of susceptible people)
4. End

## Key Insights

### 1. Interventions Matter (Small Changes, Big Effects)

**The Power of Percentages:**

Small changes in transmission rate can have HUGE impacts on epidemic size!

**Example interventions:**

**Social distancing** - Reduces contact rate
- If you normally encounter 20 people/day, staying home reduces it to 5
- That's a 75% reduction in potential transmissions!
- Effect: Dramatically lowers R₀

**Masks** - Reduces transmission probability  
- Even 50% effective masks cut transmission in half
- If everyone wears masks, effect compounds!
- Effect: Cuts R₀ proportionally

**Quarantine** - Removes infectious people from population
- Fast quarantine means less time spreading
- Effect: Reduces effective R₀

**The Math:**
- No intervention: R₀ = 3.0 (epidemic doubles every few days)
- With interventions: R₀ = 0.9 (epidemic shrinks!)
- That small difference (3.0 vs 0.9) is millions of cases vs. containment!

*Domino analogy*: 
- R₀ > 1: Each domino knocks down multiple others (exponential spread)
- R₀ < 1: Each domino doesn't quite reach the next one (epidemic dies)
- Small changes in spacing (interventions) determine which happens!

### 2. Timing is Critical (The Exponential Race)

**Early intervention is exponentially better than late!**

**Example scenario (R₀ = 2, doubles every 3 days):**

**Option A: Act on Day 9 (8 infected)**
- Reduce R₀ from 2 to 0.8
- Peak infections: ~50 people
- Total infected: ~200 people

**Option B: Wait until Day 21 (128 infected)**
- Same intervention (reduce R₀ from 2 to 0.8)
- Peak infections: ~1,000 people
- Total infected: ~5,000 people

**Same intervention, but waiting 12 days made it 25x worse!**

**"Flatten the curve" explained:**

Without intervention:
- Tall, narrow peak (lots of people sick at once)
- Hospitals overwhelmed
- People die who could have been saved

With intervention:
- Flat, wide curve (same total cases spread over time)
- Hospitals can handle the load
- Better outcomes even with same number of infections!

*Highway analogy*: 
- 1000 cars trying to merge in 5 minutes = gridlock
- Same 1000 cars merging over an hour = smooth flow
- Same total cars, different timing, drastically different outcome!

### 3. Network Structure Matters (It's Not Random!)

**The Basic Model Assumption:**
People mix randomly - everyone equally likely to encounter anyone.

**Reality:**
Real people aren't randomly mixed! We have structured networks:

**Household clusters:**
- You see family every day (high contact)
- If one family member gets sick, others likely will too
- But you rarely see other households

**Schools:**
- Kids mix intensively within school
- But different schools barely interact
- "Super-spreader" environments

**Workplaces:**
- Coworkers interact daily
- But work-from-home breaks those links

**Why this matters:**

1. **Disease spreads differently in networks**
   - Can move fast within clusters
   - Slowly between clusters
   - "Bridges" between clusters are critical

2. **Interventions work differently**
   - Closing schools cuts many connections
   - Work-from-home cuts different connections
   - Network structure determines which interventions are most effective!

3. **"Super-spreaders" exist**
   - Some people encounter many others (bartenders, teachers, flight attendants)
   - Some people encounter few others (remote workers, hermits)
   - One super-spreader can cause a massive outbreak!

*Social media analogy*:
- Random model: Every person follows random others
- Reality: Influencers have millions of followers, most people have dozens
- A meme spread by an influencer goes viral; same meme from random person doesn't
- Disease spreads the same way - network structure determines spread patterns!

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

## Ethical Considerations (With Great Power...)

**Disease models affect real policies affecting real people.**

This isn't just an academic exercise. The models YOU learn to build are similar to ones used to make decisions like:
- Should schools close?
- Should businesses shut down?
- Who gets vaccinated first?
- How many hospital beds are needed?

These decisions affect millions of lives, livelihoods, and mental health.

### Key Ethical Responsibilities:

**1. Models have assumptions and limitations**
- Every model is simplified (that's the point!)
- But simplifications can miss important factors
- *Example*: Early COVID models didn't account for people not following rules
- **Your responsibility**: Always state your assumptions clearly!

**2. Results must be communicated carefully**
- Numbers can scare people or make them complacent
- "1 million deaths" hits different than "1% mortality rate" (even if they're the same!)
- Media can misinterpret or sensationalize
- **Your responsibility**: Explain uncertainty and context!

**3. Uncertainty is important**
- Models give ranges, not exact predictions
- "50,000 to 150,000 cases" is very different from "100,000 cases"
- Ignoring uncertainty can lead to false confidence or panic
- **Your responsibility**: Show confidence intervals and ranges!

**4. Equity matters in interventions**
- Some people can work from home; others can't
- Some people can stockpile; others live paycheck to paycheck
- Some people have great healthcare; others have none
- **Your responsibility**: Consider who bears the burden of interventions!

**Real example - Vaccine priority:**
Models helped decide who got COVID vaccines first. Choices included:
- Healthcare workers (they're exposed + they help others)
- Elderly (highest death risk)
- Essential workers (can't stay home)
- Vulnerable communities (hit hardest)

Each choice is defensible, but different choices mean different people live or die. Models inform, but humans must decide based on values, not just math.

**The Spider-Man Principle:**
"With great power comes great responsibility."

You're learning a powerful tool. Use it wisely. Be honest about limitations. Consider impacts on real people. And never forget: behind every number in your simulation is a human being.

*"All models are wrong, but some are useful."* - George Box (famous statistician)

The goal isn't perfect prediction - it's useful insight that helps people make better decisions!

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
