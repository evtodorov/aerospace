"""
Some numerical integration stuff
06 May 2014
@author: etodorov
"""
m = 2.
g = -9.81
y = 10.
vy = 0.

dt = 0.01

tTab = []
yTab = []
vTab = []

for i in xrange(1000):
    t = i*dt
    
    F = m*g
    a = F/m
    vy += a*dt
    y += vy*dt
    
    tTab.append(t)
    yTab.append(y)
    vTab.appen(vy)
