# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 11:01:22 2014

@author: etodorov
"""

amount = int(float(raw_input("Enter an amount in euros: "))*100)    #cents

banknotes = [500,200,100,50,20,10,5]    #euros
coins = [200,100,50,20,10,5,2,1]        #cents
answer_b = []   #euros
answer_c = []   #cents
for note in banknotes:
    _n = amount / (note*100)
    if (_n):
        amount -= _n*note*100
        for _i in xrange(_n):
            answer_b.append(note)

for coin in coins:
    _m = amount / coin
    if (_m != amount):
        amount -= _m*coin
        for _j in xrange(_m):
            answer_c.append(coin)
            
print "Baknotes (in euros):"
for b in answer_b: print b
print "\nCoins (in cents):"
for c in answer_c: print c