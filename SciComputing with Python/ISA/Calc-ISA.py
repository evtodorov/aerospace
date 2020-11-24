import math
#data
p0 = 101325.0       #Pa
T0 = 288.15         #K
rho0 = 1.225        #kg/m3
hTrop = 11000.      #m
hStrat = 20000.     #m
aTrop = -0.0065     #K/m
g0=9.80665          #m/s^2
R = 287.            

TStrat = T0 + aTrop*hTrop
pStrat = (TStrat/T0)**(-g0/aTrop/R)*p0
rhoStrat = (TStrat/T0)**(-g0/aTrop/R-1)*rho0

print "*** ISA Calculations ***"

#menu
menu0 = int()
while(menu0<=0 or menu0>=3):
    menu0 = int(input("What do you want to do? \n \
1) Calculate pressure and density at altitude \n \
2) Calculate altitude from pressure \n"))

# 01 pressure and density
if (menu0==1):
        print "Calculating pressure and density"
        menu1 = int()
        while(menu1<=0 or menu1>=3):
            menu1 = input("Choose units for the input \n \
1) Enter an altitude in meters \n \
2) Enter an altitude in feet \n")
        if (menu1==1):
                h = input("Altitude in meters: ")
        elif (menu1==2):
                h = input("Altitude in feet: ")*0.3048
        else: print "Something is wrong"
	#troposhpere
        if(h<=hTrop):
		#temperature
                T = T0 + aTrop*h
		#pressure and density
                p = (T/T0)**(-g0/aTrop/R)*p0
                rho = (T/T0)**(-g0/aTrop/R-1)*rho0
                
	#stratoshpere   
        elif(hTrop<h<=hStrat):
		#temperature
                T = TStrat
		#pressure and density calculation
                p = math.exp(-g0/R/T*(h-hTrop))*pStrat
                rho = math.exp(-g0/R/T*(h-hTrop))*rhoStrat
	
        else:
                print "Can't calculate that" 
	
	#print results
        print "T = ",T,"K"
        print "p = ",p,"Pa"
        print "rho = ",rho,"kg/m3"

# 02 altitude
elif (menu0==2):
        print "Calculating altitude (less than 20km)"
        #input
        p = input("Enter pressure in Pa: ")
        #calculate temperature
        T = T0*(p/p0)**(-aTrop*R/g0)
        #stratosphere
        if(T<216.65):
                T = 216.65
                h = math.log(p/pStrat)*(-R*T/g0)+hTrop
        #troposhpere
        else:
                h = (T-T0)/aTrop

        #check validity
        if(h>=20000): print "Can't calculate that"

        #print results
        menu2 = input("Do you want the altitude in \n 1) meters \n 2) feet \n 3) FL \n")
        if(menu2==1):
                print "h = ",h,"m"
                
        if(menu2==2):
                print "h = ", h/0.3048,"ft"
                
        if(menu2==3):
                hFL = h/0.3048/100
                if(hFL<10): print "h = FL00"+str(int(hFL))
                elif(hFL<100): print "h = FL0"+str(int(hFL))
                else: print "h = FL"+str(int(hFL))

#hold
dummy = raw_input("Press enter")
