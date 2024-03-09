#9번
import turtle
import random
outFile = None
inFile = None
inStr = ""
res = ""
inList = []
outFile = open("D:/FirstPython/turtle.txt", "w")
colorList = ['red', 'blue', 'gray', 'black', 'magenta', 'orange','green']

turtle.screensize(500,500)
turtle.shape('turtle')
turtle.penup()
turtle.speed(5)

for i in range(50) :
    color = random.choice(colorList)
    size = random.randint(1,4)
    x = random.randint(-250,250)
    y = random.randint(-250,250)
    angle = random.randint(0,360)
    
    res = color + ", " + str(size) + ", " + str(x) + ", " + str(y) + ", " + str(angle) + ", \n"
    outFile.writelines(res)
outFile.close()

inFile = open("D:/FirstPython/turtle.txt", "r", encoding="UTF-8")
inList = inFile.readlines()

for inStr in inList :
    turtle.stamp()
    turtle.fillcolor(inStr.split(", ")[0])
    turtle.pencolor(inStr.split(", ")[0])
    turtle.turtlesize(int(inStr.split(", ")[1]))
    turtle.goto(int(inStr.split(", ")[2]),int(inStr.split(", ")[3]))
    turtle.right(int(inStr.split(", ")[4]))
    
inFile.close()
turtle.done()
