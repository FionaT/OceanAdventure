import pygame, random, math
from player3 import *
from ocean import *
from wall import *
from shark import *
from monster import *
from whale import *
from jellyFish import *
from award import *
from present import *
from music import *

pygame.init()
pygame.key.set_repeat(100,100)
screen = pygame.display.set_mode((1000, 480))

monsterLocation = 700

#             /---------------------\
#____________/  game function        \___________________________________
def level1(gender):
    
    pygame.display.set_caption("ocean Adventure")
       
    background = pygame.Surface(screen.get_size())
    background.fill((74, 92, 98))
    screen.blit(background, (0, 0))
    scoreboard = Scoreboard()
 

    music = Music()

    #create the objects that will show in the game
    wall = []
    wallNum = 32
    for i in range(wallNum):
        wall.append(Wall(i))    

    shark = []
    sharkNum = 2
    for i in range(sharkNum):
        shark.append(Shark(screen))   
        
    whale = []
    whaleNum = 1
    for i in range(whaleNum):
        whale.append(Whale(screen))       

    highWall = []
    highWallNum = 40

    diamond = []
    diamondNum = 35

    coin = []
    coinNum = 32


    bubble1 = Bubble(screen, background)
    bubble2 = Bubble(screen, background)
    jellyFish1 = JellyFish(bubble1, bubble2, background)

    shell = Shell(screen)
    shells = pygame.sprite.OrderedUpdates(shell)  
    player = Player(shells, screen, background, gender)  
    ocean = Ocean(screen, player, 1) 

    #set Monster Boss
    MonsterBubble1 = MonsterBubble(screen, background)
    MonsterBubble2 = MonsterBubble(screen, background)
    monster = Monster( MonsterBubble1, MonsterBubble2, screen, 1)  
    monsters = pygame.sprite.OrderedUpdates(MonsterBubble1, MonsterBubble2, monster)
    monsterFlag = 0
    monsterLife = Lifeboard(monster.lives)

    for i in range(diamondNum):
        diamond.append(Diamond(i, screen, ocean))   

    diamonds = pygame.sprite.OrderedUpdates()

    for i in range(diamondNum):
        diamonds.add(diamond[i])

    for i in range(coinNum):
        coin.append(Coin(i, screen, ocean))   

    coins = pygame.sprite.OrderedUpdates()

    for i in range(coinNum):
        coins.add(coin[i])

    whales = pygame.sprite.OrderedUpdates()
    for i in range(whaleNum):
        whales.add(whale[i]) 
    
    allSprites = pygame.sprite.OrderedUpdates(ocean, scoreboard, monsterLife)

    playerSprites = pygame.sprite.OrderedUpdates(player) 
  

    enemySprites = pygame.sprite.OrderedUpdates(jellyFish1, bubble1, bubble2 )

    for i in range(sharkNum):
        enemySprites.add(shark[i])     

    for i in range(highWallNum):
        highWall.append(HighWall(i, screen, ocean))   

    highWalls = pygame.sprite.OrderedUpdates()


    for i in range(wallNum):
        allSprites.add(wall[i]) 
        
    for i in range(highWallNum):
        highWalls.add(highWall[i])

    player.walls = highWalls

    flag = 0

    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:

        
        clock.tick(20)

        print ocean.x

        #music.snd_gameBG.play(-2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False                  
        crash_shell_shark0 = pygame.sprite.spritecollide(shark[0], shells, False)

        if crash_shell_shark0:
            shark[0].lives -= 1
            if shark[0].lives <= 0:
                shark[0].die()     
                
        crash_shell_shark1 = pygame.sprite.spritecollide(shark[1], shells, False)

        if crash_shell_shark1:
            shark[1].lives -= 1
            if shark[1].lives <= 0:
                shark[1].die()           

        crash_shell_jelly1 = pygame.sprite.spritecollide(jellyFish1, shells, False)

        if crash_shell_jelly1:
            jellyFish1.lives -= 1
            if jellyFish1.lives <= 0:
                jellyFish1.die()  
        
        crash_shell_monster = pygame.sprite.spritecollide(monster, shells, False)

        if crash_shell_monster and monsterFlag:
            monster.lives -= 1
            monsterLife.lives -= 1
            if monster.lives <= 0:
                monster.die()         

        crash_player_diamond = pygame.sprite.spritecollide(player, diamonds, False)

        if crash_player_diamond:
            music.snd_gainDiamond.play()
            scoreboard.score += 100
            for theDiamond in crash_player_diamond:
                if theDiamond.color >= 8:
                    scoreboard.lives += 1
                    music.snd_gainLife.play()
                theDiamond.disappear()
                
        crash_player_coin = pygame.sprite.spritecollide(player, coins, False)

        if crash_player_coin:
            music.snd_gainCoin.play()
            scoreboard.score += 50
            for theCoin in crash_player_coin:
                theCoin.disappear()

        crash_player_enemySprites = pygame.sprite.spritecollide(player, enemySprites, False)

        if crash_player_enemySprites:
            #if scoreboard.lives <= 0:
            for theEnemy in crash_player_enemySprites:
                if theEnemy.dying == 0:
                    scoreboard.lives -= 1
                    music.snd_loseLife.play()
                    if scoreboard.lives <= 0:
                        keepGoing = False
                    theEnemy.reset()

        crash_player_monsters = pygame.sprite.spritecollide(player, monsters, False)
        if monsterFlag:
            if crash_player_monsters:
                #if scoreboard.lives <= 0:
                for theEnemy in crash_player_monsters:
                    if theEnemy.dying == 0:
                        scoreboard.lives -= 0.1
                        music.snd_loseLife.play()
                        if scoreboard.lives <= 0:
                            keepGoing = False
                        theEnemy.reset()

        
        print ocean.x

        if monster.lives <= 0:
            keepGoing = False
        
        if keepGoing == False:
            if monster.lives > 0:
                scoreboard.score = -999

        if ocean.x <= -monsterLocation:
            monsterFlag = 1
            shark[0].exist = 0
            shark[1].exist = 0
            jellyFish1.exist = 0 
               
        #if monster
        #if keepGoing == False:
            #if ocean.x >= -1300:
                #scoreboard.score = 0
     
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        playerSprites.update()
        playerSprites.draw(screen)
        shells.update()
        shells.draw(screen)
        enemySprites.update()
        enemySprites.draw(screen)
        highWalls.update()
        highWalls.draw(screen)
        diamonds.update()
        diamonds.draw(screen)
        coins.update()
        coins.draw(screen)
        whales.update()
        whales.draw(screen) 

        if monsterFlag:
            monsters.update()
            monsters.draw(screen)

        pygame.display.flip()

    return scoreboard.score

#             /---------------------\
#____________/  game function        \___________________________________
def level2(gender):
    
    pygame.display.set_caption("ocean Adventure")
       
    background = pygame.Surface(screen.get_size())
    background.fill((74, 92, 98))
    screen.blit(background, (0, 0))
    scoreboard = Scoreboard()
    music = Music()

    #set Monster Boss
    MonsterBubble1 = MonsterBubble(screen, background)
    MonsterBubble2 = MonsterBubble(screen, background)
    monster = Monster( MonsterBubble1, MonsterBubble2, screen, 2)  
    monsters = pygame.sprite.OrderedUpdates(MonsterBubble1, MonsterBubble2, monster)
    monsterFlag = 0
    monsterLife = Lifeboard(monster.lives)

    #create the objects that will show in the game
    wall = []
    wallNum = 32
    for i in range(wallNum):
        wall.append(Wall(i))    

    shark = []
    sharkNum = 2
    for i in range(sharkNum):
        shark.append(Shark(screen))   
        
    whale = []
    whaleNum = 2
    for i in range(whaleNum):
        whale.append(Whale(screen))       

    highWall = []
    highWallNum = 25

    diamond = []
    diamondNum = 15

    coin = []
    coinNum = 32


    bubble1 = Bubble(screen, background)
    bubble2 = Bubble(screen, background)
    bubble3 = Bubble(screen, background)
    bubble4 = Bubble(screen, background)
    jellyFish1 = JellyFish(bubble1, bubble2, background)
    jellyFish2 = JellyFish(bubble3, bubble4, background)

    shell = Shell(screen)
    shells = pygame.sprite.OrderedUpdates(shell)  
    player = Player(shells, screen, background, gender)  
    ocean = Ocean(screen, player, 2) 

    for i in range(diamondNum):
        diamond.append(Diamond(i, screen, ocean))   

    diamonds = pygame.sprite.OrderedUpdates()

    for i in range(diamondNum):
        diamonds.add(diamond[i])

    for i in range(coinNum):
        coin.append(Coin(i, screen, ocean))   

    coins = pygame.sprite.OrderedUpdates()

    for i in range(coinNum):
        coins.add(coin[i])

    whales = pygame.sprite.OrderedUpdates()
    for i in range(whaleNum):
        whales.add(whale[i]) 
    
    allSprites = pygame.sprite.OrderedUpdates(ocean, scoreboard, monsterLife)

    playerSprites = pygame.sprite.OrderedUpdates(player) 
  

    enemySprites = pygame.sprite.OrderedUpdates(jellyFish1, bubble1, bubble2, jellyFish2, bubble3, bubble4)

    for i in range(sharkNum):
        enemySprites.add(shark[i])     

    for i in range(highWallNum):
        highWall.append(HighWall(i, screen, ocean))   

    highWalls = pygame.sprite.OrderedUpdates()


    for i in range(wallNum):
        allSprites.add(wall[i]) 
        
    for i in range(highWallNum):
        highWalls.add(highWall[i])

    player.walls = highWalls

    flag = 0
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:

        
        clock.tick(20)

        #music.snd_gameBG.play(-2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False                  
        crash_shell_shark0 = pygame.sprite.spritecollide(shark[0], shells, False)

        if crash_shell_shark0:
            shark[0].lives -= 1
            if shark[0].lives <= 0:
                shark[0].die()

        crash_shell_shark1 = pygame.sprite.spritecollide(shark[1], shells, False)

        if crash_shell_shark1:
            shark[1].lives -= 1
            if shark[1].lives <= 0:
                shark[1].die()             

        crash_shell_jelly1 = pygame.sprite.spritecollide(jellyFish1, shells, False)

        if crash_shell_jelly1:
            jellyFish1.lives -= 1
            if jellyFish1.lives <= 0:
                jellyFish1.die()  

        crash_shell_jelly2 = pygame.sprite.spritecollide(jellyFish2, shells, False)

        if crash_shell_jelly2:
            jellyFish2.lives -= 1
            if jellyFish2.lives <= 0:
                jellyFish2.die()  

        crash_shell_monster = pygame.sprite.spritecollide(monster, shells, False)

        if crash_shell_monster and monsterFlag:
            monster.lives -= 1
            monsterLife.lives -= 1
            if monster.lives <= 0:
                monster.die() 

        crash_player_diamond = pygame.sprite.spritecollide(player, diamonds, False)

        if crash_player_diamond:
            music.snd_gainDiamond.play()
            scoreboard.score += 100
            for theDiamond in crash_player_diamond:
                if theDiamond.color >= 8:
                    scoreboard.lives += 1
                    music.snd_gainLife.play()
                theDiamond.disappear()
                
        crash_player_coin = pygame.sprite.spritecollide(player, coins, False)

        if crash_player_coin:
            music.snd_gainCoin.play()
            scoreboard.score += 50
            for theCoin in crash_player_coin:
                theCoin.disappear()

        crash_player_enemySprites = pygame.sprite.spritecollide(player, enemySprites, False)

        if crash_player_enemySprites:
            #if scoreboard.lives <= 0:
            for theEnemy in crash_player_enemySprites:
                if theEnemy.dying == 0:
                    scoreboard.lives -= 1
                    music.snd_loseLife.play()
                    if scoreboard.lives <= 0:
                        keepGoing = False
                    theEnemy.reset()

        crash_player_monsters = pygame.sprite.spritecollide(player, monsters, False)
        if monsterFlag:
            if crash_player_monsters:
                #if scoreboard.lives <= 0:
                for theEnemy in crash_player_monsters:
                    if theEnemy.dying == 0:
                        scoreboard.lives -= 0.1
                        music.snd_loseLife.play()
                        if scoreboard.lives <= 0:
                            keepGoing = False
                        theEnemy.reset()

        
        print ocean.x

        if monster.lives <= 0:
            keepGoing = False
        
        if keepGoing == False:
            if monster.lives > 0:
                scoreboard.score = -999

        if ocean.x <= -monsterLocation:
            monsterFlag = 1
            shark[0].exist = 0
            shark[1].exist = 0
            jellyFish1.exist = 0             

        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        playerSprites.update()
        playerSprites.draw(screen)
        shells.update()
        shells.draw(screen)
        enemySprites.update()
        enemySprites.draw(screen)
        highWalls.update()
        highWalls.draw(screen)
        diamonds.update()
        diamonds.draw(screen)
        coins.update()
        coins.draw(screen)
        whales.update()
        whales.draw(screen) 

        if monsterFlag:
            monsters.update()
            monsters.draw(screen)        

        pygame.display.flip()

    return scoreboard.score
#             /---------------------\
#____________/  game function        \___________________________________
def level3(gender):
    
    pygame.display.set_caption("ocean Adventure")
       
    background = pygame.Surface(screen.get_size())
    background.fill((74, 92, 98))
    screen.blit(background, (0, 0))
    scoreboard = Scoreboard()
    music = Music()


    #set Monster Boss
    MonsterBubble1 = MonsterBubble(screen, background)
    MonsterBubble2 = MonsterBubble(screen, background)
    monster = Monster( MonsterBubble1, MonsterBubble2, screen, 3)  
    monsters = pygame.sprite.OrderedUpdates(MonsterBubble1, MonsterBubble2, monster)
    monsterFlag = 0
    monsterLife = Lifeboard(monster.lives)  

    #create the objects that will show in the game
    wall = []
    wallNum = 32
    for i in range(wallNum):
        wall.append(Wall(i))    

    shark = []
    sharkNum = 3
    for i in range(sharkNum):
        shark.append(Shark(screen))   
        
    whale = []
    whaleNum = 2
    for i in range(whaleNum):
        whale.append(Whale(screen))       

    highWall = []
    highWallNum = 20

    diamond = []
    diamondNum = 40

    coin = []
    coinNum = 32


    bubble1 = Bubble(screen, background)
    bubble2 = Bubble(screen, background)
    bubble3 = Bubble(screen, background)
    bubble4 = Bubble(screen, background)
    jellyFish1 = JellyFish(bubble1, bubble2, background)
    jellyFish2 = JellyFish(bubble3, bubble4, background)

    shell = Shell(screen)
    shells = pygame.sprite.OrderedUpdates(shell)  
    player = Player(shells, screen, background, gender)  
    ocean = Ocean(screen, player, 3) 

    for i in range(diamondNum):
        diamond.append(Diamond(i, screen, ocean))   

    diamonds = pygame.sprite.OrderedUpdates()

    for i in range(diamondNum):
        diamonds.add(diamond[i])

    for i in range(coinNum):
        coin.append(Coin(i, screen, ocean))   

    coins = pygame.sprite.OrderedUpdates()

    for i in range(coinNum):
        coins.add(coin[i])

    whales = pygame.sprite.OrderedUpdates()
    for i in range(whaleNum):
        whales.add(whale[i]) 
    
    allSprites = pygame.sprite.OrderedUpdates(ocean, scoreboard, monsterLife)

    playerSprites = pygame.sprite.OrderedUpdates(player) 
  

    enemySprites = pygame.sprite.OrderedUpdates(jellyFish1, bubble1, bubble2, jellyFish2, bubble3, bubble4)

    for i in range(sharkNum):
        enemySprites.add(shark[i])     

    for i in range(highWallNum):
        highWall.append(HighWall(i, screen, ocean))   

    highWalls = pygame.sprite.OrderedUpdates()


    for i in range(wallNum):
        allSprites.add(wall[i]) 
        
    for i in range(highWallNum):
        highWalls.add(highWall[i])

    player.walls = highWalls

    flag = 0
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:

        
        clock.tick(20)

        #music.snd_gameBG.play(-2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False                  
        crash_shell_shark0 = pygame.sprite.spritecollide(shark[0], shells, False)

        if crash_shell_shark0:
            shark[0].lives -= 1
            if shark[0].lives <= 0:
                shark[0].die()

        crash_shell_shark1 = pygame.sprite.spritecollide(shark[1], shells, False)

        if crash_shell_shark1:
            shark[1].lives -= 1
            if shark[1].lives <= 0:
                shark[1].die()  

        crash_shell_shark2 = pygame.sprite.spritecollide(shark[2], shells, False)

        if crash_shell_shark2:
            shark[2].lives -= 1
            if shark[2].lives <= 0:
                shark[2].die()                  
        
        crash_shell_monster = pygame.sprite.spritecollide(monster, shells, False)

        if crash_shell_monster and monsterFlag:
            monster.lives -= 1
            monsterLife.lives -= 1
            if monster.lives <= 0:
                monster.die() 

        crash_shell_jelly1 = pygame.sprite.spritecollide(jellyFish1, shells, False)

        if crash_shell_jelly1:
            jellyFish1.lives -= 1
            if jellyFish1.lives <= 0:
                jellyFish1.die()  

        crash_shell_jelly2 = pygame.sprite.spritecollide(jellyFish2, shells, False)

        if crash_shell_jelly2:
            jellyFish2.lives -= 1
            if jellyFish2.lives <= 0:
                jellyFish2.die()  

        crash_player_diamond = pygame.sprite.spritecollide(player, diamonds, False)

        if crash_player_diamond:
            music.snd_gainDiamond.play()
            scoreboard.score += 100
            for theDiamond in crash_player_diamond:
                if theDiamond.color >= 8:
                    scoreboard.lives += 1
                    music.snd_gainLife.play()
                theDiamond.disappear()
                
        crash_player_coin = pygame.sprite.spritecollide(player, coins, False)

        if crash_player_coin:
            music.snd_gainCoin.play()
            scoreboard.score += 50
            for theCoin in crash_player_coin:
                theCoin.disappear()

        crash_player_enemySprites = pygame.sprite.spritecollide(player, enemySprites, False)

        if crash_player_enemySprites:
            #if scoreboard.lives <= 0:
            for theEnemy in crash_player_enemySprites:
                if theEnemy.dying == 0:
                    scoreboard.lives -= 1
                    music.snd_loseLife.play()
                    if scoreboard.lives <= 0:
                        keepGoing = False
                    theEnemy.reset()

        crash_player_monsters = pygame.sprite.spritecollide(player, monsters, False)
        
        if monsterFlag:
            if crash_player_monsters:
                #if scoreboard.lives <= 0:
                for theEnemy in crash_player_monsters:
                    if theEnemy.dying == 0:
                        scoreboard.lives -= 0.1
                        music.snd_loseLife.play()
                        if scoreboard.lives <= 0:
                            keepGoing = False
                        theEnemy.reset()

        
        print ocean.x, monster.lives

        if monster.lives <= 0:
            keepGoing = False
        
        if keepGoing == False:
            if monster.lives > 0:
                scoreboard.score = -999

        if ocean.x <= -monsterLocation:
            monsterFlag = 1
            shark[0].exist = 0
            shark[1].exist = 0
            jellyFish1.exist = 0   
            

        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        playerSprites.update()
        playerSprites.draw(screen)
        shells.update()
        shells.draw(screen)
        enemySprites.update()
        enemySprites.draw(screen)
        highWalls.update()
        highWalls.draw(screen)
        diamonds.update()
        diamonds.draw(screen)
        coins.update()
        coins.draw(screen)
        whales.update()
        whales.draw(screen)             
 
        if monsterFlag:
            monsters.update()
            monsters.draw(screen)    
        
        pygame.display.flip()

    return scoreboard.score