import tkinter as tk

import constants as c
import customtkinter as ct


class App(ct.CTk):
    def __init__(self):
        super().__init__()
        self._page = None

        self.geometry(f"{700}x{500}")
        self.title("Mary Ward University - Housing Calculator")
        self.resizable(False, False)
        self.configure(fg_color=c.FRAME_BG_COLOR)

        self.logo = tk.PhotoImage(file="housing_calc_new/assets/mw_logo.png")

        self.logo_label = ct.CTkLabel(self, image=self.logo, bg="#DCDCDD")
        self.logo_label.pack(pady=(140, 0), expand=True)
        self.name = ct.CTkLabel(
            self,
            text="Mary Ward University",
            text_color="#2B2B2C",
            text_font=c.TITLE_TEXT_FONT_S25,
        )
        self.name.pack(pady=(0, 170), expand=True)

        self.after(
            1000,
            lambda: [
                self.replace_frame(StartPage),
                self.logo_label.destroy(),
                self.name.destroy(),
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
        self.configure(fg_color="#DCDCDD")

        self.title_text_top = ct.CTkLabel(
            self,
            text="HOUSING SCORE CALCULATOR",
            text_color="#2B2B2C",
            text_font=c.TITLE_TEXT_FONT_S25,
        )
        self.title_text_top.grid(row=0, column=0, columnspan=4, pady=(50, 0))

        self.title_text_under = ct.CTkLabel(
            self,
            text="By Mary Ward University",
            text_color="#2B2B2C",
            text_font=c.TITLE_TEXT_FONT_S15,
        )
        self.title_text_under.grid(row=1, column=0, columnspan=4, sticky="N")

        self.logo_label = ct.CTkLabel(self, image=master.logo)
        self.logo_label.grid(row=2, column=0, columnspan=4, pady=(39, 40))

        self.start_button = ct.CTkButton(
            self,
            text="START",
            fg_color="#2B2B2C",
            hover_color="#001B4B",
            text_font=c.TITLE_TEXT_FONT_S15,
            command=lambda: master.replace_frame(CreditInputPage),
        )
        self.start_button.grid(row=3, column=0, columnspan=4, pady=10)


class CreditInputPage(ct.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(fg_color="#DCDCDD")

        self.question_title = ct.CTkLabel(
            self,
            text="Q1S1: How many credits do you currently have?",
            text_color="#2B2B2C",
            text_font=c.QUESTION_TEXT_FONT,
        )
        self.question_title.grid(row=0, column=0, columnspan=4, pady=(50, 0))

        self.input_box_title = ct.CTkLabel(
            self, text="Enter an integer below", text_color="#2B2B2C"
        )
        self.input_box_title.grid(
            row=1, column=0, columnspan=4, sticky="S", pady=(50, 10)
        )

        self.input_box = ct.CTkEntry(self, text_font=c.MAIN_TEXT_FONT)
        self.input_box.grid(row=2, column=0, columnspan=4, pady=(0, 10))

        self.input_box_error = ct.CTkLabel(
            self,
            text="ERROR: Please enter a valid number!",
            text_color="#FF0000",
            text_font=c.MAIN_TEXT_FONT,
        )

        self.input_box_button = ct.CTkButton(
            self,
            text="SUBMIT",
            fg_color="#2B2B2C",
            hover_color="#001B4B",
            text_font=c.TITLE_TEXT_FONT_S15,
            command=lambda: [
                self.input_box_error.forget(),
                self.input_verify(self.input_box.get()),
            ],
        )
        self.input_box_button.grid(row=3, column=0, columnspan=4, pady=10)

    def input_verify(self, user_entry):
        try:
            if (1 <= float(user_entry) <= 40) and (
                float(user_entry) % 0.5 == 0
            ):
                self.input_box_error.grid_forget()
                StudentData.credits = user_entry
                self.master.replace_frame(ChoicePage)
            else:
                self.input_box_error.grid(row=4, column=0, columnspan=4)
        except ValueError:
            self.input_box_error.grid(row=4, column=0, columnspan=4)


class ChoicePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        raise NotImplementedError("ChoicePage is not implemented yet")

    # TODO: initialize 3 groups of buttons (g1 = 2 buttons, g2 = 3 buttons, g3 = 4 buttons).    # noqa: E501
    #       groups will be independently displayed depending on question number.          # noqa: E501
    #       use .config() to change the text and command of the buttons???


class StudentData:
    credits = 0
    points = 0


# MAIN PROGRAM #


if __name__ == "__main__":
    app = App()
    app.mainloop()
