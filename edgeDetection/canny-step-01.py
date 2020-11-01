# https://towardsdatascience.com/canny-edge-detection-step-by-step-in-python-computer-vision-b49c3a2d8123
"""
The Canny edge detection algorithm is composed of 5 steps:
Convert the image to grayscale
Noise reduction;
Gradient calculation;
Non-maximum suppression;
Double threshold;
Edge Tracking by Hysteresis.
"""
import cv2
import numpy as np

img = cv2.imread("4.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", img_gray)
cv2.waitKey(0)

# Noise Reduction
# To do so, image convolution technique is applied with a Gaussian Kernel (3x3, 5x5, 7x7 etc…)
def gaussian_kernel(size, sigma=1):
    size = int(size) // 2
    x, y = np.mgrid[-size:size+1, -size:size+1]
    normal = 1 / (2.0*np.pi*sigma**2)
    g = np.exp(-((x**2 + y**2) / (2.0*sigma*2))) * normal
    return g # gaussina_kernal

# Gradient Calculation
# Edges correspond to a change of pixels’ intensity.
# To detect it, the easiest way is to apply filters that highlight this intensity change in both directions:
# horizontal (x) and vertical (y)
"""
When the image is smoothed, the derivatives Ix and Iy w.r.t. x and y are calculated. 
It can be implemented by convolving I with Sobel kernels Kx and Ky
"""