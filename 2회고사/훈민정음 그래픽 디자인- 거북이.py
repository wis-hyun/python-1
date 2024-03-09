import turtle
import random

def getXYS():
    x,y,size= 0, 0, 0
    x= random.randint(-250, 250)
    y=random.randint(-250, 250)
    size=random.randint(10, 50)
    return x, y, size

##전역변수 선언 부분
koreanStr = ''' a b c d e f g h i j k
'''
colorList = ['red','green','blue','black','magenta','orange','gray']
tX,tY, txtSize = 0, 0, 0

##메인코드 부분
turtle.shape("turtle")
turtle.setup(550, 550)
turtle.screensize(500, 500)
turtle.penup()
turtle.speed(5)

for ch in koreanStr:
    tX, tY, txtSize = getXYS()
    color = random.choice(colorList)
    turtle.goto(tX,tY)
    turtle.pencolor(color)
    turtle.write(ch, font=('맑은고딕', txtSize, 'bold'))

turtle.done()
