'''
#11번
list=[]
import random
for i in range(100):
    a=random.randint(1,6)
    list.append(a)
    
num=0
for j in list:
    num+=j
b=(num)/len(list)
print(b)
'''
#12번
import turtle
import random
turtleList=[]
colorList=['red','green','blue','black','magenta','orange','gray']
turtle.setup(550,550)
turtle.screensize(500,500)

for i in range(0,100):
    color=random.choice(colorList)
    x=random.randint(-250,250)
    y=random.randint(-250,250)
    myTurtle=turtle.Turtle('turtle')
    tup=(myTurtle, color, x, y)
    turtleList.append(tup)

for tup in turtleList:
    myTurtle=tup[0]
    myTurtle.pencolor( tup[1] )
    myTurtle.goto(tup[2], tup[3])
    myTurtle.stamp()

turtle.done()
