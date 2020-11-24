# -*- coding: utf-8 -*-
"""
Created on Tue May 13 22:53:31 2014

@author: etodorov
"""
import time
start = time.time()
import numpy as np

table = np.genfromtxt("11 - gridProduct.txt")

#products = {}


product = 1

for i in xrange(len(table)):
    #products["row"+str(i)] = {}
    for j in xrange(len(table[i])):
        #products["row"+str(i)][str(j)]={}
        diagLR = 1
        diagRL = 1
        hor = 1
        ver = 1
        for k in xrange(4):
            if(i+k < len(table) and j+k < len(table[i])):diagLR *= table[i+k][j+k]
            if(i+k < len(table) and j-k > 0):diagRL *= table[i+k][j-k]
            if(j+k < len(table[i])):hor *= table[i][j+k]
            if(i+k < len(table)):ver *= table[i+k][j]
        #products["row"+str(i)][str(j)]["diagLR"]=diagLR
        #products["row"+str(i)][str(j)]["diagRL"]=diagRL
        #products["row"+str(i)][str(j)]["hor"]=hor
        #products["row"+str(i)][str(j)]["ver"]=ver
        product = max(diagLR,diagRL,hor,ver,product)
print product
print time.time()-start
#col6 row12 89*94*97*87 = 70600674