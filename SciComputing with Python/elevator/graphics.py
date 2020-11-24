# -*- coding: utf-8 -*-
"""
Created on Sun Jun 01 16:06:58 2014

@author: etodorov
"""
import pygame as pg
from physics import *

global graphic_scale,screen
graphic_scale = 250000 #m/px
#background

background = pg.image.load("background.jpg") #change to png
screen_size = background.get_size()
screen = pg.display.set_mode(screen_size)
#screen.blit(background,(0,0))
def ph2gx((phx,phy)):
    #converts physicsalto grpahical cooridnates
    gxx = int(phx*graphic_scale)
    gxy = int(phy*graphic_scale)
    return (gxx,gxy)

def update(self):
    #updates the physical objects for the graphic
    print "updated",self
    dx= screen.get_width()/2
    dy= screen.get_height()/2
    self.rect.center = (int(self.r[0]/graphic_scale+dx),int(self.r[1]/graphic_scale+dy))
    
def draw(self):
    #draw the physical object
    screen.blit(self.image,self.rect)

Object.update = update
Object.draw = draw

#planet
planet.image = pg.image.load("earth.png").convert_alpha()

planet.image = pg.transform.smoothscale(planet.image,(int(planet.radius/graphic_scale),int(planet.radius/graphic_scale)))
planet.rect = planet.image.get_rect()
#

#station
station.image = pg.image.load('station.png').convert_alpha()
station.image = pg.transform.smoothscale(station.image,(int(10**7/graphic_scale),int(10**7/graphic_scale)))
station.rect = station.image.get_rect()

#def drawCable(start, end): pg,draw.line
#cable.draw = drawCable
#station.update()
#station.draw()
#planet.update()
#planet.draw()
#pg.display.flip()