import networkx as nx
import matplotlib.pyplot as plt
from mock_results import pair_preference
from constants import MORAL_VALUES

OPTIONS = {
    "font_size": 12,
    "node_size": 3000,
    "node_color": "lightblue",
    "edgecolors": "black",
    "linewidths": 2.5,
    "width": 1.5,
}


def llama3(preferences):
    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes and edges to the graph
    for key, weight in preferences.items():
        source, target = key[0], key[1]
        G.add_edge(source, target)

    # Position the nodes
    pos = nx.spring_layout(G)

    # Draw the graph
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=5000)
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Show the plot
    plt.show()


def new():

    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes
    G.add_nodes_from(["A", "B", "C", "D", "E"])

    # Add directed edges
    G.add_edge("A", "B")  # A -> B
    G.add_edge("B", "C")  # B -> C
    G.add_edge("D", "E")  # D -> E

    # Add bidirectional edges (represented as two directed edges)
    G.add_edge("C", "D")  # C -> D
    G.add_edge("D", "C")  # D -> C

    # Add non-directional edges (using add_edge for simplicity; in a truly undirected graph, you'd use nx.Graph)
    G.add_edge("A", "E")  # A -- E (represented as A -> E and E -> A in this DiGraph)
    G.add_edge("E", "A")  # E -- A

    # Print the edges to see the connections
    print(G.edges)

    # Visualize the graph (optional)

    pos = nx.spring_layout(G)
    nx.draw(
        G, pos, with_labels=True, node_color="skyblue", node_size=1500, arrowsize=20
    )
    plt.title("Graph with Directed, Bidirectional, and Non-Directional Edges")
    plt.show()


def default_plot():
    G = nx.DiGraph([(0, 3), (1, 3), (2, 4), (3, 5), (3, 6), (4, 6), (5, 6)])

    # group nodes by column
    left_nodes = [0, 1, 2]
    middle_nodes = [3, 4]
    right_nodes = [5, 6, 7]

    # set the position according to column (x-coord)
    pos = {n: (0, i) for i, n in enumerate(left_nodes)}
    pos.update({n: (1, i + 0.5) for i, n in enumerate(middle_nodes)})
    pos.update({n: (2, i + 0.5) for i, n in enumerate(right_nodes)})
    pos.update({7: (1, 1)})

    nx.draw_networkx(G, pos, **OPTIONS)

    # Set margins for the axes so that nodes aren't clipped
    ax = plt.gca()
    ax.margins(0.20)
    plt.axis("off")
    plt.show()


def plot_pair_preference(node_coords, edges):

    G = nx.DiGraph(edges)

    nx.draw_networkx(G, node_coords, **OPTIONS)

    # Set margins for the axes so that nodes aren't clipped
    ax = plt.gca()
    ax.margins(0.20)
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    # pair_preference
    # new()
    # plot_pair_preference()
    new_dict = {}
    for pair, preferences in pair_preference.items():
        if preferences[pair[0]] > preferences[pair[1]]:
            new_dict[(pair[1], pair[0])] = preferences[pair[0]] - preferences[pair[1]]
        elif preferences[pair[0]] < preferences[pair[1]]:
            new_dict[(pair[0], pair[1])] = preferences[pair[1]] - preferences[pair[0]]
        elif preferences[pair[0]] == preferences[pair[1]]:
            new_dict[(pair[0], pair[1])] = 0
            new_dict[(pair[1], pair[0])] = 0

    # count for each val how many edges are pointing to it
    counts = {val: 0 for val in MORAL_VALUES}
    for _, key in new_dict.keys():
        counts[key] += 1

    print(new_dict)
    print(counts)
    print(sorted(counts, key=counts.get))
    sorted_nodes = sorted(counts, key=counts.get)
    node_coords = {
        node: (3 + (-1) ** i + i * 0.5, i) for i, node in enumerate(sorted_nodes)
    }
    print(node_coords)
    plot_pair_preference(node_coords=node_coords, edges=new_dict.keys())
    # llama3(preferences)
