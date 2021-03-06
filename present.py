import pygame, random, math
import os
p = os.path.join

#             /-------------\
#____________/  Selectplayer \___________________________________ 
class Selectplayer(pygame.sprite.Sprite):
    def __init__(self, screen, background, gender):
        pygame.sprite.Sprite.__init__(self)
        self.gender = gender
        self.loadImages()
        self.image = self.imageStand
        self.background = background
        self.screen = screen
        self.rect = self.image.get_rect()
        self.num = 0
        self.frame = 0
        self.delay = 6
        self.pause = 0

    def update(self):
        if self.gender == 0:
            self.x = 400
            self.y = 240
        else:
            self.x = 600
            self.y = 240
        self.rect.center = (self.x, self.y)        
        self.pause += 1
        if self.pause >= self.delay:
            #reset pause and advance animation
            self.pause = 0
            self.image = self.shows[ self.num ]
            self.num += 1
            if self.num >= 12:
                self.num %= 12
        


    def loadImages(self):
        if self.gender == 0:
            self.imageStand = pygame.image.load("playerImages/Gstand4.png")
        else:
            self.imageStand = pygame.image.load("playerImages/Bstand4.png")

        self.imageStand = self.imageStand.convert()
        transColor = self.imageStand.get_at((1, 1))
        self.imageStand.set_colorkey(transColor)

        self.shows = []
        for i in range(12):
            if self.gender == 0:
                imgName = "playerImages/Gshow%d.png" % i
                tmpImage = pygame.image.load(imgName)
                tmpImage = tmpImage.convert()
                transColor = tmpImage.get_at((1, 1))
                tmpImage.set_colorkey(transColor)
                self.shows.append(tmpImage)
            else:
                imgName = "playerImages/Bshow%d.png" % i
                tmpImage = pygame.image.load(imgName)
                tmpImage = tmpImage.convert()
                transColor = tmpImage.get_at((1, 1))
                tmpImage.set_colorkey(transColor)
                self.shows.append(tmpImage)


#             /-------------------\
#____________/  Moving Background  \___________________________________
class MovingBackground(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(p("backgroundImages", "sea.jpg"))
        self.rect = self.image.get_rect()
        self.width = 2040
        self.x = self.width/2
        self.y = 240
        self.screen = screen
        self.flag = 1
        self.rect.center = (self.x, self.y)

        self.dx = 3
        
    def update(self):
        if self.flag == 1:
            self.rect.right -= self.dx
            if self.rect.right <= 1000:
                self.reset() 
        else:
            self.rect.right += self.dx
            if self.rect.right >= self.width:
                self.reset() 
    
    def reset(self):
        self.flag *= -1


#             /-------------\
#____________/  Scoreboard   \___________________________________
class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 8.00
        self.score = 0
        self.font = pygame.font.SysFont("None", 50)
        
    def update(self):
        self.text = "Lives: %d, score: %d" % (self.lives, self.score)
        self.image = self.font.render(self.text, 1, (102, 255, 255))
        self.rect = self.image.get_rect()

#             /-------------\
#____________/  lifeboard   \___________________________________
class Lifeboard(pygame.sprite.Sprite):
    def __init__(self, monsterLives):
        pygame.sprite.Sprite.__init__(self)
        self.lives = monsterLives
        self.font = pygame.font.SysFont("None", 50)
        
    def update(self):
        self.text = "monster Lives: %d" % self.lives
        self.image = self.font.render(self.text, 1, (102, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (800, 20)



#             /-------------\
#____________/  Label        \___________________________________
class Label(pygame.sprite.Sprite):
    """ Label Class (simplest version) 
        Attributes:
            font: any pygame font object
            text: text to display
            center: desired position of label center (x, y)
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("None", 30)
        self.text = ""
        self.center = (120, 140)
                
    def update(self):
        self.image = self.font.render(self.text, 1, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = self.center

#             /-------------\
#____________/  Mouse        \___________________________________
class Mouse(pygame.sprite.Sprite):
        
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(p("backgroundImages", "diamond.png"))

        self.Rect = [] 
        self.diamonds = []
        self.num = 0
        for i in xrange( 8 ):
            self.Rect.append((0 + i * 32, 0, 32, 32))
            self.diamonds.append( self.image.subsurface( self.Rect[ -1 ] ) )

        self.rect = self.diamonds[0].get_rect()        

    def update(self):
        self.rect = self.image.get_rect() 
        self.image = self.diamonds[ self.num ]
        self.num += 1
        if self.num >= 8:
            self.num %= 8
        self.rect.center = pygame.mouse.get_pos()
