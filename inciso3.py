# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 00:31:48 2018

@author: Jorge O. Gonzalez
"""

import cv2
from scipy import signal
import numpy
# Filtrar una imagen.
imagen=cv2.imread("antena.png",cv2.IMREAD_GRAYSCALE)
h_soft_haar_3=numpy.ones((1,4))*(1.0/4)
h_soft_haar_3x3=numpy.matmul(h_soft_haar_3.T,h_soft_haar_3)
image_suave=signal.convolve2d(imagen,h_soft_haar_3x3,'same').astype('uint8')
cv2.imshow('imagensuave',image_suave)
cv2.waitKey(0)
cv2.destroyAllWindows()
