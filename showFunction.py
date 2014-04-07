import pygame, random, math
from player3 import *
from ocean import *
from wall import *
from shark import *
from monster import *
from whale import *
from jellyFish import *
from award import *
from present import *
from music import *
from gameFunction import *
import os
p = os.path.join

pygame.init()
pygame.key.set_repeat(100,100)
screen = pygame.display.set_mode((1000, 480))

#             /---------------\
#____________/  Select player  \___________________________________ 
def selectPlayer():
    pygame.display.set_caption("ocean Adventure")
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    gender = 0
    mouse = Mouse()
    girl = Selectplayer(screen, background, 0)
    boy = Selectplayer(screen, background, 1)
    ocean = MovingBackground(screen) 
    word = showPicture(screen, 5)

    allSprites = pygame.sprite.OrderedUpdates(ocean, mouse, girl, boy, word)

    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                keepGoing = False
                donePlaying = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                
                if y >= 180 and y <= 300:
                    if x >= 350 and x <= 450:
                        gender = 0
                        keepGoing = False
                        donePlaying = False

                    elif x >= 550 and x <= 650:
                        gender = 1
                        keepGoing = False
                        donePlaying = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    donePlaying = True
        
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)

        pygame.display.flip()
        
    pygame.mouse.set_visible(True)
    return gender

#             /----------------------------\
#____________/  instruction function        \___________________________________    
def instructions(score):
    pygame.display.set_caption("ocean Adventure")
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    #music = Music()
    mouse = Mouse()
    ocean = MovingBackground(screen)
    word = showPicture(screen, 4)
    MonsterBubble1 = MonsterBubble(screen, background)
    MonsterBubble2 = MonsterBubble(screen, background)
    monster = Monster( MonsterBubble1, MonsterBubble2, screen, 1)    
    allSprites = pygame.sprite.OrderedUpdates(ocean, mouse, word, monster, MonsterBubble1, MonsterBubble2)
    

    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                keepGoing = False
                donePlaying = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                keepGoing = False
                donePlaying = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    donePlaying = True
        
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)


        pygame.display.flip()
        
    pygame.mouse.set_visible(True)
    return donePlaying

    
#             /------------------\
#____________/    showPicture     \___________________________________
class showPicture(pygame.sprite.Sprite):
    def __init__(self, screen, picNum):
        pygame.sprite.Sprite.__init__(self)
        self.num = picNum
        self.imageName = p("backgroundImages", "showPic%d.gif" % self.num)
        self.image = pygame.image.load(self.imageName)
        self.screen = screen
        #self.image = pygame.transform.scale(self.image, (self._ratio * 3, self._ratio))
        self.rect = self.image.get_rect()
        self.x = 500
        self.y = 240
        
    def update(self):
        self.rect.center = (self.x, self.y)

