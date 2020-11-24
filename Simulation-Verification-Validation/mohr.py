# -*- coding: utf-8 -*-
"""
Combine the stresses

@revision: 0
@author: etodorov
@date: 14 Feb 16
"""
#software imports
import sys
from base import TestProblem, Solver

#mathematical imports
import numpy as np
inputList=[  'sigma_z_r', 'sigma_z_f',
             'tau_totr', 'tau_totf',
             'xr', 'yr', 'z']
outputList = ["vonMisesStress_ring", 'vonMisesStress_floor'   ]
                 
class MisesStress(Solver):
    def solve(self,Problem):
        """
        **Stress combiner**
        \n
        sigma_z is a fucntion of (x,y,z);
        tau_tot is a 2d array in directions (theta, z);
        \n  
        vonMisesStresses are 2D arrays (z, xsectional)
        """
        for i in self.inputList:
            setattr(sys.modules[__name__], i, getattr(Problem, i))
        #YOUR CODE STARTS HERE
        vonMisesStress_ring = np.sqrt(sigma_z_r**2+3*tau_totr**2)
        vonMisesStress_floor= np.sqrt(sigma_z_f**2+3*tau_totf**2)
        #YOUR CODE ENDS HERE
        for o in self.outputList:
            if o in locals():
                setattr(Problem, o, locals()[o])
            else:
                print "WARNING: missing output ",o    
            
mohr = MisesStress(inputList,outputList)

#TODO: add unit tests
if __name__=="__main__": #exectutes only when you run THIS file
    tp1 = TestProblem()
    
#    provide all inputs in this shape
    
    tp1.sigma_z_r = 526000000
    tp1.sigma_z_f = 0
    tp1.tau_totr = 100
    tp1.tau_totf = 0
    tp1.xr = 0
    tp1.yr = 0
    tp1.z = 0
    
    #execute the solving routine
    mohr.solve(tp1)
    
    #verify that outputs agree with expectation
    print tp1.vonMisesStress_ring
    print tp1.vonMisesStress_floor
    
    