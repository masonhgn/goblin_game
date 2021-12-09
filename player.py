import pygame as p
from entity import entities
from gamemap import maps, map_used
player_img = p.image.load('goblins/images/player.png')
player_velocity = 6


class player(object):
    def __init__(self,x,y,width,height, mass, left, right, top, bottom, rightReached = False, leftReached = False,
     isJump = False, collideRight = False, collideLeft = False, collideUp = False, collideDown = False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = player_velocity
        self.mass = mass
        self.rightReached = False
        self.leftReached = False
        self.isJump = False
        self.collideLeft = False
        self.collideRight = False
        self.collideUp = False
        self.collideDown = False
        self.left = 0
        self.right = 0
        self.top = 0
        self.bottom = 0



    def draw(self, w):
        self.right = self.x + self.width
        self.left = self.x
        self.bottom = self.y + self.height

        if (self.x > 500): self.rightReached = True
        if (self.x < 200): self.leftReached = True

        w.blit(player_img, (self.x, self.y))

        if self.isJump == True:
            print('jump')
            self.collideDown = False
        else:
            if self.y <= 510:
                self.y += player_velocity

        for e in entities:
                rect1 = p.Rect(e.x, e.y, e.width, e.height)
                rect2 = p.Rect(self.x,self.y,self.width,self.height)
                collide = rect1.colliderect(rect2)
                if collide:
                    #print(self.right)
                    #print(e.x)
                    if self.right >= e.x and self.right <= e.right: self.collideRight = True
                    if self.left <= e.x+e.width and self.left >= e.x: self.collideLeft = True
                    
                    if self.bottom >= e.top and self.bottom <= e.bottom - 30: self.collideDown = True
                else:
                    self.collideRight = False
                    self.collideLeft = False
                    self.collideDown = False
                if self.bottom >= 510:
                    self.collideDown = True
                


    def moveRight(self):
        if not self.collideRight:
            self.collideLeft = False
            if self.rightReached:
                for e in entities:
                    e.moveRight(self.vel)
                maps[map_used].moveRight(self.vel)
            else: 
                self.x += self.vel
                self.leftReached = False


    def moveLeft(self):
        if not self.collideLeft:
            self.collideRight = False
            if self.leftReached:
                for e in entities:
                    e.moveLeft(self.vel)
                maps[map_used].moveLeft(self.vel)
            else: 
                self.x -= self.vel
                self.rightReached = False

    def jump(self):
        f = (1/2) * self.mass * self.vel**2
        for e in entities:
            e.y += f
            self.vel -= 1

