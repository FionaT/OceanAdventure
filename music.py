import pygame, random

#             /-------------\
#____________/    Music      \___________________________________
class Music():
    def __init__(self):
        if not pygame.mixer:
            print "problem with sound"
        else:
            pygame.mixer.init()
            self.snd_gainCoin = pygame.mixer.Sound("sound\gainCoin.ogg")
            self.snd_gainDiamond = pygame.mixer.Sound("sound\gainDiamond.ogg")
            self.snd_gainLife = pygame.mixer.Sound("sound\gainLife1.ogg")
            self.snd_shoot = pygame.mixer.Sound("sound\shoot.ogg")
            self.snd_jump = pygame.mixer.Sound("sound\jump.ogg")
            self.snd_enemyDie = pygame.mixer.Sound("sound\enemyDie1.ogg")
            self.snd_loseLife = pygame.mixer.Sound("sound\enemyDie.ogg")