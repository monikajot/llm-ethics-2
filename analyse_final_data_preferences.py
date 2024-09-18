# Install python-ternary and matplotlib if not already installed
# You can uncomment the following line to install the library
# !pip install python-ternary matplotlib

import matplotlib.pyplot as plt
import ternary
import math

# Define the data
triple_preference_gpt_4o = {
    ('authority', 'care', 'fairness'): {'authority': 143, 'care': 222, 'fairness': 175, 'neither': 0},
    ('authority', 'care', 'liberty'): {'authority': 157, 'care': 231, 'liberty': 152, 'neither': 0},
    ('authority', 'care', 'loyalty'): {'authority': 152, 'care': 256, 'loyalty': 132, 'neither': 0},
    ('authority', 'care', 'sanctity'): {'authority': 142, 'care': 254, 'sanctity': 143, 'neither': 1},
    ('care', 'fairness', 'liberty'): {'care': 201, 'fairness': 193, 'liberty': 146, 'neither': 0},
    ('care', 'fairness', 'loyalty'): {'care': 224, 'fairness': 190, 'loyalty': 124, 'neither': 2},
    ('care', 'fairness', 'sanctity'): {'care': 204, 'fairness': 196, 'sanctity': 140, 'neither': 0},
    ('care', 'liberty', 'loyalty'): {'care': 249, 'liberty': 141, 'loyalty': 146, 'neither': 4},
    ('care', 'liberty', 'sanctity'): {'care': 246, 'liberty': 149, 'sanctity': 142, 'neither': 3},
    ('care', 'loyalty', 'sanctity'): {'care': 259, 'loyalty': 137, 'sanctity': 143, 'neither': 1}
}

# Filter the data to include only triples involving 'care'
filtered_data = {k: v for k, v in triple_preference_gpt_4o.items() if 'care' in k}

num_plots = len(filtered_data)
cols = 3  # Number of columns in the subplot grid
rows = math.ceil(num_plots / cols)  # Calculate the required number of rows

# Create a Matplotlib figure with a GridSpec layout
fig = plt.figure(figsize=(cols * 5, rows * 5))
gs = fig.add_gridspec(rows, cols, hspace=0.4, wspace=0.4)

# Iterate over each triple and create a ternary subplot
for idx, (triple, counts) in enumerate(filtered_data.items()):
    row = idx // cols
    col = idx % cols
    ax = fig.add_subplot(gs[row, col])
    
    # Create a ternary subplot in the specified position
    tax = ternary.TernaryAxesSubplot(ax=ax, scale=100)
    tax.set_title(f"{triple}", fontsize=12)
    
    # Remove default Matplotlib axes
    tax.boundary(linewidth=1.0)
    tax.gridlines(multiple=20, color="gray", linewidth=0.5)
    
    # Extract counts and normalize to sum to 100%
    a = counts[triple[0]]
    b = counts[triple[1]]
    c = counts[triple[2]]
    total = a + b + c
    a_norm = a / total * 100
    b_norm = b / total * 100
    c_norm = c / total * 100
    
    # Plot the normalized point
    tax.scatter([(a_norm, b_norm, c_norm)], marker='o', color='blue', label='Preference')
    
    # Set axis labels (capitalize for aesthetics)
    tax.left_axis_label(triple[0].capitalize(), fontsize=10, offset=0.14)
    tax.right_axis_label(triple[1].capitalize(), fontsize=10, offset=0.14)
    tax.bottom_axis_label(triple[2].capitalize(), fontsize=10, offset=0.14)
    
    # Optional: Add a legend if needed
    # tax.legend()


# Set the overall title for the figure
fig.suptitle("Triple Preferences Involving 'Care'", fontsize=16)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
