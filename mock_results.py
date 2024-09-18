import pandas as pd

single_preferences = {
    "authority": {"yes": 47, "no": 2, "neither": 0},
    "care": {"yes": 47, "no": 2, "neither": 0},
    "fairness": {"yes": 44, "no": 5, "neither": 0},
    "liberty": {"yes": 44, "no": 5, "neither": 0},
    "loyalty": {"yes": 38, "no": 11, "neither": 0},
    "sanctity": {"yes": 47, "no": 1, "neither": 1},
}

pair_preference = {
    ("authority", "care"): {"authority": 16, "care": 33, "neither": 0},
    ("authority", "fairness"): {"authority": 16, "fairness": 33, "neither": 0},
    ("authority", "liberty"): {"authority": 29, "liberty": 20, "neither": 0},
    ("authority", "loyalty"): {"authority": 38, "loyalty": 11, "neither": 0},
    ("authority", "sanctity"): {"authority": 29, "sanctity": 20, "neither": 0},
    ("care", "fairness"): {"care": 25, "fairness": 24, "neither": 0},
    ("care", "liberty"): {"care": 34, "liberty": 14, "neither": 1},
    ("care", "loyalty"): {"care": 40, "loyalty": 9, "neither": 0},
    ("care", "sanctity"): {"care": 40, "sanctity": 9, "neither": 0},
    ("fairness", "liberty"): {"fairness": 31, "liberty": 17, "neither": 1},
    ("fairness", "loyalty"): {"fairness": 31, "loyalty": 18, "neither": 0},
    ("fairness", "sanctity"): {"fairness": 37, "sanctity": 11, "neither": 1},
    ("liberty", "loyalty"): {"liberty": 33, "loyalty": 15, "neither": 1},
    ("liberty", "sanctity"): {"liberty": 26, "sanctity": 22, "neither": 1},
    ("loyalty", "sanctity"): {"loyalty": 25, "sanctity": 24, "neither": 0},
}

triple_preference = {
    ("authority", "care", "fairness"): {
        "authority": 15,
        "care": 18,
        "fairness": 16,
        "neither": 0,
    },
    ("authority", "care", "liberty"): {
        "authority": 14,
        "care": 21,
        "liberty": 14,
        "neither": 0,
    },
    ("authority", "care", "loyalty"): {
        "authority": 18,
        "care": 22,
        "loyalty": 9,
        "neither": 0,
    },
    ("authority", "care", "sanctity"): {
        "authority": 20,
        "care": 21,
        "sanctity": 8,
        "neither": 0,
    },
    ("authority", "fairness", "liberty"): {
        "authority": 11,
        "fairness": 20,
        "liberty": 18,
        "neither": 0,
    },
    ("authority", "fairness", "loyalty"): {
        "authority": 15,
        "fairness": 20,
        "loyalty": 14,
        "neither": 0,
    },
    ("authority", "fairness", "sanctity"): {
        "authority": 12,
        "fairness": 22,
        "sanctity": 14,
        "neither": 1,
    },
    ("authority", "liberty", "loyalty"): {
        "authority": 27,
        "liberty": 13,
        "loyalty": 8,
        "neither": 1,
    },
    ("authority", "liberty", "sanctity"): {
        "authority": 20,
        "liberty": 14,
        "sanctity": 15,
        "neither": 0,
    },
    ("authority", "loyalty", "sanctity"): {
        "authority": 17,
        "loyalty": 13,
        "sanctity": 19,
        "neither": 0,
    },
    ("care", "fairness", "liberty"): {
        "care": 17,
        "fairness": 22,
        "liberty": 10,
        "neither": 0,
    },
    ("care", "fairness", "loyalty"): {
        "care": 19,
        "fairness": 15,
        "loyalty": 15,
        "neither": 0,
    },
    ("care", "fairness", "sanctity"): {
        "care": 18,
        "fairness": 21,
        "sanctity": 10,
        "neither": 0,
    },
    ("care", "liberty", "loyalty"): {
        "care": 26,
        "liberty": 12,
        "loyalty": 10,
        "neither": 1,
    },
    ("care", "liberty", "sanctity"): {
        "care": 18,
        "liberty": 19,
        "sanctity": 12,
        "neither": 0,
    },
    ("care", "loyalty", "sanctity"): {
        "care": 22,
        "loyalty": 18,
        "sanctity": 9,
        "neither": 0,
    },
    ("fairness", "liberty", "loyalty"): {
        "fairness": 27,
        "liberty": 11,
        "loyalty": 11,
        "neither": 0,
    },
    ("fairness", "liberty", "sanctity"): {
        "fairness": 25,
        "liberty": 11,
        "sanctity": 12,
        "neither": 1,
    },
    ("fairness", "loyalty", "sanctity"): {
        "fairness": 24,
        "loyalty": 12,
        "sanctity": 13,
        "neither": 0,
    },
    ("liberty", "loyalty", "sanctity"): {
        "liberty": 19,
        "loyalty": 18,
        "sanctity": 11,
        "neither": 1,
    },
}

total_preference = {
    "authority": 5,
    "care": 13,
    "fairness": 20,
    "liberty": 6,
    "loyalty": 4,
    "sanctity": 1,
    "neither": 0,
}


single_preference_var = [
    {
        "authority": {"yes": 46, "no": 3, "neither": 0},
        "care": {"yes": 46, "no": 3, "neither": 0},
        "fairness": {"yes": 44, "no": 5, "neither": 0},
        "liberty": {"yes": 43, "no": 6, "neither": 0},
        "loyalty": {"yes": 36, "no": 13, "neither": 0},
        "sanctity": {"yes": 48, "no": 1, "neither": 0},
    },
    {
        "authority": {"yes": 49, "no": 0, "neither": 0},
        "care": {"yes": 48, "no": 1, "neither": 0},
        "fairness": {"yes": 44, "no": 5, "neither": 0},
        "liberty": {"yes": 43, "no": 5, "neither": 1},
        "loyalty": {"yes": 38, "no": 11, "neither": 0},
        "sanctity": {"yes": 47, "no": 2, "neither": 0},
    },
    {
        "authority": {"yes": 47, "no": 2, "neither": 0},
        "care": {"yes": 47, "no": 1, "neither": 1},
        "fairness": {"yes": 43, "no": 6, "neither": 0},
        "liberty": {"yes": 42, "no": 6, "neither": 1},
        "loyalty": {"yes": 37, "no": 12, "neither": 0},
        "sanctity": {"yes": 49, "no": 0, "neither": 0},
    },
    {
        "authority": {"yes": 47, "no": 2, "neither": 0},
        "care": {"yes": 47, "no": 2, "neither": 0},
        "fairness": {"yes": 43, "no": 6, "neither": 0},
        "liberty": {"yes": 41, "no": 8, "neither": 0},
        "loyalty": {"yes": 38, "no": 11, "neither": 0},
        "sanctity": {"yes": 49, "no": 0, "neither": 0},
    },
    {
        "authority": {"yes": 47, "no": 2, "neither": 0},
        "care": {"yes": 45, "no": 4, "neither": 0},
        "fairness": {"yes": 43, "no": 6, "neither": 0},
        "liberty": {"yes": 45, "no": 4, "neither": 0},
        "loyalty": {"yes": 37, "no": 12, "neither": 0},
        "sanctity": {"yes": 48, "no": 1, "neither": 0},
    },
]

pair_preference_var = [
    {
        ("authority", "care"): {"authority": 16, "care": 33, "neither": 0},
        ("authority", "fairness"): {"authority": 16, "fairness": 33, "neither": 0},
        ("authority", "liberty"): {"authority": 29, "liberty": 20, "neither": 0},
        ("authority", "loyalty"): {"authority": 38, "loyalty": 11, "neither": 0},
        ("authority", "sanctity"): {"authority": 29, "sanctity": 20, "neither": 0},
        ("care", "fairness"): {"care": 25, "fairness": 24, "neither": 0},
        ("care", "liberty"): {"care": 34, "liberty": 14, "neither": 1},
        ("care", "loyalty"): {"care": 40, "loyalty": 9, "neither": 0},
        ("care", "sanctity"): {"care": 40, "sanctity": 9, "neither": 0},
        ("fairness", "liberty"): {"fairness": 31, "liberty": 17, "neither": 1},
        ("fairness", "loyalty"): {"fairness": 31, "loyalty": 18, "neither": 0},
        ("fairness", "sanctity"): {"fairness": 37, "sanctity": 11, "neither": 1},
        ("liberty", "loyalty"): {"liberty": 33, "loyalty": 15, "neither": 1},
        ("liberty", "sanctity"): {"liberty": 26, "sanctity": 22, "neither": 1},
        ("loyalty", "sanctity"): {"loyalty": 25, "sanctity": 24, "neither": 0},
    },
    {
        ("authority", "care"): {"authority": 13, "care": 19, "neither": 18},
        ("authority", "fairness"): {"authority": 9, "fairness": 19, "neither": 22},
        ("authority", "liberty"): {"authority": 18, "liberty": 17, "neither": 15},
        ("authority", "loyalty"): {"authority": 17, "loyalty": 21, "neither": 12},
        ("authority", "sanctity"): {"authority": 9, "sanctity": 14, "neither": 27},
        ("care", "fairness"): {"care": 17, "fairness": 12, "neither": 21},
        ("care", "liberty"): {"care": 18, "liberty": 16, "neither": 16},
        ("care", "loyalty"): {"care": 19, "loyalty": 13, "neither": 18},
        ("care", "sanctity"): {"care": 15, "sanctity": 17, "neither": 18},
        ("fairness", "liberty"): {"fairness": 13, "liberty": 20, "neither": 17},
        ("fairness", "loyalty"): {"fairness": 16, "loyalty": 15, "neither": 19},
        ("fairness", "sanctity"): {"fairness": 22, "sanctity": 15, "neither": 13},
        ("liberty", "loyalty"): {"liberty": 19, "loyalty": 13, "neither": 18},
        ("liberty", "sanctity"): {"liberty": 18, "sanctity": 18, "neither": 14},
        ("loyalty", "sanctity"): {"loyalty": 18, "sanctity": 18, "neither": 14},
    },
]

gpt_35_sp = {
    "authority": {"yes": 927, "no": 133, "neither": 19},
    "care": {"yes": 1036, "no": 35, "neither": 8},
    "fairness": {"yes": 839, "no": 240, "neither": 0},
    "liberty": {"yes": 920, "no": 131, "neither": 28},
    "loyalty": {"yes": 644, "no": 389, "neither": 46},
    "sanctity": {"yes": 985, "no": 80, "neither": 14},
}
claude_2_sp = {
            "authority": {"yes": 504, "no": 565, "neither": 10},
            "care": {"yes": 822, "no": 257, "neither": 0},
            "fairness": {"yes": 696, "no": 381, "neither": 2},
            "liberty": {"yes": 575, "no": 496, "neither": 8},
            "loyalty": {"yes": 260, "no": 808, "neither": 11},
            "sanctity": {"yes": 508, "no": 563, "neither": 8},
        }

gpt_35_sp = {'authority': {'yes': 908, 'no': 142, 'neither': 29}, 'care': {'yes': 1042, 'no': 31, 'neither': 6}, 'fairness': {'yes': 849, 'no': 229, 'neither': 1}, 'liberty': {'yes': 921, 'no': 129, 'neither': 29}, 'loyalty': {'yes': 622, 'no': 413, 'neither': 44}, 'sanctity': {'yes': 978, 'no': 84, 'neither': 17}}

gpt_4_sp = {'authority': {'yes': 965, 'no': 105, 'neither': 9}, 'care': {'yes': 1024, 'no': 50, 'neither': 5}, 'fairness': {'yes': 889, 'no': 189, 'neither': 1}, 'liberty': {'yes': 942, 'no': 127, 'neither': 10}, 'loyalty': {'yes': 671, 'no': 393, 'neither': 15}, 'sanctity': {'yes': 978, 'no': 91, 'neither': 10}}

#miss 2
gpt_4o_sp = {'authority': {'yes': 820, 'no': 259, 'neither': 0}, 'care': {'yes': 982, 'no': 97, 'neither': 0}, 'fairness': {'yes': 738, 'no': 341, 'neither': 0}, 'liberty': {'yes': 831, 'no': 247, 'neither': 1}, 'loyalty': {'yes': 473, 'no': 604, 'neither': 2}, 'sanctity': {'yes': 896, 'no': 182, 'neither': 1}}

claude_3_sp = {'authority': {'yes': 323, 'no': 722, 'neither': 34}, 'care': {'yes': 699, 'no': 365, 'neither': 15}, 'fairness': {'yes': 522, 'no': 546, 'neither': 11}, 'liberty': {'yes': 397, 'no': 646, 'neither': 36}, 'loyalty': {'yes': 172, 'no': 872, 'neither': 35}, 'sanctity': {'yes': 403, 'no': 650, 'neither': 26}}

claude_35_sp = {'authority': {'yes': 742, 'no': 282, 'neither': 55}, 'care': {'yes': 954, 'no': 75, 'neither': 50}, 'fairness': {'yes': 762, 'no': 312, 'neither': 5}, 'liberty': {'yes': 762, 'no': 247, 'neither': 70}, 'loyalty': {'yes': 394, 'no': 572, 'neither': 113}, 'sanctity': {'yes': 756, 'no': 265, 'neither': 58}}

single_preferences_dict = {"GPT-3.5": gpt_35_sp, "GPT-4": gpt_4_sp, "GPT-4o": gpt_4o_sp, "Claude-2": claude_2_sp, "Claude-3": claude_3_sp, "Claude-3.5": claude_35_sp}

gpt_35_tp = {'authority': 119, 'care': 356, 'fairness': 293, 'liberty': 121, 'loyalty': 54, 'sanctity': 104, 'neither': 32}
gpt_4_tp = {'authority': 118, 'care': 226, 'fairness': 418, 'liberty': 185, 'loyalty': 52, 'sanctity': 80, 'neither': 0}
gpt_4o_tp = {'authority': 102, 'care': 309, 'fairness': 356, 'liberty': 194, 'loyalty': 45, 'sanctity': 71, 'neither': 2}
claude_2_tp = {'authority': 66, 'care': 236, 'fairness': 221, 'liberty': 191, 'loyalty': 43, 'sanctity': 61, 'neither': 261}
claude_3_tp ={'authority': 108, 'care': 279, 'fairness': 384, 'liberty': 201, 'loyalty': 32, 'sanctity': 73, 'neither': 2}
claude_35_tp = {'authority': 118, 'care': 302, 'fairness': 399, 'liberty': 158, 'loyalty': 35, 'sanctity': 63, 'neither': 4}

total_preference_dict ={"GPT-3.5": gpt_35_tp, "GPT-4": gpt_4_tp, "GPT-4o": gpt_4o_tp, "Claude-2": claude_2_tp, "Claude-3": claude_3_tp, "Claude-3.5": claude_35_tp}

#graph
pair_preference_gpt_35 = {('authority', 'care'): {'authority': 335, 'care': 741, 'neither': 3}, ('authority', 'fairness'): {'authority': 433, 'fairness': 642, 'neither': 4}, ('authority', 'liberty'): {'authority': 545, 'liberty': 525, 'neither': 9}, ('authority', 'loyalty'): {'authority': 733, 'loyalty': 331, 'neither': 15}, ('authority', 'sanctity'): {'authority': 592, 'sanctity': 482, 'neither': 5}, ('care', 'fairness'): {'care': 600, 'fairness': 478, 'neither': 1}, ('care', 'liberty'): {'care': 687, 'liberty': 386, 'neither': 6}, ('care', 'loyalty'): {'care': 900, 'loyalty': 170, 'neither': 9}, ('care', 'sanctity'): {'care': 797, 'sanctity': 276, 'neither': 6}, ('fairness', 'liberty'): {'fairness': 673, 'liberty': 401, 'neither': 5}, ('fairness', 'loyalty'): {'fairness': 790, 'loyalty': 281, 'neither': 8}, ('fairness', 'sanctity'): {'fairness': 674, 'sanctity': 403, 'neither': 2}, ('liberty', 'loyalty'): {'liberty': 717, 'loyalty': 343, 'neither': 19}, ('liberty', 'sanctity'): {'liberty': 606, 'sanctity': 460, 'neither': 13}, ('loyalty', 'sanctity'): {'loyalty': 383, 'sanctity': 678, 'neither': 18}}
triple_preference_gpt_35 = {('authority', 'care', 'fairness'): {'authority': 305, 'care': 427, 'fairness': 345, 'neither': 2}, ('authority', 'care', 'liberty'): {'authority': 332, 'care': 450, 'liberty': 287, 'neither': 10}, ('authority', 'care', 'loyalty'): {'authority': 317, 'care': 468, 'loyalty': 285, 'neither': 9}, ('authority', 'care', 'sanctity'): {'authority': 293, 'care': 474, 'sanctity': 300, 'neither': 12}, ('authority', 'fairness', 'liberty'): {'authority': 344, 'fairness': 389, 'liberty': 341, 'neither': 5}, ('authority', 'fairness', 'loyalty'): {'authority': 331, 'fairness': 427, 'loyalty': 314, 'neither': 7}, ('authority', 'fairness', 'sanctity'): {'authority': 339, 'fairness': 385, 'sanctity': 352, 'neither': 3}, ('authority', 'liberty', 'loyalty'): {'authority': 387, 'liberty': 364, 'loyalty': 312, 'neither': 16}, ('authority', 'liberty', 'sanctity'): {'authority': 407, 'liberty': 333, 'sanctity': 332, 'neither': 7}, ('authority', 'loyalty', 'sanctity'): {'authority': 384, 'loyalty': 300, 'sanctity': 382, 'neither': 13}, ('care', 'fairness', 'liberty'): {'care': 417, 'fairness': 357, 'liberty': 301, 'neither': 4}, ('care', 'fairness', 'loyalty'): {'care': 416, 'fairness': 370, 'loyalty': 285, 'neither': 8}, ('care', 'fairness', 'sanctity'): {'care': 434, 'fairness': 347, 'sanctity': 289, 'neither': 9}, ('care', 'liberty', 'loyalty'): {'care': 463, 'liberty': 278, 'loyalty': 320, 'neither': 18}, ('care', 'liberty', 'sanctity'): {'care': 452, 'liberty': 304, 'sanctity': 314, 'neither': 9}, ('care', 'loyalty', 'sanctity'): {'care': 456, 'loyalty': 277, 'sanctity': 325, 'neither': 21}, ('fairness', 'liberty', 'loyalty'): {'fairness': 416, 'liberty': 344, 'loyalty': 306, 'neither': 13}, ('fairness', 'liberty', 'sanctity'): {'fairness': 418, 'liberty': 312, 'sanctity': 344, 'neither': 5}, ('fairness', 'loyalty', 'sanctity'): {'fairness': 415, 'loyalty': 309, 'sanctity': 339, 'neither': 16}, ('liberty', 'loyalty', 'sanctity'): {'liberty': 360, 'loyalty': 330, 'sanctity': 369, 'neither': 20}}
results_trp = [3., 5. ,4., 1., 0., 2.]

pair_preference_gpt_4o = {('authority', 'care'): {'authority': 168, 'care': 368, 'neither': 4}, ('authority', 'fairness'): {'authority': 229, 'fairness': 310, 'neither': 1}, ('authority', 'liberty'): {'authority': 223, 'liberty': 316, 'neither': 1}, ('authority', 'loyalty'): {'authority': 376, 'loyalty': 157, 'neither': 7}, ('authority', 'sanctity'): {'authority': 287, 'sanctity': 250, 'neither': 3}, ('care', 'fairness'): {'care': 322, 'fairness': 217, 'neither': 1}, ('care', 'liberty'): {'care': 365, 'liberty': 175, 'neither': 0}, ('care', 'loyalty'): {'care': 468, 'loyalty': 68, 'neither': 4}, ('care', 'sanctity'): {'care': 413, 'sanctity': 127, 'neither': 0}, ('fairness', 'liberty'): {'fairness': 299, 'liberty': 241, 'neither': 0}, ('fairness', 'loyalty'): {'fairness': 417, 'loyalty': 121, 'neither': 2}, ('fairness', 'sanctity'): {'fairness': 332, 'sanctity': 207, 'neither': 1}, ('liberty', 'loyalty'): {'liberty': 406, 'loyalty': 128, 'neither': 6}, ('liberty', 'sanctity'): {'liberty': 320, 'sanctity': 218, 'neither': 2}, ('loyalty', 'sanctity'): {'loyalty': 160, 'sanctity': 376, 'neither': 4}}
triple_preference_gpt_4o = {('authority', 'care', 'fairness'): {'authority': 143, 'care': 222, 'fairness': 175, 'neither': 0}, ('authority', 'care', 'liberty'): {'authority': 157, 'care': 231, 'liberty': 152, 'neither': 0}, ('authority', 'care', 'loyalty'): {'authority': 152, 'care': 256, 'loyalty': 132, 'neither': 0}, ('authority', 'care', 'sanctity'): {'authority': 142, 'care': 254, 'sanctity': 143, 'neither': 1}, ('authority', 'fairness', 'liberty'): {'authority': 157, 'fairness': 218, 'liberty': 165, 'neither': 0}, ('authority', 'fairness', 'loyalty'): {'authority': 182, 'fairness': 229, 'loyalty': 128, 'neither': 1}, ('authority', 'fairness', 'sanctity'): {'authority': 163, 'fairness': 220, 'sanctity': 156, 'neither': 1}, ('authority', 'liberty', 'loyalty'): {'authority': 203, 'liberty': 205, 'loyalty': 131, 'neither': 1}, ('authority', 'liberty', 'sanctity'): {'authority': 156, 'liberty': 205, 'sanctity': 178, 'neither': 1}, ('authority', 'loyalty', 'sanctity'): {'authority': 190, 'loyalty': 152, 'sanctity': 196, 'neither': 2}, ('care', 'fairness', 'liberty'): {'care': 201, 'fairness': 193, 'liberty': 146, 'neither': 0}, ('care', 'fairness', 'loyalty'): {'care': 224, 'fairness': 190, 'loyalty': 124, 'neither': 2}, ('care', 'fairness', 'sanctity'): {'care': 204, 'fairness': 196, 'sanctity': 140, 'neither': 0}, ('care', 'liberty', 'loyalty'): {'care': 249, 'liberty': 141, 'loyalty': 146, 'neither': 4}, ('care', 'liberty', 'sanctity'): {'care': 246, 'liberty': 149, 'sanctity': 142, 'neither': 3}, ('care', 'loyalty', 'sanctity'): {'care': 259, 'loyalty': 137, 'sanctity': 143, 'neither': 1}, ('fairness', 'liberty', 'loyalty'): {'fairness': 226, 'liberty': 180, 'loyalty': 133, 'neither': 1}, ('fairness', 'liberty', 'sanctity'): {'fairness': 224, 'liberty': 172, 'sanctity': 143, 'neither': 1}, ('fairness', 'loyalty', 'sanctity'): {'fairness': 238, 'loyalty': 136, 'sanctity': 165, 'neither': 1}, ('liberty', 'loyalty', 'sanctity'): {'liberty': 202, 'loyalty': 150, 'sanctity': 184, 'neither': 4}}
#graph
pair_preference_claude_35 = {('authority', 'care'): {'authority': 198, 'care': 337, 'neither': 5}, ('authority', 'fairness'): {'authority': 208, 'fairness': 330, 'neither': 2}, ('authority', 'liberty'): {'authority': 262, 'liberty': 253, 'neither': 25}, ('authority', 'loyalty'): {'authority': 365, 'loyalty': 146, 'neither': 29}, ('authority', 'sanctity'): {'authority': 304, 'sanctity': 224, 'neither': 12}, ('care', 'fairness'): {'care': 276, 'fairness': 263, 'neither': 1}, ('care', 'liberty'): {'care': 372, 'liberty': 161, 'neither': 7}, ('care', 'loyalty'): {'care': 451, 'loyalty': 79, 'neither': 10}, ('care', 'sanctity'): {'care': 430, 'sanctity': 107, 'neither': 3}, ('fairness', 'liberty'): {'fairness': 323, 'liberty': 213, 'neither': 4}, ('fairness', 'loyalty'): {'fairness': 441, 'loyalty': 89, 'neither': 10}, ('fairness', 'sanctity'): {'fairness': 384, 'sanctity': 153, 'neither': 3}, ('liberty', 'loyalty'): {'liberty': 367, 'loyalty': 136, 'neither': 37}, ('liberty', 'sanctity'): {'liberty': 312, 'sanctity': 216, 'neither': 12}, ('loyalty', 'sanctity'): {'loyalty': 191, 'sanctity': 317, 'neither': 32}}
triple_preference_claude_35 = {('authority', 'care', 'fairness'): {'authority': 144, 'care': 199, 'fairness': 195, 'neither': 2}, ('authority', 'care', 'liberty'): {'authority': 168, 'care': 215, 'liberty': 154, 'neither': 3}, ('authority', 'care', 'loyalty'): {'authority': 200, 'care': 225, 'loyalty': 112, 'neither': 3}, ('authority', 'care', 'sanctity'): {'authority': 172, 'care': 240, 'sanctity': 127, 'neither': 1}, ('authority', 'fairness', 'liberty'): {'authority': 139, 'fairness': 215, 'liberty': 186, 'neither': 0}, ('authority', 'fairness', 'loyalty'): {'authority': 187, 'fairness': 236, 'loyalty': 116, 'neither': 1}, ('authority', 'fairness', 'sanctity'): {'authority': 173, 'fairness': 232, 'sanctity': 133, 'neither': 2}, ('authority', 'liberty', 'loyalty'): {'authority': 198, 'liberty': 192, 'loyalty': 145, 'neither': 5}, ('authority', 'liberty', 'sanctity'): {'authority': 205, 'liberty': 186, 'sanctity': 144, 'neither': 5}, ('authority', 'loyalty', 'sanctity'): {'authority': 217, 'loyalty': 137, 'sanctity': 177, 'neither': 9}, ('care', 'fairness', 'liberty'): {'care': 182, 'fairness': 201, 'liberty': 156, 'neither': 1}, ('care', 'fairness', 'loyalty'): {'care': 217, 'fairness': 211, 'loyalty': 110, 'neither': 2}, ('care', 'fairness', 'sanctity'): {'care': 193, 'fairness': 219, 'sanctity': 128, 'neither': 0}, ('care', 'liberty', 'loyalty'): {'care': 245, 'liberty': 162, 'loyalty': 129, 'neither': 4}, ('care', 'liberty', 'sanctity'): {'care': 219, 'liberty': 176, 'sanctity': 143, 'neither': 2}, ('care', 'loyalty', 'sanctity'): {'care': 276, 'loyalty': 130, 'sanctity': 129, 'neither': 5}, ('fairness', 'liberty', 'loyalty'): {'fairness': 241, 'liberty': 170, 'loyalty': 128, 'neither': 1}, ('fairness', 'liberty', 'sanctity'): {'fairness': 238, 'liberty': 164, 'sanctity': 138, 'neither': 0}, ('fairness', 'loyalty', 'sanctity'): {'fairness': 269, 'loyalty': 137, 'sanctity': 131, 'neither': 3}, ('liberty', 'loyalty', 'sanctity'): {'liberty': 217, 'loyalty': 149, 'sanctity': 162, 'neither': 12}}

pair_preference_claude_3 = {('authority', 'care'): {'authority': 172, 'care': 361, 'neither': 7}, ('authority', 'fairness'): {'authority': 197, 'fairness': 336, 'neither': 7}, ('authority', 'liberty'): {'authority': 221, 'liberty': 308, 'neither': 11}, ('authority', 'loyalty'): {'authority': 361, 'loyalty': 152, 'neither': 27}, ('authority', 'sanctity'): {'authority': 277, 'sanctity': 249, 'neither': 14}, ('care', 'fairness'): {'care': 287, 'fairness': 250, 'neither': 3}, ('care', 'liberty'): {'care': 321, 'liberty': 208, 'neither': 11}, ('care', 'loyalty'): {'care': 434, 'loyalty': 88, 'neither': 18}, ('care', 'sanctity'): {'care': 384, 'sanctity': 139, 'neither': 17}, ('fairness', 'liberty'): {'fairness': 302, 'liberty': 237, 'neither': 1}, ('fairness', 'loyalty'): {'fairness': 429, 'loyalty': 104, 'neither': 7}, ('fairness', 'sanctity'): {'fairness': 351, 'sanctity': 185, 'neither': 4}, ('liberty', 'loyalty'): {'liberty': 387, 'loyalty': 125, 'neither': 28}, ('liberty', 'sanctity'): {'liberty': 318, 'sanctity': 207, 'neither': 15}, ('loyalty', 'sanctity'): {'loyalty': 173, 'sanctity': 344, 'neither': 23}}
triple_preference_claude_3 = {('authority', 'care', 'fairness'): {'authority': 147, 'care': 183, 'fairness': 210, 'neither': 0}, ('authority', 'care', 'liberty'): {'authority': 151, 'care': 199, 'liberty': 188, 'neither': 2}, ('authority', 'care', 'loyalty'): {'authority': 172, 'care': 247, 'loyalty': 119, 'neither': 2}, ('authority', 'care', 'sanctity'): {'authority': 156, 'care': 241, 'sanctity': 142, 'neither': 1}, ('authority', 'fairness', 'liberty'): {'authority': 145, 'fairness': 221, 'liberty': 172, 'neither': 2}, ('authority', 'fairness', 'loyalty'): {'authority': 173, 'fairness': 244, 'loyalty': 122, 'neither': 1}, ('authority', 'fairness', 'sanctity'): {'authority': 144, 'fairness': 230, 'sanctity': 165, 'neither': 1}, ('authority', 'liberty', 'loyalty'): {'authority': 185, 'liberty': 203, 'loyalty': 150, 'neither': 2}, ('authority', 'liberty', 'sanctity'): {'authority': 162, 'liberty': 207, 'sanctity': 167, 'neither': 4}, ('authority', 'loyalty', 'sanctity'): {'authority': 209, 'loyalty': 144, 'sanctity': 186, 'neither': 1}, ('care', 'fairness', 'liberty'): {'care': 187, 'fairness': 199, 'liberty': 154, 'neither': 0}, ('care', 'fairness', 'loyalty'): {'care': 212, 'fairness': 214, 'loyalty': 113, 'neither': 1}, ('care', 'fairness', 'sanctity'): {'care': 230, 'fairness': 179, 'sanctity': 131, 'neither': 0}, ('care', 'liberty', 'loyalty'): {'care': 210, 'liberty': 204, 'loyalty': 125, 'neither': 1}, ('care', 'liberty', 'sanctity'): {'care': 200, 'liberty': 193, 'sanctity': 147, 'neither': 0}, ('care', 'loyalty', 'sanctity'): {'care': 264, 'loyalty': 139, 'sanctity': 135, 'neither': 2}, ('fairness', 'liberty', 'loyalty'): {'fairness': 222, 'liberty': 183, 'loyalty': 135, 'neither': 0}, ('fairness', 'liberty', 'sanctity'): {'fairness': 216, 'liberty': 202, 'sanctity': 122, 'neither': 0}, ('fairness', 'loyalty', 'sanctity'): {'fairness': 257, 'loyalty': 132, 'sanctity': 151, 'neither': 0}, ('liberty', 'loyalty', 'sanctity'): {'liberty': 207, 'loyalty': 148, 'sanctity': 181, 'neither': 4}}



