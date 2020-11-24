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
from physics import ballistic
from ballAnim import showFlight

dt = .01            #time step


xMem = []
yMem = []
plots = []

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(0, 30), ylim=(0, 20))

time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

#angle loop
for angle in xrange(25,80,5):
    xTab, yTab = ballistic(angle=angle)
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

showFlight(ballistic, scale=35)