# -*- coding: utf-8 -*-
"""
Solve the torisional moment diagram


@revision: 0
@author: etodorov
@date: 14 Feb 16
"""
#software imports
import sys
from base import TestProblem, Solver

#mathematical imports
import matplotlib.pyplot as plt
import math
import numpy as np

#if you need the input to include Vx and Vy, let me know
inputList=[  'L',
             'R',
             'Lf1',
             'Lf2',
             'Lf3',
             'Sx',
             'dtaily',
             'dlgy',
             "FLx",
             "FLy",
             "RLx",
             "RLy1",
             "RLy2"]
outputList = ["Tz"   ]
                 
class TorsionalMoment(Solver):
    def solve(self,Problem):
        """
        **Shear force diagram solver**
        \n
        all inputs are numbers;
        Tz is a function
        \n  
        """
        for i in self.inputList:
            setattr(sys.modules[__name__], i, getattr(Problem, i))
        #YOUR CODE STARTS HERE
        def Tz(z):
            if z>=0 and z<(L-Lf1-Lf2):
                Tz = - Sx*(dtaily-R)
            if z > (L-Lf1-Lf2) and z<(L-Lf1):
                Tz = - Sx*(dtaily-R) - RLx*(dlgy+R) -RLy1*(Lf3/2)+RLy2*(Lf3/2)
            if z > (L-Lf1):
                Tz = - Sx*(dtaily-R) - RLx*(dlgy+R) -RLy1*(Lf3/2)+RLy2*(Lf3/2) + FLx*(dlgy+R)
            return Tz
        #YOUR CODE ENDS HERE
        for o in self.outputList:
            if o in locals():
                setattr(Problem, o, locals()[o])
            else:
                print "WARNING: missing output ",o    
            
tmd = TorsionalMoment(inputList,outputList)

#TODO: add unit tests
if __name__=="__main__": #exectutes only when you run THIS file
    tp1 = TestProblem()
    
    #provide all inputs in this shape
   
    tp1.R = 3.1
    tp1.L = 70.
    tp1.Lf1 = 5.
    tp1.Lf2 = 31.2
    tp1.Lf3= 11.
    tp1.FLx = 766410.25641
    tp1.FLy = 282980.769231
    tp1.RLx = 1376410.25641
    tp1.RLy1 = 2954986.88811
    tp1.RLy2 = 4119532.34266
    tp1.Sx = 610000.
    tp1.dtaily = 7.5
    tp1.dlgy = 3.
    
#    tp1.R = 1.
#    tp1.L = 1.
#    tp1.Lf1 = 0.
#    tp1.Lf2 = 0.99
#    tp1.Lf3= 1.
#    tp1.FLx = 10.202020202
#    tp1.FLy = 4.94949494949
#    tp1.RLx = 20.202020202
#    tp1.RLy1 = -17.4747474747
#    tp1.RLy2 = 22.5252525253
#    tp1.Sx = 10.
#    tp1.dtaily = 1.
#    tp1.dlgy = 1.
#    
   
    
    
    #execute the solving routine
    tmd.solve(tp1)
   
    Tz_vector = np.vectorize(tp1.Tz)
    z = np.linspace(0,75,1000)
    plt.plot(z, Tz_vector(z))
    plt.show()
    
    #verify that outputs agree with expectation
    print - tp1.Sx*(tp1.dtaily-tp1.R) - tp1.RLx*(tp1.dlgy+tp1.R) -tp1.RLy1*(tp1.Lf3/2)+tp1.RLy2*(tp1.Lf3/2) + tp1.FLx*(tp1.dlgy+tp1.R)
    print Tz_vector(70)    
