# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 18:38:47 2018

@author: Jorge O. Gonzalez
"""

import numpy
from scipy import signal
from numpy import pi
from numpy import sin
from matplotlib import pyplot

fs=22050.0
fn=fs/2

#sañel cuadrada limitada a 700 Khz

t=numpy.arange(0,3e-3,1.0/fs)
x=sin(2*pi*1000*t)+(1.0/3)*sin(2*pi*3000*t)+(1.0/5)*sin(2*pi*5000*t)+(1.0/7)*sin(2*pi*7000*t)


#filtro paso bajas

b=numpy.array([0.03904711,0.11714134,0.11714134,0.03904711])
a=numpy.array([1,-1.32719505,0.80872764,-0.16915568])

#Filtrajo

y= signal.lfilter(b,a,x)

#Grafica

pyplot.subplot(2,1,1)
pyplot.plot(x)

pyplot.subplot(2,1,2)
pyplot.plot(y)



