# -*- coding: utf-8 -*-
"""
Created on Tue May 06 10:08:03 2014
Swinging spring
@author: etodorov
"""
import math
import matplotlib.pyplot as plt
#set parameters
m = 1.5     #kg
l = 1.      #m
k = 26.      #N/m
g = -9.81    #m/s2
#set initial conditions
x = x0 = 0.3    #m 0 is the connection, rigth+
y = y0 = -0.3   #m 0 is the connection, top+
vx = 5.         #m/s
vy = 0.         #m/s
#set plotting parameters
dt = .01        #s  time step
t=0             #s  start time
duration = 30   #s  end time

#plotting preparation
xTab = []
yTab = []
thetaTab = []
tTab = []
xTab.append(x)
yTab.append(y)
tTab.append(t)
thetaTab.append(math.atan2(y,x))

#calculation
while (t<=duration):
    #geometry
    dl = l-math.sqrt(x*x+y*y)
    theta = math.atan2(y,x)
    #dynamics
    G = m*g
    F = -k*dl
    #kinematics
    ax = -F*math.cos(theta)/m
    vx += ax*dt
    x += vx*dt

    ay = (-F*math.sin(theta)+G)/m
    vy += ay*dt
    y += vy*dt
 
    t += dt
    #save data
    xTab.append(x)
    yTab.append(y)
    thetaTab.append(theta)
    tTab.append(t)

#Plot
#theta-t
plt.subplot(2,2,1)
plt.plot(thetaTab, tTab)
plt.title("Angle(t)")
#x-y
plt.subplot(2,2,2)
plt.plot(xTab,yTab)
plt.title("Y(x)")
#x-t
plt.subplot(2,2,3)
plt.plot(xTab,tTab)
plt.title("X(t)")
#y-t
plt.subplot(2,2,4)
plt.plot(yTab,tTab)
plt.title("Y(t)")
  
plt.show()