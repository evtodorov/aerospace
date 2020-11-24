# -*- coding: utf-8 -*-
"""
Calculate the non-constant shear flow caused by the shear force


@revision: 0
@author: etodorov
@date: 14 Feb 16

@revision: 1 - possible interpretation
@author: etodorov
@date: 18 Feb 16

@revision: 2 - with tests
@author: etodorov
@date: 18 Feb 16

@revision: 3 - new constant determination
@author: etodorov
@date: 20 Feb 16

@revision: 4 - kind of working?
@author: etodorov
@data: 21 Feb 16
"""
from __future__ import division
#software imports
import sys
from base import TestProblem, Solver

#mathematical imports
import numpy as np
import math

inputList=[  'R', 'ts', 'tf', 'hf', 
             'ns',
             'p', 'm', 'k', 'k0',
             'xr', 'xf',
             'yr', 'yf',
             'Br', 'Bf',
             'z',
             'Vx',
             'Vy',
             'Ixx',
             'Iyy']
outputList = ["qsr",'qsf', 'A1', 'A2', 'theta_floor', 'Lfloor']
                 
class ShearFlow(Solver):
    def solve(self,Problem):
        """
        **Shear flow due to force**
        \n
        xr,f(r), yr,f(r), Br,f(r) are 1D arrays in tangential direction; len(Br) = m; len(Bf) = 
        z is a 1D array in longitudinal direction;
        Vx and Vy are function of longitudinal direction;
        \n
        the output q_s(r) is a 2D array
        \n  
        """
        for i in self.inputList:
            setattr(sys.modules[__name__], i, getattr(Problem, i))
           
        #TODO: YOUR CODE STARTS HERE
        import matplotlib.pyplot as plt    
        
        #domain I - upper part; domain II - lower part
        xr = Problem.xr
        yr = Problem.yr
        Br = Problem.Br
        Vx_ = np.vectorize(Vx)
        Vy_ = np.vectorize(Vy)
        
        #Ixx = (Br*xr**2).sum() + (Bf*xf**2).sum()
        #Iyy = (Br*yr**2).sum() + (Bf*yf**2).sum()        
        #print Ixx, Iyy
        xtop = xr[:k]; xbot = xr[k:]
        ytop = yr[:k]; ybot = yr[k:]
        Btop = Br[:k]; Bbot = Br[k:]
        
        BI = np.concatenate((Btop,Bf))
        xI = np.concatenate((xtop,xf));
        yI = np.concatenate((ytop,yf));
        xI -= (xI*BI).sum()/BI.sum();
        yI -= (yI*BI).sum()/BI.sum()
        
        xII = np.concatenate((np.flipud(xf),xbot))
        yII = np.concatenate((np.flipud(yf),ybot))
        BII = np.concatenate((np.flipud(Bf),Bbot))
        xII -= (xII*BII).sum()/BII.sum()
        yII -= (yII*BII).sum()/BII.sum()
        
        qbI = np.zeros((len(z),len(xI)))
        qbII = np.zeros((len(z),len(xII)))
        c1 = -Vx_(z)/Iyy     #now an array
        c2 = -Vy_(z)/Ixx     #now an array
        Bx0 = 0
        By0 = 0
        lbi = len(BI)
        for i in xrange(lbi) :
            ii = i
            #ii = k+p//2+i
            #ii = k//2+i
            if (ii >= lbi):
                ii -= lbi
            Bx0 += BI[ii]*xI[ii]
            By0 += BI[ii]*yI[ii]
            #Bx0 = (BI[:ii]*xI[:ii]).sum()            
            #By0 = (BI[:ii]*yI[:ii]).sum()
            qbI[:,ii] = c1*Bx0 + c2*By0

        Bx0 = 0
        By0 = 0
        lbii = len(BII)
        l = m - k
        for i in range(lbii):
            ii = i
            #ii = p//2+i
            #ii = p+l//2+i
            if (ii >= lbii):
                ii -= lbii
            Bx0 += BII[ii]*xII[ii]
            By0 += BII[ii]*yII[i]    
            #Bx0 = (BII[:ii]*xII[:ii]).sum()            
            #By0 = (BII[:ii]*yII[:ii]).sum()
            qbII[:,ii] = c1*Bx0 + c2*By0
            #plt.plot(xII[ii],yII[ii],'go')

        qtop = qbI[:,:k]
        qbot = qbII[:,p:]
        qbF = qbI[:,-p:] - np.fliplr(qbII[:,:p])
        
#        plt.plot(qtop[5])
#        plt.show()
#        plt.plot(qbot[5])
#        plt.show()
#        plt.plot(qbF[5])
#        plt.show()
        #deltas

        
        dtop =  np.sqrt([(xr[1]-xr[0])**2 + (yr[1]-yr[0])**2])
        dbot = dtop
        dF =  np.sqrt([(xf[1]-xf[0])**2 + (yf[1]-yf[0])**2])
        delta_top = dtop/ts
        delta_bot = dbot/ts
        deltaF = dF/tf
        #eq 4.6, 4.7 and 4.8
        #preparatory work
        pi = np.pi
        theta_floor = math.asin((hf-R)/R)
        Lfloor = math.sqrt(R*R - (hf-R)**2 )
        A0 = pi * R**2
        A2 = (pi - 2* theta_floor)/(2*pi)*A0 -  abs(hf-R)*Lfloor
        A1 = A0 - A2
        

        sdtop = delta_top*len(xtop)
        sdbot = delta_bot*len(xbot)
        sdF = deltaF*len(xf)
        sqtop = qtop.sum(axis=1)*delta_top
        sqbot = qbot.sum(axis=1)*delta_bot
        sqF   = qbF.sum(axis=1)*deltaF
        smtop = qtop.sum(axis=1)*dtop*R
        smbot = qbot.sum(axis=1)*dbot*R
        smF = qbF.sum(axis=1)*dF*(R-hf)
        
        qsI = qsII = 0
        #print .5/A1*(qsI *sdtop + qsI *sdF - qsII*sdF + sqtop + sqF)
        #print .5/A2*(qsII*sdbot + qsII*sdF - qsI *sdF + sqbot - sqF)
        
        a11 =  .5/A1*(sdtop + sdF ) - .5/A2*(-sdF)
        a12 = -.5/A2*(sdbot + sdF ) + .5/A1*(-sdF)
        b1  =  .5/A2*(sqbot - sqF ) - .5/A1*(sqtop  + sqF) 
        
        a21 = 2*A1
        a22 = 2*A2
        b2 = -smtop - smbot - smF
        
        qsII = (b2 - a21/a11 * b1) / (a22 - a21*a12/a11)
        qsI = (b1 - a12*qsII)/a11
        
        qsr = np.zeros((len(z),len(xr)))
        qsf = np.zeros((len(z),len(xf)))
        #print .5/A1*(qsI *sdtop + qsI *sdF - qsII*sdF + sqtop + sqF)
        #print .5/A2*(qsII*sdbot + qsII*sdF - qsI *sdF + sqbot - sqF)
        #print smtop + smbot + smF + 2*A1*qsI  + 2*A2*qsII
        
        qsr[:,:k] =  qtop + np.array([qsI]).T
        qsr[:,k:] =  qbot + np.array([qsII]).T

        #print qsI, qsII
        qsf = qbF + np.array([qsI]).T - np.array([qsII]).T
        #YOUR CODE ENDS HERE
        for o in self.outputList:
            if o in locals():
                setattr(Problem, o, locals()[o])
            else:
                print "WARNING: missing output ",o    
            
shearFlow = ShearFlow(inputList,outputList)

#TODO: add unit tests
if __name__=="__main__": #exectutes only when you run THIS file
    tp1 = TestProblem()
    #inputs for discretize
    tp1.L = 70
    tp1.Lf1 = 5
    tp1.Lf2 = 31.2
    tp1.R = 3.1
    tp1.hf = 2
    tp1.ns = 36
    tp1.ts =  4e-3
    tp1.tf = 25e-3
    tp1.tst= 1.2e-3
    tp1.hst= 15e-3
    tp1.wst= 20e-3
    tp1.dz = 1
    tp1.q = 99 #inbetweeners
    tp1.p = 1000 #floorers
    import discretize    
    discretize.discretize.solve(tp1)
    #provide all inputs in this shape
    def Vx(z):
        return 0
    def Vy(z):
        return 10
    tp1.Ixx = 0.444
    tp1.Iyy = 0.787
    tp1.Vx = np.vectorize(Vx)
    tp1.Vy = np.vectorize(Vy)
    #tp1.Input2 = 
    
    #execute the solving routine
    shearFlow.solve(tp1)
    import matplotlib.pyplot as plt
    qsr = tp1.qsr[3]
    qsf = tp1.qsf[3]
    r = np.sqrt(xr**2+yr**2) + qsr
    theta = np.arctan2(yr,xr)
    plt.plot(tp1.xr,tp1.yr,'b.')
    plt.plot(tp1.xf,tp1.yf,'g.')
    plt.plot(tp1.xf,tp1.yf+qsf,'r-')
    plt.plot(r*np.cos(theta), r*np.sin(theta),'k-')
    plt.axis('equal')
    plt.grid()
    plt.show()
    #verify that outputs agree with expectation
    k = tp1.k; p = tp1.p
    print qsr[0], qsr[-1], qsf[-1], qsr[-1]+qsf[-1]
    print qsr[k-1], qsr[k+1], qsf[0], qsr[k+1]+qsf[0]
    
   
    
    

    
