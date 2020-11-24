# -*- coding: utf-8 -*-
"""
Created on Thu May 15 14:13:36 2014

@author: etodorov
"""
import pygame as pg
import numpy as np
#Loading resources
pg.init()
bg = pg.image.load("background.jpg")
scrWidth, scrHeight = bg.get_width(), bg.get_height()
scr = pg.display.set_mode((scrWidth, scrHeight))
scr.blit(bg,(0,0))
ship = pg.image.load("ship.gif")
shipRect = ship.get_rect()
wShip = ship.get_width()
hShip = ship.get_height()
ast = pg.image.load("ast1.gif")
astRect = ast.get_rect()
wAst = ast.get_width()
hAst = ast.get_height()

def detectCollision(x1,y1,w1,h1,x2,y2,w2,h2): 
    if (x2+w2>=x1>=x2 and y2+h2>=y1>=y2): return True
    elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1>=y2):return True
    else: return False


print "Resources Loaded. Initializing game."
#initialize game loop

xShip = scrWidth/2
v = 100 #px/s
vAst = 400 #px/s
xAst = np.array([])
yAst = np.array([])
totAst = 0
tAst = .3   #threshold
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
    yShip = scrHeight - ship.get_height()

    dtAst =  pg.time.get_ticks()*.001 - t0Ast
    if(dtAst>=tAst):
        t0Ast = pg.time.get_ticks()*.001
        xAst = np.append(xAst,np.random.random_integers(0,scrWidth-ship.get_width()))
        yAst = np.append(yAst,ship.get_height()+1.)
        totAst += 1
    yAst += vAst*dt
    
    xAst = xAst[yAst<scrHeight]
    yAst = yAst[yAst<scrHeight]    
    
    #draw
    scr.blit(bg,(0,0))
    for x,y in zip(xAst,yAst):
        scr.blit(ast,(int(x),int(y)))
        if(detectCollision(xShip,yShip,wShip,hShip,x,y,wAst,hAst)):
            running = False
    scr.blit(ship,(int(xShip),int(yShip)))

    pg.display.flip()

score = totAst - len(xAst)
print "Your score is", score    
pg.quit()