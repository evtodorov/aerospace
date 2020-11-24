# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 11:31:05 2014

@author: etodorov
"""

import pygame as pg
display = pg.display.set_mode((600,600))
rocket = pg.image.load("rocket.gif")
rocket_rect = rocket.get_rect()
v = 50  #px/s
x = 300
y = 600
pg.init()
t0 = pg.time.get_ticks()*.001
running = True
while running:
    t = pg.time.get_ticks()*0.001
    dt = t - t0
    t0 = t
    
    y = y - v*dt
    
    rocket_rect.center = x,y
    
    display.fill((0,0,0))
    display.blit(rocket,rocket_rect)
    
    if(y<0): running = False
    
    pg.event.pump()
    pg.display.flip()

pg.quit()    