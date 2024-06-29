'''
<<<< HIGHWAY BASKET >>>>>
Author:         Redroadsl
LaunchTime:     2024 04 19
Copyright:      Redroadsl
UsingLibraries: Pygame;logging;sys;math;time;random;ctypes;os
Licence:        https://www.mozilla.org/en-US/MPL/2.0/
'''
print(__doc__)
#   #==========================================================================#
#   |  ####    #####   ####    ####    #####   #####   ####    #####   #       |
#   |  #   #   #       #   #   #   #   #   #   #   #   #   #   #       #       |
#   |  ####    #####   #   #   ####    #   #   #####   #   #   #####   #       |
#   |  #   #   #       #   #   #   #   #   #   #   #   #   #       #   #       |
#   |  #   #   #####   ####    #   #   #####   #   #   ####    #####   #####   |
#   #==========================================================================#
'''
#              ____ ___   ______  
#     /     /     /     /        /     /    \     |     |  |\     \    \
#    /     /     /     /        /     /      \    |\    |  | \     \    \
#   /_____/     /     /  ____  /_____/        \   | \   |  |  \     \____\
#  /     /     /     /      / /     /          \  |  \  |  |___\       \
# /     /     /     /      / /     /            \ |   \ |  |    \       \
#/     / ____/____ /______/ /     /              \|    \|  |     \       \
'''
_wish_=\
'''
    王者风范——严格的标准、高超的水平、智慧的谈吐，“狼王”美名远扬。以眼神的锐利威慑四方，以爪牙的敏捷驰骋山海。

    海纳百川——胸怀天下，无数的远方都与您有关；有容乃大，一颗玲珑之心爱与温柔兼备。以善念为指引，您将万千顽石点作金。

    伟岸之山——您稳重的品性，是榜样，是风向标，深沉而厚重的灵魂为学生的心灵铺上翠绿的底色，从此一生轻灵，时时热泪盈眶。


    感恩这一切最美的相遇，感恩您是最好的狼王。
                                                                                         ——王馨南，2024年6月28日
'''
#Import
import logging
logging.basicConfig(level=logging.NOTSET)
logging.disable(level=False)
logging.info('START!')
import sys,time,math,random,os
from ctypes import windll
windll.user32.SetProcessDPIAware()
os.environ['PYGAME_HIDE_SUPPORT_PROMPT']='1'
import pygame
from pygame.locals import *
from pygame._sdl2 import messagebox
logging.debug('Import finished.')

# 设置类
class _():
    width = 1600
    height= 900
    fps   = 60
    speed = 10 #动画速度的除数
    run   = True
    clock = pygame.time.Clock()
    state = 1 # 0:exit  1:title  2:about  3:beforeGame 4:game 5:exam 6:final
    def tick():
        _.clock.tick(_.fps)
    def stop():
        _.state=0
        _.run=0
        logging.info('STOP!')
    def changeScreenSize():
        global screen
        size=pygame.display.get_window_size()
        logging.debug('VideoResized:('+str(_.width)+','+str(_.height)+') -> '+str(size))
        _.width=size[0]
        _.height=size[1]
##        pygame.display.set_caption('HIGHWAY BASKET','HIGHWAY BASKET')
        screen=pygame.display.set_mode(size,RESIZABLE|DOUBLEBUF|HWSURFACE)

# 对象通用模板
class Obj(object):
    def __init__(self,item,screen):
        self.item = item
        self.x = 0
        self.y = 0
        self.width = item.get_width()
        self.height = item.get_height()
        self.screen = screen
    def display(self):
        self.screen.blit(self.item,(self.x,self.y))
    def update(self):
        pass
    def update_videoResized(self):
        self.x = (_.width-self.width)//2
        self.y = (_.height-self.height)//2

# 初始化
pygame.init()
pygame.display.set_caption('HIGHWAY BASKET','HIGHWAY BASKET')
screen=pygame.display.set_mode((_.width,_.height),RESIZABLE|DOUBLEBUF|HWSURFACE)#SCALED|FULLSCREEN
pygame.key.set_repeat(100,100)
if pygame.get_init(): logging.debug('Pygame initialized.')

# 导入图片
imgPath     = './HIGHWAY_ASSETS/IMAGE/'
img_title   = pygame.image.load(imgPath+'TITLE.png'     ).convert_alpha()
img_highway = pygame.image.load(imgPath+'HighWAY!.png'  ).convert_alpha()
img_ball    = pygame.image.load(imgPath+'BALL.png'      ).convert_alpha()
img_innerBall=pygame.image.load(imgPath+'SMALLBALL.png' ).convert_alpha()
img_outerBall=pygame.image.load(imgPath+'BIGBALL.png'   ).convert_alpha()
img_about   = pygame.image.load(imgPath+'ABOUT.png'     ).convert_alpha()
img_bg01    = pygame.image.load(imgPath+'BG01.png'      ).convert_alpha()
img_bg02    = pygame.image.load(imgPath+'BG02.png'      ).convert_alpha()
img_bg03    = pygame.image.load(imgPath+'BG03.png'      ).convert_alpha()
img_bg04    = pygame.image.load(imgPath+'BG04.png'      ).convert_alpha()
img_bg05    = pygame.image.load(imgPath+'BG05.png'      ).convert_alpha()
img_rocket1 = pygame.image.load(imgPath+'ROCKET1.png'   ).convert_alpha()
img_rocket2 = pygame.image.load(imgPath+'ROCKET2.png'   ).convert_alpha()
del imgPath

# 导入字体
fontPath    = './HIGHWAY_ASSETS/FONTS/'
font_en     = pygame.font.Font(fontPath+'FIXEDSYS.TTF' ,size=12)
font_en_small=pygame.font.Font(fontPath+'NOTOSANS.OTF' ,size=36)
font_cn     = pygame.font.Font(fontPath+'华文中宋.TTF'  ,size=60)
font_cn_big = pygame.font.Font(fontPath+'NOTOSANS.OTF' ,size=72)
fontHeight_en=font_en.get_height()
fontHeight_cn=font_cn.get_height()
del fontPath

# 方便函数
def inRect(x,y,ax,ay,bx,by):
    return True if (ax <= x <= bx and ay <= y <= by) else False
def inRect2(pos1,pos2,pos3):
    return True if (pos2[0] <= pos1[0] <= pos3[0] and pos2[1] <= pos1[1] <= pos3[1]) else False

################################
######## TITLE场合的设置 ########
################################
class Title(Obj):
    '“BASKET”标题'
    def __init__(self,item=img_title,screen=screen):
        super().__init__(item,screen)
        self.update_videoResized()
    def update(self):
        '循环调用，用于更新高度，漂浮动效。'
        self.y = 0.05*_.height+math.sin(time.time())*20
    def update_videoResized(self):
        '窗口大小改变时调用，更新X坐标，调整图片大小以符合窗口。'
        #注意此处使用老的宽高计算
        #根据更改后的item更新宽高信息
        super().__init__(pygame.transform.scale(img_title,( _.width*0.85, self.height*((_.width*0.85)/self.width) )).convert_alpha(),screen)
        self.x = (_.width-self.width)//2
    def update_quit(self):
        '大标题的退出动画。'
        self.y -= (self.y + self.height) / _.speed#(_.fps//2)
        
class Highway(Obj):
    '横8字形飞来飞去的海伟。'
    def __init__(self,item=img_highway,screen=screen):
        super().__init__(item,screen)
        self.quit=False
        self.crazyRange=1
        self.update_videoResized()
    def update(self):
        '海伟飘~'
        self.x = self.centerX + math.sin(time.time()*0.5)*100 #此处似乎还能优化性能...
        self.y = 0.35*_.height+ math.sin(time.time())*40
    def update_quit(self):
        '退场动画'
        self.x = self.x-(self.x - self.centerX)/_.speed#(_.fps//2)
        self.y = self.y-(self.y - self.centerY)/_.speed#(_.fps//2)
    def update_videoResized(self):
        '性能优化，变量变常量'
        self.centerY = (_.height-self.height)/2 #图片在屏幕中央时的坐标
        self.centerX = (_.width-self.width)/2
    def update_crazy(self):
        '发疯的四处乱窜的海伟。'
        self.x = self.centerX + random.randint(-self.crazyRange, self.crazyRange)
        self.y = self.centerY + random.randint(-self.crazyRange, self.crazyRange)
        self.crazyRange+=1

class Ball(Obj):
    '漫天飞舞的篮球中的一个'
    def __init__(self,item=img_ball,screen=screen,count=0):
        super().__init__(item,screen)
        self.sourceItem=item
        #count用于区分哪个球，设置初始X坐标尽可能地均匀分布(只使用一次)
        self.x = count*100+self.width
        self.y = _.height + random.randint(0,_.width//100)*(_.height//10) #让球错开入场
        self.rotation = 0
        self.speedY = _.height / 500
        self.speedX = _.width / 1000
        self.randomize() #随机化旋转方向和运动方向
        self.quit=False
        self.alpha=255
    def update(self):
        '到一定时间后随机化，球往上漂浮，旋转'
##        if self.quit: self.update_quit() #处理退出动画
        if self.rotation % 108 == 0: self.randomize()
        if self.y <= -self.height: self.reset()
        self.y -= self.speedY
        self.x += self.speedX
        self.rotation += self.rotateDirection
        self.item = pygame.transform.rotate(self.sourceItem,self.rotation)
    def randomize(self):
        '随机化球旋转方向和运动方向'
        self.rotateDirection = random.choice((-1,1)) #旋转方向
        self.speedX = self.speedX * random.choice((-1,1)) #运动方向
    def reset(self):
        '球碰到顶后将其重置到底部'
        self.y=_.height
        self.randomize()
        self.x = random.randint(0, _.width-self.width)
    def update_videoResized(self):
        '窗口大小改变后改变球基准x坐标'
        self.x = random.randint(0, _.width-self.width)
        self.speedY = _.height / 500
        self.speedX = _.width / 1000
    def update_quit(self):
        '退场动画，'
        self.alpha = self.alpha - self.alpha / _.speed
        self.sourceItem.set_alpha(self.alpha)
        self.update() #还要更新一下参数

title = Title()
highway = Highway()
flyBallList=[]
for i in range(_.width//100): flyBallList.append(Ball(count=i))
TITLE_quit = False #控制TITLE场合进入退出流程的变量
text_about = font_cn.render('[>关于<]',False,(255,255,255)).convert()
text_wishes= font_cn.render('[>寄语<]',False,(255,255,255)).convert()
text_start = font_cn.render('·点击海伟开始·',False,(255,255,255)).convert()
text_about_width = text_about.get_width()
text_start_width = text_start.get_width()

#######################
######## ABOUT ########
#######################
class SmallBall(Obj):
    '内圈篮球'
    def __init__(self,item=img_innerBall,screen=screen):
        super().__init__(item,screen)
        self.oitem=item
        self.update_videoResized()
        self.rotation=0
        self.speed=-20
        self.aimX=_.width/2
        self.aimY=_.height/2
        self.temp=_.width
    def update(self):
        '内圈旋转'
        self.rotation = (self.rotation-self.speed) % 360
        self.item=pygame.transform.rotate(self.oitem,self.rotation)
        rCenter=self.item.get_rect().center
        self.x=self.aimX-rCenter[0]
        self.y=self.aimY-rCenter[1]
    def update_videoResized(self):
        '使内圈符合屏幕高度'
        self.oitem=pygame.transform.scale(img_innerBall,(_.height,_.height))#.convert_alpha()
        self.aimX,self.aimY=_.width/2,_.height/2
        self.temp=_.width
    def update_fadeIn(self):
        '入场动画'
        self.rotation = (self.rotation-self.speed) % 360
        self.item=pygame.transform.rotozoom(self.oitem,self.rotation,self.temp/_.height)
        self.temp-= (self.temp-_.height)/_.speed
        self.speed-=(self.speed-0.2)/_.speed
        rCenter=self.item.get_rect().center
        self.x=self.aimX-rCenter[0]
        self.y=self.aimY-rCenter[1]

class BigBall(Obj):
    '外圈HIGHWAY'
    def __init__(self,item=img_outerBall,screen=screen):
        super().__init__(item,screen)
        self.oitem=item
        self.update_videoResized()
        self.rotation=0
        self.speed=-20
        self.aimX=_.width/2
        self.aimY=_.height/2
        self.temp=_.height
    def update(self):
        '外圈球旋转'
        self.rotation = (self.rotation+self.speed) % 360
        self.item=pygame.transform.rotate(self.oitem,self.rotation)
        rCenter=self.item.get_rect().center
        self.x=self.aimX-rCenter[0]
        self.y=self.aimY-rCenter[1]
    def update_videoResized(self):
        '使外圈符合屏幕宽'
        self.oitem=pygame.transform.scale(img_outerBall,(_.width,_.width))#.convert_alpha()
        self.aimX,self.aimY=_.width/2,_.height/2
        self.temp=_.width
    def update_fadeIn(self):
        '外圈入场动画'
        self.rotation = (self.rotation+self.speed) % 360
        self.item=pygame.transform.rotozoom(self.oitem,self.rotation,self.temp/_.width)
        self.temp-= (self.temp-_.width)/_.speed
        self.speed-=(self.speed-0.2)/_.speed
        rCenter=self.item.get_rect().center
        self.x=self.aimX-rCenter[0]
        self.y=self.aimY-rCenter[1]

class AboutImage(Obj):
    '一张关于的图片'
    def __init__(self,item=img_about,screen=screen):
        super().__init__(item,screen)
        self.update_videoResized()
        self.alpha = 0
    def update(self):
        if self.alpha != 255:
            self.alpha += 1
            self.item.set_alpha(self.alpha)
    def update_videoResized(self):
        self.x = (_.width-self.width)//2
        self.y = (_.height-self.height)//2
        self.item.set_alpha(0)
        self.alpha = 0
        
smallBall = SmallBall()
bigBall = BigBall()
aboutImg = AboutImage()

###########################
######## BEFOREGAME #######
###########################
class Animate(object):
    '时序动画'
    def __init__(self):
        '仍需要调用 init 方法并传入参数。'
    def init(self,animation={}):
        '要求动画格式：\n{\n  [开始tick,时长tick]:调用方法,\n  [开始tick,时长tick]:调用方法,\n  ......\n}'
        self.oAn = animation
        self.reset()
    def reset(self):
        '重置'
        self.an = self.oAn
        self.t = 0
        self.run = True
    def tick(self):
        '计时(写在循环末尾)'
        if self.run: self.t+=1
    def play(self):
        '播放'
        for an in self.an:
            if an[0] <= self.t:
                if (an[0]+an[1] >= self.t) or (an[1] == -1):
                    exec(self.an[an])
                else:
                    self.an.pop(an)
                    self.play()
                    return True
            else:
                return 0
        return False
    def pause(self):
        '创建等待点击事件（动画列表里调用）'
        self.run = False
    def conti(self):
        '消除等待（事件循环判断里调用）'
        self.run = True
        self.t+=1

class BG(Obj):
    '操作背景'
    def __init__(self,screen=screen):
        '仍需进一步初始化...'
        self.screen=screen
        self.index=0
        self.alpha=255
    def init(self,imgList=[img_bg02]):
        '初始化导入图片列表'
        self.imgList=imgList
        self.item=imgList[0]
        super().__init__(self.item,self.screen)
        self.update_videoResized()
    def change(self,add=1):
        '切换下一张(默认)图片'
        self.index+=add
        self.item=self.imgList[self.index]
        self.update_videoResized()
    def set_pos(self,left=0.5,top=0.5):
        self.left=left
        self.top=top
        self.update_videoResized()
    def hide(self):
        '隐藏显示'
        self.display = lambda: ''
    def unhide(self):
        '恢复显示'
        self.display = super().display
    def set_alpha(self,a):
        self.alpha=a
        self.item.set_alpha(a)
    def fadeIn(self,step=1):
        '淡入特效'
        self.alpha = min(self.alpha+step, 254)
        self.item.set_alpha(self.alpha)
    def fadeOut(self,step=1):
        '淡出特效'
        self.alpha = max(self.alpha-step,0)
        self.item.set_alpha(self.alpha)
    def rollscale(self,ro=0,sc=1):
        self.item=pygame.transform.rotozoom(self.item,ro,sc)
        super().__init__(self.item,screen)
        self.x = (_.width-self.width)*0.5
        self.y = (_.height-self.height)*0.5
    def scaleUp(self,sc):
        self.item.set_clip(Rect(0,0,_.width,_.height))
        self.item=pygame.transform.scale_by(self.item,sc)
    def update_videoResized(self):
        '缩放图片（客制化）'
        self.item=pygame.transform.scale(self.imgList[self.index],(_.width,_.height))
        super().__init__(self.item,screen)
        
class Speech(Obj):
    '台词控制'
    def __init__(self):
        self.index = 0
        self.left= 0.5
        self.top = 0.5
        self.alpha=255
    def init(self,lines=['Hello world!','TestTest..']):
        self.lines=lines
        self.render()
        self.update_videoResized()
    def change(self,add=1):
        self.index+=add
        self.render()
        self.update_videoResized()
    def render(self):
        '渲染字体'
        self.item=font_cn.render(self.lines[self.index],False,(0xFF,0xFF,0xFF))
        super().__init__(self.item,screen)
    def set_pos(self,left=0.5,top=0.5):
        self.left=left
        self.top=top
        self.update_videoResized()
    def hide(self):
        '隐藏显示'
        self.display = lambda: ''
    def unhide(self):
        '恢复显示'
        self.display = super().display
    def set_alpha(self,a):
        self.alpha=a
        self.item.set_alpha(self.alpha)
    def fadeIn(self,step=1):
        '淡入特效'
        self.item.set_alpha(self.alpha)
        self.alpha = min(self.alpha+step, 254)
    def fadeOut(self,step=1):
        '淡出特效'
        self.item.set_alpha(self.alpha)
        self.alpha = max(self.alpha-step,0)
    def update_videoResized(self):
        '在合适的位置排列台词'
        self.x = (_.width-self.width)*self.left
        self.y = (_.height-self.height)*self.top

class Next(Obj):
    def __init__(self):
        self.index=0
        self.item=font_en_small.render('点击屏幕继续',False,(255,255,255),(0,0,0))
        super().__init__(self.item,screen)
        self.update_videoResized()
    def show(self):
        self.index = (self.index + 1) % 4
        self.item=font_en_small.render('点击屏幕继续',False,(0xFF,0xE5,0x00),(0,0,0))
        screen.blit(self.item,(self.x,self.y))
    def update_videoResized(self):
        self.x = (_.width-self.width)*0.5
        self.y = _.height-self.height

class Rocket(Obj):
    '海伟的火箭'
    def __init__(self):
        self.item=img_rocket1
        super().__init__(self.item,screen)
        self.change=True
        self.x = -self.width//2
        self.y = -self.height//2
        self.rotation=0
    def update(self):
        self.item = img_rocket1 if self.change else img_rocket2
        self.change = not self.change
    def move(self,x=0,y=0):
        self.x+=x
        self.y+=y
    def rotate(self,ro):
        self.rotation += ro
        self.item = pygame.transform.rotate(img_rocket1 if self.change else img_rocket2, self.rotation)

NEXT=Next()

rocket=Rocket()

bBG=BG()
bBG.init(imgList=\
[
img_bg01,
img_bg02,
img_bg03,
img_bg04,
img_bg05,
])

bSP=Speech()
bSP.init(lines=\
[
'人类始终怀着对宇宙的好奇与向往',
'篮球男孩海伟也不例外',
'他有一个大大的梦想',
'那就是乘坐火箭，在太空漫游...',
'尽管太空充满了未知，其中不乏凶险',
'他最终豁出去了，为了未来和远方',
])

animate=Animate()
animate.init(\
{#(开始，持续)
(0,0):     'bSP.set_alpha(0),bBG.set_alpha(0)',
(0,-1):    'bBG.display(),bSP.display()',
(0,127):   'bSP.fadeIn(step=2)',
(64,127):  'bBG.fadeIn(step=3)',
(191,0):   'self.pause(),NEXT.show()',
(192,0):   'bSP.change(),bBG.hide(),bSP.set_pos(0.5,0.23)',#
(192,1):   'highway.display(),highway.update()',
(193,0):   'self.pause(),NEXT.show()',
(194,0):   'bSP.set_pos(0.5,0.5),bSP.change(),bBG.change(),bBG.set_alpha(0),bBG.unhide()',#
(195,255): 'bBG.fadeIn(step=1)',
(450,0):   'self.pause(),NEXT.show()',
(451,127): 'bBG.fadeOut(step=2),bSP.fadeOut(step=2)',
(578,0):   'bSP.change(),bBG.change(),bBG.set_alpha(0),bSP.set_alpha(0)',#
(579,127): 'bSP.fadeIn(step=2)',
(579,255): 'bBG.fadeIn(step=1)',
(835,0):   'self.pause(),NEXT.show(),rocket.display(),rocket.update(),rocket.move(x=3,y=4),rocket.rotate(-1)',
(836,127): 'bBG.fadeOut(step=2)',
(964,0):   'bSP.change(),bBG.change(),bBG.set_alpha(0)',#
(965,127): 'bBG.rollscale(sc=1.001)',
(965,128): 'bBG.fadeIn(step=2)',
(1094,0):  'self.pause(),NEXT.show()',
(1095,0):  'bBG.change(),bBG.set_alpha(0),bSP.change()',#
(1095,127):'bBG.fadeIn(step=2)',
(1223,0):  'self.pause(),NEXT.show()',
(1224,127):'bBG.fadeOut(step=2)',
(1224,255):'bSP.fadeOut(step=1)',
(1480,0):  '_.state=4'
})

###########################
######## MAIN GAME ########
###########################

def VideoResized():
    _.changeScreenSize()
    title.update_videoResized()
    highway.update_videoResized()
    smallBall.update_videoResized()
    bigBall.update_videoResized()
    for ball in flyBallList: ball.update_videoResized()
    aboutImg.update_videoResized()
    bBG.update_videoResized()
    bSP.update_videoResized()
    NEXT.update_videoResized()

# 创建主循环
while _.run:
    ######## TITLE ########
    while _.state == 1:
        for event in pygame.event.get():
            if   event.type == MOUSEMOTION: pass
            elif event.type == QUIT: _.stop()
            elif event.type == VIDEORESIZE: VideoResized()
            elif event.type == MOUSEBUTTONUP:
                if inRect2(event.pos,(0,0),(_.width, _.height-fontHeight_cn)): TITLE_quit = True #GAME
                elif inRect2(event.pos, (0,_.height-fontHeight_cn), (text_about_width,_.height)):messagebox('致亲爱的王老师:',_wish_) #Wishes
                elif inRect2(event.pos, (_.width-text_about_width,_.height-fontHeight_cn), (_.width,_.height)):_.state=2 #ABOUT
            elif event.type == KEYUP and event.key==K_RETURN: TITLE_quit = True

        if TITLE_quit:  # 处理退出动画 #
            if title.y > -title.height+1: #完成退出动画前
                for ball in flyBallList: ball.update_quit()
                title.update_quit()
                highway.update_quit()
            elif highway.crazyRange < 120: highway.update_crazy() #完成退出动画后海伟乱动
            else: _.state=3 #真正退出
        else: #   正常处理   #
            for ball in flyBallList: ball.update()
            title.update()
            highway.update()
        
        # RENDER #
        screen.fill((0,0,0))
        for ball in flyBallList: ball.display()
        highway.display()
        title.display()
        screen.blit(text_wishes,(0, _.height-fontHeight_cn))
        screen.blit(text_about, (_.width-text_about_width, _.height-fontHeight_cn))
        screen.blit(text_start,((_.width-text_start_width)/2, _.height-fontHeight_cn))
        pygame.display.flip()
        # 控制帧率 #
        _.tick()
    
    ######## ABOUT ########
    while _.state == 2:
        for event in pygame.event.get():
            if   event.type == MOUSEMOTION: pass
            elif event.type == MOUSEBUTTONUP: _.state=1
            elif event.type == QUIT: _.stop()
            elif event.type == VIDEORESIZE: VideoResized()
            elif event.type == KEYDOWN and event.key==K_ESCAPE: _.state=1
        
        if smallBall.temp > _.height + 3:
            smallBall.update_fadeIn()
            bigBall.update_fadeIn()
        else:
            smallBall.update()
            bigBall.update()
            aboutImg.update()
        
        screen.fill((0,0,0))
        bigBall.display()
        smallBall.display()
        aboutImg.display()
        pygame.display.flip()
        _.tick()
        
    ######## BEFOREGAME ########
    while _.state == 3:
        for event in pygame.event.get():
            if event.type == QUIT: _.stop()
            elif event.type==VIDEORESIZE: VideoResized()
            elif event.type==MOUSEBUTTONUP or (event.type==KEYUP and event.key==K_RETURN):
                animate.conti()
        screen.fill((0,0,0))
        animate.play()
        pygame.display.flip()
        _.tick()
        animate.tick()
    ######## MAIN GAME ########
    while _.state == 4:
        for event in pygame.event.get():
            if event.type == QUIT: _.stop()
            elif event.type==VIDEORESIZE: VideoResized()
            elif event.type==MOUSEBUTTONUP or (event.type==KEYUP and event.key==K_RETURN):
                pass
        screen.fill((0,0,0))
        pygame.display.flip()
        _.tick()
    ######## EXAMINATION ########
    while _.state == 5:
        for event in pygame.event.get():
            if event.type == QUIT: _.stop()
            elif event.type==VIDEORESIZE: VideoResized()
            elif event.type==MOUSEBUTTONUP or (event.type==KEYUP and event.key==K_RETURN):
                pass
        screen.fill((0,0,0))
        pygame.display.flip()
        _.tick()
pygame.quit()
sys.exit()
