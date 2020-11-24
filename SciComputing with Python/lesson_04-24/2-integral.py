import math
print "*** Integration of exp(-x^2)dx from xmin to xmax ***"
xmin = input("Choose lower boundary: ")
xmax = input("Choose upper boundary: ")
n = input("Choose the number of subintervals: ")
s = 0
sup = 0
sd= 0
x = float(xmin)
dx = (xmax-xmin)/float(n)
while (x<xmax-dx):
    s += math.exp(-(x+dx/2.)**2)    #midpoint
    sup += math.exp(-(x+dx)**2)     #endpoint
    sd += math.exp(-x**2)           #startpoint
    x += dx
res = dx*s
err = abs(sd-sup)
print  "Integral of exp(-x^2)dx from "+str(xmin)+" to "+str(xmax)+" is "+str(res)+" +- "+str(err)