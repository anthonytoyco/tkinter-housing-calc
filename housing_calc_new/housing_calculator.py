"""
Filename: housing_calculator_main.py
Author: Anthony Toyco, Ryan Alumkal, Ryan Lin
Date: Friday November 4, 2022
Description: A program that calculates the likelihood of a
student's acceptance into residency.
"""

# TODOLIST:
# 1. setup the ChoicePage class and loop to change buttons (8 buttons?),
#    question prompts, and points granted on each button.
#    use .config() for this part?
# 2. setup the EndPage class
# 3. setup https://github.com/TomSchimansky/CustomTkinter

import tkinter as tk
import constants as c


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.title("Mary Ward University - Housing Calculator")
        self.geometry("700x500")
        self.resizable(False, False)

        self.logo = tk.PhotoImage(file="housing_calc_new/assets/mw_logo.png")

        self._page = None
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
            font=c.TITLE_TEXT_FONT_S25,
        )
        title_text_top.grid(row=0, column=0, pady=20)

        title_text_under = tk.Label(
            self,
            fg="white",
            text="By Mary Ward University",
            font=c.TITLE_TEXT_FONT_S15,
        )
        title_text_under.grid(row=1, column=0)

        logo_label = tk.Label(self, image=master.logo, bg="white")
        logo_label.grid(row=2, column=0)

        start_button = tk.Button(
            self,
            text="START",
            font=c.MAIN_TEXT_FONT,
            command=lambda: master.replace_frame(CreditInputPage),
        )
        start_button.grid(row=3, column=0, pady=20)


class CreditInputPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        question_title = tk.Label(
            self,
            text="Q1S1: How many credits do you currently have?",
            font=c.QUESTION_TEXT_FONT,
        )
        question_title.grid(row=0, column=0)

        input_box_title = tk.Label(self, text="Enter an integer below")
        input_box_title.grid(row=1, column=0, sticky="S")

        input_box = tk.Entry(self, font=c.MAIN_TEXT_FONT)
        input_box.grid(row=2, column=0)

        self.input_box_error = tk.Label(
            self, text="ERROR: Please enter a valid number!"
        )

        input_box_button = tk.Button(
            self,
            text="Submit",
            font=c.MAIN_TEXT_FONT,
            height="1",
            width="5",
            command=lambda: [
                self.input_box_error.forget(),
                self.input_verify(input_box.get()),
            ],
        )
        input_box_button.grid(row=3, column=0)

    def input_verify(self, user_entry):
        try:
            if (1 <= float(user_entry) <= 40) and (
                float(user_entry) % 0.5 == 0
            ):
                self.input_box_error.grid_forget()
                StudentData.credits = user_entry
                self.master.replace_frame(ChoicePage)
            else:
                self.input_box_error.grid(row=4, column=0)
        except ValueError:
            self.input_box_error.grid(row=4, column=0)


class ChoicePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        raise NotImplementedError("ChoicePage is not implemented yet")

    # TODO: initialize 3 groups of buttons (g1 = 2 buttons, g2 = 3 buttons, g3 = 4 buttons).    # noqa: E501
    #       groups will  will be independently displayed depending on question number.          # noqa: E501
    #       use .config() to change the text and command of the buttons???


class StudentData:
    credits = 0
    points = 0


# MAIN PROGRAM #


if __name__ == "__main__":
    app = App()
    app.mainloop()
