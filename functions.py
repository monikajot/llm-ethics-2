import os
import time

import cohere
import pandas as pd
import random
from openai import OpenAI


client = OpenAI()
co = cohere.Client(os.environ.get("CO_API_KEY"))


def query_model(model, message, system, logprobs=False):
    try:
        if model == "cohere":
            response = co.chat(
                chat_history=[],
                message=message,
            )
            # print(response)
            response = response.text

        if model == "gpt-3.5":
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo-1106",
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": message},
                ],
                logprobs=logprobs,
            )

            # print(completion.choices[0].message)
            response = completion.choices[0].message.content

        if model == "gpt-4":
            response = client.chat.completions.create(
                model="gpt-4-0613",
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": message},
                ],
                logprobs=logprobs,
            )
            response = response.choices[0].message.content

        if model == "gpt-4o-mini":
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": message},
                ],
                logprobs=logprobs,
            )
            response = response.choices[0].message.content

        if model == "gpt-4o":
            response = client.chat.completions.create(
                model="gpt-4o-2024-05-13",
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": message},
                ],
                logprobs=logprobs,
            )
            response = response.choices[0].message.content

        if model == "claude":
            message = message
            response = client.messages.create(
                model="claude-2.1",
                max_tokens=1024,
                system=system,
                messages=[{"role": "user", "content": message}],
            )
            response = response.content[0].text
            print(response)

        if model == "mock_model_scores":
            response = random.choices(["yes", "no", "neither"])[0]

        if model == "mock_model_scores_2":
            response = random.choices(["Option 1", "Option 2", "neither"])[0]
        if model == "mock_model_scores_3":
            response = random.choices(["Option 1", "Option 2", "Option 3", "neither"])[
                0
            ]
        if model == "mock_model_scores_6":
            response = random.choices(
                [
                    "Option 1",
                    "Option 2",
                    "Option 3",
                    "Option 4",
                    "Option 5",
                    "Option 6",
                    "neither",
                ]
            )[0]

    except ValueError:
        time.sleep(30)
        response = query_model(model, message, system)
    return response


def get_direct_data():
    deontology_full_data = pd.read_csv("datasets/deontology_direct.csv")
    utilitarian_full_data = pd.read_csv("datasets/utilitarian_direct.csv")

    num_rows = (
        len(deontology_full_data) - 1
    )  # at the beginning only do for this many examples

    deontology_data = deontology_full_data[:num_rows]
    utilitarian_data = utilitarian_full_data[:num_rows]

    # # compare utilitarian vs deontology model views
    # extract only the text that has positive statements
    deon_comp_data = deontology_data[
        deontology_data["answer_matching_behavior"] == " Yes"
    ].reset_index()["statement"]
    util_comp_data = utilitarian_data[
        utilitarian_data["answer_matching_behavior"] == " Yes"
    ].reset_index()["statement"]
    return deon_comp_data, util_comp_data


def generate_dataset_from_all_scenarions():
    all_indirect_scenarios = pd.read_csv("datasets/ALL_SCENARIOS.csv")
    n = len(all_indirect_scenarios)
    data = []
    for i in range(n):
        prompt = all_indirect_scenarios["prompt"][i]
        if any(
            str in prompt.lower()
            for str in ["utilita", "deonto", "evil", "selfish", "deceitful"]
        ):
            continue
        prompt = prompt.replace("\n", " ")
        idx = prompt.find("Option")
        idx2 = prompt.find("Option", idx + 1)
        idx3 = prompt.find("Option", idx2 + 1)
        # print(idx, idx2, idx3)
        scenario = prompt[:idx]
        option_1 = prompt[idx:idx2]
        option_2 = prompt[idx2:idx3]
        option_3 = prompt[idx3:]
        if (
            len(scenario) > 15
            and len(option_1) > 15
            and len(option_2) > 15
            and len(option_3) > 15
        ):
            data.append([scenario, option_1, option_2, option_3])
    df = pd.DataFrame(data, columns=["scenario", "option_1", "option_2", "option_3"])
    N = len(df)
    df.to_csv(f"indirect_util_deon_evil_{N}.csv")


def split_text_to_options(prompt):
    idx = prompt.find("Option")
    idx2 = prompt.find("Option", idx + 1)
    idx3 = prompt.find("Option", idx2 + 1)
    # print(idx, idx2, idx3)
    scenario = prompt[:idx]
    option_1 = prompt[idx:idx2]
    option_2 = prompt[idx2:idx3]
    option_3 = prompt[idx3:]
    return [scenario, option_1, option_2, option_3]


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
    # generate_dataset_from_all_scenarions()
    # # test
    response = query_model(
        "gpt-3.5",
        "Hello! Can you help me with a maths problem",
        "You are a helpful assistant. ",
    )
    print(response)

    # completion = client.chat.completions.create(
    #   model="gpt-3.5",
    #   messages=[
    #     {"role": "system",
    #     "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    #     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    #   ]
    # )
