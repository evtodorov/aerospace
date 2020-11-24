"""
Created on Mon May 05 18:26:37 2014
Simple animation
@author: etodorov
"""
import pygame as pg

def objScale(obj,factor):
    """
    Object scaling function, gets obj and scale factor, returns an array of the scaled size
    """
    oldSize = obj.get_size()
    newSize = []
    for i in oldSize:
        newSize.append(int(i/float(factor)))
    return newSize

pg.init()

width = 1280   #px
height = 480     #px

ship = pg.image.load("ship.gif")
ship = pg.transform.scale(ship, objScale(ship,10))
scr = pg.display.set_mode((width,height))

bg = (0,0,0)            # background black
dt = 0.1                # frame length
m = 10                  # distance unit length
x = x0 = 0              # init position left
y = y0 = 400            # init poition bottom 
g = 9.81                # acceleration px/s/s
vx = 50                 # hor speed px/s
vy = 30                 # ver speed px/s


#game loop
t0 = float(pg.time.get_ticks())/1000
running = True
while running:
    for e in pg.event.get():
        if e.type == pg.QUIT:
           running = False
        if e.type == pg.KEYDOWN:
            if(e.type == pg.K_UP):
                vy += 10.
            if(e.type == pg.K_DOWN):
                vy += -10.
    #timings
    t = float(pg.time.get_ticks())/1000
    dt = t - t0
    t0 = t

    x += vx*dt*m
    y += -vy*dt*m
    
    dest = (int(x),int(y))
    
    scr.fill(bg)
    scr.blit(ship,dest)
    pg.draw.circle(scr,(0,0,255),dest,10)    
    
    if(y>400): running = False            
    
    pg.display.flip()

pg.quit()