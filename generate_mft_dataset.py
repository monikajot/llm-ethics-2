import datetime as dt
import itertools
import random
import time
import ast
import json
from tqdm import tqdm
from typing import Optional


import pandas as pd

from constants import (
    single_evaluation_task,
    foundations,
    EXAMPLE1,
    # EXAMPLE2,
    # EXAMPLE3,
    EXAMPLE4,
    EXAMPLES_MFV_BREAKING_SANCTITY,
    NEGATIVE_EVALUATION_RULES,
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
from functions import query_model, get_list_mean, string_to_json

MODEL = "gpt-4o"
NUM_EXAMPLES = 10  # 20


def generate_scenario_text(
    example: bool, rules_clear_check: bool, mft_explanation: bool, mfv_examples: bool, previous_example_str: Optional[str]
):
    generate_scenario_text = MFT_EXPLANATION
    if mft_explanation:
        value_explanations = CARE + FAIRNESS + LOYALTY + AUTHORITY + SANCTITY + LIBERTY
        generate_scenario_text += value_explanations

    generate_scenario_text += TASK + RULES

    if example:
        generate_scenario_text += "\n\nEXAMPLE: " + json.dumps(
            random.sample([EXAMPLE1, EXAMPLE4], k=1)[0]
        )
    if mfv_examples:
        generate_scenario_text += "\n\nSome examples from moral foundations vignettes. Notice these statements are negative examples of the moral faoundation, whereas we only care about positive examples: "
        generate_scenario_text += "\nSanctity: " + "".join(
            [
                "\n" + str(i) + ". " + val
                for i, val in enumerate(EXAMPLES_MFV_BREAKING_SANCTITY)
            ]
        )
    if rules_clear_check:
        generate_scenario_text += "\n If something in the task is unclear, make sure to clarify it before answering"
        generate_scenario_text += "\n Do you understand the rules? Go through each rule, explain it back to me and say if you have any uncertainties or confusions about it "
    if previous_example_str:
        generate_scenario_text += previous_example_str
    return generate_scenario_text


def generate_single_mft_scenario(
    example: bool,
    rules_clear_check: bool,
    mft_explanation: bool,
    mfv_examples: bool,
    previous_examples: bool,
    verbose: bool = False,
):
    previous_example_str = None
    if previous_examples:
        data = pd.read_csv("previous_examples.csv", index_col=0)
        row_idx = random.sample(list(range(len(data))), 5)
        previous_examples_vals = data["responses"].iloc[row_idx]
        previous_examples_scores = [str(sum(ast.literal_eval(val))) for val in data["scores"].iloc[row_idx]]
        previous_example_str = "\n\nThese are previously generated examples with their scores (max score 19). The generated example must be different from the ones already generated:"
        previous_example_str += "".join(["\n" + example + " EXAMPLE SCORE: " + previous_examples_scores[i] for i, example in enumerate(previous_examples_vals)])
    prompt = generate_scenario_text(
        example, rules_clear_check, mft_explanation, mfv_examples, previous_example_str
    )
    response = query_model(MODEL, prompt, "")
    if verbose:
        print("GENERATE_SCENARIO_TEXT  -----> ", prompt + "\n")
        print("response   ----> ", response)
    return response


def run_dataset_generation(
    example,
    rules_clear_check,
    mft_explanation,
    mfv_examples,
    previous_examples: bool,
    output_filename=None,
    num_examples=NUM_EXAMPLES,
    only_flag="",
):
    start_time = time.time()
    if output_filename is None:
        output_filename = (
            "mft_datasets" + dt.datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + ".csv"
        )
    responses = []
    responses_scores = []
    score_dict = {rule: [] for rule in EVALUATION_RULES + NEGATIVE_EVALUATION_RULES}
    for _ in tqdm(range(num_examples)):
        # generate scenario
        response = generate_single_mft_scenario(
            example, rules_clear_check, mft_explanation, mfv_examples, previous_examples
        )
        isinstance(response, dict)

        # evaluate scenario
        scores, score_dict = evaluator(response, score_dict, only_flag=only_flag)
        responses.append(response)
        responses_scores.append(scores)
        data_dict = {"responses": responses, "scores": responses_scores}
        data = pd.DataFrame({**data_dict, **score_dict})
        data.to_csv(output_filename)

    print(time.time() - start_time)
    return data


def evaluator(response: str, score_dict: dict, only_flag: str, verbose: bool = False):
    evaluations = []
    for eval_quest in EVALUATION_RULES + NEGATIVE_EVALUATION_RULES:
        task = single_evaluation_task(eval_quest, response, only_flag=only_flag)
        evaluation = query_model(MODEL, task, "")
        if eval_quest in EVALUATION_RULES:
            if "1" in evaluation and "0" not in evaluation:
                evaluation_score = 1
            elif "0" in evaluation and "1" not in evaluation:
                evaluation_score = 0
            else:
                evaluation_score = -1
        elif eval_quest in NEGATIVE_EVALUATION_RULES:
            if "1" in evaluation and "0" not in evaluation:
                evaluation_score = 0
            elif "0" in evaluation and "1" not in evaluation:
                evaluation_score = 1
            else:
                evaluation_score = -1
        else:
            evaluation_score = -1
        score_dict[eval_quest].append(evaluation_score)
        evaluations.append(evaluation_score)
        if verbose:
            print("%% START OF RULE EVALS")
            print("%% PRINTED SINGLE EVALUATION Q")
            print(eval_quest)
            print()
            print("%% EVALUATION SCORE")
            print(evaluation_score)
            print()
            print("%% EVALUATION ")
            print(evaluation)
            print("%% END OF RULE EVALS")
    return evaluations, score_dict


def scored_datasets_with_means(filename: str):
    """Append a column of TRUE/FALSE if the scenario is good enough or not"""
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
    data.to_csv(filename + "_with_mean_scores.csv")


def get_best_examples(input_filename: str, percent: int):
    data = pd.read_csv(input_filename, index_col=0)
    data["sums"] = data["scores"].apply(lambda x: ast.literal_eval(x)).apply(sum)
    sorted_data = data.sort_values(by="sums", ascending=False)
    num_rows = int(len(data) * (percent / 100))
    top_x_percent = sorted_data.head(num_rows)
    top_x_percent.to_csv(f"top_{percent}p_of_" + input_filename)


def preprocess_scenario(example: str):
    # example = example.replace("'", '"')
    example = example.replace("\n", "")

    example_dict = string_to_json(example)

    if isinstance(example_dict, dict):
        keys = [
            "scenario",
            "care",
            "fairness",
            "loyalty",
            "authority",
            "sanctity",
            "liberty",
        ]
        if set(example_dict.keys()) == set(keys):
            return example_dict
    return


def check_dataset_formatting(input_filename: str = None, data: pd.DataFrame = None, save=True):
    if input_filename:
        data = pd.read_csv(input_filename, index_col=0)
    rows = []
    for row_idx in tqdm(range(len(data))):
        # print(row_idx)
        row = data["responses"].iloc[row_idx]
        row = preprocess_scenario(row)
        rows.append(json.dumps(row))
    data["responses"] = pd.Series(rows)
    data_no_nans = data.dropna()
    reindexed_data = data_no_nans.reset_index(drop=True)
    # data drop nans
    if save:
        output_file = "test_formatted_" + input_filename
        reindexed_data.to_csv( output_file)
    return reindexed_data


def run():
    # generate and evaluate examples
    # check format
    # get best X examples
    pass


if __name__ == "__main__":
    response = generate_single_mft_scenario(example=True, rules_clear_check=False, mft_explanation=True, mfv_examples=False, previous_examples=False, verbose=True)
    print(response)
    # evaluator(response)

    name = "mft_generated_200_aug_27_gpt4o_with_examples_sanc_loya_lib_emph_9"
    # name1 = "test_formatted_mft_generated_100_aug_26_gpt4o_with_examples_sanctity_emph_2.csv"
    # print(generate_scenario_text(example=True, rules_clear_check=False, mft_explanation=True, mfv_examples=True))
    # generate data
    # data = run_dataset_generation(output_filename=f"{name}.csv", num_examples=100, only_flag="ONLY", example=True, rules_clear_check=False, mft_explanation=True, mfv_examples=False, previous_examples=False)
    # check_dataset_formatting(input_filename=f"{name}.csv")
    # data = pd.read_csv(name, index_col=0)
    # data_no_nans = data.dropna()
    # reindexed_data = data_no_nans.reset_index(drop=True)
    # reindexed_data.to_csv("no_nans"+ name)
    # get_best_examples(input_filename=f"formatted_{name}.csv", percent=50)
    # get_best_examples(f, 10)
    # pass

    # which model produces better scenarios and by how much?
    # see if g4m and g4o evaluations are the same (what percentage of them agree?)

    # can i improve preprompting to get better examples
    # cost gpt4o ~5$, gpt4o ~15c
