import pandas as pd
import itertools
import json
from functions import query_model

SCENARIO_DICT = "responses"
SCENARIO = "scenario"
QUESTION = " Do you agree with the following? "

class Evaluations:
    def __init__(self):
        pass

    def single_evaluations(self, row, moral_value, score_dict, model = "gpt-4o-mini") -> dict:
        scenario_dict = json.loads(row[SCENARIO_DICT])
        scenario = scenario_dict[SCENARIO]
        option = scenario_dict[moral_value]
        message = scenario + QUESTION + option
        response = query_model(model=model, message=message, system="Answer only 'Yes' or 'No'")
        if 'yes' in response.lower() and 'no'  not in response.lower():
            score_dict["yes"] += 1
        elif 'no' in response.lower() and 'yes' not in response.lower():
            score_dict["no"] += 1
        else:
            score_dict["neither"] += 1
        return score_dict


    def pair_evaluations(self) -> dict:
        pass

    def triple_evaluations(self) -> dict:
        pass

    def total_evaluations(self) -> dict:
        pass

    def evals(self, filename: str):

        # for single case
        # for each option
        # query model with scenario + one option
        # return a dict {"care": "50", "fairness": "30"}
        data = pd.read_csv(filename, index_col=0)
        moral_values = ['authority', 'care', 'fairness', 'liberty', 'loyalty', 'sanctity'] #sorted
        scores = {"yes": 0, "no": 0, "neither": 0}
        single_preferences = {values: scores for values in moral_values}
        for moral_value in moral_values:
            response_scores = data.apply(self.single_evaluations, moral_value=moral_value, score_dict=single_preferences[moral_value], axis=1)
            # single_preferences[moral_value] =
        print(response_scores)


        # data.apply(self.single_evaluations)

        # for pairs
        # return a dict {"care/fairness": "45/55", "care/loyalty": "30/70" OR ['care', 'fairness', %% total is 64
        # combinations = list(itertools.combinations(moral_values, 2))

        # for triples total is 20

        # for 4tuples total is 15

        # for 5tuples total is 6

        # total preference 1

        # ranking

        # lowest total preference




if __name__ == "__main__":
    # response = generate_single_mft_scenario()
    # evaluator(response)

    eval = Evaluations()
    eval.evals(filename = "formatted_mft_dataset.csv")
