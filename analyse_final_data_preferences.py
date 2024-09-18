import matplotlib.pyplot as plt
import math

# Data provided
triple_preference_gpt_4o = {
    ('authority', 'care', 'fairness'): {'authority': 143, 'care': 222, 'fairness': 175, 'neither': 0},
    ('authority', 'care', 'liberty'): {'authority': 157, 'care': 231, 'liberty': 152, 'neither': 0},
    ('authority', 'care', 'loyalty'): {'authority': 152, 'care': 256, 'loyalty': 132, 'neither': 0},
    ('authority', 'care', 'sanctity'): {'authority': 142, 'care': 254, 'sanctity': 143, 'neither': 1},
    ('fairness', 'care', 'liberty'): {'fairness': 201, 'care': 193, 'liberty': 146, 'neither': 0},
    ('fairness', 'care', 'loyalty'): {'fairness': 224, 'care': 190, 'loyalty': 124, 'neither': 2},
    ('fairness', 'care', 'sanctity'): {'fairness': 204, 'care': 196, 'sanctity': 140, 'neither': 0},
    ('liberty', 'care', 'loyalty'): {'liberty': 249, 'care': 141, 'loyalty': 146, 'neither': 4},
    ('liberty', 'care', 'sanctity'): {'liberty': 246, 'care': 149, 'sanctity': 142, 'neither': 3},
    ('loyalty', 'care', 'sanctity'): {'loyalty': 259, 'care': 137, 'sanctity': 143, 'neither': 1}
}

data = triple_preference_gpt_4o.copy()

# Define the sequence of components around the pentagon
components_sequence = ['authority', 'fairness', 'liberty', 'loyalty', 'sanctity']

def ternary_to_cartesian(values, components):
    # components is a list of the three components in order [a, b, c]
    a = values[components[0]]
    b = values[components[1]]
    c = values[components[2]]
    # Normalize the values (ignore 'neither')
    total = a + b + c
    a /= total
    b /= total
    c /= total
    # Calculate the 2D Cartesian coordinates in a ternary plot
    x = 0.5 * (2 * b + c)
    y = (math.sqrt(3) / 2) * c
    return x, y

def rotate_coordinates(x, y, theta):
    # Apply rotation matrix
    x_rotated = x * math.cos(theta) - y * math.sin(theta)
    y_rotated = x * math.sin(theta) + y * math.cos(theta)
    return x_rotated, y_rotated

# Plot 'care' at center
plt.scatter([0], [0], label='care')

initial_angle = -90  # Start from the top
num_components = len(components_sequence)
for k in range(num_components):
    primary = components_sequence[k]
    secondary = components_sequence[(k + 1) % num_components]
    # Find the key in 'data' that contains 'care', 'primary', and 'secondary'
    key_candidates = [key for key in data.keys() if set(key) == set([primary, secondary, 'care'])]
    if not key_candidates:
        print(f"No data for combination ({primary}, {secondary}, 'care')")
        continue
    key = key_candidates[0]
    val = data[key]
    # Components order is [primary, secondary, 'care']
    components = [primary, secondary, 'care']
    x, y = ternary_to_cartesian(val, components)
    # Rotate coordinates
    theta = math.radians(initial_angle + k * 72)
    x_rot, y_rot = rotate_coordinates(x, y, theta)
    plt.scatter([x_rot], [y_rot], label=f"({primary}, {secondary})")
    # Plot the vertex for 'primary'
    vertex_x, vertex_y = rotate_coordinates(0, 1, theta)  # (0, 1) is at the top
    plt.scatter([vertex_x], [vertex_y], label=primary)
    # Remove the key from data
    del data[key]

plt.legend()
plt.show()
