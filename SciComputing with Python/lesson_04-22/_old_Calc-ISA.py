import math
#data
p0 = 101325.0
T0 = 288.15
rho0 = 1.225
hTrop = 11000.
hStrat = 20000.
aTrop = -0.0065
aStrat = 0.0
g0=9.80665
R = 287.

#menu
print "*** ISA Calculations ***"
menu0 = input("What do you want to do? \n \
                1) Calculate pressure and density at altitude \n \
                2) Calculate altitude from pressure \n")

if (menu0==1):
menu1 = input("What do you want to do? \n \
                1) Enter an altitude in meters \n \
                2) Enter an altitude in feet \n")
if (menu1==1):
    h = input("Altitude in meters: ")
if (menu1==2):
    h = input("Altitude in feet: ")*0.3048

#troposhpere
if(h<=hTrop):
    #temperature
    a = aTrop
    T = T0 + a*h
    #pressure and density
    p = (T/T0)**(-g0/a/R)
    rho = (T/T0)**(-g0/a/R-1)
    #print results
    print "Relative to sea level"
    print "p = ",p,"% of the pressure at sea level"
    print "rho = ",rho,"% of the pressure at sea level"
#stratoshpere   
elif(hTrop<=h<=hStrat):
    #temperature
    a = aStrat
    T = T0 + aTrop*hTrop
    #pressure and density
    p = math.exp(-g0/R/T*(h-hTrop))
    rho = p
    #print
    print "Relative to sea level"
    print "p = ",p,"% of the pressure at sea level"
    print "rho = ",rho,"% of the pressure at sea level"
    
else:
    print "Can't calculate that"

#print results
print "T = ",T,"K"
print "p = ",p*p0,"Pa"
print "rho = ",rho,"kg/m3"
