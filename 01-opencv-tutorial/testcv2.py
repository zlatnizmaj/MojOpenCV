#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 13:59:17 2020

@author: NamNg
"""

import cv2
image = cv2.imread("jp.png")
cv2.imshow("Image", image)
cv2.waitKey(0)