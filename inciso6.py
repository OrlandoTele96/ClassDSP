# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 03:30:02 2018

@author: Jorge O. Gonzalez
"""

import cv2


imagen=cv2.imread('antena.png',cv2.IMREAD_GRAYSCALE)

imagensub=imagen[0:imagen.shape[0]:2,0:imagen.shape[1]:2]

cv2.imshow('imagensub',imagensub)
cv2.waitKey(0)
cv2.destroyAllWindows()