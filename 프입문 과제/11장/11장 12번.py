import pygame
import random
import sys

monitor = None
colorList = ['red','green','blue','black','magenta','orange','gray']
imageList = ['turtles','t0','t1','t2','t3','t4','t5','t6','t7','t8','t9']

pygame.init()
monitor=pygame.display.set_mode((500,700))
color=random.choice(colorList)
img = 'D:/firstpython/picture/'+random.choice(imageList)+'.png'
img = pygame.image.load(img)
tx, ty = 200, 300

while True:
    monitor.fill(color)
    monitor.blit(img, (tx,ty))
    pygame.display.update()
    
    for e in pygame.event.get():
        if e.type in [pygame.QUIT]:
            pygame.quit()
            sys.exit()
            
        if e.type in [pygame.KEYDOWN] : 
            if e.key == pygame.K_SPACE : 
                tx = random.randint(0,500)
                ty = random.randint(0,700)
                color=random.choice(colorList)
                img = 'D:/firstpython/picture/'+random.choice(imageList)+'.png'
                img = pygame.image.load(img)
            
