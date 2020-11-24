# -*- coding: utf-8 -*-
"""
Created on Tue May 20 10:50:33 2014
Plotting and analyzing a sound file
@author: etodorov
"""
import matplotlib.pyplot as pl
import scipy.io.wavfile as wav
import numpy as np

rate, data = wav.read("vodka.wav")

sample1 = data[::rate,0]
sample2 = data[::rate,1]

t = np.array([0])
for i in xrange(1,len(sample1)):
    t = np.append(t,i*rate)

pl.subplot(211)
pl.plot(t,sample1)
pl.subplot(212)
pl.plot(t,sample2)
pl.show()

wav.write("vodka1.wav",rate,data*2)
