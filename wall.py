import pygame, random, math
import os
p = os.path.join

#               /-----------\
#--------------/    Wall     \-------------------------------------------
class Wall(pygame.sprite.Sprite):
    def __init__(self,position):
        #to gain different colors of the walls
        pygame.sprite.Sprite.__init__(self)  
        imgName = p("backgroundImages", "wall.png")
        self.image = pygame.image.load(imgName)
        self.image = self.image.convert()
        transColor = self.image.get_at((1, 1))
        self.image.set_colorkey(transColor)
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        
        self.row = position
        self.startPoint = ( -20, 460 )
        self.x = self.startPoint[0] + 40 + self.row * 40
        self.y = self.startPoint[1]
        self.rect.center = ( self.x, self.y )


#               /---------------\
#--------------/    HighWall     \-------------------------------------------
class HighWall(pygame.sprite.Sprite):
    def __init__(self, num, screen, ocean):
        #to gain different colors of the walls
        pygame.sprite.Sprite.__init__(self)  
        self.type = 0

        imgName = p("backgroundImages", "highWall%d.png" % self.type)
        self.image = pygame.image.load(imgName)
        self.image = self.image.convert()
        transColor = self.image.get_at((1, 1))
        self.image.set_colorkey(transColor)
        self.image = pygame.transform.scale(self.image, (120, 40))
        self.rect = self.image.get_rect()
        self.ocean = ocean
        self.screen = screen
        self.num = num
          
        self.position = random.randrange(0, 2)

        if self.position == 0:
            self.y = self.oldy = 200
        elif self.position == 1:
            self.y = self.oldy = 320

        self.num += random.randrange( -7, 6 )

        self.x = self.oldx = self.num * 120
        
        self.y = self.oldy = 320

        self.rect.center = ( self.x, self.y )

    def update(self):
        self.x = self.ocean.x + (1020 - self.oldx) 

        self.rect.center = (self.x, self.y)
