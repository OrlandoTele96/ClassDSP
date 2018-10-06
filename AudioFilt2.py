# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 18:36:55 2018

@author: Jorge O. Gonzalez
"""

#Biblioteca 
import numpy
import wave 
import struct
from scipy import signal 

#el filtro 
fc = 1500.0
fs = 44100.0
b,a = signal.butter(3,2*fc/fs,btype = 'low',analog=False)
edo = numpy.zeros(3)

#Lector
lector = wave.open('original.wav','rb')

#Escritor 
escritor = wave.open('copia.wav','wb')

#subespacio de cabecera 
escritor.setparams(lector.getparams())


#Espacio de muestras 
strAudioPackage = lector.readframes(64)


while len(strAudioPackage)==2*64:
    #Decodificacion
    audioPackage = struct.unpack(64*'h',strAudioPackage)
    

    #filtrado
    audioPackage,edo=signal.lfilter(b,a,audioPackage,zi=edo)
    
    
    #codificacion
    strAudioPackage=''.encode() #debe creae una estructura fija
    for k in audioPackage:
        strAudioPackage+=struct.pack('h',int(k))
    
    #escritura
    escritor.writeframes(strAudioPackage)
    
    #lectura
    strAudioPackage=lector.readframes(64)
    
#cierre
lector.close()
escritor.close()