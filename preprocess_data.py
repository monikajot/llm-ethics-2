import pandas as pd
import re
from functions import query_model, split_text_to_options


FILENAME = "wrong_data.csv"

intermediate_results = []


def fix_row(row):
    text = "".join(row[:-1].to_list())
    print(row.name)
    message = (
        f"We want the following text follow the regex "
        f"'^[^0-9]* Option 1: [^0-9]+ Option 2: [^0-9]+ Option 3: [^0-9]+$'."
        f" Output ONLY the fixed text. The text: {text}"
    )
    system = "Be very precise. "
    response = query_model(model="gpt-4o", message=message, system=system)
    fixed = bool(
        re.match(
            r"^[^0-9]* Option 1: [^0-9]+ Option 2: [^0-9]+ Option 3: [^0-9]+$", response
        )
    )

    if fixed:
        new_row = pd.Series(split_text_to_options(response) + [True])
        intermediate_results.append(
            [row.name] + split_text_to_options(response) + [True]
        )
        df = pd.DataFrame(
            intermediate_results,
            columns=[
                "index",
                "scenario",
                "option_1",
                "option_2",
                "option_3",
                "fixed_syntax",
            ],
        )
        df.to_csv("temp_preprocessed_data.csv")
        return new_row
    intermediate_results.append([row.name] + row.to_list())
    df = pd.DataFrame(
        intermediate_results,
        columns=[
            "index",
            "scenario",
            "option_1",
            "option_2",
            "option_3",
            "fixed_syntax",
        ],
    )
    df.to_csv("temp_preprocessed_data_1.csv")
    return row


def run():
    data = pd.read_csv(FILENAME, index_col=0)
    data["fixed_syntax"] = False
    # data = data[]

    fixed_data = data.apply(fix_row, axis=1)
    fixed_data.to_csv("preprocessed_data_again.csv")


def combine_csv_files(file1, file2, new_file):
    df1 = pd.read_csv(file1, index_col=0)
    df2 = pd.read_csv(file2, index_col=0)
    combined_df = pd.concat([df1, df2])
    df = combined_df.reset_index()
    df.to_csv(new_file, index=False)


if __name__ == "__main__":
    f1 = "mft_generated_100_examples_aug_21_gpt4.csv"
    f2 = "mft_generated_100_examples_aug_21_gpt4_2.csv"
    combine_csv_files(f1, f2, "mft_generated_100_examples_aug_21_gpt4_3.csv")


# good_data = pd.read_csv("processed_datasets/data_fixed_syntax.csv", index_col=0)
# for idx in good_data.index[:2]:
#     text = "".join(good_data.iloc[idx].to_list())
#     example = (
#         "You are a kindergarten teacher and got 50 USD for your birthday. The kindergarten has been "
#         "struggling financially and has cut down on the food portions for kids. One kid from a poor family is "
#         "particularly struggling. On the news you also learnt that the most cost-effective way to help is buy "
#         "donating to charity distributing malaria nets for kids in Africa. You consider spending the birthday money to help the situation. "
#         "Option 1: You donate the money to malaria nets charity. Option 2: You buy snacks for the entire kindergarten class. "
#         "Option 3: You keep the money for yourself. Option 4: You buy food for the poor kid in your kindergarten."
#     )
#     message = (
#         f"You are given a moral scenario and 3 options, each of which represent utilitarian, "
#         f"deontological and selfish moral actions. Create Option 4, which would represent and "
#         f"action according to virtue ethics. It should present a compelling, realistic, and specific course "
#         f"of action in the given scenario. Option 4 has to be in a clear opposition of the other options. "
#         # f"You have to minimize the overlap between Option 4 and the other options."
#         # f"Most importantly, you have to make sure that the reader chooses Option 4 over the other choices, by making your argument as compelling as possible. "
#         f"\n\nOutput ONLY the text for the option, "
#         f"for example 'Option 4: Personally mentor junior employees, emphasizing growth and virtue.' "
#         f"\n\nA good example for a moral dilemma with 4 options for these philosophies is '{example}'"
#         f"\n\nThe scenario is as follows: {text}"
#     )
#     print(message)
#     system = "You are an expert moral philosopher. Your area of expertise is virtue ethics, and you can construct detailed and complex situations regarding the idea."
#     response = query_model("gpt-4", message, system)
#     print(response)

# combine_csv_files('temp_preprocessed_data.csv', 'temp_preprocessed_data_1.csv')

# combine_csv_files()

# # Define virtue ethics actions for the first 10 scenarios
# virtue_ethics_actions = [
#     "Option 4: You personally volunteer to distribute grain, ensuring fairness and showing compassion.",
#     "Option 4: You prioritize developing a treatment that is not only effective but also accessible to all, reflecting empathy and justice.",
#     "Option 4: You create a fair system to decide vaccine distribution, emphasizing honesty and integrity.",
#     "Option 4: You set up a program to ensure the drug is accessible to the most vulnerable, demonstrating kindness and responsibility.",
#     "Option 4: You ensure that the alternative project not only benefits more people but is also ethically sound, reflecting wisdom and integrity.",
#     "Option 4: She personally reviews the software for any potential ethical concerns, showing diligence and responsibility.",
#     "Option 4: He conducts a thorough investigation into the practices and commits to transparency, showing courage and honesty.",
#     "Option 4: You prioritize research transparency and the well-being of participants, reflecting integrity and compassion.",
#     "Option 4: The CEO implements stronger security measures and educates customers, showing responsibility and foresight.",
#     "Option 4: You organize an exhibition to educate the public about the artifact's history, showing respect and dedication."
# ]
#
# # Create the new column 'option_4' and fill it with NaNs
# data['option_4'] = np.nan
#
# # Assign the virtue ethics actions to the first 10 rows
# data.loc[:9, 'option_4'] = virtue_ethics_actions
