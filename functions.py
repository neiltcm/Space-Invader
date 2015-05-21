import pygame, random
from pygame.locals import *
pygame.init()


def randomize():
    num = random.randint(32,800-32)
    return num

def collision(bullet,target):
    if (abs(bullet.y-target.y) < bullet.rad + target.rad and abs(bullet.x - target.x) < bullet.rad + target.rad):
        return True
    else:
        return False
    
def shipcollision(keystate, screen, ship, width, height):
    left = keystate[K_LEFT]
    right = keystate[K_RIGHT]
    if left == True:
        ship.x -= ship.speed
    elif right == True:
        ship.x += ship.speed
    screen.blit(ship.image, (ship.x, height-ship.h))
    if ship.x + (ship.w) >= width:
        ship.x = width - ship.w
        screen.blit(ship.image, (width-ship.w, height-ship.h))
    elif ship.x <= 0:
        ship.x = 0
        screen.blit(ship.image, (0, height-ship.h))
        
        
def drawAllbullet(blist, bulletspeed):
    for i in blist:
        i.move(bulletspeed)
        if i.y + i.h <= 0:
            blist.remove(i)
        i.draw()
        
def drawAllenemy(enemylist, fallspeed, screen_height):
    liveslost = 0
    for i in enemylist:
        i.move(fallspeed)
        i.draw()
        if i.y >= screen_height:
            enemylist.remove(i)
            liveslost += 1
    return liveslost

def drawSpecial(special, ship, fallspeed, screen_height):
    special.move(fallspeed)
    special.draw()
    if (special.y >= screen_height):
        return 'w'
    elif special.y + special.h >= ship.y:
        if (special.x + special.w) > ship.x and special.x < ship.x + ship.w:
            return 's'
        else:
            return False
    else:
        return False
        
        
def drawline(weaponlist, speed):
    for i in weaponlist:
        i.move(speed)
        i.draw()
        if i.y <= 0:
            weaponlist.remove(i)
    
def weaponcollision(weaponlist, elist):
    addscore = 0
    for i in weaponlist:
        for j in elist:
            if j.y >= i.y and (j.x+j.w) > i.x and j.x < i.x + i.w:
                addscore += 1
                elist.remove(j)
    return addscore
        
def collision(blist, elist):
    collided = False
    for i in blist:
        for j in elist:
            if (i.y - j.y) <= j.h and (i.x+i.w) > j.x and i.x < (j.x+j.w):
                elist.remove(j)
                collided = True
                break
        if collided == True:
            blist.remove(i)
            return True
    return False