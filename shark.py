import pygame, random, math
from music import *
import os
p = os.path.join

#             /-------------\
#____________/    shark      \___________________________________
class Shark(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.exist = 1
        self.music = Music()
        self.image = pygame.image.load(p("sharkImages","shark.gif"))
        self._ratio = random.randrange(90, 150)
        self.screen = screen
        self.image = pygame.transform.scale(self.image, (self._ratio * 3, self._ratio))

        self.swimImage = pygame.image.load(p("sharkImages","sharkSwim.gif"))
        self.swimbackImage = pygame.image.load(p("sharkImages","sharkSwimback.gif"))
        self.swimImage = pygame.transform.scale(self.swimImage, (self._ratio * 3, self._ratio))
        self.swimbackImage = pygame.transform.scale(self.swimbackImage, (self._ratio * 3, self._ratio))

        self.rect = self.image.get_rect()
        self.rect.width /= 3
        self.dy = random.randrange(8, 15)
        self.x = self.y = -100
        self.Rect = [] 

        self.swimImages = []
        self.swimbackImages = []

        self.num = 0
        self.dying = 0
        self.lives = 30
        self.dir = 1

        for i in xrange( 3 ):
            self.Rect.append((0 + i * self._ratio, 0, self._ratio, self._ratio))
            self.swimImages.append(self.swimImage.subsurface(self.Rect[ -1 ]))
            self.swimbackImages.append(self.swimbackImage.subsurface(self.Rect[ -1 ]))

        self.reset()
  
    def update(self):
        if self.exist:
            if not self.dying:
                if self.dir == 1:
                    self.swim()
                else:
                    self.swimback()
            else:
                #print self.dying
                self.y -= random.randrange(0, self.dy)
                self.dying -= 1
                if self.rect.top <= 0 and self.dying <= 0:
                    self.reset()
                    self.change()
                    self.dying = 0

            self.rect.center = (self.x, self.y) 
        else:
            self.rect.centerx = 200 + self._ratio
            self.rect.centery = 200 - self._ratio
            self.swimback()     
            
    def swim(self):
        self.image = self.swimImages[ self.num/10 ]
        self.num += 1
        if self.num >= 30:
            self.num %= 30

        self.x -= random.randrange(0, self.dy)
            
        if self.rect.left < 0:
            self.dir *= -1
            #self.reset()
            #self.change()

    def swimback(self):
        self.image = self.swimbackImages[ self.num/10 ]
        self.num += 1
        if self.num >= 30:
            self.num %= 30

        self.x += random.randrange(0, self.dy)
                        
        if self.rect.right >= self.screen.get_width():
            self.dir *= -1

    def reset(self):
        self.rect.left = self.screen.get_width()
        self.y = random.randrange(380, self.screen.get_height() - 50)
        self.x = random.randrange(850, 1000)
        
    def die(self):
        self.lives = 30
        self.dying = random.randrange(300,500)
        self.music.snd_enemyDie.play()
        self.image = pygame.image.load(p("sharkImages","dieShark.png"))
        self.image = pygame.transform.scale(self.image, (self._ratio, self._ratio))

    def change(self):
        self._ratio = random.randrange(60, 150)
        self.image = pygame.image.load(p("sharkImages","shark.gif"))
        self.image = pygame.transform.scale(self.image, (self._ratio* 3, self._ratio))
        self.Rect = [] 
        self.fishs = []
        self.num = 0
        for i in xrange( 3 ):
            self.Rect.append((0 + i * self._ratio, 0, self._ratio, self._ratio))
            self.fishs.append( self.image.subsurface( self.Rect[ -1 ] ) )
   
