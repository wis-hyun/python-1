#11번

a=int(input('숫자 1 ==>'))
b=int(input('숫자 2 ==>'))

print('a / b =', a/b)
print('a%b =', a%b)
print('a//b =', a//b)
print('a**b =', a**b)

#12번
import turtle

a=input('거북이 모양(turtle, circle, square, rectangle) ==> ')
b=int(input('거북이 선 두께 ==> '))
c=input('거북이 색상(red, blue, green, yellow, magenta) ==> ')

turtle.shape(a)
turtle.pensize(b)
turtle.pencolor(c)

while True:
    angle=int(input('거북이의 회전 각도 ==> '))
    distance=int(input('거북이의 이동 거리 ==> '))

    turtle.right(angle)
    turtle.forward(distance)



