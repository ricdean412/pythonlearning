# frame = a rectangle container to group and hold widgets

from tkinter import *

window = Tk()

frame = Frame(window,bg="pink",relief=SUNKEN)
frame.place(x=0,y=0)

Button(frame,text="W",font=("Consoloas",25),width=3).pack(side=TOP)
Button(frame,text="A",font=("Consoloas",25),width=3).pack(side=LEFT)
Button(frame,text="S",font=("Consoloas",25),width=3).pack(side=LEFT)
Button(frame,text="D",font=("Consoloas",25),width=3).pack(side=LEFT)

window.mainloop()