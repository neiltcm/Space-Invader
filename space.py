import pygame
import sys, os
from pygame.locals import *
from functions import *
from classes import *

pygame.init()
pygame.mouse.set_visible(0)

def run_game():
    clock = pygame.time.Clock()
    
    #IMAGES
    background = pygame.image.load("img/space_bg.png")
    bgbox = background.get_rect()
    bg_w = bgbox[2]
    bg_h = bgbox[3]
    
    shipimg = pygame.image.load("img/spaceship.png")
    enemy = pygame.image.load("img/enemy.jpg")
    bullet = pygame.image.load("img/bullet.jpg")
    lineweapon = pygame.image.load("img/lineweapon.png")
    weaponicon = pygame.image.load("img/weapicon.jpg")
    
    shipbox = shipimg.get_rect()
    ship_height = shipbox[3]
    ship_width = shipbox[2]
    
    bulletbox = bullet.get_rect()
    bullet_height = bulletbox[3]
    bullet_width = bulletbox[2]
    
    enemybox = enemy.get_rect()
    enemy_width = enemybox[2]
    enemy_height = enemybox[3]
    
    linebox = lineweapon.get_rect()
    line_width = linebox[2]
    line_height = linebox[3]
    
    wiconbox = weaponicon.get_rect()
    icon_width = wiconbox[2]
    
    #SCREEN
    w = bg_w
    h = bg_h
    screen = pygame.display.set_mode((w,h))
    
    
    #VARIABLES
    track = 0
    bulletspeed = 10
    fallspeed = 0.5
    weaponfallspeed = 6
    threshold = 30
    score = 0
    life = 20
    level = 1
    bulletcount = 0
    
    #SWITCHES
    GameActive = True
    DisplaySpecial = False
    special = 0
    
    #CHARACTERS
    ship = Ship(screen, 300, h-(ship_height), shipimg, 10)
    weaponlist = []
    blist = []
    enemylist = []
    weaponicon = Enemy(screen, random.randint(0, w-icon_width), 0, weaponicon)
    
    #font
    gamefont = pygame.font.Font(None, 20)
    losefont = pygame.font.Font(None, 100)
    
    losetext = losefont.render('YOU LOST!', 2, [255,255,255])
    losebox = losetext.get_rect()
    lose_xpos = w/2 - (losebox[2]/2)
    
    specialtext = gamefont.render('SPECIALS: '+str(special), 2, [255,255,255])
    specialbox = specialtext.get_rect()
    sp_x = w - 10 - specialbox[2]
    
    while 1:
        clock.tick(49)
        screen.blit(background, (0,0))
        #ship movement
        keystate = pygame.key.get_pressed()
        #screenbound
        shipcollision(keystate, screen, ship, w, h)
        
        #TEXTS
        scoretext = gamefont.render('SCORE: '+str(score), 2, [255,255,255])
        lifetext = gamefont.render('LIVES REMAINING: '+str(life), 2, [255,255,255])
        leveltext = gamefont.render('LEVEL: '+str(level), 2, [255,255,255])
        specialtext = gamefont.render('SPECIALS: '+str(special), 2, [255,255,255])
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == KEYDOWN and GameActive == True:
                if event.key == K_SPACE:
                    blist.append(Bullet(screen, ship.x+(ship.w/2)-(bullet_width/2), h-ship_height-bullet_height, bullet))
                    bulletcount += 1
                    if bulletcount > 0 and bulletcount%100 == 0:
                        DisplaySpecial = True
                        fallspeed += 0.25
                        level += 1
                        threshold -= 6
                elif event.key == K_s:
                    if special > 0:
                        special -= 1
                        weaponlist.append(Weapon(screen, ship.x + (ship.w/2) - line_width/2, ship.y - line_height, lineweapon))
                        
                
        #creation of enemies
        if track%threshold == 0:
            enemylist.append(Enemy(screen, random.randint(0, w-enemy_width), 0, enemy))
        track += 1
                
        
        #bullet and enemies movement/display
        drawAllbullet(blist,bulletspeed)
        life -= drawAllenemy(enemylist, fallspeed, h)
        if life <= 0:
            screen.blit (losetext, (lose_xpos, 200))
            GameActive = False
        if blist and enemylist:
            if collision(blist, enemylist):
                score += 1
                
        #weapon movement/display
        if DisplaySpecial == True:
            status = drawSpecial(weaponicon, ship, weaponfallspeed, h)
            if status != False:
                weaponicon.x = random.randint(0, w-icon_width)
                weaponicon.y = 0 
                DisplaySpecial = False
                if status == 's':
                    special += 2 * level
                    
        #specialweapon movement/display/collision
        drawline(weaponlist, bulletspeed)
        if enemylist:
            score += weaponcollision(weaponlist, enemylist)
        
            
                
        #DISPLAY SCORE   
        screen.blit(scoretext, [5,5])
        screen.blit(lifetext, [5,20])
        screen.blit(leveltext, [5, 35])
        screen.blit(specialtext, [sp_x, 5])
        
        pygame.display.flip()
        
run_game()
    
    
    
    


