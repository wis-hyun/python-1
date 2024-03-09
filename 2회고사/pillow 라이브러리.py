import PIL
import random

from PIL import Image, ImageFilter, ImageEnhance, ImageOps
number = random.randint(1,99)
if number<10:
    number = '0' + str(number)
else : 
    number = str(number)

filename = 'D:/firstpython/picture'+number+'.jpg'

img = Image.open(filename)
img.show()
img = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
img.show()
img = img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
img.show()
img = img.rotate(45, expand=True)
img.show()
img = img.filter(ImageFilter.CONTOUR)
img.show()