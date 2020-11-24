# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 13:45:58 2014
parser file
@author: etodorov
"""
from math import *
import numpy as np

class Parameter:
    def __init__(self,dic):
        """
        for key in dic: \n
        \t setattr(self,key,float(dic[key]))
        """
        for key in dic:
            setattr(self,key,float(dic[key]))
class Load:
    def __init__(self,dic):
        pass
class Panel:
    compressionMAX = 0.
    def __init__(self,core,skin):
        self.core = core
        self.skin = skin
        
    def shear(self,insert):
        skin = self.skin
        force = 2*skin.t*skin.sigma*insert.r + 8*insert.r**2*self.core.tau        
        return force
    
    def pull_out(self,insert):
        core = self.core
        skin = self.skin
        rpotting = insert.r
        b = core.h/skin.t        
        c = b/(b+1)
        k = -0.931714
        n = 0.262866
        hi = 1/skin.t*sqrt(skin.G/skin.E*12*(1-skin.nu**2)*(b/2+1+2/3/b))
        rtaumax = rpotting/(1-exp(k*(hi*rpotting)**n))
        Kmax = rpotting/rtaumax*(1-sqrt(rtaumax/rpotting)*exp(hi*(rpotting-rtaumax)))
        force = 2*pi*rpotting*core.h*core.tau/c/Kmax
        return force

    def compression(self,Q,P,insert,numBolts):
        sigmaH = P/(pi*insert.M*self.core.h)/numBolts
        sigmaV = Q/(pi*insert.washer**2)/numBolts
        if sigmaH > self.compressionMAX: self.compressionMAX = sigmaH
        if sigmaV > self.compressionMAX: self.compressionMAX = sigmaV
        v = sigmaV < insert.compression
        h = sigmaH < insert.compression
        return v and h

    def weight(self,insert):
        
            if(False):
                return self.core.h*2*pi*insert.r*insert.t*insert.rho
            else:
                return self.core.h*pi*insert.r**2*insert.rho
        

    def size(self,insert,Q,P, numBolts):
        """
        Q - out of plane; P - in plane
        """
        print "sizing..."
        r = 1.
        bigEnough = False
        while not bigEnough and r<1000:
            r+=.5    
            insert.r = r
            Qs = self.pull_out(insert)
            Ps = self.shear(insert)
            if (P/Ps)**2 + (Q/Qs)**2 <= 1/1.5:
                bigEnough = True
        strongEnough = self.compression(Q,P,insert,numBolts)    
        m = self.weight(insert)
        return r, m , strongEnough

def analyse(fname,p="False"):
    """
    fname should be the name of a properly formatted csv file \n
    see input.csv for sample formating of the input \n 
    output filename is *input*_out \n
    p = True prints the output to the console
    """
    raw = {}
    isloadcase = False
    #get the data
    with open(fname+".csv",'r') as data:
        for line in data.readlines():
            if(line[0]=="#"): continue
            words = line.split(",")
            if(not words[0]==''):
                try:
                    raw[name]=dic
                except: pass
                name = words[0]
                dic = {} 
            if(words[0]=='loadcase'):
                isloadcase = True
            if(words[0]=='' and not words[1]==''):
                dic[words[1]] = words[2]
            if(isloadcase):
                dic[words[1]] = [words[2],words[3],words[5][:-1]]
        raw[name]=dic
    output = ''
    #create parameters    
    skin = Parameter(raw["skin"])
    core = Parameter(raw["core"])
    insert = Parameter(raw["insert"])
    insert.type="solid"
    #ctube = Parameter(raw["ctube"])
    #ctube.type = 'ctube'
    panel = Panel(core,skin)
    loadcases = raw["loadcase"]
    #analyse each loadcase
    for loadcase in loadcases:
        print loadcase, loadcases[loadcase]
        try:
            outofplane = float(loadcases[loadcase][0])
            inplane = float(loadcases[loadcase][1])
            numBolts = float(loadcases[loadcase][2])
            print numBolts
        except:
            continue
        
        #if too big, go for solid insert        
        r, m, strongEnough = panel.size(insert,outofplane,inplane, numBolts)
        output += "Case " + loadcase + ", P = ,"+ str(outofplane) +", [kN], N = ,"+ str(inplane) +", [kN], r = ,"+str(r)+", [mm], L = ,"+str(6.28*r)+",[mm], m = ," + str(m)+ ", [g], Solid insert \n"
        if not strongEnough:
            output = output[:-2]
            output += ",WEAK \n "
       
    output += "\n Sigma >, %d , [MPa]"% (1000*panel.compressionMAX)
    with open(fname+"_out.csv",'w') as outf:
        outf.write(output)
    if(p): print output
    return

analyse(raw_input("Name to analyse: "))
