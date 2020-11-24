# -*- coding: utf-8 -*-
"""
Shear stress solver


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
import numpy as np
#mathematical imports

inputList=[  'qsr', 'qsf',
             'qT',
             'p','k', 'z',
             'ts','tf']
outputList = ["q_totr", "q_totf",
              "tau_totr", "tau_totf"]
                 
class ShearStress(Solver):
    def solve(self,Problem):
        """
        **Shear stress solver**
        \n
        qsf and qsr are a 2D array (z, (x,y) );
        qT is functions of z returning qT_top,bot,f;
        the other inputs are constant;
        q_tot and tau_tot are 2d arrays
        """
        for i in self.inputList:
            setattr(sys.modules[__name__], i, getattr(Problem, i))
        #YOUR CODE STARTS HERE
        qT_ = np.vectorize(qT)
        qT_top, qT_bot, qT_f = qT_(z)
        q_totr = np.zeros(np.shape(qsr))
        q_totf = np.zeros(np.shape(qsf))
        q_totr[:,:k] = qsr[:,:k] + np.array([qT_top]).T
        q_totr[:,k:] = qsr[:,k:] + np.array([qT_bot]).T
        q_totf = qsf + np.array([qT_f]).T
        
        tau_totr = q_totr/ts
        tau_totf = q_totf/tf
        
        #YOUR CODE ENDS HERE
        for o in self.outputList:
            if o in locals():
                setattr(Problem, o, locals()[o])
            else:
                print "WARNING: missing output ",o
                
            
shearStress = ShearStress(inputList,outputList)

#TODO: add unit tests
if __name__=="__main__":
    tp1 = TestProblem()
    
    #tp1.Input1 = 
    #tp1.Input2 = 
    
    shearStress.solve(tp1)
    
    print #tp1.Output1
    print #tp2.Output2
 
