from tkinter import *
import time
WIDTH=500
HEIGHT=500
xVelocity=3
yVelocity=2
window=Tk()
canvas=Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()
photo_image=PhotoImage(file='w3lynx_200.png')
my_image=canvas.create_image(0,0,image=photo_image,anchor=NW)

background_photo=PhotoImage(file='tobecovrted1.png')
background=canvas.create_image(0,0,image=background_photo,anchor=NW)

image_width=photo_image.width()
image_height=photo_image.height()


while True:
    coordinates=canvas.coords(my_image)
    print(coordinates)
    if(coordinates[0]>WIDTH-image_width or coordinates[0]<0):
        xVelocity=-xVelocity
    if (coordinates[0] > (HEIGHT - image_height) or coordinates[0] < 0):
        yVelocity = -yVelocity
    canvas.move(my_image,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()