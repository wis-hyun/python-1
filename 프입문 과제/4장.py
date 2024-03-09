#11번
ss = "파이썬은 재밌어요~~ Python is Funny. ^^"

print('원본 문자열 : ', ss)
print('모두 대문자로 : ', ss.upper())
print('모두 소문자로 : ', ss.lower())
print('Python 글자의 시작 위치 : ',ss.find('Python'))

#12번
import turtle
turtle.shape('turtle')

while True:
    a=input('펜 색상(red,blue, green, yellow, magenta) ==> ')
    b=int(input('X위치 ==>'))
    c=int(input('Y위치 ==>'))
    d1=input('쓰고 싶은 글자 (최대 4글자) ==> ')
    d=d1.upper()
    
    turtle.pencolor(a)
    turtle.goto(b,c)
    turtle.write(d[3]+d[2]+d[1]+d[0], font=('Arial',30))
    
turtle.done()
