# -*- coding: utf-8 -*-
"""
Created on Thu May 15 14:13:36 2014

@author: etodorov
"""
import random
import pygame as pg
import sys
#Loading resources
pg.init()

bg = pg.image.load("background.jpg")
scrWidth, scrHeight = bg.get_width(), bg.get_height()
scr = pg.display.set_mode((scrWidth, scrHeight))
scr.blit(bg,(0,0))

shipImg = pg.image.load("ship.gif")
ship = pg.sprite.Sprite()
ship.image = shipImg.convert()
ship.rect = ship.image.get_rect()
ship.mask = pg.mask.from_surface(shipImg)

astImg = pg.image.load("ast1.gif")
astMask = pg.mask.from_surface(astImg)
asteroids = pg.sprite.Group()

class astSprite(pg.sprite.Sprite):
    image = astImg
    mask = astMask       
    passed = 0
    total = 0

    def __init__(self,location):
        pg.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.topleft = location
        
    def update(self,vx,vy,dt):
        self.rect.topleft = self.rect.topleft[0]+vx*dt, self.rect.topleft[1]+vy*dt
        if(self.rect.topleft[1]>scrHeight):
            astSprite.passed += 1
            self.kill()

print "Resources Loaded. Initializing game."
#initialize game loop

xShip = scrWidth/2
v = 200 #px/s
vAst = 400 #px/s
tAst = .5   #threshold
t0Ast = 0
running = True
t0 = pg.time.get_ticks()*.001
while running:
    pg.event.pump()
    
    #get time
    t = pg.time.get_ticks()*.001
    dt = t-t0
    t0 = t
    
    #events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE]:
        running = False  
    if keys[pg.K_LEFT]:
        xShip += -v*dt
    if keys[pg.K_RIGHT]:
        xShip += v*dt
    
    #engine
    yShip = scrHeight - ship.image.get_height()
    ship.rect.topleft=[xShip,yShip]
    dtAst =  pg.time.get_ticks()*.001 - t0Ast
    
    if(dtAst>=tAst):
        t0Ast = pg.time.get_ticks()*.001
        ast = astSprite((random.randint(0,scrWidth),0))
        asteroids.add(ast)
        astSprite.total += 1
    
    asteroids.update(0,vAst,dt) 

    if(pg.sprite.spritecollide(ship, asteroids, False, pg.sprite.collide_mask)): 
        running = False
    #draw
    scr.blit(bg,(0,0))
    asteroids.draw(scr)
    scr.blit(ship.image,ship.rect)
    #if(sys.stdin.read(1)): running = False
    pg.display.flip()

score = astSprite.total - astSprite.passed
print "Your score is", score    
pg.quit()
