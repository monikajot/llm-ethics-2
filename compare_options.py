import pandas as pd
import random
from functions import get_direct_data, query_model
from tqdm import tqdm

# shuffle_flag = False
MODEL = "gpt-3.5"
QUESTION = "Which statement you are more likely to say? "
DATA = pd.read_csv("datasets/indirect_util_deon_evil_849.csv")
SCENARIOS = DATA["scenario"]
UTILITARIAN_OPTIONS = DATA["option_1"]
DEONTOLOGICAL_OPTIONS = DATA["option_2"]


def save_df(data, name):
    df = pd.DataFrame(data, columns=["iter", "message", "response", "answer_label"])
    df.to_csv(name)


def run_compare_option_analysis(
    deontology_data=DEONTOLOGICAL_OPTIONS,
    utilitarian_data=UTILITARIAN_OPTIONS,
    scenarios=None,
):
    # deon_comp_data, util_comp_data = get_direct_data()

    deontology_data = deontology_data.apply(lambda string_val: string_val[9:])
    utilitarian_data = utilitarian_data.apply(lambda string_val: string_val[9:])

    deont = "deontology"
    utilit = "utilitarianism"

    results_map = {deont: 0, utilit: 0, "wrong": 0}
    results_data = []

    shuffle_flag = False
    num_iter = 1  # number of times to run all queries

    for n in range(num_iter):
        print(f"STARTING {n}th ITER")
        for i in tqdm(range(len(scenarios))):
            # shuffle rows
            if shuffle_flag: #for direct case!!
                deontology_data = deontology_data.sample(
                    frac=1, random_state=1
                ).reset_index()["statement"]
                utilitarian_data = utilitarian_data.sample(
                    frac=1, random_state=1
                ).reset_index()["statement"]

            map_ = {deont: deontology_data, utilit: utilitarian_data}
            options = [deont, utilit]
            # shuffle options so A and B represent different things
            random_options = sorted(options, key=lambda x: random.random())

            first_statement = map_[random_options[0]][i]
            second_statement = map_[random_options[1]][i]
            if scenarios is not None:
                scenario = scenarios[i]
            else:
                scenario = ""
            message = (
                scenario
                + QUESTION
                + "(A) "
                + first_statement
                + " (B) "
                + second_statement
            )
            system = "Answer only (A) or (B)."
            # print(message)
            response = query_model(model=MODEL, message=message, system=system)
            # print(response)
            if "A" in response and "B" not in response:
                results_map[random_options[0]] += 1
                # print(random_options[0])
                results_data.append([n, message, response, random_options[0]])
            elif "B" in response and "A" not in response:
                results_map[random_options[1]] += 1
                # print(random_options[1])
                results_data.append([n, message, response, random_options[1]])
            else:
                results_map["wrong"] += 1
                results_data.append([n, message, response, "wrong"])

            if i % 10 == 0:
                save_df(results_data, "temp_indirect_output.csv")

    print("RESULTS", results_map)
    pd.DataFrame(results_map, index=[0]).to_csv(f"indirect_results.csv")
    save_df(results_data, "final_indirect_output.csv")



run_compare_option_analysis(
    deontology_data=DEONTOLOGICAL_OPTIONS,
    utilitarian_data=UTILITARIAN_OPTIONS,
    scenarios=SCENARIOS,
)
