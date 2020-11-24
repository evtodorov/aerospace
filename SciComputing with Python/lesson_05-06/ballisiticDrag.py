# -*- coding: utf-8 -*-
"""
Created on Tue May 06 09:47:05 2014
Ballistic trajectories Case 2 Drag
@author: etodorov
"""
import math
import matplotlib.pyplot as plt
v0 = 50.         #m/s
x0 = 0.
y0 = 0.
deg = math.pi/180.
g = -9.81
dt = .01            #time step
cD = .47            #drag c
A = 0.8             # m^2
m = 3.              #kg
rho = 1.225
for i in xrange(25,80,5):
    xTab = []
    yTab = []
    t = 0
    vx = v0*math.cos(i*deg)
    vy = v0*math.sin(i*deg)
    x = x0
    y = y0
    while y>=y0:
        phi = math.atan2(vy,vx)
        D = cD*A*.5*rho*(vx*vx+vy*vy)
        ax = -D*math.cos(phi)/m
        vx += ax*dt
        x += vx*dt
        ay = g-D*math.sin(phi)/m
        vy += ay*dt
        y += vy*dt
        xTab.append(x)
        yTab.append(y)
    plt.plot(xTab,yTab, label=str(i))
    plt.legend()
    plt.title("Ballisitic trajectories")
    plt.xlabel("x-position [m]")
    plt.ylabel("y-posiiton [m]")

plt.show()