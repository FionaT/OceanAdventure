import pygame, random, math
from music import *

#           /--------\
#__________/  player  \_________________
class Player(pygame.sprite.Sprite):
    def __init__(self, shells, screen, background, gender):
        pygame.sprite.Sprite.__init__(self)
        self.gender = gender
        self.loadImages()
        self.image = self.imageStand
        self.background = background
        self.screen = screen
        self.rect = self.image.get_rect()
        self.walls = pygame.sprite.OrderedUpdates()
        self.music = Music()
        
        self.shells = shells

        self.dx = 0
        self.dy = 0
        self.dir = 0
        self.speed = 0
        self.accel = 0.9
        self.gravi = .5
        self.state = "stand"
        self.lastState = "stand"
        self.key = "down"
        self.flag = 0
        self.jumpState = "rising"

        self.frame = 0
        self.delay = 3
        self.pause = 0

        self.x = 320
        self.y = 240
        self.rect.center = (self.x, self.y)

    def update(self):

        self.check_keys()
        self.get_new_state()
        self.set_new_state()
        self.calc_pos()
        self.check_pos()
        self.take_action()

    def check_keys(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.flag = 1
            self.key = "up"
            self.music.snd_jump.play()

        elif keys[pygame.K_DOWN]:
            self.key = "down"

        elif keys[pygame.K_LEFT]:
            self.key = "left"

        elif keys[pygame.K_RIGHT]:
            self.key = "right"
        else:
            self.key = "no press"

        if keys[pygame.K_a]:
            self.music.snd_shoot.play()
            newShell = Shell(self.screen)
            newShell.x = self.rect.centerx
            newShell.y = self.rect.centery
            newShell.speed = 25
            newShell.dir = 180

            self.shells.add(newShell) 

        if keys[pygame.K_w]:
            self.music.snd_shoot.play()
            newShell = Shell(self.screen)
            newShell.x = self.rect.centerx
            newShell.y = self.rect.centery
            newShell.speed = 25
            newShell.dir = 90

            self.shells.add(newShell) 

        if keys[pygame.K_d]:
            self.music.snd_shoot.play()
            newShell = Shell(self.screen)
            newShell.x = self.rect.centerx
            newShell.y = self.rect.centery
            newShell.speed = 25
            newShell.dir = 0

            self.shells.add(newShell) 

        if keys[pygame.K_s]:
            self.music.snd_shoot.play()
            newShell = Shell(self.screen)
            newShell.x = self.rect.centerx
            newShell.y = self.rect.centery
            newShell.speed = 25
            newShell.dir = 270

            self.shells.add(newShell) 

    def get_new_state(self):


        if self.state == "stand" or self.state == "walk":
            if self.key == "up":
                self.state = "jump"
            if self.key == "down":
                self.state = "stand"
            if self.key == "right":
                self.state = "walk"
            if self.key == "left":
                self.speed = 0
                self.state = "walkback"
        elif self.state == "walkback":
            if self.key == "up":
                self.state = "jumpback"
            if self.key == "down":
                self.state = "stand"
            if self.key == "right":
                self.speed = 0
                self.state = "walk"
            if self.key == "left":
                self.state = "walkback"             
        elif self.state == "jump":
            if self.key == "up":
                self.state = "jump"
            if self.key == "down" or self.key == "right" or self.key == "left":
                self.state = "stand"
                self.jumpState == "droping"
                self.speed = 0
        elif self.state == "jumpback":
            if self.key == "up":
                self.state = "jumpback"
            if self.key == "down" or self.key == "right" or self.key == "left":
                self.state = "stand"
                self.jumpState == "droping"
                self.speed = 0
        
        self.key = "no press"
        #print "***state", self.state

    def set_new_state(self):

        if self.state == "stand":
            self.speed = 0
            self.dir = 0

        if self.state == "walk":
            self.speed += self.accel
            self.dir = 0
            if self.speed >= 8:
                self.speed = 8

        if self.state == "walkback":  
            self.speed -= self.accel
            self.dir = 0
            if self.speed <= -8:
                self.speed = -8

        if self.state == "jump":
            self.speed = 12
            self.dir = 50

        if self.state == "jumpback":   
            self.speed = 12           
            self.dir = 130
        
        #print "speed", self.speed, "dir", self.dir, "flag", self.flag

    def calc_pos(self):
        if self.state == "walk" or self.state == "walkback" or self.state == "stand":
            radians = self.dir * math.pi / 180
            self.dx = math.cos(radians)
            self.dy = math.sin(radians)
            self.dx *= self.speed
            self.dy *= self.speed
            self.dy *= -1
            self.dy = 0

        radians = self.dir * math.pi / 180

        if self.dir == 50:
            if self.flag == 1:
                self.flag = 0
                self.dx = math.cos(radians)
                self.dy = math.sin(radians)
                self.dx *= self.speed
                self.dy *= self.speed
                self.dy *= -1

            self.dy += self.gravi
            #print "self.dy += self.gravi", self.dy

        if self.dir == 130:
            if self.flag == 1:
                self.flag = 0
                self.dx = math.cos(radians)
                self.dy = math.sin(radians)
                self.dx *= self.speed
                self.dy *= self.speed
                self.dy *= -1
            self.dy += self.gravi

        #print "dx", self.dx, "dy", self.dy
        
        if self.dy <= 0:
            self.jumpState = "rising"
        else:
            self.jumpState = "droping"
        
        self.x += self.dx
        self.y += self.dy 

    def check_pos(self):
        if self.x > self.screen.get_width() - 40:
            self.x = self.screen.get_width() - 40
            self.state = "stand"
        if self.x < 40:
            self.x = 40
            self.state = "stand"
        if self.y > self.screen.get_height() - 60:
            self.state = "stand"
            self.y = 406
        if self.y < 60:
            self.y = 40

        if self.jumpState == "droping":
            crash = pygame.sprite.spritecollide(self, self.walls, False)
            if crash:
                self.y = 260
                self.state = "stand"
        
        if self.state == "stand" or self.state == "walk" or self.state == "walkback":
            if self.y <= 270:
                self.y = 270

            self.rect.center = (self.x, self.y)
            crash = pygame.sprite.spritecollide(self, self.walls, False)

            if crash:
                self.y = 270
            else:
                self.y = 406

    def take_action(self):
        if self.state == "stand":
            self.stand()
        elif self.state == "walk":
            self.walk()
        elif self.state == "walkback":
            self.walkback()
        elif self.state == "jump":
            self.jump()
        elif self.state == "jumpback":
            self.jumpback()
        
        self.rect.center = (self.x, self.y)
        

    def stand(self):
        self.pause += 1
        if self.pause >= self.delay:
            #reset pause and advance animation
            self.pause = 0
            self.image = self.walkImages[1]

    def walk(self):
        self.lastDir = 1
        self.lastAct = "stand"
        self.pause += 1
        if self.pause >= self.delay:
            #reset pause and advance animation
            self.pause = 0
            self.frame += 1
            if self.frame >= len(self.walkImages):
                self.frame = 0
            self.image = self.walkImages[self.frame]    

    def walkback(self):
        self.lastDir = 0
        self.lastAct = "walk"
        self.pause += 1
        if self.pause >= self.delay:
            #reset pause and advance animation
            self.pause = 0
            self.frame += 1
            if self.frame >= len(self.walkbackImages):
                self.frame = 0
            self.image = self.walkbackImages[self.frame] 

    def jump(self):
        self.lastDir = 1
        self.lastAct = "walkback"
        self.pause += 1
        if self.pause >= self.delay:
            #reset pause and advance animation
            self.pause = 0
            self.image = self.walkImages[1]

    def jumpback(self):
        self.lastDir = 0
        self.lastAct = "jump"
        self.pause += 1
        if self.pause >= self.delay:
            #reset pause and advance animation
            self.pause = 0
            self.image = self.walkbackImages[1]

    def loadImages(self):
        if self.gender == 0:
            self.imageStand = pygame.image.load("playerImages/Gstand4.png")
        else:
            self.imageStand = pygame.image.load("playerImages/Bstand4.png")

        self.imageStand = self.imageStand.convert()
        transColor = self.imageStand.get_at((1, 1))
        self.imageStand.set_colorkey(transColor)

        self.walkImages = []
        for i in range(4):
            if self.gender == 0:
                imgName = "playerImages/Gwalk%d.png" % i
                tmpImage = pygame.image.load(imgName)
                tmpImage = tmpImage.convert()
                transColor = tmpImage.get_at((1, 1))
                tmpImage.set_colorkey(transColor)
                self.walkImages.append(tmpImage)
            else:
                imgName = "playerImages/Bwalk%d.png" % i
                tmpImage = pygame.image.load(imgName)
                tmpImage = tmpImage.convert()
                transColor = tmpImage.get_at((1, 1))
                tmpImage.set_colorkey(transColor)
                self.walkImages.append(tmpImage)

        self.walkbackImages = []
        for i in range(4):
            if self.gender == 0:
                imgName = "playerImages/Gwalkback%d.png" % i
                tmpImage = pygame.image.load(imgName)
                tmpImage = tmpImage.convert()
                transColor = tmpImage.get_at((1, 1))
                tmpImage.set_colorkey(transColor)
                self.walkbackImages.append(tmpImage) 
            else:
                imgName = "playerImages/Bwalkback%d.png" % i
                tmpImage = pygame.image.load(imgName)
                tmpImage = tmpImage.convert()
                transColor = tmpImage.get_at((1, 1))
                tmpImage.set_colorkey(transColor)
                self.walkbackImages.append(tmpImage) 



#           /--------\
#__________/  shell   \_________________
class Shell(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        
        self.image = pygame.Surface((10, 10))
        self.image.fill((0xff, 0xff, 0xff))
        self.image.set_colorkey((0xff, 0xff, 0xff))
        pygame.draw.circle(self.image, (0, 0, 0), (5, 5), 5)
        #self.image = pygame.transform.scale(self.image, (5, 5))
        self.rect = self.image.get_rect()
        self.rect.center = (-100, -100)
        self.image = pygame.image.load("explosion.png")
        self.image = pygame.transform.scale(self.image, (32*17, 32))
        self.speed = 0
        self.dir =0
        self.reset()



        self.Rect = [] 
        self.explosions = []
        self.num = 0
        for i in xrange( 17 ):
            self.Rect.append((0 + i * 32, 0, 32, 32))
            self.explosions.append( self.image.subsurface( self.Rect[ -1 ] ) )

    def update(self):

        self.image = self.explosions[ self.num ]
        self.rect = self.image.get_rect()

        self.num += 1
        if self.num >= 17:
            self.num %= 17

        self.calcVector()
        self.calcPos()
        self.checkBounds()
        self.rect.center = (self.x, self.y)
   
    def calcVector(self):
        radians = self.dir * math.pi / 180
        
        self.dx = self.speed * math.cos(radians)
        self.dy = self.speed * math.sin(radians)
        self.dy *= -1
    
    def calcPos(self):
        self.x += self.dx
        self.y += self.dy
    
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
    
    def reset(self):
        """ move off stage and stop"""
        self.x = -100
        self.y = -100
        self.speed = 0

