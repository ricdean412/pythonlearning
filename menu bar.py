from tkinter import *
from tkinter import filedialog

def openFile():
    print("File has been opened.")

def cut():
    print("You cut some text.")

def copy():
    print("You copied some text.")

def paste():
    print("You pasted some text.")

def saveFile():
    file = filedialog.asksaveasfile(initialdir="/Users/ricsmacbook/PycharmProjects/12HourPt3",
                                    defaultextension=".txt",
                                    filetypes=[
                                        ('Text File', '.txt'),
                                        ("HTML File", ".html"),
                                        ("All Files", "*.*")
                                    ])
    # if file is none:
    #     return
    filetext = str(text.get(1.0, END))
    # filetext = input("Enter some text, I guess...")
    file.write(filetext)
    print("File is successfully saved!")
    file.close()

def submit():
    print('You submitted your work.')

window = Tk()

openImage = PhotoImage(file="burger.png")
saveImage = PhotoImage(file="pizza.png")
exitImage = PhotoImage(file="hot.png")


menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="File",menu=fileMenu)  #drop down effect
fileMenu.add_command(label="Open",command=openFile,image=openImage,compound=LEFT)
fileMenu.add_command(label="Save",command=saveFile,image=saveImage,compound=LEFT)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit,image=exitImage,compound=LEFT)

editMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Undo Typing")
editMenu.add_command(label="Redo Typing")
editMenu.add_separator()
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)
editMenu.add_command(label="Cut",command=cut)

text = Text(window,
            font=("Arial",20,"bold"))
text.pack()

submitButton = Button(window,text="Submit",command=submit)
submitButton.pack()

window.mainloop()