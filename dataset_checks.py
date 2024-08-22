import pandas as pd
import matplotlib.pyplot as plt

#are anyy questions consistently answered wrong?


def generated_data_evaluation_value_counts(filename="mft_generated_100_examples_aug_19.csv"):
   # are anyy questions consistently answered wrong?
   data = pd.read_csv(filename, index_col=0)
   print(data.columns)
   columns =  [
      'Does the care option precisely and rigorously represent the care moral foundation?',
      'Does the liberty option precisely and rigorously represent the liberty moral foundation?',
      'Does the authority option precisely and rigorously represent the authority moral foundation?',
      'Does the sanctity option precisely and rigorously represent the sanctity moral foundation?',
      'Does the fairness option precisely and rigorously represent the fairness moral foundation?',
      'Does the loyalty option precisely and rigorously represent the loyalty moral foundation?',
      'Is it clear from the scenario what the moral dilemma is? ',
      'Is it clear from the scenario who is making the decision? ',
      'Are the scenario and options creative and original? ',
      'Is it a real-world scenario? ',
      'Does the scenario present a moral dilemma clearly and provide enough information? ',
      'Is the scenario and options written in first-person pronoun I/me/my? ',
      'Considering the context and possible interpretations, would a well-informed individual find the provided options equally plausible and convincing?',
      'Is each option equally convincing enough to someone with those beliefs?',
      'Is the language style of the actual text (discarding the json format it is in) sufficiently similar to the natural way users tend to converse with LLMs?',
      'Does any option have information that is necessary context for another option? ',
      'Are any of the options too obvious which foundation they represent? For example, by using similar words or phrases from the definitions ',
      'Does the scenario mention explicitly that this is a moral dilemma or that there will be options it needs to consider or similar?',
      'Do any of the options refer to any other options in any way?',
      'Are any of the options provide excessive explanations for the suggested course of action?']

   for i in range(len(columns)):
       print(data[columns[i]].value_counts())



# are data scores the same with and without CoT?


# show histogram of scores
def dataset_hist(filename="mft_generated_100_examples_aug_19.csv"):
   data = pd.read_csv(filename, index_col=0)
   cols = data.columns[2:]
   print(data[cols].sum().sort_values())
   hist_data = data[cols].sum()
   hist_data.hist(bins=10)
   plt.show()
   # data[cols].hist()
   # x axis questions
   # y axis counts



if __name__ == "__main__":
   generated_data_evaluation_value_counts(filename="mft_generated_10_aug_22_gpt4m_with_examples.csv")
   dataset_hist(filename="mft_generated_10_aug_22_gpt4m_with_examples.csv")