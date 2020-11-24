import scipy as sp
import matplotlib.pyplot as plt

# Read file into tables:
table = sp.genfromtxt("flightlog.dat",delimiter="=",comments="C")
xtab=table[:,0]
ytab=table[:,1]
plt.title('Noisy data')
plt.plot(xtab,ytab,"r+")
plt.show()

# Polyfitting 10th order polynomial

coefficients = sp.polyfit(xtab, ytab, 10)
polynomial = sp.poly1d(coefficients)
ysmooth = sp.polyval(polynomial,xtab)


plt.plot(xtab,ysmooth)
plt.plot(xtab,ytab,"r+")
plt.title('Polynomial 10th order')
plt.show()

# Polyfitting 20th order

coefficients = sp.polyfit(xtab, ytab, 20)
polynomial = sp.poly1d(coefficients)
ysmooth = sp.polyval(polynomial,xtab)


plt.plot(xtab,ysmooth)
plt.plot(xtab,ytab,"r+")
plt.title('Polynomial 20th order')
plt.show()

g = open("filtered.log","w")
g.write("C\n")
g.write("C Data smoothed by fitting a 20th order polynomial\n")
g.write("C\n")
for i in range(len(xtab)):
    line = str(xtab[i])+" = "+str(ysmooth[i])+"\n"
    g.write(line)
#    print line
g.close()

   
    

    
