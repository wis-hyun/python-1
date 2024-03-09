#가위바위 보 게임하기
'''
import random
me=input('사람: 가위/바위/보 ==> ')
computer=random.choice(['가위','바위','보'])
print('컴퓨터 : 가위/바위/보==> %s' %computer)
print('컴퓨터 : 가위/바위/보 ==> {0}' .format(computer))

if  me =='가위':
    if computer=='가위': print('비겼습니다.')
    elif computer=='바위': print('졌습니다.')
    else: print('이겼습니다.')

elif me=='바위':
    if computer=='가위': print('이겼습니다.')
    elif computer=='바위': print('비겼습니다.')
    else: print('졌습니다.')
    
elif me=='보':
    if computer=='가위': print('졌습니다.')
    elif computer=='바위': print('이겼습니다.')
    else: print('비겼습니다.')
'''
#거북이
import turtle
import random

turtle.shape('turtle')
turtle.pensize(5)
turtle.pencolor('blue')
turtle.screensize(300,300)
turtle.setup(330,330)

while True:
    angle=random.randint(0,360)
    distance=random.randint(10,100)
    turtle.right(angle)
    turtle.forward(distance)
    curX=  turtle.xcor()
    curY= turtle.ycor()

    if (curX >= -150 and curY <=150) and (curY >= -150 and curY <= 150):
        print('good boy')
    else: turtle.goto(0,0)

turtle.done()
