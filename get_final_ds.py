import pandas as pd

from generate_mft_dataset import check_dataset_formatting
from functions import combine_csv_files
from dataset_checks import generated_data_evaluation_value_counts, dataset_hist

path = "datasets/"
files = [
    "test_formatted_mft_generated_100_examples_aug_21_gpt4_3.csv",
    "formatted_mft_generated_100_examples_aug_19.csv",
    "test_formatted_mft_generated_100_aug_26_gpt4o_with_examples.csv",
    "test_formatted_mft_generated_100_aug_26_gpt4o_with_examples_sanctity_emph.csv",
    "test_formatted_mft_generated_100_aug_26_gpt4o_with_examples_sanctity_emph_2.csv",
    "test_formatted_mft_generated_100_aug_26_gpt4o_with_examples_sanctity_emph_MFV.csv",
]
files = [
    "combined_6_files.csv",
    "no_nanstest_formatted_mft_generated_100_aug_26_gpt4o_with_examples_sanc_loya_lib_emph.csv"
]
cols = ['Does the care option precisely and rigorously represent the care moral foundation?',
       'Does the authority option precisely and rigorously represent the authority moral foundation?',
       'Does the liberty option precisely and rigorously represent the liberty moral foundation?',
       'Does the fairness option precisely and rigorously represent the fairness moral foundation?',
       'Does the sanctity option precisely and rigorously represent the sanctity moral foundation?',
       'Does the loyalty option precisely and rigorously represent the loyalty moral foundation?',]

if __name__ == "__main__":
    # all_data = []
    # for file in files:
    #     all_data.append(check_dataset_formatting(path + file, save=False))
    # all_data_df = pd.concat(all_data)
    # all_data_df.to_csv("combined_6_files.csv")

    # df1 = pd.read_csv(files[0], index_col=0)
    # df2 = pd.read_csv(files[1], index_col=0)
    # all_data_df = pd.concat([df1, df2])
    # df = all_data_df.dropna(subset=["responses"]).reset_index(drop=True)
    # df.to_csv("combined_7_files.csv")


    file = "combined_7_files.csv"
    data = pd.read_csv(file, index_col=0)
    col1 = 'Does the sanctity option precisely and rigorously represent the sanctity moral foundation?'
    col2 = 'Does the liberty option precisely and rigorously represent the liberty moral foundation?'
    col3 = 'Does the loyalty option precisely and rigorously represent the loyalty moral foundation?'
    filtered_df = data[(data[[col1]] == 1).any(axis=1)]
    for col in cols:
        print(filtered_df[col].value_counts())
    # data.sort_values(by=['Does the care option precisely and rigorously represent the care moral foundation?',
    #                      'Does the authority option precisely and rigorously represent the authority moral foundation?',
    #                      'Does the liberty option precisely and rigorously represent the liberty moral foundation?',
    #                      'Does the fairness option precisely and rigorously represent the fairness moral foundation?',
    #                      'Does the sanctity option precisely and rigorously represent the sanctity moral foundation?',
    #                      'Does the loyalty option precisely and rigorously represent the loyalty moral foundation?', ],
    #                  ascending=[False] * 6)
    # sanctity_df = data[data[col1 = 'Does the sanctity option precisely and rigorously represent the sanctity moral foundation?'] == 1]
    # non_sanc_df = data[data['Does the sanctity option precisely and rigorously represent the sanctity moral foundation?'] == 0]
    # liberty_df = non_sanc_df[non_sanc_df['Does the liberty option precisely and rigorously represent the liberty moral foundation?'] == 1]
    #
    # loyalty_df = data[data['Does the loyalty option precisely and rigorously represent the loyalty moral foundation?'] == 1]
    # good_data = pd.concat([sanctity_df, liberty_df, loyalty_df])

    # generated_data_evaluation_value_counts(
    #     filename=file
    # )
    # # generated_data_evaluation_value_counts(filename="mft_generated_100_examples_aug_21_gpt4_3.csv")
    # dataset_hist(
    #     filename=file
    # )
