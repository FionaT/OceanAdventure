import pygame, random
import os

#             /-------------\
#____________/    Music      \___________________________________
class Music():
    def __init__(self):
        if not pygame.mixer:
            print "problem with sound"
        else:
            pygame.mixer.init()
            self.snd_gainCoin = pygame.mixer.Sound("sound"+os.sep+"gainCoin.wav")
            self.snd_gainDiamond = pygame.mixer.Sound("sound"+os.sep+"gainDiamond.wav")
            self.snd_gainLife = pygame.mixer.Sound("sound"+os.sep+"gainLife1.ogg")
            self.snd_shoot = pygame.mixer.Sound("sound"+os.sep+"shoot.wav")
            self.snd_jump = pygame.mixer.Sound("sound"+os.sep+"jump.wav")
            self.snd_enemyDie = pygame.mixer.Sound("sound"+os.sep+"enemyDie1.ogg")
            self.snd_loseLife = pygame.mixer.Sound("sound"+os.sep+"enemyDie.ogg")