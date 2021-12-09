import pygame as p
import os
from entity import entities
os.chdir('C:/Users/desktop/pythonstuff')
currentmap = p.image.load('goblins/images/map1.png')
map_used = 0
maps = []

class gameMap(object):
    def __init__(self,x,y, rightReached, leftReached):
        self.x = x
        self.y = y
        self.velocity = 6
        self.rightReached = False
        self.leftReached = False
        maps.append(self)
        
    
    def draw(self, w):
        if self.x > 0: self.leftReached = True
        if self.x < -6200: self.rightReached = True
        w.blit(currentmap, (self.x, self.y))

    


    def moveRight(self, velocity):
        if not self.rightReached:
            self.x -= velocity
            self.leftReached = False
        
            

    def moveLeft(self, velocity):
            if not self.leftReached:
                self.x += velocity
                self.rightReached = False



