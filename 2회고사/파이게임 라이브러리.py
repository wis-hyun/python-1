import pygame
import random
import sys

monitor = None
colorList = ['red','green','blue','black','magenta','orange','gray']

pygame.init()
monitor = pygame.display.set_mode((500,700))
color = random.choice(colorList)
turtle=pygame.image.load('d:/firstpython/turtles.png')
tx, ty = 200, 300

while True:
    monitor.fill(color)
    monitor.blit(turtle, (tx, ty))
    pygame.display.update() 

    for e in pygame.event.get():
        if e.type in [pygame.QUIT]:
            pygame.quit()
            sys.exit()
        if e.type in [pygame.KEYDOWN]:
            if e.key==pygame.K_LEFT: 
                tx -= 50
            elif e.key == pygame.K_RIGHT : 
                tx +=50
            elif e.key == pygame.K_UP : 
                ty -=50
            elif e.key == pygame.K_DOWN : 
                ty +=50