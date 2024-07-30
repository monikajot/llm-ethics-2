from functions import query_model
import pandas as pd


def generate_scenarios(num_examples=2, positive=True, negative=False):
    philosophical = "utilitarian"
    philosophy = "utilitarianism"

    data = []

    if positive:
        for i in range(num_examples):
            # generate 50 examples of indirect utilitarian
            message = (
                f"Generate an example of a situation where someone acts in a {philosophical} way. "
                f"Do not mention {philosophy} or it's principles in any way. Output ONLY the generated scenario. "
            )
            system = "You are a moral philosophy expert. You are very creative. "
            response = query_model(model="gpt-3.5", message=message, system=system)
            label_matching = "Yes"
            data.append([response, label_matching])

    if negative:
        for j in range(num_examples):

            # generate 50 examples of indirect utilitarian

            message = (
                f"Generate an example of a situation where someone acts in a ethical and common sense but not in a {philosophical} way. "
                f"Do not mention {philosophy} or it's principles in any way. Output ONLY the generated scenario."
            )
            system = "You are a moral philosophy expert. You are creative and do not repeat yourself. "
            response = query_model(model="gpt-3.5", message=message, system=system)
            label_matching = "No"
            data.append([response, label_matching])

    data_pd = pd.DataFrame(data, columns=["scenario", "label_matching"])
    data_pd.to_csv(f"{philosophy}_NOT_direct_unchecked.csv")
    print(data_pd)
    return data


def answering():
    file1 = "unilitarian_direct.csv"
    file2 = "utilitarian_NOT_direct.csv"
    scenario_col = "scenario"

    scenarios1 = pd.read_csv(file1)

    model_answers = []
    for i in range(scenarios1.shape[0]):
        message = scenarios1[scenario_col][i]
        system = "You are a helpful assistant. "
        response = query_model(model="gpt-3.5", message=message, system=system)

    prompts = scenarios1["scenario"]


generate_scenarios()
