'''
#9번
a=int(input('시작값 ==>'))
b=int(input('끝값 ==>'))
c=int(input('증가값 ==>'))

num=0
for i in range(a, b, c):
    num+=i
print(a,'에서', b,'까지', c,'씩 증가한 값의 합 : ', num)
'''
#10번
import turtle
turtle.shape('turtle')
import random
colors=['red', 'green', 'magenta', 'blue', 'black']

for i in range(0, 50):
    for j in range(0,500,10):
        turtle.color(random.choice(colors))
        turtle.forward(j)
        turtle.left(90)
    
    
