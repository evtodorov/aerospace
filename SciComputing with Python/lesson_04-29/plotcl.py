import numpy as np
import scipy as sp
import matplotlib as mplt
import matplotlib.pyplot as plt

# Reading method 1
f=open("clalpha.dat","r")
atab = []
cltab = []
for line in f.readlines():
    numbers = line.split()
    atab.append(numbers[0])
    cltab.append(numbers[1])

# Reading method 2
table = np.genfromtxt("clalpha.dat",delimiter ="," , comments="C")

atab  = table[:,0]
cltab = table[:,1]

# Plotting the graph
plt.plot(atab,cltab)
plt.xlabel("alpha [deg]")
plt.ylabel("CL [-]")
plt.title("Lift coefficient")

plt.grid(True)
plt.show()

# Interpolation method 1: by hand

alpha = input("Give alpha:")
cl = None
for i in range(len(atab)-1):
    if atab[i]<alpha<=atab[i+1]:
        factor = (alpha - atab[i])/(atab[i+1]-atab[i])
        cl = (1-factor)*cltab[i]+factor*cltab[i+1]

if cl==None:
    print "Alpha",alpha,"out of range"
else:
    print "CL(",alpha,") =",cl

# Interpolation method 2: using Numpy

alpha = input("Give alpha:")
cl = np.interp(alpha, atab, cltab,left=-100.,right=-100.) 

if cl>0:
    print "CL(",alpha,") =",cl
else:
    print "Alpha",alpha,"out of range"

