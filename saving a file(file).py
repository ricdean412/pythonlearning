from tkinter import *
from tkinter import filedialog

def savefile():
    file = filedialog.asksaveasfile(initialdir="/Users/ricsmacbook/PycharmProjects/12HourPt3",
                                    defaultextension=".txt",
                                    filetypes=[
                                        ('Text File','.txt'),
                                        ("HTML File",".html"),
                                        ("All Files","*.*")
                                    ])
    if file is none:
        return
    filetext = str(text.get (1.0,END))
    # filetext = input("Enter some text, I guess...")
    file.write(filetext)
    print("File is successfully saved!")
    file.close()

window = Tk()

button = Button(window,text='save',command=savefile)
button.pack()
text = Text(window,font=("Arial",20,"bold"))
text.pack()



window.mainloop()