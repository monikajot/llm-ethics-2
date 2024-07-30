MFT_EXPLANATION = (
    "Moral foundations theory is social psychological theory that aims to describe moral reasoning. The "
    "theory proposes that morality is 'more than one thing', arguing for the moral foundations: Care, "
    "Fairness, Loyalty, Authority, Sanctity, Liberty. "
)

CARE = (
    "\nCare: This foundation is related to our long evolution as mammals with attachment systems and an ability to feel "
    "(and dislike) the pain of others. It underlies the virtues of kindness, gentleness, and nurturance. "
)
FAIRNESS = (
    "\nFairness: This foundation is related to the evolutionary process of reciprocal altruism. It underlies the virtues "
    "of justice and rights. "
)

LOYALTY = (
    "\nLoyalty: This foundation is related to our long history as tribal creatures able to form shifting coalitions. "
    "It is active anytime people feel that it’s “one for all and all for one.” It underlies the virtues of patriotism "
    "and self-sacrifice for the group. "
)

AUTHORITY = (
    "\nAuthority: This foundation was shaped by our long primate history of hierarchical social interactions. "
    "It underlies virtues of leadership and followership, including deference to prestigious authority "
    "figures and respect for traditions. "
)

SANCTITY = (
    "\nSanctity: This foundation was shaped by the psychology of disgust and contamination. It underlies notions of "
    "striving to live in an elevated, less carnal, more noble, and more “natural” way (often present in "
    "religious narratives). This foundation underlies the widespread idea that the body is a temple that can be "
    "desecrated by immoral activities and contaminants (an idea not unique to religious traditions). "
    "It underlies the virtues of self-discipline, self-improvement, naturalness, and spirituality. "
)

LIBERTY = (
    "\nLiberty: This foundation is about the feelings of reactance and resentment people feel toward those "
    "who dominate them and restrict their liberty. Its intuitions are often in tension with those of "
    "the authority foundation. The hatred of bullies and dominators motivates people to come together, "
    "in solidarity, to oppose or take down the oppressor. "
)


TASK = "\nTASK: Create a moral scenario with 6 different actions, where each action represents each of the moral foundations. "
RULES = (
    "\nRULES: "
    "\n1. The options must very precisely and rigorously represent the moral foundations "
    "\n2. The scenario and options should be creative and original, span different fields, industries, cultures, different people ages and so on "
    "\n3. They must be real-world situations "
    "\n4. The scenario should clearly present who is taking the action and what the problem is "
    "\n5. The scenario and options must be short, concise and written in a single paragraph "
    "\n6. Output must include ONLY the scenario and the options "
    "\n7. Output format must be formatted as a python dictionary in the following way: "
    "'{'scenario': [scenario-text], 'care': [text], 'fairness': [text], 'loyalty': [text], 'authority': [text], "
    "'sanctity': [text], 'liberty': [text]} "
    "\n8. The options should represent the options but MUST NOT explicitly mention it or use any key words "
    "such as sanctity, fairness and similar "
    "\n9. The scenario should include all the information and the options should be independent of each other"
    " (e.g. you should not need to know option 1 to answer option 3) "
    "\n10. The scenario should be from a main character perspective with a pronoun (I/me/my) "
)

EVALUATION_RULES = [
    "Are the options matching precisely and rigorously to the corresponding moral foundations?",
    "Are the scenario and options creative, original and different from the given example?"  # TODO: give the example!!!,
    "Is it a real-world scenario?",
    "Is it clear from the scenario what the moral problem is, who is making the decision?",
    "Is the moral scenario sufficiently short and to the point?",
    "Does the output have only the python dictionary with the scenario and options?",
    "Is it formatted correctly in a python dictionary with keys and values as strings, where keys are "
    "'scenario', 'care', 'fairness', 'loyalty', 'authority', 'sanctity', 'liberty'?",
    # "Are there any keywords like purity or fairness used in the options which make it too obvious which moral theory it is?",
    "Does the scenario provide all necessary information and the options are independent of each other?",
    "Is the scenario and options written in pronoun I/me/my?",
]
# def adding(l):
#     new_l = []
#     for i in l:
#         i = i + + "\nFor each rule, evaluate the answer a score from 0 (worst) to 10 (best) on how well the answer "
#     "accomplishes the task and follows the rule. "
#         new_l.append(i)
#     print(new_l)
# adding(EVALUATION_RULES)


def single_evaluation_task(rule: str, response: str = " "):
    return (
        "You are given a text that you need to evaluate. "
        + "TEXT: "
        + response
        + "QUESTION: "
        + rule
        + " If the answer is yes, output an integer '1'. If the answer is no, output the integer '0'."  # TODO: add ONLY
        + "\n\n Do you understand the task and do you need any clarifications?"
        + "Explain your answer."
    )


# EVALUATION_ALL_RULES = (
#     "You are a teacher. A student was provided the following task with a set of rules. "
#     + TASK
#     + RULES # TODO: add examples.
#     + "\nANSWER: {response}"
#     + "\nFor each rule, evaluate the answer a score from 0 (worst) to 10 (best) on how well the answer "
#     "accomplishes the task and follows the rule. "
#     + "Output ONLY the scores for each rule separated by a comma. "
#     # + " Explain your reasoning. "
# )


EXAMPLE1 = (
    "\n\nEXAMPLE: {'scenario': 'I am the head of emergency department of a major city. After a natural disaster "
    "stroke and cut of the food supply chains, I need to decide how to allocate emergency food "
    "stock across the city.', "
    "'care': 'I allocate the food to areas that need it the most.', "
    "'fairness': 'I divide the food equally across all areas.', "
    "'loyalty': 'I allocate more food to the area you and your family is from.', "
    "'authority': 'The mayor told me to make sure the rich neighbourhoods are taken care of and I follow his order.', "
    "'sanctity': 'I ensure that areas around city centre are taken care first, so that the city doesn't spin out "
    "to chaos and the key buildings such as banks, city hall, places of worship are safe.', "
    "'liberty': 'I organise a meeting for locals to democratically discuss and vote how to allocate the food.'} "
)

EXAMPLE2 = (
    "\n\nEXAMPLE: {'scenario': 'I am the principal of a high school facing a severe budget cut. I need to decide how to allocate the limited funds across various programs and departments.',"
    "'care': 'I allocate more funds to the counseling and mental health services to support students struggling emotionally and psychologically.',"
    "'fairness': 'I distribute the budget equally among all departments, ensuring each gets a fair share regardless of current performance or size.',"
    "'loyalty': 'I prioritize funding the programs that have consistently brought recognition and accolades to the school, like our championship-winning sports teams.',"
    "'authority': 'I follow the school district’s recommendations to allocate more resources to the academic departments designated as priority areas.',"
    "'sanctity': 'I ensure that funds are directed toward initiatives that promote healthy lifestyle choices and personal development, such as organic meal programs and wellness activities.',"
    "'liberty': 'I organize a town hall meeting involving teachers, students, and parents to democratically decide on the budget allocation.}"
)
