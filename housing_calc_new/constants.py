"""Constants for housing_calc_new."""

QUESTION_TEXT_FONT = ("Arial", 20, "bold")
MAIN_TEXT_FONT = ("Arial", 15)
TITLE_TEXT_FONT_S25 = ("Arial", 25, "bold")
TITLE_TEXT_FONT_S15 = ("Arial", 15, "bold")
FRAME_BG_COLOR = "#DCDCDD"

points = {
    "q1p1o1": 2,
    "q1p1o2": 1,
    "q1p1o3": 0,
    "q1p1o4": -1,
    "q1p2o1": -1,
    "q1p2o2": 1,
    "q1p3o1": 0,
    "q1p3o2": 1,
    "q1p4o1": 1,
    "q1p4o2": -1,
    "q1p4o3": -1,
}

prompts = {
    "q1p1": "What year are you currently in?",
    "q1p2": "Were you previously in residence?",
    "q1p3": "Have you been denied entry into residence before?",
    "q1p4": "Please specify the reason on why you have been denied residence:",
}

two_button_setup = {
    "1": 1,
    "2": 2,
}

three_button_setup = {
    "1": 1,
    "2": 2,
    "3": 3,
}

four_button_setup = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
}

questions = {
    "q1": {"s1": 1, "s2": 2, "s3": 3, "s4": 4},
}
