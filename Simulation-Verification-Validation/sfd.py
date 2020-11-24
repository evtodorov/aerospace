# -*- coding: utf-8 -*-
"""
Solve the shear force diagram


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

inputList=[  'L',
             'Lf1',
             'Lf2',
             'FLx',
             'FLy',
             "RLx",
             "RLy1",
             "W",
             "Sx",
             "gtd",
             "RLy2"]
outputList = ["Vx","Vy"   ]
                 
class ShearForce(Solver):
    def solve(self,Problem):
        """
        **Shear force diagram solver**
        \n
        all inputs are numbers;
        Vx and Vy are functions
        \n  
        """
        for i in self.inputList:
            setattr(sys.modules[__name__], i, getattr(Problem, i))
        #YOUR CODE STARTS HERE
        def Vx(z):
            if z>=0 and z<(L-Lf1-Lf2):
                Vx =  Sx
            if z > (L-Lf1-Lf2) and z<(L-Lf1):
                Vx = Sx - RLx
            if z > (L-Lf1):
                Vx = Sx - RLx + FLx
            return Vx
        
        def Vy(z):
            if z>=0 and z<(L-Lf1-Lf2):
                Vy = - (W*gtd/L)*z
            if z > (L-Lf1-Lf2) and z < (L-Lf1):
                Vy = -(W*gtd/L)*z + RLy1 + RLy2
            if z > (L-Lf1):
                Vy = - (W*gtd/L)*z + RLy1 + RLy2 + FLy
            return Vy
       # Problem.Vx = Vx
        #Problem.Vy = Vy
        #YOUR CODE ENDS HERE
        for o in self.outputList:
            if o in locals():
                setattr(Problem, o, locals()[o])
            else:
                print "WARNING: missing output ",o    
            
sfd = ShearForce(inputList,outputList)

#TODO: add unit tests
if __name__=="__main__": #exectutes only when you run THIS file
    tp1 = TestProblem()
   
    #provide all inputs in this shape
    tp1.L = 70.
    tp1.Lf1 = 5.
    tp1.Lf2 = 31.2
    tp1.FLx = 766410.25641
    tp1.FLy = 282980.769231
    tp1.RLx = 1376410.25641
    tp1.RLy1 = 2954986.88811
    tp1.RLy2 = 4119532.34266
    tp1.W = 250000.
    tp1.Sx = 610000.
    tp1.gtd = 29.43
    
#    tp1.L = 1.
#    tp1.Lf1 = 0.
#    tp1.Lf2 = 0.99
#    tp1.FLx = 10.202020202
#    tp1.FLy = 4.94949494949
#    tp1.RLx = 20.202020202
#    tp1.RLy1 = -17.4747474747
#    tp1.RLy2 = 22.5252525253
#    tp1.W = 1.
#    tp1.Sx = 10.
#    tp1.gtd = 10.
    


    sfd.solve(tp1)
    Vx_vector = np.vectorize(tp1.Vx)
    z = np.linspace(0,1.1,1000)
    plt.plot(z, Vx_vector(z))
    plt.show()
    Vy_vector = np.vectorize(tp1.Vy)
  
    plt.plot(z, Vy_vector(z))
    plt.show()
    #execute the solving routine
    
    #verify that outputs agree with expectation
    print tp1.Vx(0)
    print tp1.Vy(0)
    
