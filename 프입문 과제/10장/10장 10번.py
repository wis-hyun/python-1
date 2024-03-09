#10번
import turtle
import random

class Rabbit:

    myTurtle = None

    def __init__(self, shape, size, angle, color, x, y):
        self.myTurtle = turtle.Turtle()
        self.myTurtle.shape(shape)
        self.myTurtle.shapesize(size)
        self.myTurtle.color(color)
        self.myTurtle.goto(x, y)
        self.myTurtle.pendown()
        self.myTurtle.setheading(angle)

colorList =  ['red', 'green','blue', 'gray', 'black', 'magenta', 'orange']
shapeList = ['turtle','triangle','circle','square','arrow']
turtle.setup(550, 550)
turtle.screensize(500,500)

for _ in range(20):
    shape = random.choice(shapeList)
    size = random.randint(1,4)
    angle = random.randint(0,360)
    color = random.choice(colorList)
    x=random.randint(-250,250)
    y=random.randint(-250,250)
    myRab = Rabbit(shape, size, angle, color, x, y)

turtle.done()
