import pickle

from visualize_results import plot_pair_graph, plot_pair_heatmaps
from generate_mft_dataset import (
    run_dataset_generation,
    check_dataset_formatting,
    get_best_examples,
)
from evaluate_models import Evaluations


def run_evals():
    name = "test_name"

    # generate data
    run_dataset_generation(output_filename=f"{name}.csv", num_examples=10)
    check_dataset_formatting(input_filename=f"{name}.csv")
    get_best_examples(input_filename=f"formatted_{name}.csv", percent=50)

    # evals
    eval = Evaluations(eval_models=["mock"])  # ["gpt-3.5", "gpt-4o-mini"]
    eval.evals(input_filename=f"formatted_{name}.csv")

    # visualisations
    with open(f"PREFERENCES.pkl", "rb") as f:
        preferences = pickle.load(f)
    # print(preferences["pair_preference"][0])
    plot_pair_heatmaps(preferences["pair_preference"][0])
    plot_pair_graph(preferences["pair_preference"][0])

    # check inconsistencies

    # check variance


if __name__ == "__main__":
    run_evals()
