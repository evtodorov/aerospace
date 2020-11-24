import numpy as np

A = np.mat("0 2 -1;3 0 2;-1 -1 1")
a = np.mat("1;9;0")

B = np.mat("3 4 -1;-2 -1 3;5 -1 1")
b = np.mat("1;2;3")

C = np.mat("2 1 3;11 2 -5;3 1 -4")
c = np.mat("4;0;5")

print "A) x = ",A.I*a

print "B) x = ",np.linalg.solve(B,b)
print "B) x = ",np.linalg.solve(B,b)*np.linalg.det(B)
print "det B=",np.linalg.det(B)

print "C) x = ",np.linalg.inv(C)*c
print "C) x = ",np.linalg.inv(C)*c*np.linalg.det(C)
print "det B=",np.linalg.det(C)



