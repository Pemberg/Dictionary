import tkinter as tk
from tkinter import Button as but, Entry, Label, OptionMenu
import pandas as pd
import random
import menu


class Vocabulary:
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
        self.option_menu.place(x=340, y=200, anchor="center")


        self.button_load_data = but(window, text="Load Data", font=("Arial", 15), command=self.load_data)
        self.button_load_data.place(x=460, y=200, anchor="center")

        self.label_word = Label(window, text="", font=("Arial", 20))
        self.label_word.place(x=400, y=250, anchor="center")

        self.button_next_word = but(window, text="Next Word", font=("Arial", 15), command=self.next_word)
        self.button_next_word.place(x=400, y=300, anchor="center")

        self.button_check = but(window, text="Check", font=("Arial", 15), command=self.check_translation)
        self.button_check.place(x=400, y=400, anchor="center")

        self.button_return = but(window, text="🔙", font=("Arial", 15), height=1, width=2, bg="#008000", command=lambda: [self.delete_vocabulary(), menu.Menu.open_menu(window, canvas)])
        self.button_return.place(x=40, y=40, anchor="center")

        self.button_exit = but(window, text="❌", font=("Arial", 15), height=1, width=2, bg="#FF0000", command=self.close_vocabulary)
        self.button_exit.place(x=760, y=40, anchor="center")

        self.entry_translation = Entry(window, font=("Arial", 12))
        self.entry_translation.place(x=350, y=350)

        self.label_translation = Label(window, text="Enter translation:", font=("Arial", 12))
        self.label_translation.place(x=200, y=350)

        self.result_label = Label(window, text="", font=("Arial", 12))

    def load_sheet_names(self):
        file_path = "Data.xlsx"
        try:
            xls = pd.ExcelFile(file_path)
            self.sheet_names = xls.sheet_names
        except Exception as e:
            print("Error occurred while loading sheet names:", e)

    def load_data(self):
        sheet_name = self.selected_sheet.get()
        file_path = "Data.xlsx"
        try:
            if sheet_name:
                self.data = pd.read_excel(file_path, sheet_name).values.tolist()
                self.shuffle_data()
                self.show_word()
                if hasattr(self, 'result_label'):
                    self.result_label.place_forget()
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
            if hasattr(self, 'result_label'):
                self.result_label.place_forget()
        else:
            self.label_word.config(text="No more words")

    def check_translation(self):
        if self.current_index < len(self.data):
            entered_translation = self.entry_translation.get().strip().lower()
            english_word = self.data[self.current_index][0].lower()
            polish_word = self.data[self.current_index][1].lower()
            if self.show_english:
                actual_translation = polish_word
            else:
                actual_translation = english_word
            if entered_translation == actual_translation:
                result = "Correct!"
            else:
                result = "Incorrect!"
            if hasattr(self, 'result_label'):
                self.result_label.config(text=result)
                self.result_label.place(x=400, y=450, anchor="center")
            else:
                self.result_label = Label(self.window, text=result, font=("Arial", 12))
                self.result_label.place(x=400, y=450, anchor="center")
        else:
            self.label_word.config(text="No more words")

    @staticmethod
    def open_vocabulary(window, canvas):
        Vocabulary(window, canvas)

    def close_vocabulary(self):
        self.window.destroy()

    def delete_vocabulary(self):
        self.canvas.delete("all")
        self.button_exit.destroy()
        self.button_return.destroy()
        self.label_translation.destroy()
        self.button_check.destroy()
        self.button_load_data.destroy()
        self.button_next_word.destroy()
        self.label_word.destroy()
        self.entry_translation.destroy()
        self.result_label.destroy()
        self.option_menu.destroy()
