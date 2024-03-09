#6번

a=int(input('연도를 입력 ==> '))
if a%4==0 and a%100!=0:
    print('윤년입니다.')
elif a%400==0:
    print('윤년입니다.')
else: print('평년입니다.')

#7번
import random
a=random.randint(0,100)
print('뽑힌 점수 : ',a)

if a>=90: print('장학생입니다.')
elif a>=60: print('합격입니다.')
else: print('불합격입니다.')

#8번
import turtle
import random

turtle.shape('turtle')
turtle.screensize(300,300)
turtle.setup(330,330)
turtle.pensize(5)
i=0

while True:
    angle= random.randint(0, 360)
    distance=random.randint(10, 100)
    turtle.right(angle)
    turtle.forward(distance)

    curx= turtle.xcor()
    cury= turtle.ycor()
    
    if (curx>=-150 and curx<=150) and (cury >= -150 and cury <= 150):
        turtle.pencolor('blue')
    else:
        turtle.goto(0,0)
        i+=1
        if  i==1:
            turtle.pencolor('green')
        elif  i==2:
            turtle.pencolor('orange')
        elif  i>=3:
            turtle.pencolor('red')
            
turtle.done()
