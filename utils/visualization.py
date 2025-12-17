"""
Visualization utilities for simulations.

Simple tools to help students see what their simulations are doing.
Visual feedback is essential for understanding!
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle
import numpy as np


def plot_time_series(data, title="Simulation Results", xlabel="Time", ylabel="Value", 
                     labels=None, colors=None):
    """
    Plot one or more time series on a graph.
    
    Args:
        data: List of lists or 2D array - each row/list is a series to plot
        title: Graph title
        xlabel: Label for x-axis (usually "Time" or "Steps")
        ylabel: Label for y-axis
        labels: List of labels for each series (for legend)
        colors: List of colors for each series
    
    Example:
        populations = [[100, 95, 90], [10, 15, 20]]
        plot_time_series(populations, "Predator-Prey", labels=["Prey", "Predator"])
    """
    plt.figure(figsize=(10, 6))
    
    # Handle single series
    if not isinstance(data[0], (list, np.ndarray)):
        data = [data]
    
    # Plot each series
    for i, series in enumerate(data):
        label = labels[i] if labels and i < len(labels) else f"Series {i+1}"
        color = colors[i] if colors and i < len(colors) else None
        plt.plot(series, label=label, linewidth=2, color=color)
    
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_histogram(data, title="Distribution", xlabel="Value", bins=30, color='skyblue'):
    """
    Plot a histogram to see the distribution of values.
    
    Great for visualizing random events, final positions, etc.
    
    Args:
        data: List of values to plot
        title: Graph title
        xlabel: Label for x-axis
        bins: Number of bins in histogram
        color: Bar color
    """
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=bins, color=color, alpha=0.7, edgecolor='black')
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.show()


def plot_scatter(x_data, y_data, title="Scatter Plot", xlabel="X", ylabel="Y", 
                color='blue', alpha=0.6):
    """
    Plot points in 2D space.
    
    Useful for random walks, final positions, phase plots.
    
    Args:
        x_data: X coordinates
        y_data: Y coordinates
        title: Graph title
        xlabel: Label for x-axis
        ylabel: Label for y-axis
        color: Point color
        alpha: Transparency (0=invisible, 1=solid)
    """
    plt.figure(figsize=(10, 10))
    plt.scatter(x_data, y_data, color=color, alpha=alpha, s=50)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    plt.tight_layout()
    plt.show()


class GridAnimation:
    """
    Animate a grid-based simulation.
    
    Perfect for: traffic, disease spread, cellular automata, etc.
    
    Example:
        anim = GridAnimation(grid_size=(50, 50))
        anim.add_frame(grid1)
        anim.add_frame(grid2)
        anim.show()
    """
    
    def __init__(self, grid_size, interval=100, colormap='viridis', title="Grid Simulation"):
        """
        Initialize the animation.
        
        Args:
            grid_size: Tuple (rows, cols) for grid dimensions
            interval: Milliseconds between frames
            colormap: Color scheme ('viridis', 'plasma', 'hot', 'RdYlGn', etc.)
            title: Animation title
        """
        self.grid_size = grid_size
        self.frames = []
        self.interval = interval
        self.colormap = colormap
        self.title = title
    
    def add_frame(self, grid):
        """Add a snapshot of the grid at this time step."""
        self.frames.append(np.array(grid))
    
    def show(self):
        """Display the animation."""
        if not self.frames:
            print("No frames to animate! Use add_frame() to add data.")
            return
        
        fig, ax = plt.subplots(figsize=(10, 10))
        
        # Initial frame
        im = ax.imshow(self.frames[0], cmap=self.colormap, interpolation='nearest')
        plt.colorbar(im, ax=ax)
        ax.set_title(f"{self.title} - Frame 0", fontsize=14, fontweight='bold')
        
        def update(frame_num):
            im.set_array(self.frames[frame_num])
            ax.set_title(f"{self.title} - Frame {frame_num}", fontsize=14, fontweight='bold')
            return [im]
        
        anim = animation.FuncAnimation(fig, update, frames=len(self.frames),
                                      interval=self.interval, blit=True, repeat=True)
        plt.tight_layout()
        plt.show()
        return anim


def plot_grid(grid, title="Grid State", colormap='viridis', show_values=False):
    """
    Display a single grid snapshot.
    
    Args:
        grid: 2D array or list of lists
        title: Plot title
        colormap: Color scheme
        show_values: If True, display the numeric value in each cell
    """
    grid = np.array(grid)
    plt.figure(figsize=(10, 10))
    plt.imshow(grid, cmap=colormap, interpolation='nearest')
    plt.colorbar()
    plt.title(title, fontsize=14, fontweight='bold')
    
    if show_values:
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                plt.text(j, i, f'{grid[i, j]:.1f}', 
                        ha='center', va='center', color='white', fontsize=8)
    
    plt.tight_layout()
    plt.show()


def plot_walk(x_positions, y_positions, title="Random Walk", show_start_end=True):
    """
    Visualize a path through 2D space.
    
    Shows the trajectory with start and end points marked.
    
    Args:
        x_positions: List of x coordinates over time
        y_positions: List of y coordinates over time
        title: Plot title
        show_start_end: Mark start (green) and end (red) points
    """
    plt.figure(figsize=(10, 10))
    
    # Draw the path
    plt.plot(x_positions, y_positions, 'b-', alpha=0.5, linewidth=1)
    
    # Mark start and end
    if show_start_end:
        plt.plot(x_positions[0], y_positions[0], 'go', markersize=15, label='Start')
        plt.plot(x_positions[-1], y_positions[-1], 'ro', markersize=15, label='End')
        plt.legend()
    
    plt.xlabel("X Position", fontsize=12)
    plt.ylabel("Y Position", fontsize=12)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    plt.tight_layout()
    plt.show()


def side_by_side_comparison(data1, data2, title1="Simulation 1", title2="Simulation 2",
                            xlabel="Time", ylabel="Value"):
    """
    Compare two simulations side by side.
    
    Perfect for "what-if" analysis.
    
    Args:
        data1, data2: Time series data to compare
        title1, title2: Titles for each subplot
        xlabel, ylabel: Axis labels
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    ax1.plot(data1, linewidth=2, color='blue')
    ax1.set_xlabel(xlabel, fontsize=12)
    ax1.set_ylabel(ylabel, fontsize=12)
    ax1.set_title(title1, fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    ax2.plot(data2, linewidth=2, color='red')
    ax2.set_xlabel(xlabel, fontsize=12)
    ax2.set_ylabel(ylabel, fontsize=12)
    ax2.set_title(title2, fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()


# Quick test if run directly
if __name__ == "__main__":
    print("Testing visualization utilities...")
    
    # Test time series plot
    time_data = [[i + np.random.randint(-2, 3) for i in range(100)]]
    plot_time_series(time_data, title="Test Time Series", ylabel="Random Value")
    
    print("Visualization utilities are working!")
