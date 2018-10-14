# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 18:23:23 2018

@author: Jorge O. Gonzalez
"""

#import cv2
#
#imagen_gris=cv2.imread('antena.png',cv2.IMREAD_GRAYSCALE) #  Lee la imagen antena.png y la guarda en imagen en blanco y negro.
#
#cv2.imshow('Imagengris',imagen_gris) # Abre una ventana nombrada imagen y muestra el contenido de la variable imagen(antena.png).
#cv2.waitKey(0) #Espera cualquier simbolo que sea tecleado 
#cv2.destroyAllWindows() # cierrra la ventana.

#import cv2
#import numpy
#from scipy import signal
#image = cv2.imread('antena.png', cv2.IMREAD_GRAYSCALE)
#h_soft_bin_3=numpy.array([[1],[3],[3],[1]])*(1.0/8)
#h_soft_bin_3x3=numpy.matmul(h_soft_bin_3.T,h_soft_bin_3)
#imagen_suave=signal.convolve2d(imagen,h_soft_bin_3x3,'same').astype('uint8')
#cv2.imshow('imagenSuave', imagen_suave)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


import numpy
import cv2
from scipy import signal
# Interpolar una imagen.
def upsample(matrix,fct):
    f=numpy.copy(matrix)
    for k in range(1,fct*f.shape[0],fct):
        f=numpy.insert(f,k,numpy.zeros((fct-1,1),dtype='float32'),axis=0)
    for k in range(1,fct*f.shape[1],fct):
        f=numpy.insert(f,k,numpy.zeros((fct-1,1),dtype='float32'),axis=1)
    return f
imagen=cv2.imread("antena.png",cv2.IMREAD_GRAYSCALE)
imagensobre=upsample(imagen,2)
w_soft_bar_2=numpy.zeros((1,2))
w_soft_bar_2x2=numpy.matmul(w_soft_bar_2.T,w_soft_bar_2)
imagen_inter=signal.convolve2d(imagensobre,w_soft_bar_2x2,'same').astype('uint8')
cv2.imshow('imagen',imagen_inter)
cv2.waitKey(0)
cv2.destroyAllWindows()