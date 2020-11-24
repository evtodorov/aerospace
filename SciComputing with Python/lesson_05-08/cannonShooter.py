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
    scr.fill(bg) 
    #game loop
    print "Initialize game"
    angle = 45
    i = 0
    t0 = float(pg.time.get_ticks())/1000.
    running = True
    fire = False
    pressed_space = False
    
    while(running):
        
        #events
        for e in pg.event.get():
            if e.type == pg.QUIT: running = False
            elif e.type == pg.KEYDOWN:
                print e.key
                if e.key == pg.K_UP:
                    angle += 5
                    print angle
                if e.key == pg.K_DOWN:
                    angle += -5
                    print angle
                if e.key == pg.K_SPACE and (not pressed_space):
                    fire = True
                    pressed_space = True
                    fired = False                    
        #time
        t = float(pg.time.get_ticks())/1000.
        dt = t - t0 
        if dt<frame: continue
        t0 = t

        #clear screen        
        scr.fill(bg)  

        #once angle is chosen
        if(not fire): continue
        if(pressed_space and (not fired)): 
            xTab, yTab = func(dt=frame,angle=angle)
            fired = True
        #flight animation
        if i< len(xTab):
            dest = (xTab[i]*scale,(scrHeight-yTab[i]*scale))
        else: running = False
                      
        scr.blit(ball, dest)
        i+=1
        
        
        #pg.event.pump()
        pg.display.flip()
    
    pg.quit()

from physics import ballistic
showFlight(ballistic,scale=35)