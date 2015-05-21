import pygame
pygame.init()

#SCREEN
w = 800
h = 600
screen = pygame.display.set_mode((w,h))
            
class Object():
    def __init__(self, screen, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.screen = screen
        self.w = image.get_rect()[2]
        self.h = image.get_rect()[3]
    def draw(self):
        x = self.x
        y = self.y
        self.screen.blit(self.image, (x,y))
        
class Ship(Object):
    def __init__(self, screen, x, y, image, speed):
        Object.__init__(self, screen, x, y, image)
        self.speed = speed
    def move(self, dir):
        if dir == 'l':
            self.x -= self.speed
        else:
            self.x += self.speed
        
class Bullet(Object):
    def __init__(self, screen, x, y, image):
        Object.__init__(self, screen, x, y, image)
    def draw(self):
        Object.draw(self)
        
    def move(self, speed):
        self.y -= speed
        
class Enemy(Object):
    def __init__(self, screen, x, y, image):
        Object.__init__(self, screen, x, y, image)
        self.w = image.get_rect()[2]
    def draw(self):
        Object.draw(self)
    
    def move(self, fallspeed):
        self.y += fallspeed
        
class Weapon(Object):
    def __init__(self, screen, x, y, image):
        Object.__init__(self, screen, x, y, image)
        self.On = False
        
    def draw(self):
        Object.draw(self)
        
    def move(self, speed):
        self.y -= speed