'''
Classes
'''
import pygame
from pygame.locals import *

class 场景(object):
    '场景模板类'
    def __init__(self):
        pass
    def 主循环(self):
        pass
    def 退场(self):
        pass

class 对象(object):
    def __init__(self,item,screen):
        self.item = item.get_rect()
        self.x = x
        self.y = y
        self.width = item.get_width()
        self.height = item.get_height()
        self.screen = screen
    def display(self):
        self.screen.blit(self.item,(self.x,self.y))
    
        

        
