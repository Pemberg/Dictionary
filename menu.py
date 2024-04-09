from tkinter import Button as but
from tkinter.messagebox import showinfo
import learning
import vocabulary
import add


class Menu:
    def __init__(self, window, canvas):
        self.window = window
        self.canvas = canvas

        buttonLearning = but(window, text="Learning", font=("Arial", 25), height=4, width=9, bg="#778899", command=lambda: [Menu.delete_menu(canvas), learning.Learning.open_learning(window, canvas)])
        buttonVocabulary = but(window, text="Vocabulary", font=("Arial", 25), height=4, width=9, bg="#696969", command=lambda: [Menu.delete_menu(canvas), vocabulary.Vocabulary.open_vocabulary(window, canvas)])
        buttonAdd = but(window, text="Add a word", font=("Arial", 25), height=4, width=9, bg="#C0C0C0", command=lambda: [Menu.delete_menu(canvas), add.Add.open_add(window, canvas)])
        buttonInfo = but(window, text='ℹ', font=("Arial", 15), height=1, width=2, bg="#00FFFF", command=lambda: self.button_info(self))
        buttonExit = but(window, text="❌", font=("Arial", 15), height=1, width=2, bg="#FF0000", command=lambda: self.close_menu())

        canvas.create_window(400, 300, anchor="center", window=buttonLearning)
        canvas.create_window(600, 300, anchor="center", window=buttonVocabulary)
        canvas.create_window(200, 300, anchor="center", window=buttonAdd)
        canvas.create_window(40, 40, anchor="center", window=buttonInfo)
        canvas.create_window(760, 40, anchor="center", window=buttonExit)



    def button_info(self):
        showinfo(title='Information', message='This is a program that allows you to learn words using flashcards. You can also check your spelling or add new words.')

    def delete_menu(canvas):
        canvas.delete("all")

    def close_menu(window):
        window.destroy()

    @staticmethod
    def open_menu(window, canvas):
        Menu(window, canvas)

    def window_size(window, window_width, window_height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))

        window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
