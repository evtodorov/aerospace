# -*- coding: utf-8 -*-
"""
Created on Tue May 06 16:44:38 2014
Swinging spring problem with added air and spring damping
animation inspired by http://jakevdp.github.io/blog/2013/02/16/animating-the-lorentz-system-in-3d/
possible TODOs:
    realisitc spring (i.e. max dl = 10%)
    more?
@author: etodorov
"""
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
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
y = y0 = -0.85   #m 0 is the connection, top+
vx = 5.         #m/s
vy = 0.         #m/s
#set plotting parameters
dt = .01        #s  time step
t=0             #s  start time
duration = 500   #s  end time

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

#visualization
#initialize plots
fig = plt.figure()
a = fig.add_subplot(111, autoscale_on=False, xlim=(-2.5,2.5), ylim=(-3,0))
pendulum, = a.plot([],[],"-o",lw=2)
trajectory, = a.plot([],[])

time_template = 'time = %.1fs'
time_text = a.text(0.05, 0.9, '', transform=a.transAxes)

def init():
    pendulum.set_data([],[])
    trajectory.set_data([],[])
    time_text.set_text('')
    return pendulum, trajectory, time_text
def animate(i):
    pendulum.set_data([0,xTab[i]],[0,yTab[i]])
    trajectory.set_data(xTab[:i],yTab[:i])
    time_text.set_text(time_template%(i*dt))
    return pendulum, trajectory, time_text

#set interval
from time import time
tAni0 = time()
animate(0)
tAni1 = time()
interval =1000* dt

ani = animation.FuncAnimation(fig,animate, init_func=init,blit=True, interval=interval)
  
plt.show()
