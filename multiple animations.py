from tkinter import *
from Ball import *
import time

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,2,2,"white")
tennis_ball = Ball(canvas,0,0,50,4,3,"green")
basket_ball = Ball(canvas,0,0,125,8,7,"orange")
base_ball = Ball(canvas,0,0,50,10,9,"red")
leif_ball = Ball(canvas,0,0,200,4,5,"blue")

while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    base_ball.move()
    leif_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()