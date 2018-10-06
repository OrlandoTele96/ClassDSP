# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 19:22:21 2018

@author: Jorge O. Gonzalez
"""

import wave

lector=wave.open("original.wav",'rb')
escritor=wave.open("copia.wav","wb")
#Cabecereas
escritor.setparams(lector.getparams())

strAudioFrame=lector.readframes(1)

while len(strAudioFrame)==2:
    escritor.writeframes(strAudioFrame)
    strAudioFrame=lector.readframes(1)
    
lector.close()
escritor.close()