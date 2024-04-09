import tkinter as tk
from tkinter import Button as but, Entry, OptionMenu
import pandas as pd
import menu


class Add:
    def __init__(self, window, canvas):
        self.window = window
        self.canvas = canvas
        self.sheet_names = []

        self.button_return = but(window, text="🔙", font=("Arial", 15), height=1, width=2, bg="#008000",
                                 command=lambda: [self.delete_add(), menu.Menu.open_menu(window, canvas)])
        self.button_return.place(x=40, y=40, anchor="center")

        self.button_exit = but(window, text="❌", font=("Arial", 15), height=1, width=2, bg="#FF0000",
                               command=self.close_add)
        self.button_exit.place(x=760, y=40, anchor="center")

        self.label_english_word = tk.Label(window, text="English word:", font=("Arial", 12))
        self.label_english_word.place(x=200, y=200)

        self.entry_english_word = Entry(window, font=("Arial", 12))
        self.entry_english_word.place(x=350, y=200)

        self.label_polish_word = tk.Label(window, text="Polish translation:", font=("Arial", 12))
        self.label_polish_word.place(x=200, y=250)

        self.entry_polish_word = Entry(window, font=("Arial", 12))
        self.entry_polish_word.place(x=350, y=250)

        self.label_sheet = tk.Label(window, text="Select sheet:", font=("Arial", 12))
        self.label_sheet.place(x=200, y=300)

        self.load_sheet_names()
        self.selected_sheet = tk.StringVar(window)
        self.selected_sheet.set(self.sheet_names[0]) if self.sheet_names else None
        self.option_menu = OptionMenu(window, self.selected_sheet, *self.sheet_names)
        self.option_menu.config(font=("Arial", 12))
        self.option_menu.place(x=350, y=300)

        self.button_add_word = but(window, text="Add Word", font=("Arial", 12), bg="#FFA500", command=self.add_word_to_excel)
        self.button_add_word.place(x=350, y=350)

    def load_sheet_names(self):
        file_path = "Data.xlsx"
        try:
            xls = pd.ExcelFile(file_path)
            self.sheet_names = xls.sheet_names
        except Exception as e:
            print("Error occurred while loading sheet names:", e)

    def add_word_to_excel(self):
        file_path = "Data.xlsx"
        english_word = self.entry_english_word.get()
        polish_word = self.entry_polish_word.get()
        selected_sheet = self.selected_sheet.get()
        if not english_word or not polish_word:
            print("Fields cannot be empty!")
            return
        try:
            if pd.ExcelFile(file_path).sheet_names:
                df = pd.read_excel(file_path, sheet_name=selected_sheet, header=None)
            else:
                df = pd.DataFrame(columns=[0, 1])
            new_data = pd.DataFrame([[english_word, polish_word]])
            df = pd.concat([df, new_data], ignore_index=True)
            with pd.ExcelWriter(file_path, mode='a', if_sheet_exists='replace') as writer:
                df.to_excel(writer, sheet_name=selected_sheet, index=False, header=False)
            print("Word added to {} sheet in Excel file.".format(selected_sheet))
        except Exception as e:
            print("An error occurred while adding word to Excel:", e)

    @staticmethod
    def open_add(window, canvas):
        Add(window, canvas)

    def close_add(self):
        self.window.destroy()

    def delete_add(self):
        self.canvas.delete("all")
        self.button_return.destroy()
        self.button_exit.destroy()
        self.button_add_word.destroy()
        self.label_sheet.destroy()
        self.label_polish_word.destroy()
        self.label_english_word.destroy()
        self.entry_english_word.destroy()
        self.entry_polish_word.destroy()
        self.option_menu.destroy()
