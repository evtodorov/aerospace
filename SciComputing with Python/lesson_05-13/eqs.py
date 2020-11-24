"""
Created on Tue May 13 09:47:59 2014

@author: etodorov
"""
import numpy as np
import matplotlib.pyplot as pl
'''
x1 = np.arange(-2,2,.001)
y1 = np.sin(x1-np.sin(x1))
ans1 = []
for i in xrange(len(y1)):
    if(-0.99999>y1[i]>-1.00001): ans.append(x1[i])
pl.plot(x1,y1)
#-2.310 +- 2k*pi

x2 = np.arange(-1,1,0.001)
y21 = np.cos(x2)
y22 = x2**2
pl.plot(x2,y21)
pl.plot(x2,y22)
#+- .824

x3 = np.arange(-10,10,0.001)
y31 = np.sin(x3)
y32 = x3 + 2.
pl.plot(x3,y31)
pl.plot(x3,y32)
#-2.554
'''

x4 = np.arange(-100,100,0.1)
y4 = x4**3-4*x4**2+5*x4+1
y40 = 0.*x4
pl.plot(x4,y4)
pl.plot(x4,y40)

pl.show()