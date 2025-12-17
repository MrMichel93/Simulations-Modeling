# Instructor Guide

## Welcome, Educator!

This course is designed to help students aged 16-20 discover how code can be a tool for **thinking about and understanding complex systems**.

## Course Philosophy

### Code as Thinking Tool

This isn't a "learn Python" course (though they will!).
This is a "learn to think computationally about systems" course.

**Core Principle:** Rules → Behavior → Outcomes

Students learn to:
1. Identify the rules governing a system
2. Encode those rules
3. Observe emergent behavior
4. Understand why it happens

### Minimal Math, Maximum Insight

We deliberately avoid:
- Heavy calculus
- Complex equations
- Formal proofs

We emphasize:
- Intuition
- Visualization
- Experimentation
- Plain language explanation

**Why?** Many students are intimidated by math but comfortable with code. Let's use their strengths!

### Play-Based Learning

The best learning happens when students are **curious and experimenting**, not when they're anxious about grades.

Encourage:
- "What if I change this?"
- Breaking things
- Unexpected discoveries
- Creative variations

Discourage:
- "What's the right answer?"
- Fear of mistakes
- Rushing to completion
- Copying without understanding

## Course Structure

### Suggested Pacing

**Total: 8-12 weeks** (flexible)

- **Week 1**: Module 1 (Foundations)
- **Week 2-3**: Module 2 (Dice & Probability)
- **Week 3-4**: Module 3 (Random Walks)
- **Week 5-6**: Module 4 (Predator-Prey)
- **Week 7-8**: Module 5 (Traffic Flow)
- **Week 9-10**: Module 6 (Disease Spread)
- **Week 11-12**: Final projects

Can be compressed or extended based on your needs.

### Session Format (90 minutes)

**Opening (10 min)**
- Review previous session
- Preview today's topic
- Connect to real world

**Exploration (30 min)**
- Students run base simulation
- Make predictions first
- Observe results
- Discuss surprises

**Experimentation (30 min)**
- Modify parameters
- Test hypotheses
- Record observations
- Compare with peers

**Synthesis (15 min)**
- Group discussion
- Share discoveries
- Explain in plain language
- Connect concepts

**Reflection (5 min)**
- What did you learn?
- What surprised you?
- What do you want to try next?

## Teaching Strategies

### 1. Predict Before Running

**Always** have students predict outcomes before running code.

Why?
- Activates prior knowledge
- Creates cognitive dissonance when wrong
- Makes results more memorable
- Builds mental models

Example:
> "Before running this, write down: Will the population grow faster or slower as time goes on? Why?"

### 2. Think-Pair-Share

After running a simulation:
1. **Think**: Individual reflection (2 min)
2. **Pair**: Discuss with partner (3 min)
3. **Share**: Groups share with class (5 min)

Gets everyone processing, not just the loud students.

### 3. Live Coding

Sometimes code together:
- Think aloud as you code
- Make deliberate mistakes
- Debug together
- Show your process

Students learn coding is iterative, not magic.

### 4. Gallery Walk

Students create visualizations → print/display → walk around viewing others' work → discuss patterns

Great for seeing how parameters affect outcomes.

### 5. Expert Groups

Divide class into groups, each explores one parameter:
- Group 1: Low values
- Group 2: Medium values
- Group 3: High values
- Group 4: Extreme values

Then regroup to share findings. Builds collective understanding.

## Common Challenges

### Challenge 1: "My code doesn't work!"

**Strategy:**
- Celebrate the error - it's data!
- What did you expect?
- What happened instead?
- What does the error tell us?
- Add print statements to see what's happening

Make debugging a learning opportunity.

### Challenge 2: "I don't know what to change."

**Strategy:**
- Start with guided questions
- "What if we doubled this number?"
- "What if we made this zero?"
- Gradually release to open exploration

Provide scaffolding, then remove it.

### Challenge 3: "This is boring."

**Strategy:**
- Connect to their interests (sports stats, games, social media)
- Let them choose project topics
- Add competition/gaming elements
- Show real-world impact

Find the hook for each student.

### Challenge 4: "I'm not good at coding."

**Strategy:**
- Emphasize growth mindset
- Show that understanding > perfect code
- Celebrate small wins
- Pair with supportive peer
- Provide working code to modify

Lower the barrier to entry.

### Challenge 5: Wide skill range

**Strategy:**
- Core exercises for everyone
- Extension challenges for advanced
- Peer tutoring
- Multiple paths to success
- Focus on growth, not absolute level

## Differentiation

### For Advanced Students

- Implement more complex models
- Optimize code for speed
- Add sophisticated visualizations
- Research real applications
- Create original simulations
- Help teach peers

### For Struggling Students

- Work with simpler examples
- Focus on understanding over implementation
- Modify rather than create from scratch
- Use print statements liberally
- Pair with mentor
- Allow more time

### For Different Learning Styles

**Visual learners:**
- Emphasize graphs and animations
- Draw diagrams of systems
- Color-code code sections

**Kinesthetic learners:**
- Act out simulations physically
- Use manipulatives
- Lots of hands-on coding time

**Auditory learners:**
- Explain to partners
- Record voice explanations
- Listen to discussions

**Reading/writing:**
- Write explanations
- Research background
- Document experiments

## Discussion Facilitation

### Good Questions to Ask

**Understanding:**
- "Why did that happen?"
- "What surprised you?"
- "How would you explain this to a friend?"

**Prediction:**
- "What will happen if we change X?"
- "Which parameter has the biggest effect?"
- "How high can we make Y go?"

**Connection:**
- "What real-world system behaves like this?"
- "Have you seen this pattern before?"
- "Where else might this apply?"

**Experimentation:**
- "How could we test that?"
- "What's the next question?"
- "What would break this model?"

### Avoid These Questions

- "What's the right answer?" (There often isn't one!)
- "Did you get X?" (Assumes one correct result)
- "Who finished?" (Speed isn't the goal)

## Creating a Learning Culture

### Foster:
- ✅ Curiosity over correctness
- ✅ Exploration over completion
- ✅ Explanation over memorization
- ✅ Collaboration over competition
- ✅ Process over product

### Avoid:
- ❌ Shaming mistakes
- ❌ Rushing through material
- ❌ Focusing on grades
- ❌ Comparing students
- ❌ Perfect code expectations

## Assessment Tips

See ASSESSMENT.md for detailed guidance.

**Key principles:**
1. Assess understanding through explanation
2. Value process over product
3. Allow revision and iteration
4. Focus on growth
5. Use portfolios over tests

## Technical Setup

### Recommended Environment

**Option A: Local Installation**
- Python 3.8+
- matplotlib
- numpy
- IDLE, VS Code, or PyCharm

**Option B: Online Platform**
- Replit
- Google Colab
- Jupyter notebooks

Choose based on your constraints.

### First Day Setup

Spend time ensuring everyone can:
1. Run a basic Python script
2. Install required packages
3. Display a simple plot
4. Save and load files

Don't rush this - solid setup prevents frustration.

## Module-Specific Tips

### Module 1: Foundations
- Keep it short and engaging
- Build excitement
- Emphasize that math will be minimal
- Show cool examples of later modules

### Module 2: Dice & Probability
- Very hands-on and intuitive
- Great for building confidence
- Students love the Monte Carlo pi demo
- Connect to games and sports

### Module 3: Random Walks
- Visualizations are beautiful
- √n rule often surprises them
- Good connection to physics and finance
- Multiple walkers create stunning scatter plots

### Module 4: Predator-Prey
- Students love the ecological angle
- The cycles are very satisfying to discover
- Great for parameter exploration
- Connect to local ecosystems

### Module 5: Traffic Flow
- Very relatable (everyone experiences traffic!)
- Phantom jams blow minds
- Great for discussing policy
- Can get competitive (who creates worst jam?)

### Module 6: Disease Spread
- Extremely relevant and important
- Sensitive topic - be mindful
- Powerful for understanding policy
- Connect to COVID-19 experiences carefully

## Extension Activities

### Guest Speakers
- Local researchers who use simulation
- Public health officials
- Traffic engineers
- Data scientists

### Field Trips
- University research labs
- Science museums
- Traffic control centers
- Weather forecasting

### Competitions
- Best visualization
- Most interesting finding
- Creative simulation
- Real-world application

### Public Showcase
- Science fair
- School presentation
- Parent demo night
- Community event

## Resources for You

### Books
- "The Model Thinker" by Scott Page
- "Complexity: A Guided Tour" by Melanie Mitchell
- "The Nature of Code" by Daniel Shiffman

### Websites
- NetLogo Models Library
- Complexity Explorer
- Santa Fe Institute

### Communities
- Agent-based modeling groups
- Computational social science
- System dynamics society

## Self-Care for Instructors

This course can be intense because:
- Wide skill ranges
- Debugging help needed constantly
- Students go in unexpected directions

**Remember:**
- You don't need to know everything
- "Let's figure it out together" is fine
- Mistakes are learning opportunities
- Celebrate small wins
- Take breaks

## Growth Mindset Reminders

**For students:**
- "You can't do this *yet*"
- "Mistakes help your brain grow"
- "Every expert was once a beginner"

**For you:**
- First time teaching this? That's okay!
- Not a Python expert? Learn together!
- Simulations surprising you? That's the magic!

## Final Thoughts

This course is about **empowering students to think about complex systems**.

If they leave with:
- Curiosity about how things work
- Comfort with computational thinking
- Ability to build simple models
- Excitement about simulation

**You've succeeded.**

The goal isn't to create professional simulation engineers (though some might!).

The goal is to help young people see that:
- **Code is a way to think**
- **Complex behavior emerges from simple rules**
- **They can build tools to understand the world**

Thank you for teaching this course. You're helping shape how the next generation thinks about complexity.

---

**Questions? Ideas? Improvements?**

This is a living course. Share your experiences and help make it better!

🚀 Happy teaching!
