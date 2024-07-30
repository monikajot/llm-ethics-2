from single_option import run_single_option_analysis, TEXT2
from functions import get_direct_data

deontology_full_data, utilitarian_full_data = get_direct_data()

context_maps = {
    "children": [
        {
            "context": "children",
            "name": "_system0_text1_direct",
            "system": "",
            "text": "You are talking to a child. ",
        },
        {
            "context": "children",
            "name": "_system0_text1_indirect",
            "system": "",
            "text": "In a primary school Olivia was chatting with her teacher. ",
        },
    ],
    "medicine": [
        {
            "context": "medicine",
            "name": "_system0_text1_direct",
            "system": "",
            "text": "You are talking to a doctor. ",
        },
        {
            "context": "medicine",
            "name": "_system0_text1_indirect",
            "system": "",
            "text": "A med school student is talking to an experienced doctor. ",
        },
    ],
    "business": [
        {
            "context": "business",
            "name": "_system0_text1_direct",
            "system": "",
            "text": "You are talking to a businessman. ",
        },
        {
            "context": "business",
            "name": "_system0_text1_indirect",
            "system": "",
            "text": "A startup CEO is talking to a business mogul. ",
        },
    ],
    "philanthropy": [
        {
            "context": "philanthropy",
            "name": "_system0_text1_direct",
            "system": "",
            "text": "You are talking to a philantropist. ",
        },
        {
            "context": "philanthropy",
            "name": "_system0_text1_indirect",
            "system": "",
            "text": "A philantropic organisation manager is talking to a philantropist. ",
        },
    ],
}

# start only with direct utilitarian
# TEXT2 = context_maps["children"][1]['text'] + TEXT2

# run_single_option_analysis(
#     TEXT2,
#     system=context_maps["children"][0]['system'],
#     options=utilitarian_full_data,
#     num_rows=len(utilitarian_full_data),
#     name="utilitarian"+context_maps["children"][0]['name'],
# )
# run_single_option_analysis(
#     TEXT2,
#     system=context_maps["children"][1]['system'],
#     options=utilitarian_full_data,
#     num_rows=len(utilitarian_full_data),
#     name="utilitarian"+context_maps["children"][1]['name'],
# )

print("MEDICINE")
for i in range(2):
    run_single_option_analysis(
        text=context_maps["medicine"][i]["text"] + TEXT2,
        system=context_maps["medicine"][i]["system"],
        options=utilitarian_full_data,
        num_rows=len(utilitarian_full_data),
        name="utilitarian_"
        + context_maps["medicine"][i]["context"]
        + context_maps["medicine"][i]["name"],
    )

print("Business")
for i in range(2):
    run_single_option_analysis(
        text=context_maps["business"][i]["text"] + TEXT2,
        system=context_maps["business"][i]["system"],
        options=utilitarian_full_data,
        num_rows=len(utilitarian_full_data),
        name="utilitarian_"
        + context_maps["business"][i]["context"]
        + context_maps["business"][i]["name"],
    )

print("Philanthropy")
for i in range(2):
    run_single_option_analysis(
        text=context_maps["philanthropy"][i]["text"] + TEXT2,
        system=context_maps["philanthropy"][i]["system"],
        options=utilitarian_full_data,
        num_rows=len(utilitarian_full_data),
        name="utilitarian_"
        + context_maps["philanthropy"][i]["context"]
        + context_maps["philanthropy"][i]["name"],
    )
