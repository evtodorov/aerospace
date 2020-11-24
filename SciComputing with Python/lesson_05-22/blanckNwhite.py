# -*- coding: utf-8 -*-
"""
Created on Thu May 22 14:39:19 2014

@author: etodorov
"""

import numpy as np

dat = np.genfromtxt("ppdata.dat",delimiter=",",skip_header=7)
size = (len(dat[0]),len(dat))

import pygame as pg
pg.init()
scr = pg.display.set_mode(size]

y = 0
for row in dat:
    x = 0
    for px in row:
        grey = 255-int(px/4)
        scr.set_at((x,y),(grey,grey,grey))
        x += 1
    y+= 1

pg.image.save(scr,"photo.jpg")

pg.display.flip()

dummy = raw_input("Enter to exit")
pg.quit()
