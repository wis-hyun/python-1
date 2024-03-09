import turtle

turtle.shape('turtle')
turtle.penup()

while True:
    x=int(input('x='))
    y=int(input('y='))
    text=input('글자=')

    turtle.goto(x,y)
    turtle.write(text, font=('Arial',30))

turtle.done()
