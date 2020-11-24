# part 2a

f = open('NACA0012.dat','r')
lines = f.readlines()
f.close()

alpha = []
cl = []
for line in lines:
    col = line.split('\t')
    alpha.append(float(col[0]))
    cl.append(float(col[1][:-1])) # cut off newline (will also work with)

raw_input("Press Enter to continue")

# or using numpy:

import numpy as np

table = np.genfromtxt("NACA0012.dat",delimiter="\t")
alpha = table[:,0]
cl = table[:,1]

# interpolation part 2b:

a = float(input("Enter a value for alpha: "))

if a<min(alpha) or a > max(alpha):
    print "Alpha out of range"
else:
    for i in range(len(alpha)-1):
        if a >= alpha[i] and a <= alpha[i+1]:
            f = (alpha[i+1]-a)/(alpha[i+1]-alpha[i])
            fcl = f*cl[i] + (1.-f)*cl[i+1]

    print "CL( alpha =",a,")  = ",fcl

