# -*- coding: utf-8 -*-
"""
Created June 2014

@author: etodorov
"""
import pygame as pg
import numpy as np
from math import *

from settings import *
constants = {"G":6.67384}
#Wrapper for game stuff
class Game():
    def __init__(self):
        self.running = True
        self.screen = pg.display.set_mode((1280,720))#,pg.FULLSCREEN)
        self.start = pg.time.get_ticks()*.001
    def end(self):
        self.running = False

#Grid
class Cell():
    """
    Grid cell class
    """
    def __init__(self,row,col,size):
        self.row = row
        self.col = col
        self.size = size
        self.w = int(size[0])
        self.h = int(size[1])
        self.x = self.y = self.vx = self.vy = self.Fx = self.Fy = 0.
    
    def barycenter(self,m,x,y):
        '''
        find the barycenter of the itr (by idea the group)
        '''
        mTot = m.sum()
        mx = m*x
        my = m*y
        if(mTot!=0): 
            self.x = mx.sum()/mTot
            self.y = my.sum()/mTot
        else:
            self.x = self.y = 0
            mTot = 1
        self.m = mTot
    
    def attract(self,other):
        """
        attraction between the barycenters of the cells
        """
        G = constants["G"]
        R2 = (other.x-self.x)**2+(other.y-self.y)**2
        if(R2<1): R2 = 1  #fix tending to infinity force at too small distances
        theta = atan2(other.y-self.y,other.x-self.x)
        mag = self.m*other.m*G/R2
        self.Fx += mag*cos(theta)
        self.Fy += mag*sin(theta)
#        print self.Fx,self.Fy
    def newton(self,dt):
        """
        numerical integration for the cell barycenters
        """
        ax = self.Fx/self.m
        ay = self.Fy/self.m
        self.vx += ax*dt
        self.vy += ay*dt
#particles
class Matter(pg.sprite.Sprite):
    image = pg.image.load("matter.png")
    def __init__(self,r,**kwargs):
        scals = ["m"]
        for key in scals:
            if key in kwargs:
                setattr(self,key,float(kwargs[key]))
            else:
                setattr(self,key,0)
        pg.sprite.Sprite.__init__(self)
        self.r = r
        self.rect = self.image.get_rect()
        self.update(r[0],r[1])
    
    def __str__(self):
        return str(self.r)+str(self.f)
       
    def update(self,x,y):
        """
        Match world to graphic coordiantes
        """
        try:
            self.x = int(x)
            self.y = int(y)
            
        except: 
            self.x = 0
            self.y = 0
        
        try:
            self.rect.topleft=(self.x,self.y)
        except: pass

#in the grid (vector functions)
def gravity(m,x,y,Fx,Fy,bcX,bcY,bcM):
    """
    Calcualte the attraction to the barycenter bc \n
    return Fx,Fy
    """
    G = constants["G"]
    R2 = (x-bcX)**2+(y-bcY)**2
    
    if(R2<=100): return Fx,Fy   #tending to infinity force at too small distances

    theta = atan2(bcY-y,bcX-x)
    mag = m*bcM*G/R2
    Fx += mag*cos(theta)
    Fy += mag*sin(theta)
    return Fx,Fy

gravityVec = np.vectorize(gravity,excluded=['bc'])

#numerical integration      
def newton(x,y,vx,vy,ax,ay,Fx,Fy,m,dt):
    '''
    Calculate the movement given the initial conditions and the force \n
    Includes the check that stops the partical when it leaves the screen \n
    return x,y,vx,vy,ax,ay,Fx,Fy
    '''
    #check
    left = x < -50
    right = x > 1300
    top = y < -50
    bottom = y > 750
    #if at the boundary, put back in the screen and restart the integration    
    if( left or right or top or bottom):
        Fx = 0
        Fy = 0
        x -= vx*dt
        y -= vy*dt
        vx *= 0
        vy *= 0
        return x,y,vx,vy,ax,ay,Fx,Fy
    
    #numerical integration    
    ax = Fx/m
    ay = Fy/m
    vx += ax*dt
    vy += ay*dt
    x += vx*dt
    y += vy*dt
    return x,y,vx,vy,ax,ay,Fx,Fy

newtonVec = np.vectorize(newton,excluded=['dt'])

