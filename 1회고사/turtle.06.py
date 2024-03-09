#거북이 무늬의 벽지 만들기
import turtle
import random
turtle.shape('turtle')
colors=['red','green','magenta','blue','black']
turtle.penup()
turtle.screensize(300,300)
turtle.setup(350,350)

for i in range(7):
    x= i*50-150
    for j in range(7):
        y=j*50-150
        turtle.goto(x,y)
        turtle.color(random.choice(colors))
        turtle.stamp()

turtle.done()
