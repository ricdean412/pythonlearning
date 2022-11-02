from tkinter import *

def submit():
    print("The temperature is "+str(scale.get())+" degrees C")

window = Tk()
hotimage = PhotoImage(file="hot.png")
hotLabel = Label(image=hotimage)
hotLabel.pack()


scale = Scale(window,
              from_=100,to=0,
              length=500,
              orient=VERTICAL, #orientation of scale
              font=("Arial",30,"bold"),
              tickinterval=10, # adds numerical indicators
              showvalue = 1,
              resolution=5,
              troughcolor="#5cfcff",
              fg="#FF1C00",
              bg="black"

              )

scale.set(((scale['from']-scale['to'])/2)+scale['to'])
scale.pack()


coldimage = PhotoImage(file="pizza.png")
coldLabel = Label(image=coldimage)
coldLabel.pack()

button = Button(window,text="Submit",command=submit)
button.pack()

window.mainloop()
