# -*- coding: utf-8 -*-
"""
Created on Thu Jun 05 22:58:16 2014

@author: etodorov
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
data = np.genfromtxt("clcd.txt",delimiter=",",skip_header=2)
aoa = data[:,0]
cl = data[:,1]
cd = data[:,2]

k, cd0, r, p, stderror = linregress(cl**2,cd)

print "k =",k,"C_DO =",cd0, "Standard Error = ", stderror
plt.subplot(121)
plt.scatter(cd,cl)
plt.subplot(122)
plt.scatter(aoa,cl)
plt.show()