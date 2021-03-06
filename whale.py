import pygame, math, random
import os
p = os.path.join

#             /-------------\
#____________/    Whale      \___________________________________
class Whale(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(p("backgroundImages","whale.gif"))
        self._ratio = random.randrange(50, 200)
        self.screen = screen
        self.image = pygame.transform.scale(self.image, (self._ratio * 3, self._ratio))
        self.rect = self.image.get_rect()
        self.rect.width /= 3
        self.reset()
        self.dy = self._ratio / 10
        self.Rect = [] 
        self.fishs = []
        self.num = 0
        for i in xrange( 3 ):
            self.Rect.append((0 + i * self._ratio, 0, self._ratio, self._ratio))
            self.fishs.append(self.image.subsurface(self.Rect[ -1 ]))
  
    def update(self):
        self.image = self.fishs[ self.num/10 ]
        self.num += 1
        if self.num >= 30:
            self.num %= 30

        self.rect.centerx -= random.randrange(0, self.dy)
        if self.rect.left < 0:
            self.reset()
            
    def reset(self):
        self.rect.left = self.screen.get_width()
        self.rect.centery = random.randrange(50, 200)
