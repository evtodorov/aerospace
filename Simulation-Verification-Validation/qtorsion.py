# -*- coding: utf-8 -*-
"""
Determine the constant shear flow due to torsion

@revision: 0
@author: etodorov
@date: 14 Feb 16

@revison: 1 - add solver
@author: etodorov
@date: 20 Feb 16
"""
#software imports
import sys
from base import TestProblem, Solver

#mathematical imports
import numpy as np
inputList=[  'Tz',
             'R', 'A1', 'A2', 'theta_floor', 'Lfloor',
             'L',
             'Lf1',
             'Lf2',
             'ts',
             'tf',
             'hf']
             
outputList = ["qT"   ]
                 
class TorsoinalShearFlow(Solver):
    def solve(self,Problem):
        """
        **Shear flow due to torsion solver**
        \n
        Tz is function of z;
        all other inputs are numbers;
        qT is function  of z returning qT_top, qT_bot, qT_f
        \n  
        """
        for i in self.inputList:
            setattr(sys.modules[__name__], i, getattr(Problem, i))
        #YOUR CODE STARTS HERE
        #def Tz(z):
         #   return Tz

        def qT(z):
            '''
            return qT_top, qT_bot, qT_f
            '''
            
            pi = np.pi
            a1 = ((pi+2*theta_floor)*R/ts+Lfloor/tf)*1/(2*A1)+1/(2*A2)*Lfloor/tf
            a2 = ((pi-2*theta_floor)*R/ts+Lfloor/tf)*1/(2*A2)+1/(2*A1)*Lfloor/tf

            T = Tz(z)
            q1 = T/(2*A1+2*A2*a1/a2)
            q2 = a1/a2*q1
            
            return q1, q2, q1-q2

        #YOUR CODE ENDS HERE
        for o in self.outputList:
            if o in locals():
                setattr(Problem, o, locals()[o])
            else:
                print "WARNING: missing output ",o    
            
qtorsion = TorsoinalShearFlow(inputList,outputList)

#TODO: add unit tests
if __name__=="__main__": #exectutes only when you run THIS file
    tp1 = TestProblem()
    
    #provide all inputs in this shape


    tp1.Tz = 10000
    tp1.R = 3.2
    tp1.A1 = 23.58
    tp1.A2 = 8.58896
    tp1.theta_floor = 0.3843967745
    tp1.Lfloor = 5.93296
    tp1.L = 70.0
    tp1.Lf1 = 5.0
    tp1.Lf2 = 31.2
    tp1.ts = 0.005
    tp1.tf = 0.03
    tp1.hf = 2.0
    
    def Tz_(z):
        return 1e+4

    tp1.Tz = Tz_
    
    #execute the solving routine
    qtorsion.solve(tp1)
    
    #verify that outputs agree with expectation
    print tp1.qT(1)
    #print #tp2.Output2
