from tkinter import *
import time

WIDTH = 500
HEIGHT = 500
xVelocity = 3
yVelocity = 2

window = Tk()

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack(expand=TRUE)

background = PhotoImage(file="/Users/ricsmacbook/Desktop/Misc/Wallpapers/piece2.png")
bgphoto = canvas.create_image(0,0,image=background,anchor=NW)

image2 = PhotoImage(file="utube.png")
myimage = canvas.create_image(0,0,image=image2,anchor=NW)

image_width = image2.width()
image_height = image2.height()
while True:
    coordinates = canvas.coords(myimage)
    print(coordinates)
    if(coordinates[0]>=WIDTH-image_width or coordinates[0]<0):
        xVelocity = -xVelocity
    if (coordinates[0] >=HEIGHT- image_height or coordinates[0]<0):
        yVelocity = -yVelocity
    canvas.move(myimage,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()