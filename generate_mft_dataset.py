import datetime as dt
import itertools
import time
import ast
import json

from json.decoder import JSONDecodeError

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
        # + " \n If something in the task is unclear, make sure to clarify it before answering"
        # + "\n Do you understand the rules? Go through each rule, explain it back to me and say if you have any uncertainties or confusions about it. "
        # + EXAMPLE1  # TODO: have more and randomly change them. specify only the keys and not vals
)

MODEL= "gpt-4o"
NUM_EXAMPLES = 40# 20


def generate_single_mft_scenario(verbose: bool = True):
    response = query_model(MODEL, GENERATE_SCENARIO_TEXT, "")
    if verbose:
        print("GENERATE_SCENARIO_TEXT  -----> ", GENERATE_SCENARIO_TEXT + "\n")
        print("response   ----> ", response)
    return response


def run_dataset_generation(output_filename=None, num_examples=NUM_EXAMPLES):
    start_time = time.time()
    if output_filename is None:
        output_filename = "mft_datasets" + dt.datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + ".csv"
    responses = []
    responses_scores = []
    score_dict = {rule: [] for rule in EVALUATION_RULES}
    for i in range(num_examples):
        response = generate_single_mft_scenario()
        # test response format
        isinstance(response, dict)
        scores, score_dict = evaluator(response, score_dict)
        responses.append(response)
        # dont apply mean score
        # score = get_list_mean(score)
        responses_scores.append(scores)
        data_dict = {"responses": responses, "scores": responses_scores}
        data = pd.DataFrame({**data_dict, **score_dict})
        data.to_csv(output_filename)
    print(time.time()-start_time)


def evaluator(response: str, score_dict: dict, verbose: bool = True):
    evaluations = []
    for eval_quest in EVALUATION_RULES:
        task = single_evaluation_task(eval_quest, response)
        evaluation = query_model(MODEL, task, "")
        if "1" in evaluation and "0" not in evaluation:
            evaluation_score = 1
        elif "0" in evaluation and "1" not in evaluation:
            evaluation_score = 0
        else:
            evaluation_score = -1
        score_dict[eval_quest].append(evaluation_score)
        evaluations.append(evaluation_score)
        if verbose:
            print("%% START OF RULE EVALS")
            print("%% PRINTED SINGLE EVALUATION Q")
            print(eval_quest)
            print()
            print("%% EVALUATIION SCORE")
            print(evaluation_score)
            print()
            print("%% EVALUATION ")
            print(evaluation)
            print("%% END OF RULE EVALS")
    return evaluations, score_dict


def scored_datasets_with_means(filename: str, ):
    """ Append a column of TRUE/FALSE if the scenario is good enough or not"""
    data = pd.read_csv(filename, index_col=0)
    # invert qs

    means = data["scores"].apply(get_list_mean)
    good_list = []
    for mean in means:
        if type(mean) == float and mean > 9:
            good_list.append(True)
        else:
            good_list.append(False)
    data["example_score"] = good_list
    data.to_csv(filename+"_with_mean_scores.csv")


def get_best_examples(filename: str, percent: int):
    data = pd.read_csv(filename, index_col=0)
    data["sums"] = data["scores"].apply(lambda x: ast.literal_eval(x) ).apply(sum)
    sorted_data = data.sort_values(by="sums", ascending=False)
    num_rows = int(len(data) * (percent / 100))
    top_x_percent = sorted_data.head(num_rows)
    top_x_percent.to_csv( f"top_{percent}p_of_" + filename)


def preprocess_scenario(example: str):
    example = example.replace("'", "")
    example = example.replace("\n", "")

    try:
        example_dict = json.loads(example)
    except JSONDecodeError:
        return

    if isinstance(example_dict, dict):
        keys = ['scenario', 'care', 'fairness', 'loyalty', 'authority', 'sanctity', 'liberty']
        if list(example_dict.keys()) == keys:
            return example
    return


def check_dataset_formatting(filename: str):
    data = pd.read_csv(filename, index_col=0)
    rows = []
    for row_idx in range(len(data)):
        print(row_idx)
        row = data["responses"].iloc[row_idx]
        row = preprocess_scenario(row)
        rows.append(row)
    data["responses"] = pd.Series(rows)
    #data drop nans
    data.to_csv("formatted_" + filename)

def run():
    # generate and evaluate examples
    # check format
    # get best X examples
    pass


if __name__ == "__main__":
    # response = generate_single_mft_scenario()
    # evaluator(response)

    # run_dataset_generation()
    pass
    # get_best_examples(f, 10)


