'''
# Highway Basket #
Startup: 2024 04 19
玩法介绍：
海伟坐上火箭，篮球在太空飘荡，海伟躲避篮球前进
直到里程达到10000km后，进入文常答题环节。
答对获得10篮球，答错无
获得篮球后，海伟继续坐火箭，太空中漂浮着篮筐，海伟投篮
投中加一点充能（最多20点）
充能达到20后进入下一等级（总共3）
每增加一等级，篮球\球筐出现更频繁，速度更快。
海伟火箭被篮球击中，后退
退无可退，失败。
TODO:

'''
# HIGHWAY BASKETBALL
_W=1920
_H=1080
FPS=60

import sys,time,math,random,ctypes,os
ctypes.windll.user32.SetProcessDPIAware()
os.environ['PYGAME_HIDE_SUPPORT_PROMPT']='1'
import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption('HIGHWAY BASKET | HIGHWAY BASKET | HIGHWAY BASKET | HIGHWAY BASKET | HIGHWAY BASKET | HIGHWAY BASKET | HIGHWAY BASKET |')
screen=pygame.display.set_mode((_W,_H),RESIZABLE|DOUBLEBUF|HWSURFACE|FULLSCREEN)#|SCALED)#|FULLSCREEN)
pygame.key.set_repeat(10,10)

imgPath='./HIWAY-ASSETS/IMAGE/'
头图=pygame.image.load(imgPath+'HighWAY!.png').convert_alpha()
标题=pygame.image.load(imgPath+'TITLE.png').convert_alpha()
海伟L=pygame.image.load('High-Way.PNG').convert_alpha()
海伟R=pygame.image.load('High-Way2.PNG').convert_alpha()
球=pygame.image.load(imgPath+'BALL.png').convert_alpha()

class BALL(object):
    def __init__(self,screen):
        self.x=random.randint(0,_W)
        self.y=_H
        self.scr=screen
        self.direction=random.choice((-1,1))
        self.rotation=0
        self.rotateDirection=random.choice((-1,1))
    def display(self):
        self.scr.blit(pygame.transform.rotate(球,self.rotation*self.rotateDirection),(self.x, self.y))
        if self.y % 100 == 0:
            self.direction=random.choice((-1,1))
        if self.y<=-100:
            self.x=random.randint(0,_W)
            self.y=_H
        else:
            self.rotation+=1
            self.y-=2
            self.x+= (_H - self.y)/200 * self.direction
    def quit(self):
        'Animation for quitting'
        pass

class Enemy(BALL):
    def __init__(self,screen):
        super().__init__()
        self.scr=screen
        self.x=random.randint(0,_W)
        self.y=0
        self.rect=pygame.Rect(0,0,0,0)
        self.speedY=1
        self.speedX=random.randint(-300,300)/100
    def display(self):
        self.rect = self.scr.blit(球,(self.x, self.y))
        self.y+=self.speedY
        self.x=abs(self.x+self.speedX)
blist=[BALL(screen)]
clock=pygame.time.Clock()
RUN=1
count=0

def 最大分辨率():
    return pygame.display.get_desktop_sizes()
def 重置分辨率():
    global _W,_H
    _W,_H=pygame.display.get_window_size()[0],pygame.display.get_window_size()[1]


step=1

s2y=0
s2oy=0.05*_H+math.sin(time.time())*20
h2ox,h2oy=(_W-337)//2+math.sin(time.time()*0.5)*100, 0.39*_H+math.sin(time.time())*40
h2x,h2y=0,0
h2r=1
h2rx=h2ry=0
unfinish1=1

class Finger(object):
    def __init__(self,state=False,id=0,x=0,y=0):
        self.state=state
        self.id=id
        self.x=x
        self.y=y
fingerR=Finger(id=0)
fingerL=Finger(id=1)
HWy=0
HWx=0
HWside=True

while step:
    while step == 1:
        clock.tick(FPS)
        pygame.display.flip()
        screen.fill('black')
        if count<=1200:
            if count%60==0:
                blist.append(BALL(screen))
            count+=1
        for b in blist:
            b.display()
        screen.blit(标题,((_W-1600)//2,0.05*_H+math.sin(time.time())*20))
        screen.blit(头图,((_W-337)//2+math.sin(time.time()*0.5)*100,0.39*_H+math.sin(time.time())*40))
        #screen.blit(球,((_W-82)//2+math.sin(time.time())*_W,(_H-86)//2+math.sin(time.time())*200))
        events=pygame.event.get()
        for event in events:
            if event.type==QUIT:
                step=0
                RUN=0
            elif event.type==VIDEORESIZE:
                _W,_H=pygame.display.get_window_size()[0],pygame.display.get_window_size()[1]
            elif event.type==MOUSEBUTTONDOWN or event.type==KEYUP:
                step=2
                s2oy=0.05*_H+math.sin(time.time())*20
                h2ox,h2oy=(_W-337)//2+math.sin(time.time()*0.5)*100, 0.39*_H+math.sin(time.time())*40
                h2x,h2y=0,0
                h2r=1
                h2rx=h2ry=0
                unfinish1=1
    #GAME
    while step==2:
        
        if unfinish1:
            if s2y<350:
                s2y += 360//FPS
                screen.blit(标题,((_W-1600)//2, s2oy-s2y))
                h2ox=h2ox-(h2ox-(_W-337)//2)//20
                h2oy=h2oy-(h2oy-(_H-415)//2)//20
            else:
                h2r=min(300,h2r+3)
                h2rx=random.randint(-h2r,h2r)
                h2ry=random.randint(-h2r,h2r)
            screen.blit(头图,(h2ox+h2rx,h2oy+h2ry))
            if h2r==300:
                unfinish1=0
        else: #播放完成退场动画后
            HWy = HWy - (HWy - fingerR.y)*0.5
            HWx = HWx - (HWx - fingerR.x)*0.5
            screen.blit(海伟L if HWside else 海伟R, (HWx+88, HWy+141))
            
        events=pygame.event.get()
        for event in events:
            if event.type==QUIT:
                step=0
                RUN=0
            elif event.type==VIDEORESIZE:
                重置分辨率()
            elif event.type==FINGERDOWN:
##                print(event)
                if event.x > 0.5:
##                    print('右')
                    fingerR.id= event.finger_id
                    fingerR.state=True
                    fingerR.x= event.x*_W
                    fingerR.y= event.y*_H
                else:
                    print('左')
                    pass
            elif event.type==FINGERMOTION:
                if event.finger_id==fingerR.id:
                    fingerR.x=event.x*_W
                    fingerR.y=event.y*_H
                else:
                    fingerL.x=event.x*_W
                    fingerL.y=event.y*_H
            elif event.type==FINGERUP:
                if event.finger_id==fingerR.id:
                    fingerR.state=False
                else:
                    fingerL.state=False
            elif event.type==KEYDOWN:
                if event.key==K_DOWN:
                    fingerR.y+=_H//100
                elif event.key==K_UP:
                    fingerR.y-=_H//100
                elif event.key==K_RIGHT:
                    fingerR.x+=_W//100
                    HWside=False
                elif event.key==K_LEFT:
                    fingerR.x-=_W//100
                    HWside=True
        clock.tick(FPS)
        pygame.display.flip()
        screen.fill('black')
pygame.quit()
sys.exit()
