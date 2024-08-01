import datetime as dt
import itertools
import time

import pandas as pd

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
from functions import query_model, get_list_mean

GENERATE_SCENARIO_TEXT = (
        MFT_EXPLANATION
        + CARE
        + FAIRNESS
        + LOYALTY
        + AUTHORITY
        + SANCTITY
        + LIBERTY
        + TASK
        + RULES
        # + EXAMPLE1  # TODO: have more and randomly change them. specify only the keys and not vals
    )

MODEL= "gpt-4o-mini"
NUM_EXAMPLES = 10


def generate_single_mft_scenario(verbose: bool = True):
    response = query_model(MODEL, GENERATE_SCENARIO_TEXT, "")
    if verbose:
        print("GENERATE_SCENARIO_TEXT  -----> ", GENERATE_SCENARIO_TEXT + "\n")
        print("response   ----> ", response)
    return response


def evaluator(response: str, verbose: bool = True):
    evaluations = []
    for rule in EVALUATION_RULES:
        task = single_evaluation_task(rule, response)
        evaluation = query_model(MODEL, task, "")
        if "1" in evaluation and "0" not in evaluation:
            evaluation_score = 1
        elif "0" in evaluation and "1" not in evaluation:
            evaluation_score = 0
        else:
            evaluation_score = -1
        evaluations.append(evaluation_score)
        if verbose:
            print("%% START OF RULE EVALS")
            print("%% PRINTED SINGLE EVALUATION TASK")
            print(task)
            print()
            print("%% EVALUATIION SCORE")
            print(evaluation_score)
            print()
            # print("%% EVALUATION ")
            # print(evaluation)
            print("%% END OF RULE EVALS")
    return evaluations


def run_dataset_generation(output_filename=None, num_examples=NUM_EXAMPLES):
    start_time = time.time()
    if output_filename is None:
        output_filename = "mft_datasets" + dt.datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + ".csv"
    responses = []
    responses_scores = []
    for i in range(num_examples):
        response = generate_single_mft_scenario()
        scores = evaluator(response)
        responses.append(response)
        # dont apply mean score
        # score = get_list_mean(score)
        responses_scores.append(scores)
        data = pd.DataFrame({"responses": responses, "scores": responses_scores})
        data.to_csv(output_filename)
    print(time.time()-start_time)


def evaluate_scored_datasets(filename: str, ):
    """ Append a column of TRUE/FALSE if the scenario is good enough or not"""
    data = pd.read_csv(filename, index_col=0)

    means = data["scores"].apply(get_list_mean)
    good_list = []
    for mean in means:
        if type(mean) == float and mean > 9:
            good_list.append(True)
        else:
            good_list.append(False)
    data["example_score"] = good_list
    data.to_csv(filename+"_with_mean_scores.csv")


if __name__ == "__main__":
    # response = generate_single_mft_scenario()
    # evaluator(response)

    run_dataset_generation()
