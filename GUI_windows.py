# Graphical User Interface

from tkinter import *

# windows = serves as a container to hold or contain these widgets
# widgets = GUI elements: buttons, textboxes, labels, images

window = Tk() #instantiate an instance of a window
window.geometry("420x420")
window.title("My First GUI Program")

icon = PhotoImage(file='Test.png')
window.iconphoto(True,icon)
window.config(background="#5cfcff")


window.mainloop() #place window on cpu screen, listen for events


