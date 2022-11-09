import tkinter as tk
import customtkinter as ct
import constants as c


class App(ct.CTk):
    def __init__(self):
        super().__init__()
        self._page = None

        self.geometry(f"{700}x{500}")
        self.title("Mary Ward University - Housing Calculator")
        self.resizable(False, False)

        self.logo = tk.PhotoImage(file="housing_calc_new/assets/mw_logo.png")

        self.logo_label = tk.Label(self, image=self.logo, bg="#DCDCDD")
        self.logo_label.pack(ipady=20, fill="both", expand=True)

        self.after(
            1000,
            lambda: [
                self.replace_frame(StartPage),
                self.logo_label.destroy(),
            ],
        )

    def replace_frame(self, page):
        new_page = page(self)
        if self._page is not None:
            self._page.destroy()
        self._page = new_page
        self._page.pack()


class StartPage(ct.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

        self.title_text_top = ct.CTkLabel(
            self,
            text="HOUSING SCORE CALCULATOR",
            text_font=c.TITLE_TEXT_FONT_S25,
        )
        self.title_text_top.grid(row=0, column=0, columnspan=4)

        self.title_text_under = ct.CTkLabel(
            self,
            text="By Mary Ward University",
            text_font=c.TITLE_TEXT_FONT_S15,
        )
        self.title_text_under.grid(row=1, column=0, columnspan=4)

        self.logo_label = ct.CTkLabel(
            self, image=master.logo, bg_color="#DCDCDD"
        )
        self.logo_label.grid(row=2, column=0)

        self.start_button = tk.Button(
            self,
            text="START",
            font=c.MAIN_TEXT_FONT,
            command=lambda: master.replace_frame(CreditInputPage),
        )
        self.start_button.grid(row=3, column=0, pady=20)


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
