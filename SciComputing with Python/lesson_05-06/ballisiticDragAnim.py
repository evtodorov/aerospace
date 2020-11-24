# -*- coding: utf-8 -*-
"""
Created on Tue May 06 09:47:05 2014

Ballistic trajectories Case 2 Drag Animated

Based on code from:  http://matplotlib.sourceforge.net/examples/animation/double_pendulum_animated.py

@author: etodorov
"""
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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

xMem = []
yMem = []
plots = []

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(0, 30), ylim=(0, 20))

time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

#angle loop
for angle in xrange(25,80,5):
    xTab = []
    yTab = []
    vx = v0*math.cos(angle*deg)
    vy = v0*math.sin(angle*deg)
    x = x0
    y = y0
    #integration loop
    while y>=y0:
        phi = math.atan2(vy,vx)
        D = cD*A*.5*rho*(vx*vx+vy*vy)
        aX = -D*math.cos(phi)/m
        vx += aX*dt
        x += vx*dt
        aY = g-D*math.sin(phi)/m
        vy += aY*dt
        y += vy*dt
        xTab.append(x)
        yTab.append(y)
    xMem.append(xTab)
    yMem.append(yTab)

    plot = ax.plot([],[])
    plots.append(plot[0])


def init():
    for plot in plots:
        plot.set_data([],[])
    return plots
    
def animate(i):
    for plot, xTab, yTab in zip(plots, xMem, yMem):
        xNow = xTab[:i]
        yNow = yTab[:i]
        plot.set_data(xNow,yNow)
    time_text.set_text(time_template%(i*dt))    
    return plots

from time import time
tAni0 = time()
animate(0)
tAni1 = time()
interval =1000* dt - (tAni1-tAni0)
ani = animation.FuncAnimation(fig,animate, init_func=init, interval=interval)

    
plt.show()