from tkinter import *

# label = an area widget that holds text and/or an image within a window

window = Tk()
window.geometry("1920x1080")


# photo = PhotoImage(file='sikickz.png')

label = Label(window,
              text="Bro, do you even code",
              font=("Arial",40,"bold"),
              fg="#5cfcff",
              bg='black',
              relief=RAISED,  #SUNKEN
              bd=10,
              padx=20,
              pady=0,
              compound='top')


label.pack()   #center
# label.place(x=0,y=0) #top left
# label.place(x=100,y=100) # pixel based


window.mainloop()