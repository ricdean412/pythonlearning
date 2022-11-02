from tkinter import *

def create_window():
    # new_window = Toplevel()     # New Window 'on top' of other windows
                                  # ,linked to a 'bottom window.'
                                  # Tk() = new independent window
    new_window = Tk()
    old_window.destroy()
old_window = Tk()
Button(old_window,text="Create New Window",command=create_window).pack()
old_window.mainloop()