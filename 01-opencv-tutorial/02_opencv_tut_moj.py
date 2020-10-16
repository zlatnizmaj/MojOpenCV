# link tutorial: https://www.pyimagesearch.com/2018/07/19/opencv-tutorial-a-guide-to-learn-opencv/
# USAGE
# python opencv_tutorial_02.py --image tetris_blocks.png

# import the necessary packages
import argparse
import imutils
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(ap.parse_args())
# args["image"]  in the script, we’re referring to the path to the input image.

# Converting an image to grayscale
# load the input image (whose path was supplied via command line
# argument) and display the image to our screen
image = cv2.imread(args["image"])
cv2.imshow("Image", image)
cv2.waitKey(0)

# convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)

# Edge detection
# applying edge detection we can find the outlines of objects in images
# Using the popular Canny algorithm (developed by John F. Canny in 1986)
# we can find the edges in the image.
edged = cv2.Canny(gray, 30, 150) # aperture_size : The Sobel kernel size. By default this value is 3
cv2.imshow("Edged", edged)
cv2.waitKey(0)

# Thresholding
# Thresholding can help us to remove lighter or darker regions and contours of images
# threshold the image by setting all pixel values less than 225
# to 255 (white; foreground) and all pixel values >= 225 to 255
# (black; background), thereby segmenting the image
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]
# Grabbing all pixels in the gray  image greater than 225 and setting them to 0 (black)
# which corresponds to the background of the image
# Setting pixel vales less than 225 to 255 (white)
# which corresponds to the foreground of the image (i.e., the Tetris blocks themselves).
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)
# Prior to finding contours, we threshold the grayscale image.
# We performed a binary inverse threshold so that the foreground shapes
# become white while the background becomes black.

# Detecting and drawing contours
# find contours (i.e., outlines) of the foreground objects in the
# thresholded image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
print(len(cnts), type(cnts))
output = image.copy()

# loop over the contours
for c in cnts:
    # draw each contour on the output image with a 3px thick purple
	# outline, then display the output contours one at a time
    cv2.drawContours(output, [c], -1, (240, 0, 159), 3)
    cv2.imshow("Contours", output)
    cv2.waitKey(0)

# draw the total number of contours found in purple
text = f"I found {len(cnts)} objects!"
cv2.putText(output, text, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (240, 0, 159), 2)
cv2.imshow("Contours", output)
cv2.waitKey(0)

# Erosions and dilations
# Erosions and dilations are typically used to reduce noise in binary images
# (a side effect of thresholding).
# we apply erosions to reduce the size of foreground objects
mask = thresh.copy()
mask = cv2.erode(mask, None, iterations=5)
cv2.imshow("Eroded", mask)
cv2.waitKey(0)

# similarly, dilations can increase the size of the ground objects
mask = thresh.copy()
mask = cv2.dilate(mask, None, iterations=5)
cv2.imshow("Dilated", mask)
cv2.waitKey(0)

#Masking and bitwise operations
# Masks allow us to “mask out” regions of an image we are uninterested in.
# We call them “masks” because they will hide regions of images we do not care about.
# a typical operation we may want to apply is to take our mask and
# apply a bitwise AND to our input image, keeping only the masked
# regions
mask = thresh.copy()
output = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Output", output)
cv2.waitKey(0)