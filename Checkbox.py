from tkinter import *

def display():
    if(x.get()==1):
        print("You agreed! :)")
    else:
        print("You disagreed! :(")

window = Tk()
window.geometry("1270x420")
photo = PhotoImage(file="utube.png")

x = IntVar() #or StringVar or BooleanVar or IntVar

check_button = Checkbutton(window,
                           text="I agree to something.",
                           font=("Arial",30,"bold"),
                           fg="#5cfcff",
                           bg="black",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           padx=20,
                           pady=10,
                           image=photo,
                           compound="left")

check_button.pack()


window.mainloop()
