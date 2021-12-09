import pygame as p

import random
entities = []

rock = p.image.load('goblins/images/tile.png')

class entity(object):
    def __init__(self, spawnx, spawny, x, y, width, height, name, entity_type):
        self.name = name
        self.entity_type = entity_type
        self.spawnx = spawnx
        self.spawny = spawny
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        entities.append(self)

        self.left = 0
        self.right = 0
        self.top = 0
        self.bottom = 0
    
    def __str__(self):
        return self.name

    def moveRight(self, velocity):
        self.x -= velocity

    def moveLeft(self, velocity):
        self.x += velocity



    def draw(self, w):

        self.right = self.x + self.width
        self.left = self.x
        self.top = self.y
        self.bottom = self.y + self.height

        if self.name == 'rock':
            w.blit(rock, (self.x,self.y))
        
        


