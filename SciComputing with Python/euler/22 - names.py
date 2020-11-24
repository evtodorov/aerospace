# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 12:26:11 2014

@author: etodorov
"""

names = open("22 - names.txt").read()[1:-1].split('","')

names.sort()
score = 0
for i in xrange(len(names)):
    name = names[i]
    letterScore = 0
    for letter in name:
        letterScore += ord(letter)-64
    score += (i+1)*letterScore