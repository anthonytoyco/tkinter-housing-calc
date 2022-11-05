"""
Filename: MWU_Housing_Calculator_REPLIT.py
Author: Anthony Toyco, Ryan Alumkal, Ryan Lin
Date: Tuesday June 21, 2022
Description: A program that assigns the order in which they enter residency
based on a set of prompts, students are awarded points based on factors.
"""

import tkinter as tk

# FUNCTIONS


def hide_widgets(*widgets):
    for widget in widgets:
        widget.grid_forget()


def calculate_points(answer):
    global point_counter
    if answer[0] == "q1":
        if answer[1] == "s1":
            global credits
            point_counter += credits / -4
        elif answer[1] == "s2":
            if answer[2] == "op1":
                point_counter -= 1
            elif answer[2] == "op2":
                point_counter += 1
        elif answer[1] == "s3":
            if answer[2] == "op1":
                pass
            elif answer[2] == "op2":
                point_counter += 1
        elif answer[1] == "s4":
            if answer[2] == "op1":
                point_counter += 1
            elif answer[2] == "op2":
                point_counter -= 1
            elif answer[2] == "op3":
                point_counter -= 1
    elif answer[0] == "q2":
        if answer[1] == "s1":
            if answer[2] == "op1":
                point_counter += 1
            elif answer[2] == "op2":
                point_counter -= 1
        elif answer[1] == "s2":
            if answer[2] == "op1":
                point_counter += 1
            elif answer[2] == "op2":
                point_counter += 1
            elif answer[2] == "op3":
                pass
            elif answer[2] == "op4":
                point_counter -= 1
    elif answer[0] == "q3":
        if answer[2] == "op1":
            point_counter += 1
        elif answer[2] == "op2":
            point_counter -= 1
    elif answer[0] == "q4":
        if answer[2] == "op1":
            point_counter -= 1
        elif answer[2] == "op2":
            point_counter -= 2
        elif answer[2] == "op3":
            point_counter -= 3
        elif answer[2] == "op4":
            point_counter += 1
    elif answer[0] == "q5":
        if answer[1] == "s1":
            if answer[2] == "op1":
                point_counter -= 1
            elif answer[2] == "op2":
                point_counter += 1
        elif answer[1] == "s2":
            if answer[2] == "op1":
                point_counter -= 1
            elif answer[2] == "op2":
                point_counter += 1
    elif answer[0] == "q6":
        if answer[2] == "op1":
            point_counter += 1
        elif answer[2] == "op2":
            pass
    elif answer[0] == "q7":
        if answer[1] == "s1":
            if answer[2] == "op1":
                point_counter += 1
            elif answer[2] == "op2":
                point_counter -= 1
        elif answer[1] == "s2":
            if answer[2] == "op1":
                point_counter += 1
            elif answer[2] == "op2":
                pass
        elif answer[1] == "s3":
            if answer[2] == "op1":
                point_counter += 1
            elif answer[2] == "op2":
                pass
    elif answer[0] == "q8":
        if answer[1] == "s1":
            if answer[2] == "op1":
                point_counter += 1
            elif answer[2] == "op2":
                pass
        elif answer[1] == "s2":
            if answer[2] == "op1":
                point_counter += 1
            elif answer[2] == "op2":
                pass
        elif answer[1] == "s3":
            if answer[2] == "op1":
                point_counter += 1
            elif answer[2] == "op2":
                pass
    elif answer[0] == "q9":
        if answer[2] == "op1":
            point_counter += 1
        elif answer[2] == "op2":
            point_counter -= 1
    elif answer[0] == "q10":
        if answer[1] == "s1":
            if answer[2] == "op1":
                point_counter += 1
            elif answer[2] == "op2":
                point_counter -= 1
        if answer[1] == "s2":
            if answer[2] == "op1":
                point_counter -= 1
            elif answer[2] == "op2":
                point_counter += 1
            elif answer[2] == "op2":
                point_counter += 2
    elif answer[0] == "q11":
        if answer[1] == "s1":
            if answer[2] == "op1":
                point_counter += 1
            elif answer[2] == "op2":
                point_counter -= 1
        if answer[1] == "s2":
            if answer[2] == "op1":
                point_counter += 1
            elif answer[2] == "op2":
                pass
    elif answer[0] == "q12":
        if answer[2] == "op1":
            point_counter -= 1
        elif answer[2] == "op2":
            point_counter += 1
        elif answer[2] == "op3":
            pass


def pg_welcome():
    # Reset/Initialize point counter variables
    global point_counter
    point_counter = 100

    # First title text
    title_text_top = tk.Label(
        main_frame,
        fg="#090A0B",
        bg="#DCDCDD",
        text="HOUSING SCORE CALCULATOR",
        font=title_text_font_s25,
    )
    title_text_top.grid(row=0, column=0, columnspan=6, sticky="S")

    # Second title text
    title_text_bottom = tk.Label(
        main_frame,
        fg="#090A0B",
        bg="#DCDCDD",
        text="By Mary Ward University",
        font=title_text_font_s15,
    )
    title_text_bottom.grid(row=1, column=0, columnspan=6, sticky="N")

    # MW logo
    global logo
    logo = tk.PhotoImage(file="housing_calc_old/mw_logo.png")
    logo_label = tk.Label(main_frame, image=logo, bg="#DCDCDD")
    logo_label.grid(row=2, column=1, columnspan=4)

    # Next page button
    next_page_button = tk.Button(
        main_frame,
        bg="#C5C3C6",
        text="Click here to start the app",
        command=lambda: [
            hide_widgets(
                next_page_button, title_text_top, logo_label, title_text_bottom
            ),
            pg_ques1_s1(),
        ],
    )
    next_page_button.grid(row=4, column=2, columnspan=2)


def pg_ques1_s1():
    def pg_ques1_s4():

        # Question title
        q1_s4_text = tk.Label(
            main_frame,
            text="Q1S4: Please specify the reason\n on why you have been denied residence",
            font=question_text_font,
        )
        q1_s4_text.grid(row=1, column=0, columnspan=6)

        # Top left option
        q1_s4_op1 = tk.Button(
            main_frame,
            text="Did not qualify",
            font=main_text_font,
            height="5",
            width="30",
            command=lambda: [
                hide_widgets(q1_s4_text, q1_s4_op1, q1_s4_op2, q1_s4_op3),
                calculate_points(["q1", "s4", "op1"]),
                pg_ques2_s1(),
            ],
        )
        q1_s4_op1.grid(row=3, column=0, rowspan=3, columnspan=3)

        # Top right option
        q1_s4_op2 = tk.Button(
            main_frame,
            text="Academic Probation",
            font=main_text_font,
            height="5",
            width="30",
            command=lambda: [
                hide_widgets(q1_s4_text, q1_s4_op1, q1_s4_op2, q1_s4_op3),
                calculate_points(["q1", "s4", "op2"]),
                pg_ques2_s1(),
            ],
        )
        q1_s4_op2.grid(row=3, column=3, rowspan=3, columnspan=3)

        # Bottom left option
        q1_s4_op3 = tk.Button(
            main_frame,
            text="Other",
            font=main_text_font,
            height="5",
            width="30",
            command=lambda: [
                hide_widgets(q1_s4_text, q1_s4_op1, q1_s4_op2, q1_s4_op3),
                calculate_points(["q1", "s4", "op3"]),
                pg_ques2_s1(),
            ],
        )
        q1_s4_op3.grid(row=6, column=0, rowspan=3, columnspan=3)

    def pg_ques1_s3():

        # Question title
        q1_s3_text = tk.Label(
            main_frame,
            text="Q1S3: Have you been denied\n entry into residence before?",
            font=question_text_font,
        )
        q1_s3_text.grid(row=1, column=0, columnspan=6)

        # Top left option
        q1_s3_op1 = tk.Button(
            main_frame,
            text="Yes",
            font=main_text_font,
            height="10",
            width="30",
            command=lambda: [
                hide_widgets(q1_s3_text, q1_s3_op1, q1_s3_op2),
                calculate_points(["q1", "s3", "op1"]),
                pg_ques1_s4(),
            ],
        )
        q1_s3_op1.grid(row=3, column=0, rowspan=6, columnspan=3)

        # Top right option
        q1_s3_op2 = tk.Button(
            main_frame,
            text="No",
            font=main_text_font,
            height="10",
            width="30",
            command=lambda: [
                hide_widgets(q1_s3_text, q1_s3_op1, q1_s3_op2),
                calculate_points(["q1", "s3", "op2"]),
                pg_ques2_s1(),
            ],
        )
        q1_s3_op2.grid(row=3, column=3, rowspan=6, columnspan=3)

    def pg_ques1_s2():

        # Question title
        q1_s2_text = tk.Label(
            main_frame,
            text="Q1S2: Were you previously in residence?",
            font=question_text_font,
        )
        q1_s2_text.grid(row=1, column=0, columnspan=6)

        # Top left option
        q1_s2_op1 = tk.Button(
            main_frame,
            text="Yes",
            font=main_text_font,
            height="10",
            width="30",
            command=lambda: [
                hide_widgets(q1_s2_text, q1_s2_op1, q1_s2_op2),
                calculate_points(["q1", "s2", "op1"]),
                pg_ques1_s3(),
            ],
        )
        q1_s2_op1.grid(row=3, column=0, rowspan=6, columnspan=3)

        # Top right option
        q1_s2_op2 = tk.Button(
            main_frame,
            text="No",
            font=main_text_font,
            height="10",
            width="30",
            command=lambda: [
                hide_widgets(q1_s2_text, q1_s2_op1, q1_s2_op2),
                calculate_points(["q1", "s2", "op2"]),
                pg_ques1_s3(),
            ],
        )
        q1_s2_op2.grid(row=3, column=3, rowspan=6, columnspan=3)

    def input_verify(user_input):

        global credits, print_error

        try:
            credits = float(user_input)
            if credits <= 40 and credits > 0 and credits % 0.5 == 0:
                calculate_points(["q1", "s1", "box"])
                hide_widgets(
                    q1_s1_text,
                    q1_s1_box_title,
                    q1_s1_box,
                    q1_s1_box_button,
                    q1_s1_box_error,
                )
                pg_ques1_s2()
                print_error = False
            else:
                print_error = True
        except ValueError:
            print_error = True
        if print_error:
            q1_s1_box_error.grid(row=6, column=1, columnspan=4)

    global print_error
    print_error = False

    # Question title
    q1_s1_text = tk.Label(
        main_frame,
        text="Q1S1: How many credits do you currently have?",
        font=question_text_font,
    )
    q1_s1_text.grid(row=1, column=0, columnspan=6)

    # Input Box Title
    q1_s1_box_title = tk.Label(main_frame, text="Enter an integer below")
    q1_s1_box_title.grid(row=2, column=1, columnspan=4, sticky="S")

    # Input Box
    q1_s1_box = tk.Entry(main_frame, font=main_text_font)
    q1_s1_box.grid(row=3, column=2, columnspan=2)

    # Input Box Submit Button
    q1_s1_box_button = tk.Button(
        main_frame,
        text="Submit",
        font=main_text_font,
        height="1",
        width="5",
        command=lambda: [input_verify(q1_s1_box.get())],
    )
    q1_s1_box_button.grid(row=4, column=1, columnspan=4)


def pg_ques2_s1():
    def pg_ques2_s2():

        # Question title
        q2_s2_text = tk.Label(
            main_frame,
            text="Q2S2: How many courses are you\n currently taking in the upcoming term?",
            font=question_text_font,
        )
        q2_s2_text.grid(row=1, column=0, columnspan=6)

        # Top left option
        q2_s2_op1 = tk.Button(
            main_frame,
            text="2.0+",
            font=main_text_font,
            height="5",
            width="30",
            command=lambda: [
                hide_widgets(
                    q2_s2_text, q2_s2_op1, q2_s2_op2, q2_s2_op3, q2_s2_op4
                ),
                calculate_points(["q2", "s2", "op1"]),
                pg_ques3_s1(),
            ],
        )
        q2_s2_op1.grid(row=3, column=0, rowspan=3, columnspan=3)

        # Top right option
        q2_s2_op2 = tk.Button(
            main_frame,
            text="1.5",
            font=main_text_font,
            height="5",
            width="30",
            command=lambda: [
                hide_widgets(
                    q2_s2_text, q2_s2_op1, q2_s2_op2, q2_s2_op3, q2_s2_op4
                ),
                calculate_points(["q2", "s2", "op2"]),
                pg_ques3_s1(),
            ],
        )
        q2_s2_op2.grid(row=3, column=3, rowspan=3, columnspan=3)

        # Bottom left option
        q2_s2_op3 = tk.Button(
            main_frame,
            text="1.0",
            font=main_text_font,
            height="5",
            width="30",
            command=lambda: [
                hide_widgets(
                    q2_s2_text, q2_s2_op1, q2_s2_op2, q2_s2_op3, q2_s2_op4
                ),
                calculate_points(["q2", "s2", "op3"]),
                pg_ques3_s1(),
            ],
        )
        q2_s2_op3.grid(row=6, column=0, rowspan=3, columnspan=3)

        # Bottom right option
        q2_s2_op4 = tk.Button(
            main_frame,
            text="0.5",
            font=main_text_font,
            height="5",
            width="30",
            command=lambda: [
                hide_widgets(
                    q2_s2_text, q2_s2_op1, q2_s2_op2, q2_s2_op3, q2_s2_op4
                ),
                calculate_points(["q2", "s2", "op4"]),
                pg_ques3_s1(),
            ],
        )
        q2_s2_op4.grid(row=6, column=3, rowspan=3, columnspan=3)

    # Question title
    q2_s1_text = tk.Label(
        main_frame,
        text="Q2S1: Are you a full-time or part-time student?",
        font=question_text_font,
    )
    q2_s1_text.grid(row=1, column=0, columnspan=6)

    # Top left option
    q2_s1_op1 = tk.Button(
        main_frame,
        text="Full-Time",
        font=main_text_font,
        height="5",
        width="30",
        command=lambda: [
            hide_widgets(q2_s1_text, q2_s1_op1, q2_s1_op2),
            calculate_points(["q2", "s1", "op1"]),
            pg_ques2_s2(),
        ],
    )
    q2_s1_op1.grid(row=3, column=0, rowspan=3, columnspan=3)

    # Top right option
    q2_s1_op2 = tk.Button(
        main_frame,
        text="Part-Time",
        font=main_text_font,
        height="5",
        width="30",
        command=lambda: [
            hide_widgets(q2_s1_text, q2_s1_op1, q2_s1_op2),
            calculate_points(["q2", "s1", "op2"]),
            pg_ques2_s2(),
        ],
    )
    q2_s1_op2.grid(row=3, column=3, rowspan=3, columnspan=3)


def pg_ques3_s1():
    # Question title
    q3_s1_text = tk.Label(
        main_frame,
        text="Q3S1: What is your current age?",
        font=question_text_font,
    )
    q3_s1_text.grid(row=1, column=0, columnspan=6)

    # Top left option
    q3_s1_op1 = tk.Button(
        main_frame,
        text="18-22",
        font=main_text_font,
        height="5",
        width="30",
        command=lambda: [
            hide_widgets(q3_s1_text, q3_s1_op1, q3_s1_op2),
            calculate_points(["q3", "s1", "op1"]),
            pg_ques4_s1(),
        ],
    )
    q3_s1_op1.grid(row=3, column=0, rowspan=3, columnspan=3)

    # Top right option
    q3_s1_op2 = tk.Button(
        main_frame,
        text="23+",
        font=main_text_font,
        height="5",
        width="30",
        command=lambda: [
            hide_widgets(q3_s1_text, q3_s1_op1, q3_s1_op2),
            calculate_points(["q3", "s1", "op2"]),
            pg_ques4_s1(),
        ],
    )
    q3_s1_op2.grid(row=3, column=3, rowspan=3, columnspan=3)


def pg_ques4_s1():
    # Question title
    q4_s1_text = tk.Label(
        main_frame,
        text="Q4S1: Have you or will you possibly\n be on academic/disciplinary probation? ",
        font=question_text_font,
    )
    q4_s1_text.grid(row=1, column=0, columnspan=6)

    # Top left option
    q4_s1_op1 = tk.Button(
        main_frame,
        text="Yes, I AM/HAVE BEEN\n on academic probation",
        font=main_text_font,
        height="5",
        width="30",
        command=lambda: [
            hide_widgets(
                q4_s1_text, q4_s1_op1, q4_s1_op2, q4_s1_op3, q4_s1_op4
            ),
            calculate_points(["q4", "s1", "op1"]),
            pg_ques5_s1(),
        ],
    )
    q4_s1_op1.grid(row=3, column=0, rowspan=3, columnspan=3)

    # Top right option
    q4_s1_op2 = tk.Button(
        main_frame,
        text="Yes, I WILL POSSIBLY\n face an academic suspension",
        font=main_text_font,
        height="5",
        width="30",
        command=lambda: [
            hide_widgets(
                q4_s1_text, q4_s1_op1, q4_s1_op2, q4_s1_op3, q4_s1_op4
            ),
            calculate_points(["q4", "s1", "op2"]),
            pg_ques5_s1(),
        ],
    )
    q4_s1_op2.grid(row=3, column=3, rowspan=3, columnspan=3)

    # Bottom left option
    q4_s1_op3 = tk.Button(
        main_frame,
        text="Yes, I HAVE\n faced disciplinary probation",
        font=main_text_font,
        height="5",
        width="30",
        command=lambda: [
            hide_widgets(
                q4_s1_text, q4_s1_op1, q4_s1_op2, q4_s1_op3, q4_s1_op4
            ),
            calculate_points(["q4", "s1", "op3"]),
            pg_ques5_s1(),
        ],
    )
    q4_s1_op3.grid(row=6, column=0, rowspan=3, columnspan=3)

    # Bottom right option
    q4_s1_op4 = tk.Button(
        main_frame,
        text="No, I HAVE NOT / WILL NOT\n be on academic or\n disciplinary probation",
        font=main_text_font,
        height="5",
        width="30",
        command=lambda: [
            hide_widgets(
                q4_s1_text, q4_s1_op1, q4_s1_op2, q4_s1_op3, q4_s1_op4
            ),
            calculate_points(["q4", "s1", "op4"]),
            pg_ques5_s1(),
        ],
    )
    q4_s1_op4.grid(row=6, column=3, rowspan=3, columnspan=3)


def pg_ques5_s1():
    def pg_ques5_s2():
        # Question title
        q5_s2_text = tk.Label(
            main_frame,
            text="Q5S2: Do you live within\n a 25km radius of the school?",
            font=question_text_font,
        )
        q5_s2_text.grid(row=1, column=0, columnspan=6)

        # Top left option
        q5_s2_op1 = tk.Button(
            main_frame,
            text="Yes",
            font=main_text_font,
            height="5",
            width="30",
            command=lambda: [
                hide_widgets(q5_s2_text, q5_s2_op1, q5_s2_op2),
                calculate_points(["q5", "s2", "op1"]),
                pg_ques6_s1(),
            ],
        )
        q5_s2_op1.grid(row=3, column=0, rowspan=3, columnspan=3)

        # Top right option
        q5_s2_op2 = tk.Button(
            main_frame,
            text="No",
            font=main_text_font,
            height="5",
            width="30",
            command=lambda: [
                hide_widgets(q5_s2_text, q5_s2_op1, q5_s2_op2),
                calculate_points(["q5", "s2", "op2"]),
                pg_ques6_s1(),
            ],
        )
        q5_s2_op2.grid(row=3, column=3, rowspan=3, columnspan=3)

    # Question title
    q5_s1_text = tk.Label(
        main_frame,
        text="Q5S1: Do you plan to live with a parent or guardian?",
        font=question_text_font,
    )
    q5_s1_text.grid(row=1, column=0, columnspan=6)

    # Top left option
    q5_s1_op1 = tk.Button(
        main_frame,
        text="Yes",
        font=main_text_font,
        height="5",
        width="30",
        command=lambda: [
            hide_widgets(q5_s1_text, q5_s1_op1, q5_s1_op2),
            calculate_points(["q5", "s1", "op1"]),
            pg_ques5_s2(),
        ],
    )
    q5_s1_op1.grid(row=3, column=0, rowspan=3, columnspan=3)

    # Top right option
    q5_s1_op2 = tk.Button(
        main_frame,
        text="No",
        font=main_text_font,
        height="5",
        width="30",
        command=lambda: [
            hide_widgets(q5_s1_text, q5_s1_op1, q5_s1_op2),
            calculate_points(["q5", "s1", "op2"]),
            pg_ques5_s2(),
        ],
    )
    q5_s1_op2.grid(row=3, column=3, rowspan=3, columnspan=3)


def pg_ques6_s1():
    # Question title
    q6_s1_text = tk.Label(
        main_frame,
        text="Q6S1: Are you an international student?",
        font=question_text_font,
    )
    q6_s1_text.grid(row=1, column=0, columnspan=6)

    # Top left option
    q6_s1_op1 = tk.Button(
        main_frame,
        text="Yes",
        font=main_text_font,
        height="5",
        width="30",
        command=lambda: [
            hide_widgets(q6_s1_text, q6_s1_op1, q6_s1_op2),
            calculate_points(["q6", "s1", "op1"]),
            pg_ques7_s1(),
        ],
    )
    q6_s1_op1.grid(row=3, column=0, rowspan=3, columnspan=3)

    # Top right option
    q6_s1_op2 = tk.Button(
        main_frame,
        text="No",
        font=main_text_font,
        height="5",
        width="30",
        command=lambda: [
            hide_widgets(q6_s1_text, q6_s1_op1, q6_s1_op2),
            calculate_points(["q6", "s1", "op2"]),
            pg_ques7_s1(),
        ],
    )
    q6_s1_op2.grid(row=3, column=3, rowspan=3, columnspan=3)


def pg_ques7_s1():
    def pg_ques7_s3():

        # Question title
        q7_s3_text = tk.Label(
            main_frame,
            text="Q7S3: Are any special accommodations\n needed for your physical disability?",
            font=question_text_font,
        )
        q7_s3_text.grid(row=1, column=0, columnspan=6)

        # Top left option
        q7_s3_op1 = tk.Button(
            main_frame,
            text="Yes",
            font=main_text_font,
            height="5",
            width="30",
            command=lambda: [
                hide_widgets(q7_s3_text, q7_s3_op1, q7_s3_op2),
                calculate_points(["q7", "s3", "op1"]),
                pg_ques8_s1(),
            ],
        )
        q7_s3_op1.grid(row=3, column=0, rowspan=3, columnspan=3)

        # Top right option
        q7_s3_op2 = tk.Button(
            main_frame,
            text="No",
            font=main_text_font,
            height="5",
            width="30",
            command=lambda: [
                hide_widgets(q7_s3_text, q7_s3_op1, q7_s3_op2),
                calculate_points(["q7", "s3", "op2"]),
                pg_ques8_s1(),
            ],
        )
        q7_s3_op2.grid(row=3, column=3, rowspan=3, columnspan=3)

    def pg_ques7_s2():

        # Question title
        q7_s2_text = tk.Label(
            main_frame,
            text="Q7S2: Is the physical disability\n persistent or prolonged?",
            font=question_text_font,
        )
        q7_s2_text.grid(row=1, column=0, columnspan=6)

        # Top left option
        q7_s2_op1 = tk.Button(
            main_frame,
            text="Yes",
            font=main_text_font,
            height="5",
            width="30",
            command=lambda: [
                hide_widgets(q7_s2_text, q7_s2_op1, q7_s2_op2),
                calculate_points(["q7", "s2", "op1"]),
                pg_ques7_s3(),
            ],
        )
        q7_s2_op1.grid(row=3, column=0, rowspan=3, columnspan=3)

        # Top right option
        q7_s2_op2 = tk.Button(
            main_frame,
            text="No",
            font=main_text_font,
            height="5",
            width="30",
            command=lambda: [
                hide_widgets(q7_s2_text, q7_s2_op1, q7_s2_op2),
                calculate_points(["q7", "s2", "op2"]),
                pg_ques7_s3(),
            ],
        )
        q7_s2_op2.grid(row=3, column=3, rowspan=3, columnspan=3)

    # Question title
    q7_s1_text = tk.Label(
        main_frame,
        text="Q7S1: Do you have a physical disability?",
        font=question_text_font,
    )
    q7_s1_text.grid(row=1, column=0, columnspan=6)

    # Top left option
    q7_s1_op1 = tk.Button(
        main_frame,
        text="Yes",
        font=main_text_font,
        height="5",
        width="30",
        command=lambda: [
            hide_widgets(q7_s1_text, q7_s1_op1, q7_s1_op2),
            calculate_points(["q7", "s1", "op1"]),
            pg_ques7_s2(),
        ],
    )
    q7_s1_op1.grid(row=3, column=0, rowspan=3, columnspan=3)

    # Top right option
    q7_s1_op2 = tk.Button(
        main_frame,
        text="No",
        font=main_text_font,
        height="5",
        width="30",
        command=lambda: [
            hide_widgets(q7_s1_text, q7_s1_op1, q7_s1_op2),
            calculate_points(["q7", "s1", "op2"]),
            pg_ques8_s1(),
        ],
    )
    q7_s1_op2.grid(row=3, column=3, rowspan=3, columnspan=3)


def pg_ques8_s1():
    def pg_ques8_s3():

        # Question title
        q8_s3_text = tk.Label(
            main_frame,
            text="Q8S3: Are any special accommodations\n needed for your mental disability?",
            font=question_text_font,
        )
        q8_s3_text.grid(row=1, column=0, columnspan=6)

        # Top left option
        q8_s3_op1 = tk.Button(
            main_frame,
            text="Yes",
            font=main_text_font,
            height="5",
            width="30",
            command=lambda: [
                hide_widgets(q8_s3_text, q8_s3_op1, q8_s3_op2),
                calculate_points(["q8", "s3", "op1"]),
                pg_ques9_s1(),
            ],
        )
        q8_s3_op1.grid(row=3, column=0, rowspan=3, columnspan=3)

        # Top right option
        q8_s3_op2 = tk.Button(
            main_frame,
            text="No",
            font=main_text_font,
            height="5",
            width="30",
            command=lambda: [
                hide_widgets(q8_s3_text, q8_s3_op1, q8_s3_op2),
                calculate_points(["q8", "s3", "op2"]),
                pg_ques9_s1(),
            ],
        )
        q8_s3_op2.grid(row=3, column=3, rowspan=3, columnspan=3)

    def pg_ques8_s2():

        # Question title
        q8_s2_text = tk.Label(
            main_frame,
            text="Q8S2: Is your mental\n disability persistent or prolonged?",
            font=question_text_font,
        )
        q8_s2_text.grid(row=1, column=0, columnspan=6)

        # Top left option
        q8_s2_op1 = tk.Button(
            main_frame,
            text="Yes",
            font=main_text_font,
            height="5",
            width="30",
            command=lambda: [
                hide_widgets(q8_s2_text, q8_s2_op1, q8_s2_op2),
                calculate_points(["q8", "s2", "op1"]),
                pg_ques8_s3(),
            ],
        )
        q8_s2_op1.grid(row=3, column=0, rowspan=3, columnspan=3)

        # Top right option
        q8_s2_op2 = tk.Button(
            main_frame,
            text="No",
            font=main_text_font,
            height="5",
            width="30",
            command=lambda: [
                hide_widgets(q8_s2_text, q8_s2_op1, q8_s2_op2),
                calculate_points(["q8", "s2", "op2"]),
                pg_ques8_s3(),
            ],
        )
        q8_s2_op2.grid(row=3, column=3, rowspan=3, columnspan=3)

    # Question title
    q8_s1_text = tk.Label(
        main_frame,
        text="Q8S1: Do you have any mental disabilities?",
        font=question_text_font,
    )
    q8_s1_text.grid(row=1, column=0, columnspan=6)

    # Top left option
    q8_s1_op1 = tk.Button(
        main_frame,
        text="Yes",
        font=main_text_font,
        height="5",
        width="30",
        command=lambda: [
            hide_widgets(q8_s1_text, q8_s1_op1, q8_s1_op2),
            calculate_points(["q8", "s1", "op1"]),
            pg_ques8_s2(),
        ],
    )
    q8_s1_op1.grid(row=3, column=0, rowspan=3, columnspan=3)

    # Top right option
    q8_s1_op2 = tk.Button(
        main_frame,
        text="No",
        font=main_text_font,
        height="5",
        width="30",
        command=lambda: [
            hide_widgets(q8_s1_text, q8_s1_op1, q8_s1_op2),
            calculate_points(["q8", "s1", "op2"]),
            pg_ques9_s1(),
        ],
    )
    q8_s1_op2.grid(row=3, column=3, rowspan=3, columnspan=3)


def pg_ques9_s1():
    # Question title
    q9_s1_text = tk.Label(
        main_frame,
        text="Q9S1: Are you part of an\n athletics team on campus?",
        font=question_text_font,
    )
    q9_s1_text.grid(row=1, column=0, columnspan=6)

    # Top left option
    q9_s1_op1 = tk.Button(
        main_frame,
        text="Yes",
        font=main_text_font,
        height="5",
        width="30",
        command=lambda: [
            hide_widgets(q9_s1_text, q9_s1_op1, q9_s1_op2),
            calculate_points(["q9", "s1", "op1"]),
            pg_ques10_s1(),
        ],
    )
    q9_s1_op1.grid(row=3, column=0, rowspan=3, columnspan=3)

    # Top right option
    q9_s1_op2 = tk.Button(
        main_frame,
        text="No",
        font=main_text_font,
        height="5",
        width="30",
        command=lambda: [
            hide_widgets(q9_s1_text, q9_s1_op1, q9_s1_op2),
            calculate_points(["q9", "s1", "op2"]),
            pg_ques10_s1(),
        ],
    )
    q9_s1_op2.grid(row=3, column=3, rowspan=3, columnspan=3)


def pg_ques10_s1():
    def pg_ques10_s2():

        # Question title
        q10_s1_text = tk.Label(
            main_frame,
            text="Q10S2: How much is your OSAP?",
            font=question_text_font,
        )
        q10_s1_text.grid(row=1, column=0, columnspan=6)

        # Top left option
        q10_s1_op1 = tk.Button(
            main_frame,
            text=">$4,000",
            font=main_text_font,
            height="5",
            width="30",
            command=lambda: [
                hide_widgets(q10_s1_text, q10_s1_op1, q10_s1_op2, q10_s1_op3),
                calculate_points(["q10", "s2", "op1"]),
                pg_ques11_s1(),
            ],
        )
        q10_s1_op1.grid(row=3, column=0, rowspan=3, columnspan=3)

        # Top right option
        q10_s1_op2 = tk.Button(
            main_frame,
            text="$4,000 - $6,999",
            font=main_text_font,
            height="5",
            width="30",
            command=lambda: [
                hide_widgets(q10_s1_text, q10_s1_op1, q10_s1_op2, q10_s1_op3),
                calculate_points(["q10", "s2", "op2"]),
                pg_ques11_s1(),
            ],
        )
        q10_s1_op2.grid(row=3, column=3, rowspan=3, columnspan=3)

        # Bottom left option
        q10_s1_op3 = tk.Button(
            main_frame,
            text="$7,000+",
            font=main_text_font,
            height="5",
            width="30",
            command=lambda: [
                hide_widgets(q10_s1_text, q10_s1_op1, q10_s1_op2, q10_s1_op3),
                calculate_points(["q10", "s2", "op3"]),
                pg_ques11_s1(),
            ],
        )
        q10_s1_op3.grid(row=6, column=0, rowspan=3, columnspan=3)

    # Question title
    q10_s1_text = tk.Label(
        main_frame, text="Q10S1: Are you on OSAP?", font=question_text_font
    )
    q10_s1_text.grid(row=1, column=0, columnspan=6)

    # Top left option
    q10_s1_op1 = tk.Button(
        main_frame,
        text="Yes",
        font=main_text_font,
        height="5",
        width="30",
        command=lambda: [
            hide_widgets(q10_s1_text, q10_s1_op1, q10_s1_op2),
            calculate_points(["q10", "s1", "op1"]),
            pg_ques10_s2(),
        ],
    )
    q10_s1_op1.grid(row=3, column=0, rowspan=3, columnspan=3)

    # Top right option
    q10_s1_op2 = tk.Button(
        main_frame,
        text="No",
        font=main_text_font,
        height="5",
        width="30",
        command=lambda: [
            hide_widgets(q10_s1_text, q10_s1_op1, q10_s1_op2),
            calculate_points(["q10", "s1", "op2"]),
            pg_ques11_s1(),
        ],
    )
    q10_s1_op2.grid(row=3, column=3, rowspan=3, columnspan=3)


def pg_ques11_s1():
    def pg_ques11_s2():

        # Question title
        q11_s2_text = tk.Label(
            main_frame,
            text="Q11S2: Would you be interested in\n pursuing a job opportunity on campus?",
            font=question_text_font,
        )
        q11_s2_text.grid(row=1, column=0, columnspan=6)

        # Top left option
        q11_s2_op1 = tk.Button(
            main_frame,
            text="Yes",
            font=main_text_font,
            height="5",
            width="30",
            command=lambda: [
                hide_widgets(q11_s2_text, q11_s2_op1, q11_s2_op2),
                calculate_points(["q11", "s2", "op1"]),
                pg_ques12_s1(),
            ],
        )
        q11_s2_op1.grid(row=3, column=0, rowspan=3, columnspan=3)

        # Top right option
        q11_s2_op2 = tk.Button(
            main_frame,
            text="No",
            font=main_text_font,
            height="5",
            width="30",
            command=lambda: [
                hide_widgets(q11_s2_text, q11_s2_op1, q11_s2_op2),
                calculate_points(["q11", "s2", "op2"]),
                pg_ques12_s1(),
            ],
        )
        q11_s2_op2.grid(row=3, column=3, rowspan=3, columnspan=3)

    # Question title
    q11_s1_text = tk.Label(
        main_frame,
        text="Q11S1: Do you currently have a job on campus?",
        font=question_text_font,
    )
    q11_s1_text.grid(row=1, column=0, columnspan=6)

    # Top left option
    q11_s1_op1 = tk.Button(
        main_frame,
        text="Yes",
        font=main_text_font,
        height="5",
        width="30",
        command=lambda: [
            hide_widgets(q11_s1_text, q11_s1_op1, q11_s1_op2),
            calculate_points(["q11", "s1", "op1"]),
            pg_ques12_s1(),
        ],
    )
    q11_s1_op1.grid(row=3, column=0, rowspan=3, columnspan=3)

    # Top right option
    q11_s1_op2 = tk.Button(
        main_frame,
        text="No",
        font=main_text_font,
        height="5",
        width="30",
        command=lambda: [
            hide_widgets(q11_s1_text, q11_s1_op1, q11_s1_op2),
            calculate_points(["q11", "s1", "op2"]),
            pg_ques11_s2(),
        ],
    )
    q11_s1_op2.grid(row=3, column=3, rowspan=3, columnspan=3)


def pg_ques12_s1():

    # Question title
    q12_s1_text = tk.Label(
        main_frame,
        text="Q12S1: Any specific preferences for residency?",
        font=question_text_font,
    )
    q12_s1_text.grid(row=1, column=0, columnspan=6)

    # Top left option
    q12_s1_op1 = tk.Button(
        main_frame,
        text="Private",
        font=main_text_font,
        height="5",
        width="30",
        command=lambda: [
            hide_widgets(q12_s1_text, q12_s1_op1, q12_s1_op2, q12_s1_op3),
            calculate_points(["q12", "s1", "op1"]),
            pg_end(),
        ],
    )
    q12_s1_op1.grid(row=3, column=0, rowspan=3, columnspan=3)

    # Top right option
    q12_s1_op2 = tk.Button(
        main_frame,
        text="Shared",
        font=main_text_font,
        height="5",
        width="30",
        command=lambda: [
            hide_widgets(q12_s1_text, q12_s1_op1, q12_s1_op2, q12_s1_op3),
            calculate_points(["q12", "s1", "op2"]),
            pg_end(),
        ],
    )
    q12_s1_op2.grid(row=3, column=3, rowspan=3, columnspan=3)

    # Bottom left option
    q12_s1_op3 = tk.Button(
        main_frame,
        text="None",
        font=main_text_font,
        height="5",
        width="30",
        command=lambda: [
            hide_widgets(q12_s1_text, q12_s1_op1, q12_s1_op2, q12_s1_op3),
            calculate_points(["q12", "s1", "op3"]),
            pg_end(),
        ],
    )
    q12_s1_op3.grid(row=6, column=0, rowspan=3, columnspan=3)


def pg_end():
    # MW logo
    global logo
    logo = tk.PhotoImage(file="housing_calc_old/mw_logo.png")
    logo_label = tk.Label(main_frame, image=logo, bg="#DCDCDD")
    logo_label.grid(row=0, column=1, columnspan=4)

    # Middle text
    global point_counter
    points = str(round(point_counter, 1))
    middle_text = tk.Label(
        main_frame,
        fg="#090A0B",
        bg="#DCDCDD",
        text="Your information was successfully submitted.\nThank you for using the MWU Housing Calculator.\n\nYour points: "
        + points,
        font=title_text_font_s15,
    )
    middle_text.grid(row=1, column=0, columnspan=6, sticky="S")

    # Repeat button
    repeat_button = tk.Button(
        main_frame,
        bg="#C5C3C6",
        text="Click here to run the calculator again",
        command=lambda: [
            hide_widgets(logo_label, middle_text, repeat_button),
            pg_welcome(),
        ],
    )
    repeat_button.grid(row=4, column=1, columnspan=4)


win = tk.Tk()
win.title("Mary Ward University")
win.minsize("700", "500")
win.maxsize("700", "500")


main_frame = tk.Frame(win, width="700", height="500")
main_frame.pack()


main_frame.rowconfigure(0, weight=2)
main_frame.rowconfigure(1, weight=2)
main_frame.rowconfigure(2, weight=2)
main_frame.rowconfigure(3, weight=1)
main_frame.rowconfigure(4, weight=1)
main_frame.rowconfigure(5, weight=1)
main_frame.rowconfigure(6, weight=1)
main_frame.rowconfigure(8, weight=1)
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.columnconfigure(2, weight=1)
main_frame.columnconfigure(3, weight=1)
main_frame.columnconfigure(4, weight=1)
main_frame.columnconfigure(5, weight=1)


background = tk.Frame(main_frame, bg="#DCDCDD", width="700", height="500")
background.grid(row=0, column=0, rowspan=9, columnspan=6)


question_text_font = ("FreeSans", 20, "bold")
main_text_font = ("FreeSans", 15)
title_text_font_s25 = ("FreeSans", 27, "bold")
title_text_font_s15 = ("FreeSans", 15, "bold")


point_counter = 100


q1_s1_box_error = tk.Label(
    main_frame, text="ERROR: Please enter a valid input!", font=main_text_font
)


pg_welcome()


win.mainloop()
