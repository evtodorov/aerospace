# -*- coding: utf-8 -*-
"""
Created June 2014

@author: etodorov
"""
from engine import *
from PIL import Image as pyimg


#read the image in grayscale+alpha
im = pyimg.open(CMB_image_name).convert("LA")
imW,imH=im.size
#get the middle band, the pixel data, lose the alpha
speeds = np.array(im.getdata())[:,0]


#create arrays of particles
x = np.array([])
y = np.array([])
vx = np.array([])
vy = np.array([])
ax = np.array([])
ay = np.array([])
m = np.array([])
Fx = np.array([])
Fy = np.array([])

#initialize particles
for i in xrange(64):
        for j in xrange(36):
            x = np.append(x,i*20)
            y = np.append(y,j*20)
            m = np.append(m,10)
            #change in speed from Cosmic Microwave Background data
            #i-th row, j-th pixel, centered, map only
            dv = (255-speeds[j::imW][imH/2-i])*.005
            vx = np.append(vx,(1+dv)*(-1)**np.random.randint(0,10))   #random direction
            vy = np.append(vy,(1+dv)*(-1)**np.random.randint(0,10))   #random direction
            ax = np.append(ax,0)
            ay = np.append(ay,0)
            Fx = np.append(Fx,0)
            Fy = np.append(Fy,0)

#intialize particle visualization
bodies = pg.sprite.Group()       
for X,Y in zip(x,y):
    body = Matter(r=(X,Y))
    bodies.add(body)

#create cells
cells = []
cellW = resX/cellCols
cellH = resY/cellRows
for R in range(cellRows):
    for C in range(cellCols):
        cells.append(Cell(R,C,(cellW,cellH)))

#calculate initial barycenter
bcX = x.copy()
bcY = y.copy()
bcM = m.copy()
for cell in cells:
        #check which body is in the cell
        boolR =np.floor(y/cell.h) == cell.row
        boolC = np.floor(x/cell.w) == cell.col
        aBool =  boolR * boolC  #and
        #barycenter location
        cell.barycenter(m[aBool],x[aBool],y[aBool])         
        bcX[aBool]=cell.x
        bcY[aBool]=cell.y
        bcM[aBool]=cell.m
