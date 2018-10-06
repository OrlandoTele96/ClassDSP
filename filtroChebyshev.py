# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 18:18:04 2018

@author: Jorge O. Gonzalez
"""
import numpy as np
import  math
from scipy import signal
from matplotlib import pyplot
## Calcula la plantilla

fsl=84.0
fpl=200.0
fph=6000.0
fsh=10000.0
As=0.1
Ap=0.9

fsl=(fpl*fph)/fsh
Os=(fsh-fsl)/(fph-fpl)
delta=np.sqrt((1/As)-1)
e=np.sqrt((1/Ap)-1)
n=(math.acosh(delta/e))/(math.acosh(Os))
n=np.round(n)

## Funcion de transferencia

Fs=44100.0
Fn=0.5*Fs #Frecuencia de Nyquist
rp=-10*math.log10(0.9)
b,a=signal.cheby1(n,rp,np.array([200,6000])/Fn,'bandpass',analog=False)

## Respuesta en la frecuencia 0 a 1000 Hz incrementos de 10 Hz
f=np.arange(0,10000,10)
w=np.pi*f/Fn
w,h=signal.freqz(b,a,w)


##Grafica

pyplot.plot(f,np.abs(h))
pyplot.show()

