from math import cos, sin, radians
from tkinter import *

SIZE=600
R=200
DOT_SIZE = 5
SPEED = 1
x0 = SIZE / 2
y0 = SIZE / 2
REVERSE = False

root = Tk()
canvas = Canvas(root, width=SIZE, height=SIZE, bg="white")
canvas.pack()
ball = canvas.create_oval(
    SIZE / 2 - R,
    SIZE / 2 - R,
    SIZE / 2 + R,
    SIZE / 2 + R,
    width = 0,
    fill = '#FFCC66'
    )
root.update()

t = 0
if REVERSE:
    func = [sin, cos]
else:
    func = [cos, sin]  

def x1_y1():
    global R, DOT_SIZE, x0, y0, t, func
    
    x1 = x0 + (R + DOT_SIZE) * func[0](t)
    y1 = y0 + (R + DOT_SIZE) * func[1](t)  
    return x1, y1

x1, y1 = x1_y1()

my_point = canvas.create_oval(
    x1 - DOT_SIZE,
    y1 - DOT_SIZE,
    x1 + DOT_SIZE,
    y1 + DOT_SIZE,
    width = 0,
    fill = "red")

def motion():
    global SPEED, my_point, x1, y1, t
    t += radians(SPEED*6/100)
    x2, y2 = x1_y1()
    canvas.move(my_point, x2 - x1, y2 - y1)
    x1, y1 = x2, y2
    root.after(10, motion)
 
motion()
 
root.mainloop()