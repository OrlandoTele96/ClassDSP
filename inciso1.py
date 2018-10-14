# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 00:19:03 2018

@author: Jorge O. Gonzalez
"""

import cv2
#Mostrar una imagen a color.
imagen=cv2.imread("antena.png")
cv2.imshow('imagen',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()