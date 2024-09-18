import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
import seaborn as sns
import pickle

from constants import MORAL_VALUES
from mock_results import pair_preference, pair_preference_gpt_4o, gpt_4o_sp, gpt_4o_tp

OPTIONS = {
    "font_size": 8,
    "node_size": 1500,
    "node_color": "lightblue",
    "edgecolors": "black",
    "linewidths": 1.5,
    "width": 1.5,
}


def plot_pair_graph(pair_preferences=pair_preference, output_filename="pair_graph.png"):
    new_dict = create_edges(pair_preferences)
    # count for each val how many edges are pointing to it
    counts = get_counts(new_dict)

    sorted_nodes = sorted(counts, key=counts.get)
    node_coords = {
        node: (3 + (-1) ** i + i * 0.5, i) for i, node in enumerate(sorted_nodes)
    }

    G = nx.DiGraph(new_dict.keys())
    nx.draw_networkx(G, node_coords, **OPTIONS)

    # Set margins for the axes so that nodes aren't clipped
    ax = plt.gca()
    ax.margins(0.20)
    plt.axis("off")
    # plt.show()
    plt.close()
    ax.figure.savefig(output_filename)


def plot_single_graph(edges, node_coords, output_filename="single_graph.png"):
    G = nx.DiGraph(edges)
    nx.draw_networkx(G, node_coords, **OPTIONS)

    # Set margins for the axes so that nodes aren't clipped
    ax = plt.gca()
    ax.margins(0.20)
    plt.axis("off")
    plt.show()
    # plt.close()
    # ax.figure.savefig(output_filename)


def get_counts(new_dict):
    # get the number of edges that are pointing to a value
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
    fig.savefig(output_filename)
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

if __name__ == "__main__":
    # with open(f"PREFERENCES.pkl", "rb") as f:
    #     preferences = pickle.load(f)
    # print(preferences["pair_preference"][0])
    # plot_preference_matrix_heatmap()
    # plot_pair_graph(pair_preference_gpt_4o)

    plot_single_graph(edges)
