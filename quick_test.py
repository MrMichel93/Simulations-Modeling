"""
Quick Test Script

Run this to make sure everything is set up correctly!
"""

import sys

def test_imports():
    """Test that required packages are available."""
    print("Testing package imports...")
    
    try:
        import matplotlib
        print("  ✓ matplotlib found")
    except ImportError:
        print("  ✗ matplotlib NOT found - run: pip install matplotlib")
        return False
    
    try:
        import numpy
        print("  ✓ numpy found")
    except ImportError:
        print("  ✗ numpy NOT found - run: pip install numpy")
        return False
    
    return True


def test_visualization():
    """Test that visualization utilities work."""
    print("\nTesting visualization utilities...")
    
    try:
        from utils.visualization import plot_time_series
        print("  ✓ Can import visualization utils")
    except ImportError as e:
        print(f"  ✗ Cannot import visualization utils: {e}")
        return False
    
    return True


def test_simple_plot():
    """Try to create a simple plot."""
    print("\nTesting plot generation...")
    
    try:
        import matplotlib
        matplotlib.use('Agg')  # Use non-interactive backend for testing
        import matplotlib.pyplot as plt
        
        # Create simple plot
        plt.figure()
        plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
        plt.title("Test Plot")
        
        # Save to temp file
        import os
        temp_file = "/tmp/test_plot.png"
        plt.savefig(temp_file)
        plt.close()
        
        # Check if file was created
        if os.path.exists(temp_file):
            print("  ✓ Successfully created a plot")
            os.remove(temp_file)  # Clean up
            return True
        else:
            print("  ✗ Plot file not created")
            return False
            
    except Exception as e:
        print(f"  ✗ Error creating plot: {e}")
        return False


def main():
    print("=" * 60)
    print("SIMULATIONS & MODELING - SETUP TEST")
    print("=" * 60)
    print()
    
    all_passed = True
    
    # Test imports
    if not test_imports():
        all_passed = False
    
    # Test visualization
    if not test_visualization():
        all_passed = False
    
    # Test plot generation
    if not test_simple_plot():
        all_passed = False
    
    print("\n" + "=" * 60)
    if all_passed:
        print("✅ ALL TESTS PASSED!")
        print()
        print("You're ready to start learning!")
        print()
        print("Next steps:")
        print("  1. Read the main README.md")
        print("  2. Open GETTING_STARTED.md for detailed instructions")
        print("  3. Start with modules/01_foundations/")
        print()
        print("Have fun exploring! 🚀")
    else:
        print("❌ SOME TESTS FAILED")
        print()
        print("Please fix the issues above before continuing.")
        print()
        print("Common fixes:")
        print("  - Install packages: pip install matplotlib numpy")
        print("  - Check Python version: python --version (need 3.8+)")
        print("  - Try running from the main directory")
    print("=" * 60)


if __name__ == "__main__":
    main()
