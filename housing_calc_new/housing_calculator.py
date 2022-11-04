"""
Filename: housing_calculator_main.py
Author: Anthony Toyco, Ryan Alumkal, Ryan Lin
Date: Friday November 4, 2022
Description: A program that calculates the likelihood of a
student's acceptance into residency.
"""

import tkinter as tk

from dicts import points_dict, prompts

QUESTION_TEXT_FONT = ("FreeSans", 20, "bold")
MAIN_TEXT_FONT = ("FreeSans", 15)
TITLE_TEXT_FONT_S25 = ("FreeSans", 27, "bold")
TITLE_TEXT_FONT_S15 = ("FreeSans", 15, "bold")


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

        self.title("Mary Ward University - Housing Calculator")
        self.geometry("700x500")
        self.resizable(False, False)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        label = tk.Label(
            self,
            text="Mary Ward University - Housing Calculator",
            font=TITLE_TEXT_FONT_S25,
        )
        label.grid(row=0, column=0, sticky="nsew")

        title_text_top = tk.Label(
            self,
            fg="#090A0B",
            bg="#DCDCDD",
            text="HOUSING SCORE CALCULATOR",
            font=TITLE_TEXT_FONT_S25,
        )
        title_text_top.grid(row=1, column=0, sticky="nsew")


class QuestionPage(tk.Frame):
    # Static variable
    point_counter = 100

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


class Counters:
    def __init__(self, std_credits, std_points):
        self.std_credits = std_credits
        self.std_points = std_points


# MAIN PROGRAM #


if __name__ == "__main__":
    app = App()
    app.mainloop()
