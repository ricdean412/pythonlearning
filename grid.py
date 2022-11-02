from tkinter import *

#grid() = geometry manager that organizes widgets in a table-like structure in a parent

# def submit():
    # sub = Entry.get(1.0,END)
    # print("Your information is safe:" +str(sub))

window = Tk()

titleLabel = Label(window,text="Enter your information:",font=("Arial",15,"bold")).grid(row=0,column=0,columnspan=2)

firstNameLabel = Label(window,text="First Name:",bg="red").grid(row=1,column=0)
firstNameEntry = Entry(window,fg="white").grid(row=1,column=1)

lastNameLabel = Label(window,text="Last Name:",bg="blue").grid(row=2,column=0)
lastNameEntry = Entry(window,fg="white").grid(row=2,column=1)

emailLabel = Label(window,text="Email:",bg="green").grid(row=3,column=0)
emailEntry = Entry(window,fg="white").grid(row=3,column=1)

submitButton = Button(window,text="Submit").grid(row=4,column=1)

window.mainloop()