# -*- coding: utf-8 -*-
"""
Shear flow in the frames solver


@revision: 1
@author: wessel
@date: 16 Feb 16
"""
#software imports
import sys
from base import TestProblem, Solver

#mathematical imports
import math

inputList=[  'qsr', 'z', 'L',
             'Lf1',
             'Lf2']
outputList = ["q_frame1", 'q_frame2']
                 
class FrameShear(Solver):
    def solve(self,Problem):
        """
        **Shear flow in the frames solver**
        \n
        qs is a 2D array, 
        the other inputs are constant;
        q_frame 1 and 2 are 1d arrays with theta (or r)
        """
        for i in self.inputList:
            setattr(sys.modules[__name__], i, getattr(Problem, i))
        #YOUR CODE STARTS HERE
        # q = V * Q / Ixx
        idz1 = z < (L-Lf1-Lf2)
        q_frame1 = qsr[idz1][-1] - qsr[idz1!=1][0]
        idz2 = z < (L-Lf1)
        q_frame2 = qsr[idz2][-1] - qsr[idz2!=1][0]
        #YOUR CODE ENDS HERE
        for o in self.outputList:
            if o in locals():
                setattr(Problem, o, locals()[o])
            else:
                print "WARNING: missing output ",o    
            
frameShear = FrameShear(inputList,outputList)

#TODO: add unit tests
if __name__=="__main__": #exectutes only when you run THIS file
    tp1 = TestProblem()
    
    #provide all inputs in this shape
    
    #tp1.Input1 = 
    #tp1.Input2 = 
    
    #execute the solving routine
    frameShear.solve(tp1)
    
    #verify that outputs agree with expectation
    print #tp1.Output1
    print #tp2.Output2
    
