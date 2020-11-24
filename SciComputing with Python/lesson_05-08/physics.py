"""
Created on Thu May 08 13:50:43 2014
Physics module
So far contains ballisitic trajectory and spring pendulum
@author: etodorov
"""
import math
def ballistic(v0=50., angle=45., x0=0., y0=0., dt = .01, cD=.47, A=.8, m=3.):
    """
    Ballisitic function with drag
    gets parameters (floats):
    speed, angle, intitial posiiton, time step, drag coefficient, Area, mass
    If you want no drag, pass cD=.0
    return arrays of the Y and X position
    """
    g = -9.81
    rho = 1.225
    xTab = []
    yTab = []
    vx = v0*math.cos(math.radians(angle))
    vy = v0*math.sin(math.radians(angle))
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
    return xTab, yTab
def springPendulum(
#parameters
m = 1.5,        #kg
l = 1.,         #m
k = 26.,        #N/m    spring coefficient
cD = 0.5,       #       drag coefficient     
A = .4,         #m2
c = .4,        #kg/s   damping coefficient
#initial conditions
x =  0.3,   #m 0 is the connection, rigth+
y = -0.3,  #m 0 is the connection, top+
vx = 5.,        #m/s
vy = 0.,        #m/s
#time parameters
dt = .01,        #s  time step
t=0,             #s  start time
duration = 30):   #s  end time
    """
    Spring pendulum with spring damping and drag \n
    gets parameters (float): mass, length of pendulum, spring k, drag coefficient, area, damping coefficient, initial position and speed, timing parameters \n
    return arrays of the X and Y position, time, angle of pendulum with horizontal
    """
    g = -9.81
    rho = 1.225
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
        print m
        G = m*g                         #gravity
        F = -k*dl                       #spring force
        D = -cD*A*rho*.5*(vx*vx+vy*vy)#drag
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
    return xTab, yTab, tTab, thetaTab