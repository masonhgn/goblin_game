import pygame as p
from gamemap import gameMap
from player import player
from pygame.locals import *
from stuff import *
import os
os.chdir('C:/Users/desktop/pythonstuff')
jumpCount = 10

screen_width = 800
screen_height = 800

w = p.display.set_mode((screen_width, screen_height))
p.display.set_caption("Mason's Goblin game")



p.init()
c = p.time.Clock()

def drawGame():
    game_map.draw(w)
    mason.draw(w)
    for e in entities:
        e.draw(w)
    p.display.update()


run = True
while run:
    p.time.delay(30)
    
    for event in p.event.get():
        #QUIT GAME
        if event.type == p.QUIT:
            run = False

    #gravity
    if mason.collideDown == False:
        mason.y += jumpCount
        
    k = p.key.get_pressed()
    #if game_map.rightReached: print('right reached')
    #if game_map.leftReached: print('left reached')
    if k[p.K_d]:
        mason.moveRight()
    elif k[p.K_a]:
        mason.moveLeft()
    if (not mason.isJump):
        if k[p.K_SPACE]:
            mason.isJump = True
            
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            mason.y -= (jumpCount ** 2) * 0.4 * neg
            jumpCount -= 1
        else:
            mason.isJump = False
            jumpCount = 10



    drawGame()


p.quit()
