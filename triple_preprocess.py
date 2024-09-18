import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from mock_results import triple_preference, triple_preference_gpt_35
from constants import MORAL_VALUES
from calculate_scores import kemeny_young

def tuple_to_pairwise_matrix(triples):
    # Get all unique items and map them to indices
    unique_items = MORAL_VALUES
    n = len(MORAL_VALUES)
    index_map = {item: i for i, item in enumerate(MORAL_VALUES)}

    # Initialize the pairwise preference matrix
    matrix = np.zeros((n, n), dtype=int)

    # Fill the matrix based on the triples
    for A, B, C in triples:
        i, j, k = index_map[A[0]], index_map[B[0]], index_map[C[0]]
        matrix[i][j] += A[1]  # A preferred over B
        matrix[i][k] += B[1]  # A preferred over C
        matrix[j][k] += C[1]  # B preferred over C

    return matrix, unique_items


def triples_to_preference_matrix(triple_preference):
    triples = []

    for key, pref in triple_preference.items():
        pref.pop("neither")
        triples.append(sorted(list(zip(pref.keys(), pref.values())), key=lambda x:x[1], reverse=True))

    pairwise_matrix, items = tuple_to_pairwise_matrix(triples)
    df = pd.DataFrame(pairwise_matrix, columns=MORAL_VALUES, index=MORAL_VALUES)
    return df

def get_triple_pref_ranking(preference_matrix):
    # best_ranking, min_distance = kemeny_young_method(MORAL_VALUES, pair_preference_var[0])
    # print("Kemeny-Young ranking:", best_ranking, min_distance)

    matrix = pd.DataFrame(data=preference_matrix, columns=MORAL_VALUES, index=MORAL_VALUES)
    matrix["row_sums"] = matrix.apply(sum, axis=1)
    matrix["row_sums"] = matrix["row_sums"].apply(int)
    matrix = matrix.sort_values(by="row_sums", ascending=False)

    matrix = matrix[MORAL_VALUES]
    for col in matrix.columns:
        matrix[col] = matrix[col].astype(int)
        matrix[col] = matrix[col].apply(lambda val: val*100/1079/5)
    rankings = kemeny_young(preference_matrix)

    # total_scores = sorted(zip(MORAL_VALUES, rankings, matrix["row_sums"].values), key=lambda x:x[1])
    print(matrix)
    print("Kemeny-Young Ranking Scores:", rankings)
    # print(matrix["row_sums"].values)
    sns.heatmap(matrix, cmap="Blues",annot=True, fmt=".0f")
    plt.show()
    return rankings

if __name__ == "__main__":
    matrix = triples_to_preference_matrix(triple_preference_gpt_35)
    print(matrix)
    x= get_triple_pref_ranking(matrix.to_numpy())
    # print([MORAL_VALUES[int(i)] for i in x ])

