# -*- coding: utf-8 -*-
"""
Created on Tue May 06 09:28:05 2014
Ballistic trajectories Case 1 No drag
@author: etodorov
"""
import math
import matplotlib.pyplot as plt
v0 = 50.         #m/s
x0 = 0.
y0 = 0.
deg = math.pi/180.
g = -9.81
dt = .01          #time step

for i in xrange(25,80,5):
    xTab = []
    yTab = []
    vx = v0*math.cos(i*deg)
    vy = v0*math.sin(i*deg)
    x = x0
    y = y0
    while y>=y0:
        x += vx*dt
        vy += g*dt
        y += vy*dt
        xTab.append(x)
        yTab.append(y)
    plt.plot(xTab,yTab, label=str(i))
    plt.legend()
    plt.title("Ballisitic trajectories")
    plt.xlabel("x-position [m]")
    plt.ylabel("y-posiiton [m]")

plt.show()