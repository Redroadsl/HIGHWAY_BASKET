#Draw A circle
from ctypes import windll
windll.user32.SetProcessDPIAware()

import pygame
from pygame.locals import *
from random import randint

pygame.init()
screen=pygame.display.set_mode((1920,1080))
clock=pygame.time.Clock()

screen.fill('black')
for x in range(100):
    X=randint(0,1920)
    Y=randint(0,1080)
    R=randint(1,3)
    pygame.draw.circle(screen,'white',(X,Y),R)
    pygame.display.flip()
##    screen.scroll(0,x)
    clock.tick(60)
pygame.image.save(screen,'BIG.png')
