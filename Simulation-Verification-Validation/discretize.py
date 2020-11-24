# -*- coding: utf-8 -*-
"""
Discretize the system with booms


@revision: 0
@author: etodorov
@date: 14 Feb 16

@revision: 1 - inputs added: yf, xf, Bf, m, k, k0; completed z
@author: etodorov
@date: 16 Feb 16

@revision: 2 - finished + visualization unit test
@author: etodorov
@date: 17 Feb 16
"""
from __future__ import division
#software imports
import sys
from base import TestProblem, Solver

#mathematical imports

import numpy as np
import math
pi = np.pi
inputList=[  'L', 
             'Lf1', 
             'Lf2',
             'R',
             'hf',
             'ts',
             'tf',
             'tst',
             'hst',
             'wst',
             'ns',
             'dz',
             'p',
             'q']
outputList = ['xr', 'xf',
              'yr', 'yf',
              'Br', 'Bf',
              'm', 'k', 'k0',
              'z']
                 
class Discretize(Solver):
    def solve(self,Problem):
        """
        **Main discretizer**
        \n \t
        Determine the locations of the booms and 
        \n
        all inputs are numbers; \n  
        z is a 1D array;
        \n
        m = n + (n-1)*q - ring booms number \n
        the floor starts b/n k-1st and kth boom
        \n
        xr(r), yr(r), Br(r) are 1D arrays; 
        \n
        Indexing: k0 are the number of booms bf the 1st stringer;
        Br[k0::q+1] are stringer booms; len(ir) = m; len(if) = p
        """
        for i in self.inputList:
            setattr(sys.modules[__name__], i, getattr(Problem, i))
        #YOUR CODE STARTS HERE
       
        eps = 1e-6  #just before/after value
        zrear  = L-Lf1-Lf2
        zfront = L-Lf1
        
        #split each part s.t. we have "just before/after" node
        ztail = np.linspace(0,(zrear-eps), int(zrear/dz + 1))
        zmid = np.linspace(zrear+eps,zfront-eps, int(Lf2/dz + 1))
        znose = np.linspace(zfront-eps,L, int(Lf1/dz + 1))
        
        ########
        z = np.concatenate((ztail,zmid,znose))        
        ########
        
        #################################
        #####
        m = ns + ns*q
        #####
        
        # there are q small booms between each stringer
        Astr = tst*(wst + hst)        
        Br = np.ones((m,))*(2*pi*R*ts/m) #create m booms
        Br[::(q+1)] += Astr           #increment every q+1st boom
        
        # the stringers are symmetric w.r.t y axis
        theta_floor = math.asin((hf-R)/R)
        dtheta_str = (2*pi/ns)
        dtheta = 2*pi/m
        theta0 = math.copysign(abs(theta_floor)//dtheta,theta_floor)*dtheta
        theta0_str = math.copysign( abs(theta_floor) // dtheta_str, theta_floor ) * dtheta_str
        thetar = np.linspace(theta0,2*pi+theta0,m+1)[:-1]        
        
        ######
        xr = R*np.cos(thetar)
        yr = R*np.sin(thetar)
        k0 = len(np.where(thetar < theta0_str)[0])
        Br = np.roll(Br,k0)
        k = np.where(yr < hf-R)[0][0]
        ######
        Problem.theta_floor = theta_floor
        Lfloor = math.sqrt(R*R - (hf-R)**2 )        
        
        #######
        yf = np.ones((p,))*(hf-R)
        xf = np.linspace(-Lfloor,Lfloor,p)
        Bf = np.ones((p,))*(tf*2*Lfloor/p)
        ######
        #YOUR CODE ENDS HERE
        for o in self.outputList:
            if o in locals():
                setattr(Problem, o, locals()[o])
            else:
                print "WARNING: missing output ",o    
            
discretize = Discretize(inputList,outputList)

#TODO: add unit tests
if __name__=="__main__": #exectutes only when you run THIS file
    tp1 = TestProblem()
    
    #provide all inputs in this shape
    
    tp1.L = 70
    tp1.Lf1 = 5
    tp1.Lf2 = 31.2
    tp1.R = 3.1
    tp1.hf = 1.5
    tp1.ns = 36
    tp1.ts =  4e-3
    tp1.tf = 25e-3
    tp1.tst=1.2e-3
    tp1.hst= 15e-3
    tp1.wst= 20e-3
    tp1.dz = 1
    tp1.q = 4 #inbetweeners
    tp1.p = 20 #floorers    
    #execute the solving routine
    discretize.solve(tp1)
    
    #verify that outputs agree with expectation
    print tp1.z
    import matplotlib.pyplot as plt
    plt.plot(tp1.xr,tp1.yr,'b.')
    plt.plot(tp1.xr[tp1.Br > tp1.Br[0]],tp1.yr[tp1.Br > tp1.Br[0]],'go')
    plt.plot(tp1.xr[tp1.k0::tp1.q+1],tp1.yr[tp1.k0::tp1.q+1],'r.')
    plt.plot(tp1.xf, tp1.yf, 'k*')
    plt.plot(tp1.xr[tp1.k-1],tp1.yr[tp1.k-1],'ro')    
    plt.plot(tp1.xr[tp1.k],tp1.yr[tp1.k],'bo')
    plt.plot(tp1.xr[0],tp1.yr[0],'ro')    
    plt.plot(tp1.xr[-1],tp1.yr[-1],'bo')
    plt.plot(tp1.R*np.cos(tp1.theta_floor),tp1.R*np.sin(tp1.theta_floor),'ko')
    plt.grid()
    plt.show()
    