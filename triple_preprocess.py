import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from mock_results import triple_preference
from constants import MORAL_VALUES


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


