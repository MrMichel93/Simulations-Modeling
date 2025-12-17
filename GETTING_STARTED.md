# Getting Started

Welcome to **Simulations & Modeling: Understanding Systems Through Code**!

This guide will help you get up and running quickly.

## 🎯 What You'll Need

### Prerequisites
- Basic Python knowledge (variables, loops, functions)
- Python 3.8 or higher installed
- A code editor (IDLE, VS Code, PyCharm, or similar)
- Curiosity about how things work!

### No Prerequisites Needed
- ❌ Advanced math
- ❌ Prior simulation experience
- ❌ Professional coding skills
- ❌ Special hardware

## 📦 Installation

### Step 1: Clone or Download

**Option A: Using Git**
```bash
git clone https://github.com/MrMichel93/Simulations-Modeling.git
cd Simulations-Modeling
```

**Option B: Download ZIP**
1. Click the green "Code" button on GitHub
2. Select "Download ZIP"
3. Extract to a folder
4. Open terminal/command prompt in that folder

### Step 2: Install Required Packages

```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install matplotlib numpy
```

**Note for Mac/Linux users:** You might need to use `pip3` instead of `pip`

### Step 3: Test Your Setup

Run this command to verify everything works:

```bash
python modules/01_foundations/first_simulation.py
```

If you see a graph appear, you're all set! 🎉

## 🚀 Your First Simulation

Let's run a quick example to see what this course is all about.

### Try It Now

1. Navigate to the first module:
```bash
cd modules/01_foundations
```

2. Run the first simulation:
```bash
python first_simulation.py
```

3. Follow the prompts:
   - Make a prediction
   - Press Enter
   - See the results
   - Compare to your prediction!

### What Just Happened?

You just ran a **deterministic simulation** of population growth!

The code:
- Started with 100 organisms
- Applied a simple growth rule
- Repeated for 100 time steps
- Showed you the results visually

Simple rules → Complex behavior → Understanding!

## 📚 Course Path

### Recommended Order

Follow the modules in sequence:

1. **Module 1: Foundations** (Start here!)
   - `modules/01_foundations/`
   - Understand what simulations are
   - Learn key concepts
   - Run your first simulation

2. **Module 2: Dice & Probability**
   - `modules/02_dice_probability/`
   - Experiment with randomness
   - See probability in action
   - Calculate π with random numbers!

3. **Module 3: Random Walks**
   - `modules/03_random_walks/`
   - Watch random movement create patterns
   - Discover the √n rule
   - Visualize beautiful paths

4. **Module 4: Predator-Prey**
   - `modules/04_predator_prey/`
   - Model ecological dynamics
   - See population cycles emerge
   - Balance the ecosystem

5. **Module 5: Traffic Flow**
   - `modules/05_traffic_flow/`
   - Create traffic jams from scratch
   - Understand emergent behavior
   - Test traffic interventions

6. **Module 6: Disease Spread**
   - `modules/06_disease_spread/`
   - Model epidemic dynamics
   - Understand R₀ and herd immunity
   - Test intervention strategies

### Each Module Contains

- **README.md**: Concepts and exercises
- **Simulation files**: Working Python code
- **Challenges**: Things to try

## 🎮 How to Learn

### The Learning Loop

For each simulation:

1. **📖 Read** the module README
2. **🤔 Predict** what will happen
3. **▶️ Run** the code
4. **👀 Observe** the results
5. **💭 Reflect** on what you learned
6. **🧪 Experiment** by changing things
7. **📝 Explain** in your own words

### Tips for Success

**✅ DO:**
- Make predictions before running code
- Change parameters and see what happens
- Break things intentionally
- Ask "what if?" constantly
- Visualize everything
- Explain results in plain English
- Be curious and explore

**❌ DON'T:**
- Rush through without understanding
- Copy code without reading it
- Skip the visualizations
- Worry about perfect code
- Be afraid to make mistakes
- Compare yourself to others

## 🛠️ Common Issues

### Issue: ModuleNotFoundError

**Problem:** Python can't find matplotlib or numpy

**Solution:**
```bash
pip install matplotlib numpy
```

### Issue: No graphs appear

**Problem:** Matplotlib backend issue

**Solution:** Add this at the top of Python files:
```python
import matplotlib
matplotlib.use('TkAgg')  # or 'Qt5Agg' or 'MacOSX'
```

### Issue: ImportError with sys.path

**Problem:** Code can't find utils module

**Solution:** Make sure you're running from the correct directory, or adjust the path:
```python
sys.path.append('../../')  # Adjust based on your location
```

### Issue: Python version

**Problem:** Code doesn't work on older Python

**Solution:** Upgrade to Python 3.8+:
```bash
python --version  # Check current version
```

## 📁 Project Structure

Here's what you'll find:

```
Simulations-Modeling/
├── README.md                 # Main course overview
├── GETTING_STARTED.md        # This file!
├── ASSESSMENT.md             # How learning is assessed
├── INSTRUCTORS.md            # Guide for teachers
├── requirements.txt          # Python packages needed
├── utils/
│   └── visualization.py      # Plotting and animation tools
├── modules/
│   ├── 01_foundations/       # Start here
│   ├── 02_dice_probability/
│   ├── 03_random_walks/
│   ├── 04_predator_prey/
│   ├── 05_traffic_flow/
│   └── 06_disease_spread/
└── sandbox/
    └── (your experiments!)   # Play here!
```

## 🎯 Quick Start Guide

### 5-Minute Start

1. Install Python 3.8+
2. Install packages: `pip install matplotlib numpy`
3. Run: `python modules/01_foundations/first_simulation.py`
4. Read the module README
5. Start experimenting!

### 1-Hour Start

1. Complete the 5-minute start
2. Work through Module 1 completely
3. Try the exercises
4. Modify parameters
5. Read Module 2 README
6. Run one Module 2 simulation

### 1-Day Start

1. Complete Module 1 fully
2. Complete Module 2 fully
3. Start Module 3
4. Experiment with visualizations
5. Create something in the sandbox
6. Share what you learned

## 💬 Getting Help

### When Stuck

1. **Read error messages** - they're trying to help!
2. **Add print statements** - see what's happening
3. **Start simple** - comment out code until it works
4. **Check the README** - it might answer your question
5. **Experiment** - try changing one thing at a time

### Learning Resources

**Python Basics:**
- python.org/about/gettingstarted
- pythontutor.com (visualize code execution)

**Matplotlib:**
- matplotlib.org/stable/gallery
- Look at examples similar to what you want

**Simulation Concepts:**
- Module READMEs explain everything
- No outside resources needed!

## 🎨 What to Do After the Course

### Projects to Try

1. **Combine modules** - mix concepts together
2. **Model your interest** - sports, games, nature, etc.
3. **Research real systems** - find data and compare
4. **Create visualizations** - make something beautiful
5. **Teach someone else** - best way to learn!

### Where to Go Next

- **Agent-Based Modeling** - more complex simulations
- **System Dynamics** - feedback loops and stocks/flows
- **Network Science** - connections and graphs
- **Computational Social Science** - model human behavior
- **Data Science** - analyze real data from simulations

## 🌟 Community

### Share Your Work

Created something cool?
- Add it to the sandbox/
- Document what you learned
- Share with others!
- Consider contributing back

### Improve the Course

Found a bug? Have an idea?
- Open an issue on GitHub
- Suggest new simulations
- Improve documentation
- Help other learners

## 🎓 For Self-Learners

Working through this alone? Great!

**Tips:**
- Set a schedule (e.g., one module per week)
- Keep a learning journal
- Explain concepts out loud (even to yourself!)
- Find a study buddy online
- Share your work on social media
- Join simulation communities

**Stay Motivated:**
- ✨ Celebrate completing each module
- 🏆 Set personal challenges
- 📸 Save your best visualizations
- 📝 Write about what you learned
- 🎯 Build a portfolio of projects

## 🎉 Ready to Start?

You're all set! Here's what to do next:

1. Open `modules/01_foundations/README.md`
2. Read it carefully
3. Run `first_simulation.py`
4. Complete the exercises
5. Move to Module 2 when ready

**Remember: The goal is understanding, not speed.**

Take your time. Experiment. Break things. Learn!

---

## Quick Command Reference

```bash
# Navigate to a module
cd modules/01_foundations

# Run a simulation
python first_simulation.py

# Go back to main directory
cd ../..

# Install packages
pip install -r requirements.txt

# Check Python version
python --version
```

---

**Have fun exploring systems through code!** 🚀

If you get stuck, remember: every expert was once a beginner who kept going.

You've got this! 💪
