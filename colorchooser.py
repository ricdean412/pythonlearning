from tkinter import *
from tkinter import colorchooser #this is a submodule

def click():
    # color = colorchooser.askcolor()
    # print(color)
    # colorHex = color[1]
    # print(colorHex)
    # window.config(bg=colorHex) #change bg color

    window.config(bg=colorchooser.askcolor()[1])

window = Tk()
window.geometry("420x420")

button = Button(text="Click Me",command=click)
button.pack()
window.mainloop()

