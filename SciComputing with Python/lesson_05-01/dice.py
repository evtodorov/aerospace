"""
Created on May 01 2014
Throws a die, prints, plots
@author: etodorov
"""
import matplotlib.pyplot as plt

def die():
    '''Throws a die and returns the result'''
    return int(6*random()+1)

nThrows=1000
nDice=10

throws=[]
distribution=7*nDice*[0]
for i in range(nThrows):
    throw = 0
    for k in range(nDice):
        throw += die()
    throws.append(throw)
for j in throws:
    distribution[j]+=1
plotRange = len(distribution)
plt.plot(range(plotRange),distribution)
