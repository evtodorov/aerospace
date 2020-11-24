# -*- coding: utf-8 -*-
"""
Created on Sun Jun 29 15:24:07 2014

@author: etodorov
"""
def longDivision(dividend, divisor):
    """
    dividend and  divisor should be integers
    returns a string!
    """
    dividend = int(dividend)
    divisor = int(divisor)
    run = True
    ans = ""
    tab = []
    while run:
        i = dividend/divisor
        ans += str(i)
        dividend = dividend%divisor*10
        if dividend in tab: 
            run = False
            #pos = tab.index(dividend)
            #ans = ans[:pos+1]+"("+ans[pos+1:]
        tab.append(dividend)
    del tab
    return ans #ans[0]+"."+ans[1:]+")"

stored = ""
num = 0
for i in xrange(1,1001):
    current = longDivision(1,i)
    if len(current)>=len(stored):
        stored = current
        num = i
print num