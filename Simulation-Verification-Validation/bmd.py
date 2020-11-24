# -*- coding: utf-8 -*-
"""
Solve the bending moment diagram


@revision: 0
@author: etodorov
@date: 14 Feb 16
"""
#software imports
import sys
from base import TestProblem, Solver

#mathematical imports
import numpy as np
import matplotlib.pyplot as plt
#if you need the input to include Vx and Vy, let me know
inputList=[  'L',
             'Lf1',
             'Lf2',
             "FLx",
             "FLy",
             "RLx",
             "RLy1",
             "RLy2",
             "W",
             "gtd",
             "dtailz",
             "Sx"]
outputList = ["Mx","My"   ]
                 
class BendingMoment(Solver):
    def solve(self,Problem):
        """
        **Bending moment diagram solver**
        \n
        all inputs are numbers;
        Mx and My are functions
        \n  
        """
        for i in self.inputList:
            setattr(sys.modules[__name__], i, getattr(Problem, i))
        
        
        def My(z):
            Moment=0
           
            if z < (L-Lf1-Lf2) and z>= 0:
                Moment=-Sx*(z+dtailz)
            elif z > (L-Lf1-Lf2) and z< (L-Lf1):
                Moment=-Sx*(z+dtailz)+RLx*(z-L+Lf1+Lf2)
            elif z > (L-Lf1) and z<= L:
                Moment=-Sx*(z+dtailz)+RLx*(z-L+Lf1+Lf2)-FLx*(z-L+Lf1)  
            elif z<0:
                raise ValueError("Z should be larger than 0!")
           # else:
               # raise ValueError("Discontinuity")
            return Moment
                        
            
        def Mx(z):
            distrload=gtd*W/L
            Moment=0
            if z < (L-Lf1-Lf2) and z>= 0:
                Moment=-distrload*z**2./2.
            elif z > (L-Lf1-Lf2) and z< (L-Lf1):
                Moment=-distrload*z**2./2.+(RLy1+RLy2)*(z-L+Lf1+Lf2)
            elif z > (L-Lf1) and z <= L:
                Moment=-distrload*z**2./2.+(RLy1+RLy2)*(z-L+Lf1+Lf2)+FLy*(z-L+Lf1)
            elif z<0:
                raise ValueError("Z should be larger than 0!")
          #  else:
          #      raise ValueError("Discontinuity")
            return -Moment
            
        #YOUR CODE ENDS HERE
        for o in self.outputList:
            if o in locals():
                setattr(Problem, o, locals()[o])
            else:
                print "WARNING: missing output ",o    
            
bmd = BendingMoment(inputList,outputList)

#TODO: add unit tests
if __name__=="__main__": #exectutes only when you run THIS file
    tp1 = TestProblem()
    
    #provide all inputs in this shape
    
    tp1.L = 70.0
    tp1.Lf1 = 5.0
    tp1.Lf2=31.2
    tp1.FLx=766410.25641
    tp1.FLy=282980.769231
    tp1.RLx=1376410.25641
    tp1.RLy1=2954986.88811
    tp1.RLy2=4119532.34266
    tp1.W=250000
    tp1.gtd=29.43
    tp1.dtailz=5.4
    tp1.Sx=610000.0
    
#    tp1.L = 100
#    tp1.Lf1 = 0.0
#    tp1.Lf2=99.99
#    tp1.FLx= 0.101
#    tp1.FLy= 4.99
#    tp1.RLx= 10.10
#    tp1.RLy1=-17.499
#    tp1.RLy2=22.5
#    tp1.W=1.
#    tp1.gtd=10.
#    tp1.dtailz=1.
#    tp1.Sx=10.
#    
    
    z=np.linspace(0.,tp1.L,1000)
    #texecute the solving routine
    bmd.solve(tp1)
    
    #verify that outputs agree with expectation
    My_vec = np.vectorize(tp1.My)
    Mx_vec = np.vectorize(tp1.Mx)
    
    plt.plot(z, My_vec(z), 'r', label = 'My')
    plt.plot(z, Mx_vec(z), label = 'Mx')
    plt.legend()
    plt.show()    
   
