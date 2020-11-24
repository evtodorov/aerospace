# -*- coding: utf-8 -*-
"""
Created on Tue May 13 10:43:31 2014

@author: etodorov
"""
import numpy as np
a1=[2,1,-1]
a2=[-2,-1,3]
a3=[5,-1,1]
b1 =[1]
b2 =[2]
b3 =[3]
A = np.matrix([a1,a2,a3])
B = np.matrix([b1,b2,b3])
sol = np.linalg.solve(A,B)
print sol