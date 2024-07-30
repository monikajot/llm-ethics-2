import time

import pandas as pd
import datetime as dt

from functions import query_model
from constants import (
    single_evaluation_task,
    EXAMPLE1,
    MFT_EXPLANATION,
    TASK,
    RULES,
    CARE,
    FAIRNESS,
    LOYALTY,
    AUTHORITY,
    SANCTITY,
    LIBERTY,
    EVALUATION_RULES,
)


def generate_mft_data(verbose=True):
    prompt = (
        MFT_EXPLANATION
        + CARE
        + FAIRNESS
        + LOYALTY
        + AUTHORITY
        + SANCTITY
        + LIBERTY
        + TASK
        + RULES
        + "\n\n You will be scored how accurately you follow each rule. "
        + EXAMPLE1  # TODO: have more and randomly change them. specify only the keys and not vals
    )
    response = query_model("gpt-4o", prompt, "")
    if verbose:
        print(prompt)
        print()
        print(response + "\n")
    return response


def evaluator(response: str, verbose: bool = True):
    evaluations = []
    for rule in EVALUATION_RULES:
        task = single_evaluation_task(rule, response)
        evaluation = query_model("gpt-4o", task, "")
        if "1" in evaluation and "0" not in evaluation:
            evaluation = 1
        elif "0" in evaluation and "1" not in evaluation:
            evaluation = 0
        evaluations.append(evaluation)
        if verbose:
            print(task)
            print()
            print(evaluation)
    return evaluations


def run_dataset_generation(output_filename=None, num_examples=1):
    if output_filename is None:
        output_filename = "mft_datasets" + str(dt.datetime.now()) + ".csv"
    responses = []
    responses_scores = []
    for i in range(num_examples):
        response = generate_mft_data()
        scores = evaluator(response)
        responses.append(response)
        # dont apply mean score
        # score = get_list_mean(score)
        responses_scores.append(scores)
        data = pd.DataFrame({"responses": responses, "scores": scores})
        data.to_csv(output_filename)


def evaluate_scored_datasets():
    data = pd.read_csv("mft_dataset_1.csv", index_col=0)

    means = data["scores"].apply(get_list_mean)
    good_list = []
    for mean in means:
        if type(mean) == float and mean > 9:
            good_list.append(True)
        else:
            good_list.append(False)
    data["example_score"] = good_list
    data.to_csv("mft_dataset_with_mean_scores.csv")


def get_list_mean(l: str):
    try:
        list_ = [int(i) for i in l.split(",")]
        mean = sum(list_) / len(list_)
        return mean
    except:
        return None


def filter_non_its(string):
    try:
        x = float(string)
    except:
        x = None
    return x


def print_discard_rate(filename="mft_dataset_60-560.csv"):
    data = pd.read_csv(filename, index_col=0)
    data["filtered_scores"] = data["scores"].apply(filter_non_its)
    print(len(data))
    print(data["filtered_scores"].isna().sum())
    print(len(data[data["filtered_scores"] > 8]))


if __name__ == "__main__":
    # generate_mft_data(verbose=True)
    response = generate_mft_data()
    evaluator(response)

    # run_dataset_generation()
