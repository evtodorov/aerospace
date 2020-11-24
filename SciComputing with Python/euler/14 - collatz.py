# -*- coding: utf-8 -*-
"""
Created on Tue May 20 22:06:39 2014

@author: etodorov
"""
def coll(n,mem):
    mem.append(n)
    if(n==1): return mem
    if(n%2==0): n = n/2
    elif(n%2==1): n = 3*n+1
    else: print "Not possible"
    return coll(n,mem)

mem = []
for i in xrange(1,1000000,2):
    temp = coll(i,[])
    if(len(temp)>=len(mem)): mem = temp
print mem[0]
