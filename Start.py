"""Game Ocean Adventure"""

import pygame, random, math
from player3 import *
from monster import *
from ocean import *
from wall import *
from shark import *
from whale import *
from jellyFish import *
from award import *
from present import *
from music import *
from gameFunction import *
from showFunction import *
import os
p = os.path.join

pygame.init()
pygame.key.set_repeat(100,100)
screen = pygame.display.set_mode((1000, 480))


#             /--------------\
#____________/  show win level\___________________________________ 
def winLevel(levelNum, score):
    pygame.display.set_caption("ocean Adventure")
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    mouse = Mouse()
    ocean = MovingBackground(screen)     
    mermaid = showPicture(screen, levelNum)
    allSprites = pygame.sprite.OrderedUpdates(ocean, mouse, mermaid)

    insFont = pygame.font.SysFont(None, 50)
    insLabels = []
    instructions = (
    "Ocean world.     Last score: %d" % score ,
    )
    
    for line in instructions:
        tempLabel = insFont.render(line, 1, (150, 0, 242))
        insLabels.append(tempLabel)

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

        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (50, 30*i))   
            
        pygame.display.flip()
        
    pygame.mouse.set_visible(True)

#             /--------------\
#____________/  show lose level\___________________________________ 
def loseLevel():
    pygame.display.set_caption("ocean Adventure")
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    levelNum = 6
    mouse = Mouse()
    ocean = MovingBackground(screen)     
    mermaid = showPicture(screen, levelNum)
    allSprites = pygame.sprite.OrderedUpdates(ocean, mouse, mermaid)

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

        
#             /---------------------\
#____________/  main function        \___________________________________           
def main():
    donePlaying = False
    score = 100
    win = 0
    level = 1
    
    channel = pygame.mixer.find_channel() 
    snd_gameBG = pygame.mixer.Sound(p("sound", "gameBG.wav"))
    

    while not donePlaying:
        donePlaying = instructions(score)
        gender = selectPlayer()

        if not donePlaying:
            if level == 1:
                print "level1"
                channel.play(snd_gameBG)
                score = level1(gender)
                if score > 0:
                    level += 1
                    winLevel(1, score)
                if score == -999:
                    loseLevel()
            if level == 2:
                print "level2"
                channel.play(snd_gameBG)
                score = level2(gender)
                if score > 0:
                    level += 1
                    winLevel(2, score)
                if score == -999:
                    loseLevel()
            if level == 3:
                print "level3"
                channel.play(snd_gameBG)
                score = level3(gender)
                if score > 0:
                    level += 1
                    winLevel(3, score)
                if score == -999:
                    loseLevel()
            elif level > 3:
                print "all win"

if __name__ == "__main__":
    main()
    
