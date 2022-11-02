from tkinter import *

def doSomething(event):
    print("Mouse Coordinates: " + str(event.x)+" , "+str(event.y))

window = Tk()

# window.bind(event,function)
# window.bind("<Button-1>",doSomething) #left click
# window.bind("<Button-3>",doSomething) #right click
# window.bind("<Button-2>",doSomething) #scroll wheel click
# window.bind("<ButtonRelease>",doSomething)
# window.bind("<Enter>",doSomething) #Enter the window
# window.bind("<Leave>",doSomething) #leave the window
window.bind("<Motion>",doSomething)
window.mainloop()