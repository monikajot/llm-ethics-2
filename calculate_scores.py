import pandas as pd

from mock_results import single_preference_var, pair_preference_var, pair_preference_gpt_4o
import matplotlib.pyplot as plt
from constants import MORAL_VALUES
import numpy as np
import numpy as np
from scipy.optimize import linear_sum_assignment
import itertools
from itertools import permutations
import seaborn as sns


def get_single_prefs_means_var():
    single_means_dict = {}
    for moral_val in MORAL_VALUES:
        vals = []
        for preference_list in single_preference_var:
            vals.append(preference_list[moral_val]["yes"])
        single_means_dict[moral_val] = [np.mean(vals), np.std(vals)]
    # print(single_means_dict)
    return single_means_dict


def normalise_pair_prefs(pair_preference_var):
    first_comb = pair_preference_var[0]
    num = sum(first_comb[list(first_comb.keys())[0]].values())
    # print(num)
    normalised_pair_prefs = []
    for i, preference_list in enumerate(pair_preference_var):
        new_dict = {}
        for comb, results in preference_list.items():
            new_dict[comb] = {k: int(v * 100 / num) for k, v in results.items()}
        normalised_pair_prefs.append(new_dict)
    # print(normalised_pair_prefs)
    return normalised_pair_prefs


def pair_preference_matrix(preference_dict):
    # Define the items
    items = ["authority", "care", "fairness", "liberty", "loyalty", "sanctity"]

    # Create the preference matrix
    preference_matrix = np.zeros((6, 6))

    # Populate the preference matrix
    for (item1, item2), preferences in preference_dict.items():
        i = items.index(item1)
        j = items.index(item2)
        preference_matrix[i, j] = preferences[item1]
        preference_matrix[j, i] = preferences[item2]
    matrix = pd.DataFrame(data=preference_matrix, columns=items, index=items)

    # print(matrix)
    return matrix, preference_matrix


def kemeny_young(matrix):
    n = len(matrix)
    scores = np.zeros(n)

    # Generate all permutations
    perms = list(permutations(range(n)))

    min_dist = float('inf')
    optimal_perm = None

    for perm in perms:
        dist = 0
        for i in range(n):
            for j in range(i+1, n):
                if matrix[perm[i]][perm[j]] < matrix[perm[j]][perm[i]]:
                    dist += matrix[perm[j]][perm[i]]
        if dist < min_dist:
            min_dist = dist
            optimal_perm = perm

    # Calculate ranking scores based on the optimal permutation
    for i in range(n):
        scores[optimal_perm[i]] = n - i - 1

    return scores

def get_pair_pref_ranking(pair_preferences=pair_preference_var[0]):
    matrix, preference_matrix = pair_preference_matrix(pair_preferences)
    # best_ranking, min_distance = kemeny_young_method(MORAL_VALUES, pair_preference_var[0])
    # print("Kemeny-Young ranking:", best_ranking, min_distance)
    # matrix["row_sums"] = matrix.apply(sum, axis=1)
    # matrix["row_sums"] = matrix["row_sums"].apply(int)

    rankings = kemeny_young(preference_matrix)

    # total_scores = sorted(zip(MORAL_VALUES, rankings, matrix["row_sums"].values), key=lambda x:x[1])
    print(matrix)
    print("Kemeny-Young Ranking Scores:", rankings)
    # print(matrix["row_sums"].values)
    sns.heatmap(matrix, cmap="Blues",annot=True, fmt=".3g")
    plt.show()
    return matrix, rankings

if __name__ == "__main__":
    get_pair_pref_ranking(pair_preference_gpt_4o)
