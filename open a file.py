from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="/Users/ricsmacbook/PycharmProjects/12HourPt3/forleif.txt",
                                          title="Open File okay?",
                                          filetypes= (("Text Files","*.txt"),
                                                      ("All Files","*.*")))

    # print(filepath)
    file = open(filepath,'r')
    print(file.read())
    file.close()


window = Tk()



button = Button(window,text="open",command=openFile)
button.pack()


window.mainloop()