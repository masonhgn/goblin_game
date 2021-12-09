import pygame as p
from player import player
from entity import entity, entities
from gamemap import gameMap

game_map = gameMap(0, -400, False, False)
rock = entity(300,510,900,510, 50, 50, 'rock','solid')
mason = player(100,510,80,100, 10, 0,0,0,0)