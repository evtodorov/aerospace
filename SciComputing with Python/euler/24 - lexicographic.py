# -*- coding: utf-8 -*-
"""
Created on Sun Jun 29 11:44:07 2014
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
@author: etodorov
"""


def fact(n):
    if n<=1: return 1
    else: return n*fact(n-1)
    
def nth_permutation(n,lst):
    n = int(n)
    l = len(lst)
    
    if(n>fact(l)): 
        print "Not possible"
        return 
        
    permutation = [""]*l
    for i in xrange(1,l):
        f = fact(l-i)
        if not n%fact(l-i)==0:
            pos = n/f
            n = n%f
        else:
            pos = n/f - 1
        
        try: permutation[i-1]=lst[pos]
        except: permutation[i-1]=lst[-1]
        try: lst.pop(pos)
        except: lst.pop(-1)
    
    permutation[-1]=lst[0]
    return permutation
        
print "".join(str(i) for i in nth_permutation(10**6,[0,1,2,3,4,5,6,7,8,9]))