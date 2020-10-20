######## Resources ###########
# 1 : https://docs.opencv.org/3.1.0/dc/dc3/tutorial_py_matcher.html
# 2 : https://stackoverflow.com/questions/42538914/why-is-ransac-not-working-for-my-code
# 3 : https://docs.opencv.org/3.1.0/d6/d00/tutorial_py_root.html
# 4 : https://towardsdatascience.com/image-stitching-using-opencv-817779c86a83

import cv2
import  numpy as np
import  matplotlib.pyplot as plt
from random import randrange

img_ = cv2.imread("uttower_right.jpeg")
img1 = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
cv2.imshow("Right Image", img_)
cv2.waitKey(0)

img = cv2.imread("uttower_left.jpeg")
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Left Image", img)
cv2.waitKey(0)

