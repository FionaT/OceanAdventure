import pygame, random, math
import os
p = os.path.join

#             /-------------\
#____________/  ocean        \___________________________________
class Ocean(pygame.sprite.Sprite):
    def __init__(self, screen, player, level):
        pygame.sprite.Sprite.__init__(self)
        self.level = level
        imageName = p("backgroundImages", "sea%d.jpg" % self.level)
        self.image = pygame.image.load(imageName)
        #self.image = pygame.transform.scale(self.image, (2040, 560))
        self.rect = self.image.get_rect()
        self.x = 1020 * 2
        self.y = 240

        if self.level == 2:
            self.y = 240 + 33
        self.screen = screen
        self.rect.center = (self.x, self.y)
        
        
        #self.rect.left = 600
        self.player = player


    def update(self):
        if self.player.x + 200 >= self.screen.get_width() - 40:
            self.x -= 5
            if self.x <= -1000:
                self.x = -1000
        if self.player.x - 100 <= 40:
            self.x += 5
            if self.x >= 1020 * 2:
                self.x = 1020 * 2       


        self.rect.center = (self.x, self.y)

        #print "ocean", self.rect.center
    
    #def reset(self):
        #self.rect.right -= 824
