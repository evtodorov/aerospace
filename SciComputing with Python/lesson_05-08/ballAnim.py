"""
Created on Thu May 08 14:03:03 2014

Animation file

@author: etodorov
"""
import pygame as pg


def showFlight(func,scrWidth=1280, scrHeight=480, bg=(0,0,120), frame = 0.03, scale=50):
    """
    Animating function, func is the function to be animated, scale is the ratio function units to px, bg is RGB background color, frame is the length of a frame in seconds
    """
    pg.init()    
    
    scr = pg.display.set_mode((scrWidth,scrHeight))
    ball = pg.image.load("ball.gif")
    
    print "Objects loaded"
    
    #game loop
    print "Initialize game"
    xTab, yTab = func(dt=frame)
    i = 0
    t0 = float(pg.time.get_ticks())/1000.
    running = True
    while(running):
        #time
        t = float(pg.time.get_ticks())/1000.
        dt = t - t0 
        if dt<frame:
            continue
        t0 = t
        
        #flight animation
        if i< len(xTab):
            dest = (xTab[i]*scale,(scrHeight-yTab[i]*scale))
        else: running = False
        scr.fill(bg)                
        scr.blit(ball, dest)
        i+=1
        
        
        pg.event.pump()
        pg.display.flip()
    
    pg.quit()
