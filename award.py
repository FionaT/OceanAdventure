import pygame, random, math
import os
p = os.path.join

#               /---------------\
#--------------/    Diamond      \-------------------------------------------
class Diamond(pygame.sprite.Sprite):
    def __init__(self, num, screen, ocean):
        #to gain different colors of the walls
        pygame.sprite.Sprite.__init__(self)  
        self.image = pygame.image.load(p("backgroundImages", "pinkDiamond.png"))
        self.color = random.randrange(0,10)

        self.pinkImage = pygame.image.load(p("backgroundImages", "pinkDiamond.png"))
        self.blueImage = pygame.image.load(p("blueDiamond.png"))
        self.Rect = [] 
        self.pinkDiamonds = []
        self.blueDiamonds = []


        self.count = 0
        for i in xrange( 8 ):
            self.Rect.append((0 + i * 32, 0, 32, 32))
            self.pinkDiamonds.append( self.pinkImage.subsurface( self.Rect[ -1 ] ) )
            self.blueDiamonds.append( self.blueImage.subsurface( self.Rect[ -1 ] ) )

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
        
        self.y = self.oldy = 200

        self.rect.center = ( self.x, self.y )
   
    def disappear(self):
        self.x = -100
        self.y = -100

        self.rect.center = (self.x, self.y)

    def update(self):
        if self.color <= 5:
            self.image = self.pinkDiamonds[ self.count ]
            self.count += 1
            if self.count >= 8:
                self.count %= 8
        else:
            self.image = self.blueDiamonds[ self.count ]
            self.count += 1
            if self.count >= 8:
                self.count %= 8

        self.x = self.ocean.x + (1020 - self.oldx) 

        self.rect.center = (self.x, self.y)


#               /---------------\
#--------------/    coin         \-------------------------------------------
class Coin(pygame.sprite.Sprite):
    def __init__(self, num, screen, ocean):
        #to gain different colors of the walls
        pygame.sprite.Sprite.__init__(self)  
        self.image = pygame.image.load(p("backgroundImages", "coin.png"))
        self.Rect = [] 
        self.coins = []
        self.count = 0
        for i in xrange( 8 ):
            self.Rect.append((0 + i * 32, 0, 32, 32))
            self.coins.append( self.image.subsurface( self.Rect[ -1 ] ) )

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
        
        self.y = self.oldy = 400

        self.rect.center = ( self.x, self.y )

    def disappear(self):
        self.x = -100
        self.y = -100

        self.rect.center = (self.x, self.y)
    def update(self):

        self.image = self.coins[ self.count ]
        self.count += 1
        if self.count >= 8:
            self.count %= 8

        self.x = self.ocean.x + (1020 - self.oldx) 

        self.rect.center = (self.x, self.y)
