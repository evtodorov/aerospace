# -*- coding: utf-8 -*-
"""
Created on Tue May 13 11:16:18 2014

@author: etodorov
"""
import numpy as np
import matplotlib.pyplot as pl
import Tkinter, tkFileDialog
#get the name of the tested file
root = Tkinter.Tk()
fName = tkFileDialog.askopenfilename()#"flight1.log" #raw_input("Give file name (with the extenision) \n")
root.quit()

#load the data from the file
fArr = np.genfromtxt(fName,skip_header=3)

t = fArr[:,0]
t = t - t[0]
lat = fArr[:,1]
lon = fArr[:,2]
alt = fArr[:,3]

#calculations
x = 60*lon*np.cos(np.radians(lat))
y = 60*lat

res = 9
dx = x[res:]-x[:-res]
dy = y[res:]-y[:-res]
dt = t[res:]-t[:-res]
ds = (dx**2+dy**2)**.5

dist = sum(ds)

v = ds/dt*3600      #in nm/hr
  
angle = np.degrees(np.arctan2(dy,dx))
#from geometric to track angle
track = []
#NED convention
#for a in angle:
#    if(0<=a<=90):
#        b = 90 - a
#    elif(90<a<=180):
#        b = 450 - a
#    elif(-180<=a<0):
#        b = 90 + abs(a)
#    track.append(b)
#ENU convention
for a in angle:
    if(0<=a<=180):
        b = a
    elif(-180<=a<0):
        b = 360 + a
    track.append(b)   
track = np.array(track)

#plot
pl.subplot(221)
pl.plot(lon,lat)
pl.title("Long vs Lat")

pl.subplot(222)
pl.plot(t,alt)
pl.title("Time vs Alt")

pl.subplot(223)
pl.plot(t[:-res],v)
pl.title("Ground speed")

pl.subplot(224)
pl.plot(t[:-res], track)
pl.title("Track angle")

pl.show()

#map
path = []
for i,j in zip(lat,lon):
    path.append((i,j))
import pygmaps
myMap = pygmaps.maps(lat[0],lon[0],10)
myMap.addpath(path,"#FF0000")
myMap.draw(fName[:-3]+"html")
import os
os.system(fName[:-3]+"html")
