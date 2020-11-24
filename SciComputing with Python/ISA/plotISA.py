'''
Plots the calculation for ISA using stdatmos
'''
import stdatmos
import matplotlib as mplt
import matplotlib.pyplot as plt
step = 100 #m
start = 0
stop = 51000

#get the data to plot
hOut=[]
pOut=[]
rhoOut=[]
TOut=[]
vSoundOut=[]
h = start
while h<stop:
    p,rho,T = stdatmos.isa(h)
    hOut.append(h)
    pOut.append(p)
    rhoOut.append(rho)
    TOut.append(T)
    vSoundOut.append((T*1.4*287)**.5)
    h+=step

#Plot
#Pressure
plt.subplot(2,2,1)
plt.plot(pOut,hOut)
plt.title("Pressure")
plt.xlabel("Pressure [Pa]")
plt.ylabel("Height [m]")
#Density
plt.subplot(2,2,2)
plt.plot(rhoOut,hOut)
plt.title("Density")
plt.xlabel("Density [kg/m3]")
plt.ylabel("Height [m]")
#Temperature
plt.subplot(2,2,3)
plt.plot(TOut,hOut)
plt.title("Temperature")
plt.xlabel("Temperature [K]")
plt.ylabel("Height [m]")
#Speed of sound
plt.subplot(2,2,4)
plt.plot(vSoundOut,hOut)
plt.title("Speed of Sound")
plt.xlabel("Speed of sound [m/s]")
plt.ylabel("Height [m]")

plt.show()