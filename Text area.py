# text widget = functions like a text area, enter multiple
# lines of text

def submit():
    input = text.get("1.0",END)
    print("You're idea is submitting as we speak: \n")
    print(input)
    print("You submitted your idea!")

from tkinter import *

window = Tk()

text = Text(window,
            font=("Ink Free",20,"bold",),
            bg="lightyellow",
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg="purple")
text.pack()

submitButton = Button(window,text="Submit",command=submit)
submitButton.pack()

window.mainloop()