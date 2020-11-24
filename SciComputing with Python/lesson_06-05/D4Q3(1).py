import numpy as np
from math import sqrt

# Problem 3: test for sum of two squares

n = int(round(float(raw_input("Enter a number to test :"))))

# brute force (ok):

swsum = False
for i in range(1,n/2+1):
    j = n-i
    if int(sqrt(i))*int(sqrt(i)) == i and  \
       int(sqrt(j))*int(sqrt(j)) == j :
        print n," is sum of two squares namely",i,"and",j
        swsum = True

if not swsum:
    print n,"is not the sum of two squares."

print "Np solution"
# Numpy solution
sq = np.arange(1,int(sqrt(n))+1)**2
swsum = False
for x in sq:
    if n-x in sq:
        print n," is sum of two squares namely",x,"and",n-x
        swsum = True
        
if not swsum:
    print n,"is not the sum of two squares."
