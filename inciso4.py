# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 00:48:14 2018

@author: Jorge O. Gonzalez
"""

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
h_soft_haar_2=numpy.ones((1,3))*(1.0/3)
h_soft_haar_2x2=numpy.matmul(h_soft_haar_2.T,h_soft_haar_2)
imagen_inter=signal.convolve2d(imagensobre,h_soft_haar_2x2,'same').astype('uint8')
cv2.imshow('imagen',imagen_inter)
cv2.waitKey(0)
cv2.destroyAllWindows()

