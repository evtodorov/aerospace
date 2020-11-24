# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 08:58:14 2014

@author: etodorov
"""
#import numpy as np
nums = range(1,10001)

def sumDevs(n):
    s = []
    sqrtn = n**.5
    i = 1
    while i < sqrtn and i < 1000:
        if(not n%i): 
            if(i!=1): s.append(n/i)
            s.append(i)
        i += 1
    return sum(s)

amicable = []
for a in nums:
    b = sumDevs(a)
    db = sumDevs(b)
    nums = nums[1:]
    if db == a and b!=a and b not in amicable:
        amicable.append(a)
        amicable.append(b)
