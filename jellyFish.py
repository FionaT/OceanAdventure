import pygame, random, math
from music import *
import os
p = os.path.join

#               /-----------\
#--------------/    Bubble    \-------------------------------------------
class Bubble(pygame.sprite.Sprite):
    def __init__(self, screen, background):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.background = background
        self.color = random.randrange(0,8)
        self.image = pygame.Surface((10, 10))
        self.image.fill((0xff, 0xff, 0xff))
        self.image.set_colorkey((0xff, 0xff, 0xff))
        #pygame.draw.circle(self.image, (0, 0, 0), (5, 5), 5)
        imgName = p("bubbleImages", "Bubble%d.png" % self.color)
        self.dying = 0
        self.exist = 1
        self.image = pygame.image.load(imgName)
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.center = (-100, -100)
        
        self.x = -100
        self.y = -100
        self.dx = 0
        self.dy = 0
        self.speed = 0
        self.dir = 0
        self.gravity = .2
        self.pause = 5
        self.lives = 1
        
    def update(self):
        self.pause -= 1
        if self.pause == 0:
            self.pause = 5
            self.color = random.randrange(0,8)
            imgName = p("bubbleImages", "Bubble%d.png" % self.color)

            self.image = pygame.image.load(imgName)
            self.image = pygame.transform.scale(self.image, (20, 20))

        self.calcPos()
        self.checkBounds()
        if self.exist:
            self.rect.center = (self.x, self.y)
        else:
            self.rect.center = (-100, -100)
   
    def calcVector(self):
        radians = self.dir * math.pi / 180
        
        self.dx = self.speed/2 * math.cos(radians)
        self.dy = self.speed/2 * math.sin(radians)
        self.dy *= -1
        
        #clear the background
        #self.background.fill((0x00, 0xCC, 0x00))
    
    def calcPos(self):
        #compensate for gravity
        self.dy += self.gravity
        
        #get old position for drawing
        oldx = self.x
        oldy = self.y
        
        self.x += self.dx
        self.y += self.dy
    
        #pygame.draw.line(self.background, (0,0,0), (oldx, oldy), (self.x, self.y))
    
    def checkBounds(self):
        screen = self.screen
        if self.x > screen.get_width():
            self.reset()
        if self.x < 0:
            self.reset()
        if self.y > screen.get_height():
            self.reset()
        if self.y < 0:
            self.reset()

    def die(self):
        self.x = -100
        self.y = -100
        self.speed = 0
        self.lives = 1

    def reset(self):
        """ move off stage and stop"""
        self.x = -100
        self.y = -100
        self.speed = 0

    def rotate(self):
        oldCenter = self.rect.center
        self.image = pygame.transform.rotate(self.imageMaster, self.dir)
        self.rect = self.image.get_rect()
        self.rect.center = oldCenter

#               /----------------\
#--------------/    JellyFish     \-------------------------------------------
class JellyFish(pygame.sprite.Sprite):
    def __init__(self, bubble1, bubble2, background):
        self.bubble1 = bubble1
        self.bubble2 = bubble2
        pygame.sprite.Sprite.__init__(self)
        self.exist = 1
        #load the image and set the position
        self.color = random.randrange(0,5)
        self.image = pygame.image.load(p("JellyImages","jellyFish3.gif"))
        self._ratio = random.randrange(60, 100)
        self.music = Music()

        self.image0 = pygame.image.load(p("JellyImages","jellyFish0.gif"))
        self.image1 = pygame.image.load(p("JellyImages","jellyFish1.gif"))        
        self.image2 = pygame.image.load(p("JellyImages","jellyFish2.gif"))        
        self.image3 = pygame.image.load(p("JellyImages","jellyFish3.gif"))
        self.image4 = pygame.image.load(p("JellyImages","jellyFish4.gif"))

        self.image0 = pygame.transform.scale(self.image0, (self._ratio * 3, self._ratio)) 
        self.image1 = pygame.transform.scale(self.image1, (self._ratio * 3, self._ratio)) 
        self.image2 = pygame.transform.scale(self.image2, (self._ratio * 3, self._ratio)) 
        self.image3 = pygame.transform.scale(self.image3, (self._ratio * 3, self._ratio)) 
        self.image4 = pygame.transform.scale(self.image4, (self._ratio * 3, self._ratio)) 

        self.image = pygame.transform.scale(self.image, (self._ratio * 3, self._ratio)) 
        
        self.rect = self.image.get_rect()
        self.rect.width /= 3
        self.dy = self._ratio / 10
        self.Rect = [] 

        self.images0 = []
        self.images1 = []
        self.images2 = []
        self.images3 = []
        self.images4 = []

        self.fishs = []

        self.num = 0
        for i in xrange( 3 ):
            self.Rect.append((0 + i * self._ratio, 0, self._ratio, self._ratio))
            self.images0.append(self.image0.subsurface(self.Rect[ -1 ]))
            self.images1.append(self.image1.subsurface(self.Rect[ -1 ]))
            self.images2.append(self.image2.subsurface(self.Rect[ -1 ]))
            self.images3.append(self.image3.subsurface(self.Rect[ -1 ]))
            self.images4.append(self.image4.subsurface(self.Rect[ -1 ]))
            self.fishs.append(self.image.subsurface(self.Rect[ -1 ]))

        self.rect.center = (70, 410)
        self.TURNRATE = 10
        self.dir = 45
        self.charge = 5
        self.pressed = 0
        self.background = background
        self.throw = 0
        self.dying = 0
        self.lives = 20

    def update(self):
        if self.exist:
            if not self.dying:
                if self.color == 0:
                    self.image = self.images0[ self.num/10 ]
                    self.num += 1
                    if self.num >= 30:
                        self.num %= 30
                if self.color == 1:
                    self.image = self.images1[ self.num/10 ]
                    self.num += 1
                    if self.num >= 30:
                        self.num %= 30               
                if self.color == 2:
                    self.image = self.images2[ self.num/10 ]
                    self.num += 1
                    if self.num >= 30:
                        self.num %= 30
                if self.color == 3:
                    self.image = self.images3[ self.num/10 ]
                    self.num += 1
                    if self.num >= 30:
                        self.num %= 30
                if self.color == 4:
                    self.image = self.images4[ self.num/10 ]
                    self.num += 1
                    if self.num >= 30:
                        self.num %= 30

                self.checkKeys()
         
                self.rect.centerx -= random.randrange(0, self.dy)
                if self.rect.left < 0:
                    self.reset()

                self.throw += 1
            else:
                #print self.dying
                self.rect.centery -= random.randrange(0, self.dy)
                self.dying -= 1
                if self.rect.top <= 0 and self.dying <= 0:
                    self.reset()
                    self.dying = 0
        else:
            self.rect.centerx = 200
            self.rect.centery = 100
            self.image = self.images0[ self.num/10 ]
            self.num += 1
            if self.num >= 30:
                self.num %= 30
        
    def checkKeys(self):
        #check that if the mouse is being pressed
        keys = pygame.mouse.get_pressed()
        if keys[0] == True:
            self.pressed = 1
            self.charge -= 1
            if self.charge < 0:
                self.charge = 200         
        if self.throw >= random.randrange(30,50):
            self.throw = 0

            if random.randrange(30,50) >= 45:
                self.bubble1.x = self.rect.centerx
                self.bubble1.y = self.rect.centery
                self.bubble1.speed = random.randrange(5,10)
                self.bubble1.dir = random.randrange(170, 230)
                self.bubble1.calcVector()
            
            if random.randrange(30,50) >= 35:
                self.bubble2.x = self.rect.centerx
                self.bubble2.y = self.rect.centery
                self.bubble2.speed = random.randrange(5,10)
                self.bubble2.dir = random.randrange(270, 330)
                self.bubble2.calcVector()

    def die(self):
        self.music.snd_enemyDie.play()
        self.lives = 20
        self.dying = random.randrange(300,400)
        if self.color == 0:
            self.image = pygame.image.load(p("JellyImages","dieJelly0.png"))
        if self.color == 1:
            self.image = pygame.image.load(p("JellyImages","dieJelly1.png"))
        if self.color == 2:
            self.image = pygame.image.load(p("JellyImages","dieJelly2.png"))
        if self.color == 3:
            self.image = pygame.image.load(p("JellyImages","dieJelly3.png"))
        if self.color == 4:
            self.image = pygame.image.load(p("JellyImages","dieJelly4.png"))

        self.image = pygame.transform.scale(self.image, (self._ratio, self._ratio))

    def reset(self):
        self.rect.centerx = 930
        self.rect.centery = random.randrange(50, 200)
        self.color = random.randrange(0,5)
        self.dy = self._ratio / random.randrange(8,18)
