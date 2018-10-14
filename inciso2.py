# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 00:27:58 2018

@author: Jorge O. Gonzalez
"""

import cv2
# Mostrar una imagen en blanco y negro.
imagen=cv2.imread("antena.png",cv2.IMREAD_GRAYSCALE)
cv2.imshow('imagen',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()