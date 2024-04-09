import tkinter as tk
from tkinter import Button, Label, OptionMenu
import pandas as pd
import random
import menu


class Learning:
    def __init__(self, window, canvas):
        self.window = window
        self.canvas = canvas
        self.data = []
        self.current_index = 0
        self.show_english = False
        self.sheet_names = []

        self.load_sheet_names()
        self.selected_sheet = tk.StringVar(window)
        self.selected_sheet.set(self.sheet_names[0]) if self.sheet_names else None
        self.option_menu = OptionMenu(window, self.selected_sheet, *self.sheet_names)
        self.option_menu.config(font=("Arial", 12))
        self.option_menu.place(x=340, y=220, anchor="center")

        self.label_word = Label(window, text="", font=("Arial", 20))
        self.label_word.place(x=400, y=300, anchor="center")

        self.button_load_data = Button(window, text="Load Data", font=("Arial", 15), command=self.load_data)
        self.button_load_data.place(x=460, y=220, anchor="center")

        self.button_show_translation = Button(window, text="Translation", font=("Arial", 15), command=self.toggle_translation)
        self.button_show_translation.place(x=400, y=380, anchor="center")

        self.button_next_word = Button(window, text="Next Word", font=("Arial", 15), command=self.next_word)
        self.button_next_word.place(x=550, y=380, anchor="center")

        self.button_previous_word = Button(window, text="Previous Word", font=("Arial", 15), command=self.previous_word)
        self.button_previous_word.place(x=250, y=380, anchor="center")

        self.button_return = Button(window, text="🔙", font=("Arial", 15), height=1, width=2, bg="#008000", command=lambda: [self.delete_learning(), menu.Menu.open_menu(window, canvas)])
        self.button_return.place(x=40, y=40, anchor="center")

        self.button_exit = Button(window, text="❌", font=("Arial", 15), height=1, width=2, bg="#FF0000", command=lambda: self.close_learning())
        self.button_exit.place(x=760, y=40, anchor="center")

    def load_sheet_names(self):
        file_path = "Data.xlsx"
        try:
            xls = pd.ExcelFile(file_path)
            self.sheet_names = xls.sheet_names
        except Exception as e:
            print("Error occurred while loading sheet names:", e)

    def load_data(self):
        if self.sheet_names:
            sheet_name = self.selected_sheet.get()
            file_path = "Data.xlsx"
            try:
                if sheet_name:
                    self.data = pd.read_excel(file_path, sheet_name).values.tolist()
                    self.shuffle_data()
                    self.show_word()
            except Exception as e:
                print("Error occurred while loading data:", e)

    def shuffle_data(self):
        random.shuffle(self.data)

    def show_word(self):
        if self.current_index < len(self.data):
            if self.show_english:
                self.label_word.config(text=self.data[self.current_index][0])
            else:
                self.label_word.config(text=self.data[self.current_index][1])
        else:
            self.label_word.config(text="No more words")

    def toggle_translation(self):
        self.show_english = not self.show_english
        self.show_word()

    def next_word(self):
        if self.current_index < len(self.data):
            self.current_index += 1
            self.show_english = False
            self.show_word()
        else:
            self.label_word.config(text="No more words")

    def previous_word(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.show_english = False
            self.show_word()

    @staticmethod
    def open_learning(window, canvas):
        Learning(window, canvas)

    def close_learning(self):
        self.window.destroy()

    def delete_learning(self):
        self.canvas.delete("all")
        self.label_word.destroy()
        if hasattr(self, "sheet_menu"):
            self.sheet_menu.destroy()
        if hasattr(self, "button_load_data"):
            self.button_load_data.destroy()
        self.button_show_translation.destroy()
        self.button_next_word.destroy()
        self.button_previous_word.destroy()
        self.button_exit.destroy()
        self.button_return.destroy()
        self.option_menu.destroy()
