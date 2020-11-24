# -*- coding: utf-8 -*-
"""
Created on Tue May 20 22:38:29 2014

@author: etodorov
"""
import time
t0 = time.time()
r = 20
c = 20
"""
#Bruteforce method would take approx 27 hours :(

lattice = [[0]*r]*c
ways = 0
def crawl(curRow,curCol):
    global ways

    #if only one choice
    if(curRow==r or curCol==c): return 1
    else:
        wayR = crawl(curRow+1,curCol) or 0
        wayC = crawl(curRow,curCol+1) or 0
        ways+= wayR + wayC
        
crawl(0,0)

print ways
"""
#dt = .001
import numpy as np
lat = np.array([c*[0L]]*r)
lat[:,0]=range(2,r+2)
#start from the end
for i in xrange(c-1):
    lat[i+1,i+1]=2*lat[i+1,i]
    for j in xrange(i,r-2):
        lat[j+2,i+1]=lat[j+1,i+1]+lat[j+2,i]
        
        
print time.time()-t0
