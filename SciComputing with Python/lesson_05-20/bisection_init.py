# -*- coding: utf-8 -*-
"""
Created on Tue May 20 10:21:30 2014
Init for bisection root finding method
@author: etodorov
"""
import bisection
eqA = "4*x**3-2*x**2+4*x-4"
eqB = "sin(x)+exp(x)-2"
eqC = "x**4-3*x**3+2*x**2-x+1"

ansA = bisection.bisection(eqA,-10,10,5)
ansB = bisection.bisection(eqB,-2,3,5)
ansC = bisection.bisection(eqC,0,2,5)
ansC2 = bisection.bisection(eqC,2,5,5)
print "In the given interval, the equation "+eqA+"=0 has the root "+str(ansA)
print "In the given interval, the equation "+eqB+"=0 has the root "+str(ansB)
print "In the given interval, the equation "+eqC+"=0 has the root "+str(ansC)
print "In the given interval, the equation "+eqC+"=0 has the root "+str(ansC2)

out = False
while not out:
    try:
        eq = raw_input("Give function to solve \n")
        a = float(raw_input("open interval: "))
        b = float(raw_input("close interval: "))
        eps = int(raw_input("accuracy: "))
        print bisection.bisection(eq,a,b,eps)
        out = input("Quit? /n")
    except:
        out = True
