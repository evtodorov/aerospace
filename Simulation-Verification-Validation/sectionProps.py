# -*- coding: utf-8 -*-
"""
Determine the section properties


@revision: 3
@author: mblanke
@date: 21 Feb 16
"""
#software imports
import sys
from base import TestProblem, Solver

#mathematical imports
import math

inputList=[  'R',
             'hf',
             'ts',
             'tf',
             'tst',
             'wst',
             'hst',
             'ns']
outputList = ["Ixx",
              "Iyy",
              "yna"]
                 
class SectionProps(Solver):
    def solve(self,Problem):
        """
        **Sectional properties**
        \n \t
        Determine the moments of inertia w/ thin walled assumption 
        \n
        all inputs are numbers;
        all outputs are numbers
        \n  
        """
        for i in self.inputList:
            setattr(sys.modules[__name__], i, getattr(Problem, i))
        #YOUR CODE STARTS HERE
        
        ##yna
        "Calculate floor width and Area"
        tf2 = tf
        
        if hf >= 2*R or hf <= 0:
            tf2 = 0
            wfloor = 0
        else:
            tf2 = tf
            wfloor = 2 * (math.sqrt(R**2-(R-hf)**2))

        Afloor = wfloor * tf2
        
        "Skin Area"
        Askin = 2*math.pi*R*ts

        "Boom area"
        Aboom = hst * tst + wst * tst
        Aboomtotal = ns * Aboom

        "find yna"
        ydistancefloor = -1*(R-hf) # center fuselage defined as zero
        yna = (ydistancefloor * Afloor)/(Askin+Aboomtotal+Afloor)

        ##Ixx
        "I floor and skin"
        yneutralaxis = R + yna
        Ixxfloor = Afloor * (yneutralaxis - hf)**2
        Ixxskin  = math.pi * R**3 * ts + Askin * (R - yneutralaxis)**2
        
        "I booms"
        n = 0
        Iboomstotal1 = 0
        while n < ns:
            Ixboom = Aboom * (R*math.cos(float(n)*(2/float(ns))*math.pi))**2
            Iboomstotal1 = Iboomstotal1 + Ixboom
            n = n+1

        Iboomsx = Iboomstotal1 + Aboomtotal * yna**2
        
        "Ixx total"
        Ixx = Ixxfloor + Ixxskin + Iboomsx

        ##Iyy
        "skin and floor"
        Iyyskin = math.pi * R**3 * ts
        Iyyfloor = float(1)/12 * tf2 * wfloor**3

        "booms"
        k = 0
        Iboomstotal2 = 0
        while k < ns:
            Iyboom = Aboom * (R*math.sin(float(k)*(2/float(ns))*math.pi))**2
            Iboomstotal2 = Iboomstotal2 + Iyboom
            k = k+1

        Iyybooms = Iboomstotal2
        
        "Iyy"
        Iyy = Iyyskin + Iyyfloor + Iyybooms

        
        #YOUR CODE ENDS HERE
        for o in self.outputList:
            if o in locals():
                setattr(Problem, o, locals()[o])
            else:
                print "WARNING: missing output ",o    
            
sectionProps = SectionProps(inputList,outputList)

#TODO: add unit tests
if __name__=="__main__": #exectutes only when you run THIS file
    tp1 = TestProblem()
    tp2 = TestProblem()
#    tp3 = TestProblem()
    tp4 = TestProblem()
    tp5 = TestProblem()
    tp6 = TestProblem()
    tp7 = TestProblem()
    tp8 = TestProblem()
    tp9 = TestProblem()
    tp10 = TestProblem()
    tp11 = TestProblem()
    
    #provide all inputs in this shape
    
    tp1.R = 3.0
    tp1.hf = 2.0
    tp1.ts = 0.005
    tp1.tf = 0.03
    tp1.tst = 0.0015
    tp1.wst = 0.01
    tp1.ns = 10
    tp1.hst = 0.01

    tp2.R = 3.0
    tp2.hf = 2.0
    tp2.ts = 0.005
    tp2.tf = 0.0
    tp2.tst = 0.0015
    tp2.wst = 0.01
    tp2.ns = 4
    tp2.hst = 0.01

##    tp3.R = 3.1
##    tp3.hf = 2.0
##    tp3.ts = 0.004
##    tp3.tf = 0.025
##    tp3.tst = 0.0012
##    tp3.wst = 0.02
##    tp3.ns = 36
##    tp3.hst = 0.015

    tp4.R = 3.0
    tp4.hf = 3.3
    tp4.ts = 0.005
    tp4.tf = 0.03
    tp4.tst = 0.0015
    tp4.wst = 0.01
    tp4.ns = 4
    tp4.hst = 0.01

    tp5.R = 3.0
    tp5.hf = 2.7
    tp5.ts = 0.005
    tp5.tf = 0.03
    tp5.tst = 0.0015
    tp5.wst = 0.01
    tp5.ns = 4
    tp5.hst = 0.01

    tp6.R = 3.0
    tp6.hf = 6.1
    tp6.ts = 0.005
    tp6.tf = 0.03
    tp6.tst = 0.0015
    tp6.wst = 0.01
    tp6.ns = 4
    tp6.hst = 0.01

    tp7.R = 3.0
    tp7.hf = 3.0
    tp7.ts = 0.005
    tp7.tf = 0.03
    tp7.tst = 0.0015
    tp7.wst = 0.01
    tp7.ns = 4
    tp7.hst = 0.01

    tp8.R = 0.15
    tp8.hf = 2.0
    tp8.ts = 0.005
    tp8.tf = 0.03
    tp8.tst = 0.0015
    tp8.wst = 0.01
    tp8.ns = 4
    tp8.hst = 0.01

    tp9.R = 195
    tp9.hf = 2.0
    tp9.ts = 0.005
    tp9.tf = 0.03
    tp9.tst = 0.0015
    tp9.wst = 0.01
    tp9.ns = 4
    tp9.hst = 0.01

    tp10.R = 3.0
    tp10.hf = 2.0
    tp10.ts = 0.005
    tp10.tf = 0.03
    tp10.tst = 0.0015
    tp10.wst = 0.01
    tp10.ns = 1
    tp10.hst = 0.01

    tp11.R = 3.0
    tp11.hf = 2.0
    tp11.ts = 0.005
    tp11.tf = 0.03
    tp11.tst = 0.0015
    tp11.wst = 0.01
    tp11.ns = 5
    tp11.hst = 0.01
    
    #execute the solving routine
    sectionProps.solve(tp1)
    sectionProps.solve(tp2)
#    sectionProps.solve(tp3)
    sectionProps.solve(tp4)
    sectionProps.solve(tp5)
    sectionProps.solve(tp6)
    sectionProps.solve(tp7)
    sectionProps.solve(tp8)
    sectionProps.solve(tp9)
    sectionProps.solve(tp10)
    sectionProps.solve(tp11)
    
    #verify that outputs agree with expectation
    print tp1.yna
    print tp1.Ixx
    print tp1.Iyy
    print
    print tp2.yna
    print tp2.Ixx
    print tp2.Iyy
    print
##    print tp3.yna
##    print tp3.Ixx
##    print tp3.Iyy

    print tp4.yna
    print tp4.Ixx
    print tp4.Iyy
    print
    print tp5.yna
    print tp5.Ixx
    print tp5.Iyy
    print
    print tp6.yna
    print tp6.Ixx
    print tp6.Iyy
    print
    print tp7.yna
    print tp7.Ixx
    print tp7.Iyy
    print
    print tp8.yna
    print tp8.Ixx
    print tp8.Iyy
    print
    print tp9.yna
    print tp9.Ixx
    print tp9.Iyy
    print
    print tp10.yna
    print tp10.Ixx
    print tp10.Iyy
    print
    print tp11.yna
    print tp11.Ixx
    print tp11.Iyy
