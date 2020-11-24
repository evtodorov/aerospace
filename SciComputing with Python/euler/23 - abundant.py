# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 13:41:42 2014

@author: etodorov
"""
from time import time
t0 = time()
"""
import numpy as np
def sumDevs(n):
    s = []
    sqrtn = n**.5
    i = 1
    while i <= sqrtn:
        if(not n%i): 
            if(i!=1 and n/i!=i): s.append(n/i)
            s.append(i)
        i += 1
    if(n==196): print s
    return sum(s)

nums = range(1,28124)

def abundant(nums):
    _abundants = []
    for n in nums:
        s = sumDevs(n)
        if (s>n): _abundants.append(n)
    return _abundants


def isabundant(n):
    if(sumDevs(n)>n): return True
    else: return False

import math
def divisors(n):
    for _i in range(2, 1 + int(math.sqrt(n))):
        if n % _i == 0:
            yield _i
            yield n / _i
def is_abundant(n):
    return 1 + sum(divisors(n)) > n

abundants = [x for x in range(1, 28123 + 1) if is_abundant(x)]

def is_abundant_sum(n):
   for i in abundants:
       if i > n:  # assume "abundants" is ordered
         return False
       if (n - i) in abundants:
           return True, i, n
   return False
#sum_of_non_abundants = sum(x for x in range(1, 28123 + 1) if not is_abundant_sum(x))
#print sum_of_non_abundants, time()-t0 


abundants2 = np.array(abundant(nums))

nums = np.array(nums)
bools = nums > 0
for i in xrange(len(abundants2)):
    for j in xrange(i,len(abundants2)):
        k1 = abundants2[i]
        k2 = abundants2[j]
        if(k1+k2==1141 or k1+k2 == 1771 or k1+k2 == 7621): print k1,k2,"\t",i,j
        if(k1+k2)>len(bools): break
        bools[k1+k2-1] = False
myans = nums[bools]
answer = nums[bools].sum()
print answer, time()-t0   
"""
LIMIT = 28123

def sum_d(n):
    s = 1
    p = 2
    while p*p<=n and n>1:
        if n % p == 0:
            j = p*p
            n = n/p
            while n % p == 0:
                j *= p
                n /= p
            s *= j-1
            s /= p-1
        p = 3 if p==2 else p+2
    if n>1:
        s *= n+1
    return s
    
def check_abun(n):
    return sum_d(n) > 2*n
    
abun_list = list(n for n in range(1,LIMIT+1) if check_abun(n))
abun_set = set(abun_list)

def check_sum_abun(n):
    for i in abun_list:
        j = n-i
        if j < 0:
            return False
        if j in abun_set:
            return True
    return False

print(sum(i for i in range(1, LIMIT+1) if not check_sum_abun(i)))
print time()-t0 