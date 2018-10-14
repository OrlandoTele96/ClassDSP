# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 03:26:58 2018

@author: Jorge O. Gonzalez
"""

# Sobre muestrear una imagen y mostrarla

import numpy
import cv2

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

cv2.imshow('imagen',imagensobre)
cv2.waitKey(0)
cv2.destroyAllWindows()