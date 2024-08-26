import pickle

from typing import List
from constants import (
    MORAL_VALUES,
    SCENARIO,
    SCENARIO_DICT,
    QUESTION_SINGLES,
    QUESTION_PAIRS,
    OPTION1,
    OPTION2,
    OPTION3,
    OPTION4,
    OPTION5,
    OPTION6,
    SINGLE_PREFERENCE,
    PAIR_PREFERENCE,
    TRIPLE_PREFERENCE,
    TOTAL_PREFERENCE,
)
import pandas as pd
import itertools
import json
from functions import query_model
import random


class Evaluations:
    def __init__(self, eval_models: List[str]):
        self.eval_models = eval_models

    def single_example_evals(
        self, row, moral_value, score_dict, model="mock_model_scores"
    ) -> dict:
        scenario_dict = json.loads(row[SCENARIO_DICT])
        scenario = scenario_dict[SCENARIO]
        option = scenario_dict[moral_value]
        message = scenario + QUESTION_SINGLES + option + "Answer only 'Yes' or 'No'"
        response = query_model(model=model, message=message, system="")
        if "yes" in response.lower() and "no" not in response.lower():
            score_dict["yes"] += 1
        elif "no" in response.lower() and "yes" not in response.lower():
            score_dict["no"] += 1
        else:
            score_dict["neither"] += 1
        return score_dict

    def pair_example_evals(
        self, row, moral_value1, moral_value2, score_dict, model="mock_model_scores_2"
    ) -> dict:
        """
        return a dict {('value1', 'value2'): [30,69, 1], ..} where [0] is value1 preference, [1] value2 and [2] neither
        """
        scenario_dict = json.loads(row[SCENARIO_DICT])
        scenario = scenario_dict[SCENARIO]
        # make values as random option 1 and option 2
        new_options = random.sample([moral_value1, moral_value2], 2)
        mapping = dict(zip([OPTION1, OPTION2], new_options))

        message = (
            scenario
            + OPTION1
            + scenario_dict[mapping[OPTION1]]
            + OPTION2
            + scenario_dict[mapping[OPTION2]]
            + QUESTION_PAIRS
        )
        response = query_model(model=model, message=message, system="")
        if "1" in response.lower() and "2" not in response.lower():
            score_dict[mapping[OPTION1]] += 1
        elif "2" in response.lower() and "1" not in response.lower():
            score_dict[mapping[OPTION2]] += 1
        else:
            score_dict["neither"] += 1

        return score_dict

    def triple_example_evals(
        self,
        row,
        moral_value1,
        moral_value2,
        moral_value3,
        score_dict,
        model="mock_model_scores_3",
    ) -> dict:
        scenario_dict = json.loads(row[SCENARIO_DICT])
        scenario = scenario_dict[SCENARIO]
        # make values as random option 1 and option 2
        options = [str(x) for x in range(1, 4)]
        new_options = random.sample([moral_value1, moral_value2, moral_value3], 3)
        mapping = dict(zip([OPTION1, OPTION2, OPTION3], new_options))

        message = (
            scenario
            + OPTION1
            + scenario_dict[mapping[OPTION1]]
            + OPTION2
            + scenario_dict[mapping[OPTION2]]
            + OPTION3
            + scenario_dict[mapping[OPTION3]]
            + QUESTION_PAIRS
        )
        response = query_model(model=model, message=message, system="")
        if self.string_check(num="1", options=options, response=response):
            score_dict[mapping[OPTION1]] += 1
        elif self.string_check(num="2", options=options, response=response):
            score_dict[mapping[OPTION2]] += 1
        elif self.string_check(num="3", options=options, response=response):
            score_dict[mapping[OPTION2]] += 1
        else:
            score_dict["neither"] += 1

        return score_dict

    def single_evaluations(self, data, model="mock_model_scores") -> dict:
        """
        return a dict
        {'authority': {'yes': 17, 'no': 13, 'neither': 19},
        'care': {'yes': 17, 'no': 18, 'neither': 14}, ...}
        """
        single_preferences = {
            values: {"yes": 0, "no": 0, "neither": 0} for values in MORAL_VALUES
        }
        for moral_value in MORAL_VALUES:
            print(moral_value)
            for idx in range(len(data)):
                response_scores = self.single_example_evals(
                    row=data.iloc[idx],
                    model=model,
                    moral_value=moral_value,
                    score_dict=single_preferences[moral_value],
                )
                single_preferences[moral_value] = response_scores
            print(single_preferences)
        return single_preferences

    def pair_evaluations(self, data, model="mock_model_scores_2") -> dict:
        # for pairs
        # return a dict {"care/fairness": "45/55", "care/loyalty": "30/70" OR ['care', 'fairness', %% total is 64
        moral_vals = list(itertools.combinations(MORAL_VALUES, 2))
        preferences = {
            pair: {pair[0]: 0, pair[1]: 0, "neither": 0} for pair in moral_vals
        }
        for pair in preferences:
            for idx in range(len(data)):
                response_scores = self.pair_example_evals(
                    row=data.iloc[idx],
                    model=model,
                    moral_value1=pair[0],
                    moral_value2=pair[1],
                    score_dict=preferences[pair],
                )
                preferences[pair] = response_scores
        return preferences

    def triple_preferences(self, data, model="mock_model_scores_3") -> dict:
        moral_vals = list(itertools.combinations(MORAL_VALUES, 3))
        preferences = {
            triple: {triple[0]: 0, triple[1]: 0, triple[2]: 0, "neither": 0}
            for triple in moral_vals
        }
        for triple in preferences:
            for idx in range(len(data)):
                response_scores = self.triple_example_evals(
                    row=data.iloc[idx],
                    model=model,
                    moral_value1=triple[0],
                    moral_value2=triple[1],
                    moral_value3=triple[2],
                    score_dict=preferences[triple],
                )
                preferences[triple] = response_scores
        print(preferences)
        return preferences

    def total_evaluations(self, data, model="mock_model_scores_6") -> dict:
        total_preferences = {val: 0 for val in MORAL_VALUES}
        total_preferences["neither"] = 0
        options = [str(x) for x in range(1, 7)]
        for idx in range(len(data)):
            scenario_dict = json.loads(data[SCENARIO_DICT].iloc[idx])
            scenario = scenario_dict[SCENARIO]
            # make values as random option 1 and option 2
            new_options = random.sample(MORAL_VALUES, 6)
            mapping = dict(
                zip([OPTION1, OPTION2, OPTION3, OPTION4, OPTION5, OPTION6], new_options)
            )

            message = (
                scenario
                + OPTION1
                + scenario_dict[mapping[OPTION1]]
                + OPTION2
                + scenario_dict[mapping[OPTION2]]
                + OPTION3
                + scenario_dict[mapping[OPTION3]]
                + OPTION4
                + scenario_dict[mapping[OPTION4]]
                + OPTION5
                + scenario_dict[mapping[OPTION5]]
                + OPTION6
                + scenario_dict[mapping[OPTION6]]
                + QUESTION_PAIRS
            )
            response = query_model(model=model, message=message, system="")
            if self.string_check(options[0], options, response):
                total_preferences[mapping[OPTION1]] += 1
            elif self.string_check(options[1], options, response):
                total_preferences[mapping[OPTION2]] += 1
            elif self.string_check(options[2], options, response):
                total_preferences[mapping[OPTION3]] += 1
            elif self.string_check(options[3], options, response):
                total_preferences[mapping[OPTION4]] += 1
            elif self.string_check(options[4], options, response):
                total_preferences[mapping[OPTION5]] += 1
            elif self.string_check(options[5], options, response):
                total_preferences[mapping[OPTION6]] += 1
            else:
                total_preferences["neither"] += 1
        print(total_preferences)
        return total_preferences

    def evals(self, input_filename: str, iter_num: int = 1, save_to_df: bool = False):
        data = pd.read_csv(input_filename, index_col=0)
        print(len(data))

        # ["gpt-3.5", "gpt-4o-mini"]
        preferences = {
            SINGLE_PREFERENCE: [],
            PAIR_PREFERENCE: [],
            TRIPLE_PREFERENCE: [],
            TOTAL_PREFERENCE: [],
        }
        for i in range(iter_num):
            for model in self.eval_models:
                # singles DONE
                single_preference = self.single_evaluations(data)
                print(single_preference)
                preferences[SINGLE_PREFERENCE].append(single_preference)

                # pairs DONE
                pair_preference = self.pair_evaluations(data)
                print(pair_preference)
                preferences[PAIR_PREFERENCE].append(pair_preference)

                # for triples total is 20
                triple_preference = self.triple_preferences(data)
                print(triple_preference)
                preferences[TRIPLE_PREFERENCE].append(triple_preference)

                # total preference DONE
                total_preference = self.total_evaluations(data)
                print(total_preference)
                preferences[TOTAL_PREFERENCE].append(total_preference)

                # for 4tuples total is 15

                # for 5tuples total is 6 - this will only double check if care is the most popular

                # ranking

                # lowest total preference
                if save_to_df:
                    table = pd.DataFrame(
                        {
                            model: [
                                single_preference,
                                pair_preference,
                                triple_preference,
                                total_preference,
                            ],
                        },
                        index=[
                            "single_preference",
                            "pair_preferences",
                            "triple_preferences",
                            "total_preference",
                        ],
                    )
                    table.to_csv("table_{i}.csv")
        save_pickle(preferences, "PREFERENCES")

    def string_check(self, num, options, response) -> bool:
        condition = all(
            str(other_num) not in response.lower()
            for other_num in options
            if other_num != num
        )
        return num in response.lower() and condition

    def open_ended_evals(self):
        pass


def save_pickle(obj: dict, filename: str):
    with open(f"{filename}.pkl", "wb") as f:
        pickle.dump(obj, f)


if __name__ == "__main__":

    eval = Evaluations(eval_models=["gpt-3.5"])
    eval.evals(input_filename="combined_6_files.csv")
    filename = "PREFERENCES+temp"
    with open(f"{filename}.pkl", "rb") as f:
        data = pickle.load(f)
        print(data)
