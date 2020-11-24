"""
Created on Tue May 13 15:03:03 2014
Using pygmaps
@author: etodorov
"""

import numpy as np
import pygmaps
paths = []
#get the name of the tested file
fNames = ["flight2.log"]
colors = ["#FF0000"]
for fName in fNames:
    #load the data from the file
    fArr = np.genfromtxt(fName,comments="$",skip_header=3)
    
    lat = fArr[:,1]
    lon = fArr[:,2]
    
    path = []
    for i,j in zip(lat,lon):
        path.append((i,j))
    paths.append(path)

myMap = pygmaps.maps(lat[0],lon[0],10)
for path,color in zip(paths,colors):
    myMap.addpath(path,color)
myMap.draw("./fight2.html")
import os
os.system("flight2.html")
