# -*- coding: utf-8 -*-
"""
Solve the statics of the fuselage system

@revision: 0
@author: etodorov
@date: 14 Feb 16
"""
#software imports
import sys
from base import TestProblem, Solver

#mathematical imports

inputList=[  'L',
             'Lf1',
             'Lf2',
             'Lf3',
             'R',
             'dtailz',
             'dtaily',
             'dlgy',
             'Sx',
             'W',
             'gtd']
outputList = [   "FLx",
                 "FLy",
                 "RLx",
                 "RLy1",
                 "RLy2"]
                 
class Statics(Solver):
    def solve(self,Problem):
        """
        **Statics solver**
        \n
        all inputs and outputs are numbers
        \n  
        """
        for i in self.inputList:
            setattr(sys.modules[__name__], i, getattr(Problem, i))
        #YOUR CODE STARTS HERE
        FLy=gtd*W*(-L*0.5+Lf1+Lf2)/Lf2 #Using sum about the moment around x
        RLx=Sx*((L-Lf1)+dtailz)/Lf2 #Using sum of moments in y and sum of forces in x
        FLx=RLx-Sx #Using sum of forces in x
        RLy2=((-FLx+RLx)*(dlgy+R)+Sx*(dtaily-R)+gtd*W*Lf3*0.5-FLy*Lf3*0.5)/Lf3 #Using sum of moments around z and sum of forces in y
        RLy1=gtd*W-FLy-RLy2 #Using sum of forces in y



    
            
        #YOUR CODE ENDS HERE
        for o in self.outputList:
            if o in locals():
                setattr(Problem, o, locals()[o])
            else:
                print "WARNING: missing output ",o    
            
statics = Statics(inputList,outputList)

#TODO: add unit tests
if __name__=="__main__": #exectutes only when you run THIS file
    tp1 = TestProblem()
    
    #provide all inputs in this shape
    
    tp1.L =70.0
    tp1.Lf1=5.
    tp1.Lf2=31.2
    tp1.Lf3=11.0
    tp1.R=3.1
    tp1.dtailz=5.4
    tp1.dtaily=7.5
    tp1.dlgy= 3.0
    tp1.Sx=610000.0
    tp1.W=250000.0
    tp1.gtd=29.43

#    tp1.L = 1.
#    tp1.Lf1 = 0.
#    tp1.Lf2 = 0.99
#    tp1.R = 1.
#    tp1.dtailz = 1.
#    tp1.dtaily = 1.
#    tp1.dlgy = 1.
#    tp1.Lf3 = 1.
#    tp1.Sx = 10.
#    tp1.W = 1.
#    tp1.gtd = 10.
    
    #execute the solving routine
    statics.solve(tp1)
    
    #verify that outputs agree with expectation
    print tp1.FLx
    print tp1.FLy
    print tp1.RLx
    print tp1.RLy1
    print tp1.RLy2
    
