# -*- coding: utf-8 -*-
"""
Created on Sun Jun 01 18:12:51 2014

@author: etodorov
"""

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
background = pg.image.load("background.png")
screen_size = background.get_size()
screen = pg.display.set_mode(screen_size,pg.FULLSCREEN)
gradient = pg.image.load("gradient.png").convert_alpha()

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
    screen.blit(background,(0,0))
    screen.blit(gradient,(100,100))
    #draw
    pg.display.flip()

pg.quit()