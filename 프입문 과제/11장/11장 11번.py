import PIL
import random
from PIL import Image, ImageFilter, ImageEnhance, ImageOps

number=random.randint(1, 99)
if number < 10:
    number = '0' + str(number)
else:
    number = str(number)
    
filename = 'D:/firstpython/picture/picture'+number+'.jpg'
img = Image.open(filename)
img.show()

while True:
    al=int(input('1:좌우반전, 2:상하버전, 3:회전, 4:흑백, 5:엠보싱, 6:스케치, 7:경계선, 0:종료 ==>'))
    if al==1:
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
    if al==2:
        img = img.transpose(Image.FLIP_TOP_BOTTOM)       
    if al==3:
        img = img.rotate(45, expand=True)        
    if al==4:
        img = ImageOps.grayscale(img)       
    if al==5:
        img = img.filter(ImageFilter.EMBOSS)        
    if al==6:
        img = img.filter(ImageFilter.CONTOUR)
    if al==7:
        img = img.filter(ImageFilter.FIND_EDGES)
    if al==0:
        break

img.show()
