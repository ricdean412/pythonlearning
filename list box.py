# listbox  = a listing of selectable text items
# within its own container

def submit():
    print("You submitted your order of:")
    print(listbox.get(listbox.curselection()))
    print("Your order will be ready soon!")

def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())

from tkinter import *

window = Tk()

listbox = Listbox(window,
                  font=("Arial",30,"bold",),
                  bg="black",
                  width=15)
listbox.pack()

listbox.insert(1,"Pizza")
listbox.insert(2,"Soup")
listbox.insert(3,"Hamburger")
listbox.insert(4,"Sushi")
listbox.insert(5,"Fried Rice")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

addButton = Button(window,text="Add",command=add)
addButton.pack()

submitButton = Button(window,text="Submit",command=submit)
submitButton.pack()

deleteButton = Button(window,text="Delete",command=delete)
deleteButton.pack()

window.mainloop()