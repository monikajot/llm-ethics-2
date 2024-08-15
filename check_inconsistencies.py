from mock_results import single_preferences, pair_preference, total_preference
from visualize_results import create_edges, get_counts

# are preference orders the same across different ways of prompting
# for each preference ordering extract a dict like { "1": "care", "2": "fairness",  "3":"authority", ... }
# then check that all these are the same across
# ordered_single_prefs_list = []
# for moral_val, score in single_preferences.items():
#     ordered_single_prefs_list.append((moral_val, score["yes"]))
# ordered_single_prefs_list.sort(key=lambda tup: tup[1])
# print(ordered_single_prefs_list)
#
# counts = get_counts(create_edges(pair_preferences=pair_preference))
# ordered_pair_prefs_list = [(moral_val, score) for moral_val, score in counts.items()]
# ordered_pair_prefs_list.sort(key=lambda tup: tup[1])
# print(ordered_pair_prefs_list)




# total_preference.pop("neither")
# ordered_total_prefs_list = [(moral_val, score) for moral_val, score in total_preference.items()]
# ordered_total_prefs_list.sort(key=lambda tup: tup[1])
# print(ordered_total_prefs_list)


# check  monotonic ordering 1 vs 2

# check  monotonic ordering 1 vs all
# check  monotonic ordering 2 vs all
# check transitive preferences

# are there cyclical preferences