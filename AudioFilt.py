import numpy
import wave
import struct
from scipy import signal

#Filtro

fc=1500.0
fs=44100
b,a=signal.butter(3,2*fc/fs,btype='low',analog=False)
edo=numpy.zeros(3)

#Lector
lector=wave.open('original.wav','rb')

#escritor 
escritor=wave.open('copia.wav','wb')

#Subespacio de cabecera
escritor.setparams(lector.getparams())

#Espacio de muestras
srtAudioPackage=lector.readframes(64)

while len(srtAudioPackage)==2*64:
	#Decodificacion
	audioPackage=struct.unpack(64*'h',srtAudioPackage)
    #filtrado 
    audioPackage,edo =signal.lfilter(b,a,audioPackage,zi=edo)
    #codificacion
#    srtAudioPackage=''.encode()
    for k in audioPackage:
        srtAudioPackage+=struct.pack('h',int(k))
    #Escritura
    escritor.writeframes(srtAudioPackage)
    #lectura
    srtAudioPackage=lector.readframes(64)
#cierre
lector.close()
escritor.close()