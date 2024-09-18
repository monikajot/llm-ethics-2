import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
from mock_results import x

foundations = ['authority', 'care', 'fairness', 'liberty', 'loyalty', 'sanctity']

# Assign colors to each foundation
foundation_colors = {
    'authority': '#e41a1c',  # red
    'care': '#377eb8',       # blue
    'fairness': '#4daf4a',   # green
    'liberty': '#ff7f00',    # orange
    'loyalty': '#984ea3',    # purple
    'sanctity': '#a65628'    # brown
}

# Compute positions of foundations on the hexagon
positions = {}
for i, foundation in enumerate(foundations):
    angle = 2 * np.pi * i / 6  # in radians
    x = np.cos(angle)
    y = np.sin(angle)
    positions[foundation] = (x, y)

# Start plotting
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')

# Plot the hexagon edges
hexagon = [positions[foundation] for foundation in foundations]
hexagon.append(positions[foundations[0]])  # Close the hexagon
hex_xs, hex_ys = zip(*hexagon)
ax.plot(hex_xs, hex_ys, 'k-', lw=2)

# Plot the foundations at the vertices
for foundation, (x, y) in positions.items():
    ax.text(x * 1.1, y * 1.1, foundation.capitalize(), fontsize=12, ha='center', va='center')

# Plot triangles for each trio
for trio, counts in triple_preference_gpt_4o.items():
    # Get positions
    coords = [positions[foundation] for foundation in trio]
    # Determine the most preferred foundation
    preferred_foundation = max(counts, key=lambda k: counts[k] if k != 'neither' else -1)
    if preferred_foundation == 'neither':
        color = '#cccccc'  # Grey for 'neither'
    else:
        color = foundation_colors[preferred_foundation]
    # Create polygon and add to plot
    triangle = Polygon(coords, closed=True, color=color, alpha=0.5, edgecolor='k')
    ax.add_patch(triangle)
    # Compute centroid for labeling
    centroid = np.mean(coords, axis=0)
    # Prepare label with counts
    label = '\n'.join([f"{k.capitalize()}: {v}" for k, v in counts.items() if k != 'neither'])
    ax.text(centroid[0], centroid[1], label, fontsize=8, ha='center', va='center')

# Remove axes
ax.axis('off')

# Show plot
plt.show()
