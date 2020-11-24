# -*- coding: utf-8 -*-
"""
Direct stress solver


@revision: 1
@author: wessel
@date: 17 Feb 16
"""
#software imports
import sys
from base import TestProblem, Solver

#mathematical imports
import numpy as np
inputList=[  'Mx',
             'My',
             'Ixx',
             'Iyy',
             'yna', 'xr', 'yr', 'xf', 'yf', 'z']
outputList = ["sigma_z_r", "sigma_z_f"   ]
                 
class DirectStress(Solver):
    def solve(self,Problem):
        """
        **Direct stress solver**
        \n
        most inputs are numbers;
        Mx and My are functions of z;
        sigma_z_r,f are arrays
        \n  
        """
        for i in self.inputList:
            setattr(sys.modules[__name__], i, getattr(Problem, i))
        #YOUR CODE STARTS HERE
        xr_ = np.array([xr]).T
        yr_ = np.array([yr]).T
        xf_ = np.array([xf]).T
        yf_ = np.array([yf]).T
        Mx_ = np.vectorize(Mx)
        My_ = np.vectorize(My)
        sigma_z_r = My_(z)/Iyy*xr_ + Mx_(z)/Ixx*(yr_-yna)
        sigma_z_f = My_(z)/Iyy*xf_ + Mx_(z)/Ixx*(yf_-yna)
        sigma_z_r = sigma_z_r.T
        sigma_z_f = sigma_z_f.T
        #YOUR CODE ENDS HERE
        for o in self.outputList:
            if o in locals():
                setattr(Problem, o, locals()[o])
            else:
                print "WARNING: missing output ",o    
            
sigma = DirectStress(inputList,outputList)

#TODO: add unit tests
if __name__=="__main__": #exectutes only when you run THIS file
    tp1 = TestProblem()
    tp2 = TestProblem()
    
    #provide all inputs in this shape
    def My(z):                  #unit test with hollow tube of R = 0.5m and t = 3mm
        return 1000             #moments Mx = 2000 Nm and My = 1000 Nm
    def Mx(z):                  #location theta = 45 degrees
        return 2000             #should give 450638.298 Nm
    tp1.My = My
    tp1.Iyy = 0.00235
    tp1.xr = 0.353
    tp1.Mx = Mx
    tp1.Ixx = 0.00235
    tp1.yr = 0.353
    tp1.yna = 0
    tp1.z = 1
    tp1.xf = tp1.yf = 0
    tp2.My = My                 #should give 300425.5319 Nm
    tp2.Iyy = 0.00235
    tp2.xr = 0
    tp2.Mx = Mx
    tp2.Ixx = 0.00235
    tp2.yr = 0.353
    tp2.yna = 0
    tp2.z = 1
    tp2.xf = tp2.yf = 0
    
    #execute the solving routine
    sigma.solve(tp1)
    sigma.solve(tp2)    
    
    #verify that outputs agree with expectation
    print 'analytical value tp1: 450638.298 Nm'
    print 'numerical value tp1:',tp1.sigma_z_r, 'Nm'
    
    print 'analytical value tp2: 3000425.5319 Nm'
    print 'numerical value tp2:',tp2.sigma_z_r, 'Nm'
    
