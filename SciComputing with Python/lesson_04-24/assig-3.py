"""
Assignment 2

An definite integral

(a)

a    : startpoint of the interval
b    : endpoint of the interval
n    : number of intervals with equal with
h    : width of one interval
error: upperbound of the error
"""
from math import exp

a = -1.0
b = 1.0
n = 100
h = (b-a)/n
#
# Calculating an approximation of the definite integral using the Midpoint Rule
#
s = 0
for i in range(n):
    x = a+i*h+h/2
    y = exp(-x*x)
    s = s+y*h
MR = s

"""

(b)

"""
#
# max |f"(x)| a <= x < = b is equal to 2.
#
error  = (2*(b-a)**3)/(24*n**2)

print "The approximation (I_MR) of the definite integral (I) of exp(-x**2) over the \
interval [-1,1] using the Midpoint Rule is equal to :",MR,"and |I-I_MR| <=",\
error, "."
print

"""

Calculating an approximation of the definite integral using the Trapezoidal Rule

"""
s=0
x0 = a
y0 = exp(-x0*x0)
for i in range(1,n+1):
    x1 = a + i*h
    y1 = exp(-x1*x1)
    s  = s + h*(y0+y1)/2
    y0 = y1
TR = s

"""

(b)

"""

#
# max |f"(x)| a <= x < = b is equal to 2.
#

error  = (2*(b-a)**3)/(12*n**2)

print "The approximation (I_TR) of the definite integral (I) of exp(-x**2) over the \
interval [-1,1] using the Trapezoidal Rule is equal to :",TR,"and |I-I_TR| <=",\
error, ".\n"
