# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 11:17:22 2014

@author: etodorov
"""
from numpy import *
#from scipy.optimize import curve_fit
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
F1_mu = [0.05,0.1,0.15,0.2,0.4, 0.6,0.8 ,1.  ,1.2, 1.4]
F1_g1 = [8.3, 3.8,2.7, 2,  0.82,0.5,0.35,0.28,0.22,0.18]

F1_mu = array(F1_mu)
F1_g1 = array(F1_g1)
F1_g1_params = polyfit(F1_mu,log(F1_g1),1)
A = exp(F1_g1_params[1])
B = F1_g1_params[0]

print A*exp(B*F1_mu)
print F1_g1

F1 = interp1d(F1_mu,F1_g1,kind="cubic")
F1_v = vectorize(F1)
print F1_v(F1_mu[0:-1]+0.025)

def f(x, a, b):
    return a*exp(b*x)

fit = curve_fit(f, F1_mu, F1_g1)[0]
def F1_fit(x):
    return fit[0]*exp(fit[1]*x)
F1_fit_v = vectorize(F1_fit)

plt.plot(F1_mu,F1_g1,color='green')
plt.plot(F1_mu,A*exp(B*F1_mu),color='red')
plt.plot(F1_mu,4.94*exp(-3.28*F1_mu),color='black')
#plt.plot(F1_mu[0:-1]+0.025,F1_v(F1_mu[0:-1]+0.025),color='blue')
plt.plot(F1_mu,(F1_fit_v(F1_mu)),color="brown")
x = linspace(0.05,1.4,1000)
plt.plot(x,F1_v(x),color='purple')
plt.plot(x,F1_fit_v(x),color="blue")
#plt.show()
def run():
    plt.show()
    return 1