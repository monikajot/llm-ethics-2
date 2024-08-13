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
