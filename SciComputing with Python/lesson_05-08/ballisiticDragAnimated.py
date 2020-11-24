# -*- coding: utf-8 -*-
"""
Created on Tue May 06 09:47:05 2014
Ballistic trajectories Case 2 Drag
@author: etodorov
"""
import math
import matplotlib.pyplot as plt
from physics import ballistic
from ballAnim import showFlight

for angle in xrange(25,80,5):
    xTab, yTab = ballistic(angle=angle)
    plt.plot(xTab,yTab, label=str(angle))
    plt.legend()
    plt.title("Ballisitic trajectories")
    plt.xlabel("x-position [m]")
    plt.ylabel("y-posiiton [m]")

plt.show()

showFlight(ballistic, scale=35)