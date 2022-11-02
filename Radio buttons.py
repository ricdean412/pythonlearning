#radio buttons - like checkboxes, but you can only select
# one from a group.

from tkinter import *

food = ["pizza","hamburger","hotdog"]

def order():
    if(x.get()==0):
        print("You ordered pizza!")
    elif(x.get()==1):
        print("You ordered a burger!")
    elif(x.get()==2):
        print("You ordered a hotdog!")
    else:
        print("Are you not hungry?")

window = Tk()

pizzaimage = PhotoImage(file="pizza.png")
hamimage = PhotoImage(file="burger.png")
hotimage = PhotoImage(file="hot.png")
foodImages = [pizzaimage,hamimage,hotimage]


x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index], #adds text to radio buttons
                              variable=x,   # groups r.bs together if they share the same variable
                              value=index,      #assigns each radiob a diff value.
                              padx=25,      #adds padding on x axis
                              font=("Arial",30,"bold"),
                              image= foodImages[index],   # adds image to radiobutton
                              compound="left",
                              indicatoron=0,    ##eliminate circle = indicators
                              width=375,
                              command=order)



    radiobutton.pack(anchor=W)
window.mainloop()