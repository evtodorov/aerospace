"""
Created on Mon May 05 18:26:37 2014
Simple animation
@author: etodorov
"""
import pygame as pg

pg.init()

ship = pg.image.load("ship.gif")
ship = pg.transform.scale(ship, (122,60))
scr = pg.display.set_mode((1280,480))

bg = (0,0,0)            # background black
dt = 0.1                # frame length
m = 10                  # distance unit length
x = x0 = 0              # init position left
y = y0 = 400            # init poition bottom 
g = 9.81                # acceleration px/s/s
vx = 50                 # hor speed px/s
vy = 80                 # ver speed px/s
running = True
while running:
    print 'start',pg.time.get_ticks()
    pg.time.delay(int(dt*1000))
    scr.fill(bg)
    vy += -g*dt*m
    x += vx*dt*m
    y += -vy*dt*m
    dest = (int(x),int(y))
    scr.blit(ship,dest)
    pg.draw.circle(scr,(0,0,255),dest,10)    
    
    if(y>400): running = False            
    
    pg.display.flip()
    pg.event.pump()
    print 'end',pg.time.get_ticks()

dummy = raw_input("press enter to quit")
pg.quit()