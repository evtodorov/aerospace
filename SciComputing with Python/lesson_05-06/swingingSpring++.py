# -*- coding: utf-8 -*-
"""
Created on Tue May 06 16:44:38 2014
Swinging spring++
with added air and spring damping
@author: etodorov
"""
import math
import matplotlib.pyplot as plt
#set parameters
m = 1.5     #kg
l = 1.      #m
k = 26.     #N/m    spring coefficient
g = -9.81   #m/s2
cD = 0.5    #       drag coefficient     
A = .4      #m2
c = .4      #kg/s   damping coefficient
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
    theta = math.atan2(y,x)     #position angle
    phi = math.atan2(vy,vx)     #velocity angle         
    #dynamics
    G = m*g                         #gravity
    F = -k*dl                       #spring force
    D = -cD*A*1.225*.5*(vx*vx+vy*vy)#drag
    C = -c*math.sqrt(vx*vx+vy*vy)   #spring damping
    #kinematics
    ax = (-F*math.cos(theta)+((C+D)*math.cos(phi)))/m
    vx += ax*dt
    x += vx*dt

    ay = (-F*math.sin(theta)+G+(C+D)*math.sin(phi))/m
    vy += ay*dt
    y += vy*dt
 
    t += dt
    #save data
    xTab.append(x)
    yTab.append(y)
    thetaTab.append(theta)
    tTab.append(t)

#Plot
plt.plot(xTab,yTab)
plt.title("Y(x)")

  
plt.show()
