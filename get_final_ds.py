import pandas as pd
import numpy as np
import ast
import matplotlib.pyplot as plt
from generate_mft_dataset import check_dataset_formatting
from functions import combine_csv_files
from dataset_checks import generated_data_evaluation_value_counts, dataset_hist

path = "datasets/"
# files = [
#     "test_formatted_mft_generated_100_examples_aug_21_gpt4_3.csv",
#     "formatted_mft_generated_100_examples_aug_19.csv",
#     "test_formatted_mft_generated_100_aug_26_gpt4o_with_examples.csv",
#     "test_formatted_mft_generated_100_aug_26_gpt4o_with_examples_sanctity_emph.csv",
#     "test_formatted_mft_generated_100_aug_26_gpt4o_with_examples_sanctity_emph_2.csv",
#     "test_formatted_mft_generated_100_aug_26_gpt4o_with_examples_sanctity_emph_MFV.csv",
#     "mft_generated_100_aug_26_gpt4o_with_examples_sanc_loya_lib_emph.csv"
#     "test_formatted_mft_generated_100_aug_26_gpt4o_with_examples_sanc_loya_lib_emph.csv",
#     "test_formatted_mft_generated_200_aug_27_gpt4o_with_examples_sanc_loya_lib_emph_2.csv",
#     "test_formatted_mft_generated_200_aug_27_gpt4o_with_examples_sanc_loya_lib_emph.csv",
#     "test_formatted_mft_generated_200_aug_27_gpt4o_with_examples_sanc_loya_lib_emph_4.csv",
#     "test_formatted_mft_generated_200_aug_27_gpt4o_with_examples_sanc_loya_lib_emph_5.csv",
# ]
files = [
    "combined_12_files.csv",
    "test_formatted_mft_generated_200_aug_27_gpt4o_with_examples_sanc_loya_lib_emph_8.csv",
    "test_formatted_mft_generated_200_aug_27_gpt4o_with_examples_sanc_loya_lib_emph_9.csv"
]
cols = [
    "Does the care option precisely and rigorously represent the care moral foundation?",
    "Does the authority option precisely and rigorously represent the authority moral foundation?",
    "Does the liberty option precisely and rigorously represent the liberty moral foundation?",
    "Does the fairness option precisely and rigorously represent the fairness moral foundation?",
    "Does the sanctity option precisely and rigorously represent the sanctity moral foundation?",
    "Does the loyalty option precisely and rigorously represent the loyalty moral foundation?",
]


def get_balanced_data(df):
    # Current count of ones
    current_ones = df.sum()

    # Target count of ones (the ideal balanced number)
    target_ones = min(current_ones)

    # Initialize an empty DataFrame to store the selected rows
    selected_rows = pd.DataFrame(columns=df.columns)

    # Iteratively select rows
    for i, row in df.iterrows():
        # If adding the current row still maintains the balance
        if all(current_ones + row <= target_ones):
            selected_rows = selected_rows.append(row)
            current_ones += row

        # Stop if balance is achieved
        if all(current_ones == target_ones):
            break

    # Print the selected rows and the final counts
    # print(selected_rows)
    print(selected_rows.sum())


if __name__ == "__main__":
    col1 = 'Does the sanctity option precisely and rigorously represent the sanctity moral foundation?'
    col2 = 'Does the liberty option precisely and rigorously represent the liberty moral foundation?'
    col3 = 'Does the loyalty option precisely and rigorously represent the loyalty moral foundation?'
    col4 = 'Does the fairness option precisely and rigorously represent the fairness moral foundation?'
    col6 = 'Does the care option precisely and rigorously represent the care moral foundation?'
    col5 = 'Does the authority option precisely and rigorously represent the authority moral foundation?'

    file = "combined_14_files.csv"
    df = pd.read_csv(file, index_col=0)
    df = df.sort_values(by=[col1, col2, col3,col4,col5,col6], ascending=[False]*3+[True]*3)
    # final_data = sorted_data[[col1, col2, col3, col4, col5, col6]].iloc[:700]

    # print(final_data)

    # get the best data
    # best_df = data[(data[cols] == [1]*6).all(axis=1)]
    # rest_df = data[~(data[cols] == [1]*6).all(axis=1)]
    # a=1
    #
    # # sort the rest
    # data["sums"] = data["scores"].apply(lambda x: ast.literal_eval(x)).apply(sum)
    # rest_df = data.sort_values(by="sums", ascending=False)
    # final_data = rest_df[:1000]
    # for col in cols:
    #     print(final_data[col].value_counts())
    inter1 = df[(df[[col1, col2, col3]] == 1).all(axis=1)]
    inter2 = df[(df[[col1, col2]] == 1).all(axis=1)]
    inter3 = df[(df[[col1, col3]] == 1).all(axis=1)]
    inter4 = df[(df[[col2, col3]] == 1).all(axis=1)]

    inter5 = df[~(df[[col4, col5]] == 1).any(axis=1) & (df[df[[col1, col2, col3]] == 1].any(axis=1))]
    sanctity_df = df[df[col1] == 1][:850]
    liberty_df = df[df[col2] == 1][:850]
    loyalty_df = df[df[col3] == 1][:840]
    good_data = pd.concat([sanctity_df, liberty_df, loyalty_df])

    chosen_data = pd.concat([inter1, inter2, inter3, good_data]).drop_duplicates()
    for col in cols:
        print(chosen_data[col].value_counts())
    # chosen_data.to_csv("final_data_27d_21h.csv")

    #
    a = 1


    # df1 = pd.read_csv("combined_12_files.csv", index_col=0)
    # all_data = [df1]
    # for file in files[1:]:
    #     df = pd.read_csv(file, index_col=0)
    #     all_data.append(df)
    # all_data_df = pd.concat(all_data).dropna(subset=["responses"]).reset_index(drop=True)
    # all_data_df.to_csv("combined_14_files.csv")

    # df1 = pd.read_csv(files[0], index_col=0)
    # df2 = pd.read_csv(files[1], index_col=0)
    # df3 = pd.read_csv(files[2], index_col=0)
    # # df4 = pd.read_csv(files[3], index_col=0)
    # all_data_df = pd.concat([df1, df2, df3])
    # df = all_data_df.dropna(subset=["responses"]).reset_index(drop=True)
    # df.to_csv("combined_12_files.csv")


    # max_ones = max(df[col1].sum(), df[col2].sum(), df[col3].sum())
    # min_ones = min(df[col1].sum(), df[col2].sum(), df[col3].sum())
    # df = df.loc[
    #     np.logical_and(
    #         df[col1] == 1, np.logical_and(df[col2] == 1, df[col3] == 1)
    #     )
    #     & (max_ones - min_ones < 50)
    # ]
    # a=1
    # for col in cols:
    #     data[col] = data[col].apply(lambda x: int(x))
    if False:
        chosen_data["sums"] = chosen_data["scores"].apply(lambda x: ast.literal_eval(x)).apply(sum)
        # get_balanced_data(data[cols])
        sorted_data = chosen_data.sort_values(by="sums", ascending=False)
        # best_data = chosen_data[chosen_data["sums"] > 15]
        # print(best_data.value_counts())

        ax = sorted_data["sums"].hist(bins=19, )
        ax.set_xlabel("Scores")
        ax.set_ylabel("Scenarios")
        plt.show()
    # filtered_df = best_data[(best_data[[col1]] == 1).any(axis=1)]
    # for col in cols:
    #     print(chosen_data[col].value_counts())
    #


    # data.sort_values(by=['Does the care option precisely and rigorously represent the care moral foundation?',
    #                      'Does the authority option precisely and rigorously represent the authority moral foundation?',
    #                      'Does the liberty option precisely and rigorously represent the liberty moral foundation?',
    #                      'Does the fairness option precisely and rigorously represent the fairness moral foundation?',
    #                      'Does the sanctity option precisely and rigorously represent the sanctity moral foundation?',
    #                      'Does the loyalty option precisely and rigorously represent the loyalty moral foundation?', ],
    #                  ascending=[False] * 6)
    # sanctity_df = data[data[col1] == 1]
    # non_sanc_df = data[data['Does the sanctity option precisely and rigorously represent the sanctity moral foundation?'] == 0]
    # liberty_df = data[data[col2] == 1][:len(sanctity_df)]
    # loyalty_df = data[data[col3] == 1][:len(sanctity_df)]
    # # good_data = pd.concat([sanctity_df, liberty_df, loyalty_df]).drop_duplicates()
    # for col in cols:
    #     print(chosen_data[col].value_counts())

    # generated_data_evaluation_value_counts(
    #     filename=file
    # )
    # # generated_data_evaluation_value_counts(filename="mft_generated_100_examples_aug_21_gpt4_3.csv")
    # dataset_hist(
    #     filename=file
    # )
