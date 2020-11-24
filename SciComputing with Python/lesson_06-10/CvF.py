from numpy import *

def c(n,m):
    arr = zeros((n/100,m/100))
    arr.reshape(m/100,n/100,order='C')
    return arr

def f(n,m):
    arr = zeros((n/100,m/100))
    arr.reshape(m/100,n/100,order='F')

from time import time

t0 = time()
for i in xrange(100):
    c2 = c(10000,100000)
print "c(10 000, 100 000):",time()-t0

t0 = time()
for i in xrange(100):
    f2 = f(10000,100000)
print "f(10 000, 100 000):", time()-t0

t0 = time()
for i in xrange(100):
    c3 = c(100000, 10000)
print "c(100 000, 10 000):", time()-t0

t0 = time()
for i in xrange(100):
    f3 = f(100000, 10000)
print "f(100 000, 10 000):", time()-t0
