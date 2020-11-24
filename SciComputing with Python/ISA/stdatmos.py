def isa(h):
    '''
    Takes altitude in meters and returns pressure in Pa, density in kg/m3 and tempreature in K
    Works in:
    1 - Troposphere
    2 - Tropopause
    3 - Stratosphere
    4 - Stratosphere
    5 - Stratopause
    '''
    import math
    #data
    g0=9.80665          #m/s^2
    R = 287.                
    
    p1 = 101325.0       #Pa
    T1 = 288.15         #K
    rho1 = 1.225        #kg/m3
    a1 = -0.0065        #K/m
    
    h2 = 11000.         #m     
    
    T2 = 216.65         #K
    p2 = 22632.         #Pa
    rho2 = .36398       #kg/m3
    
    h3 = 20000.         #m
    
    T3 = T2
    a3 = .001           #K/m
    p3 = 5474.9
    rho3 = .08805
    
    h4 = 32000.         #m
    
    T4 = 228.65
    a4 = .0028
    p4 = 868.02
    rho4 = .013227    #kg/m3

    h5 = 47000.         #m

    T5 = 270.65
    p5 = 110.91
    rho5 = .0014278

    h6 = 51000 
     
    	#temperature gradient
    def tempGrad(h,h0,a,T0,p0,rho0):
    		#temperature
         T = T0 + a*(h-h0)                   #K
    		#pressure and density
         p = (T/T0)**(-g0/a/R)*p0       #Pa
         rho = (T/T0)**(-g0/a/R-1)*rho0 #kg/m^3
         return p,rho,T
                    
    	#constant temperature   
    def tempConst(h,h0,T0,p0,rho0):
    		#temperature
         T = T0
    		#pressure and density calculation
         p = math.exp(-g0/R/T*(h-h0))*p0
         rho = math.exp(-g0/R/T*(h-h0))*rho0
         return p,rho,T
    
    if(h<h2): #troposhpere - 1
        p,rho,T = tempGrad(h,0,a1,T1,p1,rho1)
    elif(h2<=h<h3): #tropopause - 2
        p,rho,T = tempConst(h,h2,T2,p2,rho2)
    elif(h3<=h<h4): #stratosphere1 - 3
        p,rho,T = tempGrad(h,h3,a3,T3,p3,rho3)
    elif(h4<=h<h5): #stratosphere2 - 4
        p,rho,T=tempGrad(h,h4,a4,T4,p4,rho4)
    elif(h5<=h<=h6): #stratopause - 5
        p,rho,T=tempConst(h,h5,T5,p5,rho5)
    else: 
        print "The height is out of range. Height should be less than 51 km."
        return
           
    return p,rho,T


