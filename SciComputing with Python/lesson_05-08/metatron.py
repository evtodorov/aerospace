"""
Created on Mon May 05 16:52:58 2014
Pygame drawing
@author: etodorov
"""
import pygame as pg
import math
pg.init()

screen = pg.display.set_mode((1280,960))
scrRect = screen.get_rect()
center = scrRect.center
x0 = scrRect.centerx
y0 = scrRect.centery
bg = (255,255,255)  #background color
fg = (0,0,0)        #foreground colour
w = 1               #width
r = 50              #circle radius
pi = math.pi
screen.fill(bg)
points = [center]
#get the points
for i in xrange(6):
    inPointX = x0+2.*r*math.sin(pi*i/3.)
    inPointY = y0+2.*r*math.cos(pi*i/3.)
    inPoint = (int(inPointX), int(inPointY))
    outPointX = x0+4.*r*math.sin(pi*i/3.)
    outPointY = y0+4.*r*math.cos(pi*i/3.)
    outPoint = (int(outPointX), int(outPointY))
    points.append(inPoint)
    points.append(outPoint)
#draw
for point in points:
    pg.draw.circle(screen,fg,point,r,w)
    for end in points:
        pg.draw.aaline(screen,fg,point,end)

pg.display.flip()
dummy = raw_input("Press a key to quit")
pg.quit()