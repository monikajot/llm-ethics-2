import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
import seaborn as sns
import pickle
import math

from constants import MORAL_VALUES
from mock_results import pair_preference, pair_preference_gpt_4o, gpt_4o_sp, gpt_4o_tp

MORAL_VALUE_COLORS = {
    "authority": "#7b8aab",
    "care": "#e23557",
    "fairness": "#f0d43a",
    "liberty": "#22b2da", 
    "loyalty": "#9b84b7", 
    "sanctity": "#a55233",
}

OPTIONS = {
    "font_size": 8,
    "font_weight": 0.5,
    "node_size": 1500,
    "node_color": None,       # To be set dynamically
    "edgecolors": "black",
    "linewidths": 1.5,
}

def plot_pair_graph(pair_preferences=pair_preference, output_filename="pair_graph.png"):
    new_dict = create_edges(pair_preferences)
    # Count for each value how many edges are pointing to it
    counts = get_counts(new_dict)

    sorted_nodes = list(reversed(sorted(counts, key=counts.get)))
    print(sorted_nodes)
    node_coords = {
        node: (math.cos(math.radians(60)* (i%6)),4*math.sin(math.radians(60)* (i%6)) ) for i, node in enumerate(sorted_nodes)
    }
    G = nx.DiGraph()
    for edge, weight in new_dict.items():
        G.add_edge(edge[0], edge[1], weight=weight)

    # Assign colors based on the MORAL_VALUE_COLORS mapping
    node_colors = [MORAL_VALUE_COLORS.get(node, "lightblue") for node in G.nodes()]

    # Extract edge weights
    edge_weights = [G[u][v]['weight'] for u, v in G.edges()]

    # Define scaling parameters for edge widths
    # Set minimum and maximum widths
    min_width = 0.5
    max_width = 3.0

    # Handle the case where all weights are zero
    if edge_weights:
        max_weight = max(edge_weights)
        min_weight_val = min(edge_weights)
    else:
        max_weight = 1
        min_weight_val = 0

    # Avoid division by zero
    weight_range = max_weight - min_weight_val if max_weight != min_weight_val else 1

    # Scale edge widths
    widths = [
        min_width + ( (w - min_weight_val) / weight_range ) * (max_width - min_width)
        for w in edge_weights
    ]

    # Update OPTIONS with node colors
    draw_options = OPTIONS.copy()
    draw_options["node_color"] = node_colors

    # Draw the graph with dynamic edge widths
    plt.figure(figsize=(4,6))
    ax = plt.gca()
    nx.draw_networkx(
        G,
        node_coords,
        width=widths,
        ax=ax,
        **draw_options
    )

    # Create a legend for the colors
    create_legend(MORAL_VALUE_COLORS)

    # Set margins for the axes so that nodes aren't clipped
    ax = plt.gca()
    ax.margins(0.20)
    plt.axis("off")
    # plt.show()
    ax.figure.savefig(output_filename, bbox_inches='tight')
    plt.close()

def plot_single_graph(edges, node_coords, output_filename="single_graph.png"):
    G = nx.DiGraph()
    for edge, weight in edges.items():
        G.add_edge(edge[0], edge[1], weight=weight)

    # Assign colors based on the MORAL_VALUE_COLORS mapping
    node_colors = [MORAL_VALUE_COLORS.get(node, "lightblue") for node in G.nodes()]

    # Extract edge weights
    edge_weights = [G[u][v]['weight'] for u, v in G.edges()]

    # Define scaling parameters for edge widths
    min_width = 0.5
    max_width = 5.0

    if edge_weights:
        max_weight = max(edge_weights)
        min_weight_val = min(edge_weights)
    else:
        max_weight = 1
        min_weight_val = 0

    weight_range = max_weight - min_weight_val if max_weight != min_weight_val else 1

    widths = [
        min_width + ( (w - min_weight_val) / weight_range ) * (max_width - min_width)
        for w in edge_weights
    ]

    # Update OPTIONS with node colors
    draw_options = OPTIONS.copy()
    draw_options["node_color"] = node_colors

    # Draw the graph with dynamic edge widths
    nx.draw_networkx(
        G,
        node_coords,
        width=widths,
        **draw_options
    )

    # Create a legend for the colors
    create_legend(MORAL_VALUE_COLORS)

    # Set margins for the axes so that nodes aren't clipped
    ax = plt.gca()
    ax.margins(0.20)
    plt.axis("off")
    plt.show()
    plt.close()
    # ax.figure.savefig(output_filename)

def get_counts(new_dict):
    # Get the number of edges that are pointing to a value
    counts = {val: 0 for val in MORAL_VALUES}
    for _, key in new_dict.keys():
        counts[key] += 1
    return counts

def create_edges(pair_preferences):
    new_dict = {}
    for pair, scores in pair_preferences.items():
        if scores[pair[0]] > scores[pair[1]]:
            new_dict[(pair[1], pair[0])] = scores[pair[0]] - scores[pair[1]]
        elif scores[pair[0]] < scores[pair[1]]:
            new_dict[(pair[0], pair[1])] = scores[pair[1]] - scores[pair[0]]
        elif scores[pair[0]] == scores[pair[1]]:
            new_dict[(pair[0], pair[1])] = 0
            new_dict[(pair[1], pair[0])] = 0
    return new_dict

def plot_pair_heatmaps(
    pair_preferences=pair_preference, output_filename="pair_heatmaps.png"
):
    data = {}
    for pair, preferences in pair_preferences.items():
        data[(pair[0], pair[1])] = preferences[pair[0]] - preferences[pair[1]]
    mask = np.triu(np.ones([6, 6]))
    matrix = pd.DataFrame(index=MORAL_VALUES, columns=MORAL_VALUES)

    for (row_label, col_label), value in data.items():
        matrix.loc[col_label, row_label] = value

    matrix = matrix.fillna(0)
    fig = plt.figure(figsize=(10, 8))
    sns.heatmap(
        matrix,
        annot=True,
        fmt="g",
        cmap="YlGnBu",
        cbar_kws={"label": "Value"},
        mask=mask,
    )

    # Set the title and labels
    plt.title("Heatmap of Values")
    plt.xlabel("Preferred values")
    plt.ylabel("Over values")

    # Show the plot
    # plt.show()
    fig.savefig(output_filename, bbox_inches='tight')
    plt.close()

def plot_preference_matrix_heatmap(preference_matrix):
    fig = plt.figure(figsize=(10, 8))
    sns.heatmap(
        preference_matrix,
        annot=True,
        fmt="g",
        cmap="YlGnBu",
        cbar_kws={"label": "Value"},
    )

    # Set the title and labels
    plt.title("Heatmap of Values")
    plt.xlabel("Preferred values")
    plt.ylabel("Over values")

    plt.show()

def create_legend(color_mapping):
    # Create custom legend handles
    from matplotlib.patches import Patch

    legend_elements = [
        Patch(facecolor=color, edgecolor="black", label=label.capitalize())
        for label, color in color_mapping.items()
    ]

    plt.legend(
        handles=legend_elements,
        title="Moral Foundations",
        loc="upper left",
        bbox_to_anchor=(1, 1),
    )

if __name__ == "__main__":
    plot_pair_graph(pair_preference_gpt_4o)
