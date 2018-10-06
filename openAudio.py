# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 19:11:23 2018

@author: Jorge O. Gonzalez
"""
# abre un archivo de audio.
import wave

archivo=wave.open("original.wav",'rb')
print("num channels",archivo.getnchannels())
print("frec. muestreo",archivo.getframerate())
print("tamano de la muestra",archivo.getsampwidth())
print("tam ",archivo.getnframes())

archivo.close()

