from tkinter import *

# button = when you click it, then it does stuff


count = 0

def click():
    global count
    count+=1
    print(count)
    # print("You clicked the button.")

window = Tk()
window.geometry("1920x1080")
photo = PhotoImage(file="sikickz.png")

button = Button(window,
                text="click me!",
                command=click,
                font=("Comic Sans",30),
                fg="black",
                bg="black",
                activeforeground="black",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound='bottom')

button.pack()

window.mainloop()
