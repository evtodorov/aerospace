# -*- coding: utf-8 -*-
"""
Created on Sun Jun 01 15:59:07 2014

@author: etodorov
"""

import pygame as pg
from graphics import *
pg.init()
t0 = pg.time.get_ticks()*.001
running = True
while running:  

    #time
    t = pg.time.get_ticks()*0.001
    dt = t - t0
    t0 = t
    print dt
    
    #events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    pg.event.pump()
    
    #physics
    station.gravity(planet)
    station.newton(dt*1000)   
    planets = pg.sprite.Group(planet)
   
    #draw
    screen.blit(background,(0,0))
    print "update call"
    station.update()
    station.draw()
    planet.update()
    planet.draw()
    pg.display.flip()
    collision = pg.sprite.spritecollide(station,planets,True)
    print collision
    if(len(collision)): running=False

pg.quit()