from tkinter import *
import random

def press(e):
    global start_x, start_y
    start_x, start_y = e.x, e.y

def release(e):
    global end_x, end_y
    end_x, end_y = e.x, e.y

    canvas.create_rectangle(start_x, start_y, end_x, end_y, 
                            outline=random.choice(colorList), width=5)

def change_color(e):
    global colorList
    colorList = ['red', 'green', 'yellow', 'purple', 'black']

root = Tk()

canvas = Canvas(root, height=500, width=500)
canvas.pack()

colorList = ['red', 'green', 'yellow', 'purple', 'black']

canvas.bind('<Button-1>', press)
canvas.bind('<ButtonRelease-1>', release)
canvas.bind('<Button-3>', change_color)

root.mainloop()
