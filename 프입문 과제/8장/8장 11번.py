#11번
import random
import turtle

def writeKorean36(ch, radius, angle) :
    turtle.goto(0,0)
    color = random.choice(colorList)
    turtle.pencolor(color)
    turtle.forward(radius)
    turtle.right(angle)
    turtle.write(ch, font=("맑은고딕", 10, 'bold'))

colorList = ['red', 'blue', 'magenta', 'orange', 'green', 'gray']
koreanStr = """ 나랏말싸미 듕귁에 달아 문짜와로 서르 사맛디 아니할쌔 이런 젼차로 어린 백셩이 니르고
                져 홀 배 이셔도 마참내 제 뜨들 시러 펴디 못할 노미 하니라 내 이랄 위하야 어엿비 너겨 새로
                스믈여듧 짜랄 맹가노니 사람마다 해여 수비 니겨 날로 쑤메 뼌안킈 하고져 할 따라미니라 """

turtle.shape('turtle')
turtle.penup()
turtle.speed(5)

i = 0
radius = 100

for ch in koreanStr :
    
    if ch != " " :
        angle = 0
        i += 1
        angle += 10

        writeKorean36(ch, radius, angle)

        if i%37==0 :
            radius += 50
            
        if angle == 360 :
            angle = 0
        
    
turtle.done()