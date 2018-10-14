# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 02:48:43 2018

@author: Jorge O. Gonzalez
"""

import numpy
import cv2
from scipy import signal

imagen=cv2.imread('antena.png',cv2.IMREAD_GRAYSCALE)

h_soft_haar_1=numpy.ones((1,2))*(1.0/2)
h_soft_haar_1x1=numpy.matmul(h_soft_haar_1.T,h_soft_haar_1)

imagen_filt=signal.convolve2d(imagen,h_soft_haar_1x1,'same').astype('uint8')

imagen_deciamda_2d=imagen_filt[0:imagen_filt.shape[0]:2,0:imagen_filt.shape[1]:2]

cv2.imshow('imagen',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('imagen',imagen_deciamda_2d)
cv2.waitKey(0)
cv2.destroyAllWindows()