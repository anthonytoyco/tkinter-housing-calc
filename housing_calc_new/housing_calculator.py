"""
Filename: housing_calculator_main.py
Author: Anthony Toyco, Ryan Alumkal, Ryan Lin
Date: Friday November 4, 2022
Description: A program that calculates the likelihood of a
student's acceptance into residency.
"""

import tkinter as tk

from dicts import points_dict, prompts, button_order

QUESTION_TEXT_FONT = ("Arial", 20, "bold")
MAIN_TEXT_FONT = ("Arial", 15)
TITLE_TEXT_FONT_S25 = ("Arial", 25, "bold")
TITLE_TEXT_FONT_S15 = ("Arial", 15, "bold")


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._page = None

        self.title("Mary Ward University - Housing Calculator")
        self.geometry("700x500")
        self.resizable(False, False)

        self.logo = tk.PhotoImage(file="housing_calc_new/assets/mw_logo.png")

        self.replace_frame(StartPage)

    def replace_frame(self, page):
        new_page = page(self)
        if self._page is not None:
            self._page.destroy()
        self._page = new_page
        self._page.pack()


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        title_text_top = tk.Label(
            self,
            fg="white",
            text="HOUSING SCORE CALCULATOR",
            font=TITLE_TEXT_FONT_S25,
        )
        title_text_top.grid(row=0, column=0, pady=20)

        title_text_under = tk.Label(
            self,
            fg="white",
            text="By Mary Ward University",
            font=TITLE_TEXT_FONT_S15,
        )
        title_text_under.grid(row=1, column=0)

        logo_label = tk.Label(self, image=master.logo, bg="white")
        logo_label.grid(row=2, column=0)

        start_button = tk.Button(
            self,
            text="START",
            font=MAIN_TEXT_FONT,
            command=lambda: master.replace_frame(InputPage),
        )
        start_button.grid(row=3, column=0, pady=20)


class InputPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is page two").pack(
            side="top", fill="x", pady=10
        )
        tk.Button(
            self,
            text="Return to start page",
            command=lambda: master.replace_frame(StartPage),
        ).pack()


class ChoicePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is page two").pack(
            side="top", fill="x", pady=10
        )
        tk.Button(
            self,
            text="Return to start page",
            command=lambda: master.replace_frame(StartPage),
        ).pack()


class Counters:
    def __init__(self, std_credits, std_points):
        self.std_credits = std_credits
        self.std_points = std_points


# MAIN PROGRAM #


if __name__ == "__main__":
    app = App()
    app.mainloop()
