# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 11:21:20 2014
Preliminary analysis tool
@author: etodorov
"""
#TODO: import F3
#TODO: interface
#TODO: optimization algorithm

from math import *
import numpy as np
from scipy.interpolate import interp1d

class Parameter:
    
    def __init__(self,dic):
        """
        for key in dic: \n
        \t setattr(self,key,float(dic[key]))
        """
        for key in dic:
            setattr(self,key,float(dic[key]))



#define functions for the diff equations
F1_data =  [[8.3, 3.8, 2.7, 2.,.82, 0.5,.35, .28,0.22,0.18],     #0.1
            [7.1, 3.3, 2.5,1.6, .7, .42,0.3, .22,0.18,0.14],     #0.2                                                 
            [6.2, 2.9,  2.,1.5, .6, .37,.25, .18, .14, 0.1],     #0.3
            [5.1, 2.5,1.62,1.2, .5, 0.3,.21, .16,0.12, .08],     #0.4
            [4.2, 2.2,1.37,.95,.41, .26,.18, .13,0.10, .07],     #0.5
            [3.4, 1.7,1.15,.76,.33, 0.2,.14,  .1,.080, .06],     #0.6
            [2.8, 1.2,0.82,.58,.26, .16, .1, .08,.060,.055],     #0.7
            [1.9, 0.9,0.58,.39,.17, 0.1,.07,.054,.040,.035],     #0.8
            [0.9, 0.4,0.25,0.2,.09,.058,.04,.025,.020,.019]]     #0.9
mu1_data = [0.05, 0.1,0.15,0.2,0.4, 0.6,0.8,1.  ,1.2, 1.4]
F2_data =  [[ 3.4, 2.6, 2.2, 2.0,1.82, 1.7,1.65],     #0.1
            [2.35, 1.9, 1.7,1.58,1.49,1.42,1.34],     #0.2                                                 
            [1.88,1.62, 1.5, 1.4, 1.3,1.26,1.24],     #0.3
            [ 1.6,1.43,1.33,1.26,1.22,1.21, 1.2],     #0.4
            [1.48, 1.3,1.23,1.19,1.15,1.12, 1.1],     #0.5
            [1.35, 1.2,1.15,1.13, 1.1, 1.1, 1.1],     #0.6
            [1.23,1.14, 1.1, 1.1, 1.1, 1.1, 1.1],     #0.7
            [1.15,1.12, 1.1, 1.1, 1.1, 1.1, 1.1],     #0.8
            [ 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1]]     #0.9
mu2_data = [  0.2, 0.4, 0.6, 0.8, 1. , 1.2, 1.4]    
F3_data =  [[28.5,26.5,24.5,23.,21.5,20.2,19.5],     #0.1
            [13.5,11.5,10.7,10., 9.4, 8.9, 8.3],     #0.2                                                 
            [ 7.7, 7.1, 6.3,5.7, 5.3, 5.0, 4.8],     #0.3
            [ 5.0, 4.4, 4.1,3.8, 3.6, 3.5, 3.2],     #0.4
            [ 3.3, 2.8, ],     #0.5
            [],     #0.6
            [],     #0.7
            [],     #0.8
            []]     #0.9
mu3_data = [  0.2, 0.4, 0.6,0.8,  1., 1.2, 1.4]     

def F1(g,mu):
    y = np.array(F1_data[int(g*10)-1]) 
    x = np.array(mu1_data)
    f = interp1d(x,y,kind="cubic")
    print "mu",mu
    return f(mu)

def F2(g,mu):
    y = np.array(F2_data[int(g*10)-1])  
    x = np.array(mu2_data)
    f = interp1d(x,y,kind="cubic")
    return f(mu)

def F3(g,mu):
    y = np.array(F3_data[int(g*10)-1])  
    x = np.array(mu3_data)
    f = interp1d(x,y,kind="cubic")
    return f(mu)
        
class Panel:
    def __init__(self,core,skin):
        self.core = core
        self.skin = skin
        
    def shear(self,insert):
        skin = self.skin
        force = 8*insert.r**2*self.core.tau + 2*skin.t*skin.sigma*insert.r
        #force = 8*insert.r**2*self.core.tau #+ 2*skin.t*skin.sigma*insert.r
        return force
    
    def pull_out(self,insert):
        core = self.core
        skin = self.skin
        skin.t = float(self.skin.t)
        rpotting = insert.r
        b = core.h/skin.t        
        c = b/(b+1)
        k = -0.931714
        n = 0.262866
        hi = 1/skin.t*sqrt(skin.G/skin.E*12*(1-skin.nu**2)*(b/2+1+2/3/b))
        rtaumax = rpotting/(1-exp(k*(hi*rpotting)**n))
        Kmax = rpotting/rtaumax*(1-sqrt(rtaumax/rpotting)*exp(hi*(rpotting-rtaumax)))
        force = 2*pi*rpotting*core.h*core.tau/c/Kmax
        return force

    def stress(self,insert,load):
        """
        non-analytical, uses extrapolated data from plots
        required input: \n
        insert: \n
        \t G: shear modulus \n
        \t r: potting r (or equivalent) \n
        panel: \n
        \t core.h: thickness \n
        \t core.G: shear modulus \n
        \t core.nu: poisson ratio \n
        \t skin.t: thickness \n
        \t skin.E: Young modulus \n
        load: out-of-plane load [kN] \n
        inplane: in plane load [kN] \n
        output: \n
        stress (face tensile, core shear, core tensile) [GPa]
        """
        core1 = self.core
        core2 = insert
        Gc1 = core1.G
        Gc2 = core2.G
        skin = self.skin
        self.curInsert = insert
        Q0 = load/(2*pi*insert.r)
        tau0 = Q0/(core1.h+self.skin.t)
        print"t0",tau0
        g = sqrt(Gc1/Gc2)
        kv = (1-2*core1.nu)/4/(1-core1.nu)
        mu = sqrt(kv*Gc1*core1.h*(core1.h+self.skin.t)**2/self.skin.E/self.skin.t**3)
        
        
        #prepare g for Fs
        if(g>=0.95):
            print "Insert should have higher G than core"
        elif(g<0.1):
            g = 0.1
        elif(g>0.9):
            g = 0.9
        else:
            g = round(g,1)
        #due to out-of-plane
        sigmaf = tau0*F1(g,mu)*core1.h*(core1.h+skin.t)/skin.t**2       #face tensile 
        tauc = tau0*F2(g,mu)                                            #core shear
        #sigmac = tau0*F3(g,mu)                                          #core tensile
        return sigmaf, tauc#, sigmac
        #TODO: add inplane
        #TODO (maybe): failure criteria core

        
    def weight(self,insert):
        return self.core.h*pi*insert.r**2*insert.rho

    def size(self,insert,Q,P):
        """
        Q - out of plane; P - in plane
        """
        #print "sizing..."
        r = 1.
        strongEnough = False
        while not strongEnough and r<10000:
            r+=.5
            insert.r = r
            Qs = self.pull_out(insert)
            Ps = self.shear(insert)
            if (P/Ps)**2 + (Q/Qs)**2 <= 1:
                strongEnough = True
                
        m = self.weight(insert)
        return r, m
            

#validattions
#shear and pull-out - OK
core = Parameter({"h":20,"tau":0.0036})
skin = Parameter({"t":1.5,"E":42,"G":63,"nu":0.05,"sigma":.250})
insert = Parameter({"r":10})
panel = Panel(core,skin)
core2 = Parameter({"h":14.6,"tau":0.0009})
skin2 = Parameter({"t":0.24,"E":20,"G":1.8,"nu":0.059,"sigma":0.150})
insert2 = Parameter({"r":19})
panel2 = Panel(core2,skin2)
#stress_concentrations - OK
eglass = Parameter({"t":3.3,"E":16,"nu":0.3,"sigma":0.028,"G":10})
pvc = Parameter({'h':40,"G":0.040,"nu":0.32,"tau":0.001})
plywood = Parameter({'G':1.07,'r':75})
validation = Panel(pvc,eglass)

#for testing
h1 = Parameter({"h":10,"tau":0.00234,'G':0.214})
h2 = Parameter({"h":20,"tau":0.00234,'G':0.214})

t9 = Parameter({"t":.9,'E':61,"G":60,"nu":.05,"sigma":.606})
t12 = Parameter({"t":1.2,'E':61,"G":60,"nu":.05,"sigma":.606})
t13 = Parameter({"t":1.3,'E':61,"G":60,"nu":.05,"sigma":.606})
t21 = Parameter({"t":2.1,'E':61,"G":60,"nu":.05,"sigma":.606})
t26 = Parameter({"t":2.6,'E':61,"G":60,"nu":.05,"sigma":.606})
D30P = Parameter({'G':.7,'r':15})
D20P = Parameter({'G':.7,'r':10})
D20C = Parameter({'G':.1,'r':10})
D30C = Parameter({'G':.1,'r':15})
D40C = Parameter({'G':.1,'r':20})
D40P = Parameter({'G':.7,'r':20})
D50P = Parameter({'G':.7,'r':25})
D50C = Parameter({'G':.1,'r':25})
h1t09 = Panel(h1,t9)
h1t12 = Panel(h1,t12)
h1t13 = Panel(h1,t13)
h2t13 = Panel(h2,t13)
h1t21 = Panel(h1,t21)
h1t26 = Panel(h1,t26)
'''
print "h1t13.shear(D20C)", h1t13.shear(D20C)
print "h1t21.shear(D20C)", h1t21.shear(D20C)
print "h1t26.pull_out(D30C)", h1t26.pull_out(D30C)
print "h1t13.shear(D20P)", h1t13.shear(D20P)
print "h1t13.pull_out(D30P)", h1t13.pull_out(D30P)
print "h1t13.pull_out(D50P)", h1t13.pull_out(D50P)
print "h1t13.pull_out(D50B)", h1t13.pull_out(D50B)
print "h2t13.pull_out(D50P)", h2t13.pull_out(D50P)
'''

#print "h1t09.pull_out(D20C)",h1t09.pull_out(D50C)
#print "h1t09.pull_out(D30P)",h1t09.pull_out(D50P)
#print "h1t09.shear(D20P)",h1t09.shear(D20P)
#print "h1t12.shear(D20C)",h1t12.shear(D20C)
#print "h1t09.shear(D20C)",h1t09.shear(D20C)

"""
v1
h1t13.shear(D12C) 9.9476832
h1t26.shear(D12C) 19.2437232
h1t26.pull_out(D12C) 1.425207227
h1t13.shear(D20P) 17.628
h1t13.pull_out(D30P) 2.65097826818
h1t13.pull_out(D50P) 4.32718530928
h1t13.pull_out(D50B) 4.32718530928
h2t13.pull_out(D50P) 8.08937993279
v2
h1t13.shear(D20C) 17.628
h1t21.shear(D20C) 27.324
h1t26.pull_out(D20C) 2.21340062392
h1t13.shear(D20P) 17.628
h1t13.pull_out(D30P) 2.65097826818
h1t13.pull_out(D50P) 4.32718530928
h1t13.pull_out(D50B) 4.32718530928
h2t13.pull_out(D50P) 8.08937993279
v3
h1t09.pull_out(D20C) 4.11988886505
h1t09.pull_out(D30P) 4.11988886505
h1t09.shear(D20P) 12.78
h1t12.shear(D20C) 16.416
h1t09.shear(D20C) 12.78
v4
"""

#suspension front
#h15 = Parameter({"h":15,"tau":0.00234,'G':0.214})
#thincore = Panel(h15,t21)
#thickcore = Panel(h2,t21)

#TODO:
tUDpull = Parameter({"t":1.2,'E':50.,"G":40.,"nu":.05,"sigma":.603})

tUDshear = Parameter({"t":.7,'E':60.,"G":40.,"nu":.05,"sigma":.884})
#tUDshear = Parameter({"t":.7,'E':60.,"G":40.,"nu":.05,"sigma":.600})
tISO = Parameter({"t":0.4,'E':56.9,"G":40.,"nu":.05,"sigma":.656})
panelUDpull = Panel(h2,tUDpull)
panelUDshear = Panel(h2,tUDshear)
panelISO = Panel(h2,tISO)
print "D50C Pull_out", panelUDpull.pull_out(D50C)
print "D50P Pull_out", panelUDpull.pull_out(D50P)
print "D40C Shear", panelUDshear.shear(D40C)
print "D40P Shear", panelUDshear.shear(D40P)
print "D40P ISO Shear", panelISO.shear(D40P)
"""
D50C Pull_out 8.04902042719
D50P Pull_out 8.04902042719
D40C Shear 24.288
D40P Shear 24.288
D40P ISO Shear 17.984
>>> ================================ RESTART ================================
>>> 
D50C Pull_out 8.04902042719
D50P Pull_out 8.04902042719
D40C Shear 32.24
D40P Shear 32.24
D40P ISO Shear 17.984
"""
