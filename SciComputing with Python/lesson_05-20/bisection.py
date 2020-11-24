# -*- coding: utf-8 -*-
"""
Created on Tue May 20 09:54:57 2014
Bisection method for root finding
@author: etodorov
"""
import numpy as np
from math import *
def bisection(fstr,a,b,eps):
    """
    Solves the equation of the form f(x)=0 \n
    fstr is f(x) in standard Python form (e.g. "x**2+2x-1") with "from math import *"; The variable should be x \n
    a and b are the start and end of the interval \n
    eps is the decimal accuracy
    return is the answer
    """
    def f(x):
        return eval(fstr)
    c = (a+b)/2.
    if(np.sign(f(c))==np.sign(f(a))):
        a = c
    else: 
        b = c

    if(abs(b-a)>1./10.**(eps+1)): return bisection(fstr,a,b,eps)
    else: return np.round(c,decimals=eps)