# -*- coding: utf-8 -*-
"""
Created on Sun Jun 01 16:23:05 2014

@author: etodorov
"""
import pygame as pg
import numpy as np
from math import *
from game import *
class Object(pg.sprite.Sprite):
    
    def __init__(self,**kwargs):
        pg.sprite.Sprite.__init__(self)
        vecs = ["r","f","v","a"]
        scals = ["m"]
        for key in vecs:
            if key in kwargs:
                setattr(self,key,np.array(kwargs[key],dtype=float))
            else:
                setattr(self,key,np.zeros(2))
        for key in scals:
            if key in kwargs:
                setattr(self,key,float(kwargs[key]))
            else:
                setattr(self,key,0.)

    
    def __str__(self):
        return str(self.r)+str(self.f)
    
    def gravity(self,oth):
        G = 6.67*10**(-11)
        R2 = (oth.r[0]-self.r[0])**2+(oth.r[1]-self.r[1])**2
        theta = atan2(oth.r[1]-self.r[1],oth.r[0]-self.r[0])
        #print theta
        mag = self.m*oth.m*G/R2
        #print mag
        #print self.f, mag*cos(theta),mag*sin(theta)
        #self.f += np.array(mag*cos(theta),mag*sin(theta))
        self.f[0] += mag*cos(theta)
        self.f[1] += mag*sin(theta)
        #print self.f
        #print self.r
        #print "R",R,"self",self,"theta",theta,"mag",mag
    
    def newton(self,dt):
        #Verlet integration _a is old a
        _a=self.a
        #print self.f,self.m,self.a,self.f/self.m
        self.a = self.f/self.m
        self.r += self.v*dt + .5*_a*dt**2
        self.v += .5*(self.a+_a)*dt
        print self.v

planet = Object(m=5.97*10**24)
planet.radius = 6371000.
planet.day = 23*3600+56*60+4.

station = Object(m=10,r=(0,40*10**6),v=(-8100,0))

