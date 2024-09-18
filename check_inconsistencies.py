from mock_results import single_preferences, pair_preference, total_preference
from visualize_preference_rankings import create_edges, get_counts, plot_single_graph
from mock_results import pair_preference, pair_preference_gpt_4o, gpt_4o_sp, gpt_4o_tp

# are preference orders the same across different ways of prompting
# for each preference ordering extract a dict like { "1": "care", "2": "fairness",  "3":"authority", ... }
# then check that all these are the same across
ordered_single_prefs_list = []
for moral_val, score in gpt_4o_sp.items():
    ordered_single_prefs_list.append((moral_val, score["yes"]))
ordered_single_prefs_list.sort(key=lambda tup: tup[1])
print(ordered_single_prefs_list)
#
# counts = get_counts(create_edges(pair_preferences=pair_preference))
# ordered_pair_prefs_list = [(moral_val, score) for moral_val, score in counts.items()]
# ordered_pair_prefs_list.sort(key=lambda tup: tup[1])
# print(ordered_pair_prefs_list)


gpt_4o_tp.pop("neither")
ordered_total_prefs_list = [
    (moral_val, score) for moral_val, score in gpt_4o_tp.items()
]
ordered_total_prefs_list.sort(key=lambda tup: tup[1])
print(ordered_total_prefs_list)


def plot(what):
    nodes = [x for x in what]

    edges = [(nodes[i], nodes[i + 1]) for i in range(len(nodes) - 1)]
    node_coords = {node: (0, 10 * i) for i, node in enumerate(nodes)}
    print(edges)
    plot_single_graph(edges=edges, node_coords=node_coords)

plot(['liberty', 'sanctity', 'loyalty', 'care', 'authority', 'fairness'])
# plot(ordered_total_prefs_list)
# check  monotonic ordering 1 vs 2

# check  monotonic ordering 1 vs all
# check  monotonic ordering 2 vs all
# check transitive preferences

# are there cyclical preferences
