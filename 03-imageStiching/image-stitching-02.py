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
# cv2.imshow("Right Image", img_)
# cv2.waitKey(0)

img = cv2.imread("uttower_left.jpeg")
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Left Image", img)
# cv2.waitKey(0)

sift = cv2.SIFT_create()
# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

print("Len of matches: ", len(matches))
# Apply ratio
good = []
ratio = 0.5
for m in matches:
    if m[0].distance < ratio * m[1].distance:
        good.append(m)
matches = np.asarray(good)
print(matches.shape)
print(matches[2,0].queryIdx)
print(matches[2,0].trainIdx)
print(matches[2,0].distance)

if len(matches[:,0]) >= 4:
    src = np.float32([kp1[m.queryIdx].pt for m in matches[:, 0]]).reshape(-1, 1, 2)
    dst = np.float32([kp2[m.trainIdx].pt for m in matches[:, 0]]).reshape(-1, 1, 2)
    H, masked = cv2.findHomography(src, dst, cv2.RANSAC, 5.0)
    print(H.shape)
    print("Len of H: ", len(H))
    print(H)
else:
    raise AssertionError("Can't find enough keypoints.")