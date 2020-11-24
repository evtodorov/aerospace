# -*- coding: utf-8 -*-
"""
Created on Thu Jun 05 16:08:01 2014

@author: etodorov
"""

import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import os
#select file
path = "data"
files = os.listdir(path)
def getFileName(files):
    _prompt = "Choose a file: \n"+"\n".join([str(i)+": "+files[i] for i in xrange(len(files))])+"\n"
    _fnum = raw_input(_prompt)
    _fname = files[int(_fnum)]
    return _fname
try:
    fname = getFileName(files)
except:
    print "Give the number of the file you want (from 0 to %s)!" % (len(files)-1)
    fname = getFileName(files)

#get data from the file
def getFileData(path,fname):
    _data = {}
    with open(path+"/"+fname) as f:
        for line in f.readlines():
            _line = line.replace("\n","").split(";")
            _data[str(_line[0])]=_line[1]
    return _data

try:
    data = getFileData(path,fname)
except:
    print "The file you chose is corrupt"
    os.system("pause")
    quit()
#set the variables
Radius = float(data["Radius"])
Niter = int(data["Niter"])
xmin = float(data["xmin"])
xmax = float(data["xmax"])
ymin = float(data["ymin"])
ymax = float(data["ymax"])
npix = int(data["npixels"])

#construct
def construct(xmin,xmax,ymin,ymax,npix):
    _a = np.linspace(xmin,xmax,npix)
    _b = np.linspace(complex(0,ymin),complex(0,ymax),npix)
    _b = np.matrix(_b).transpose()
    _c = _a+_b
    return np.array(_c)


#calculate
def mandelbrot(z,c,Niter):
    for k in xrange(Niter):
        #get z_k
        _z = z**2+c
        #check if |z|>R
        z = np.where(np.abs(_z) < 2.,_z,2)
    return np.abs(z)

#draw Mandelbrot
c_M = construct(xmin,xmax,ymin,ymax,npix)
z_M = 0+0j
Z_M = mandelbrot(z_M,c_M,Niter)
fig = plt.figure()
plt.imshow(Z_M,cmap=cm.flag)
#events
clicks = []
def onclick(event):
    clicks.append((event.x,event.y))
eid = fig.canvas.mpl_connect("button_press_event",onclick)
plt.show()
fig.canvas.mpl_disconnect(eid)

#Draw Julia
try:
    c_J = c_M[clicks[-1][0],clicks[-1][1]]
except:
    c_J = complex(.3,-.4) #default if no clicks
z_J = construct(-1.5,1.5,-1.5,1.5,npix)
Z_J = mandelbrot(z_J,c_J,Niter)
fig_M = plt.figure()
plt.imshow(Z_J,cmap=cm.flag)
plt.title("c = "+str(c_J))
plt.show()
