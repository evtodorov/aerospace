
"""
Created on Tue May 13 10:29:51 2014

@author: etodorov
"""
import numpy as np
A = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
B = np.matrix([[1,4,7],[2,5,8],[3,6,9]])
C = np.matrix([[1,-2,0],[0,-1,4],[-2,5,-1]])
P = A*B
print P
print P*C
detA = np.linalg.det(A)
detB = np.linalg.det(B)
detC = np.linalg.det(C)
print detA,"\n",detB,"\n",detC
print A.I
print B.I
print C.I