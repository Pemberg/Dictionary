from tkinter import Tk as tk, Canvas as can
import menu


window = tk()

window.title('Dictionary')

window_width = 800
window_height = 600

menu.Menu.window_size(window, window_width, window_height)

canvas = can(window, width=800, height=600, bg="lightblue")
canvas.pack(fill="both", expand=True)

menu.Menu(window, canvas)

window.mainloop()
