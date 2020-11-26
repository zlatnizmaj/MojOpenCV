
# Loading and displaying an image
import imutils
import cv2



image = cv2.imread("jp.png")
(h, w, d) = image.shape
print(f"width= {w}, height= {h}, depth= {d}")

cv2.imshow("Image", image)
cv2.waitKey(0)

# access the RGB pixel located at x=50, y=100, keepind in mind that
# OpenCV stores images in BGR order rather than RGB
# image[height, width] ~ image[y, x]
(B, G, R) = image[100, 50]
print(f"R={R}, G={G}, B= {B}")

# Array slicing and cropping
# Extracting “regions of interest” (ROIs)

# extract a 100x100 pixel square ROI (Region of Interest) from the
# input image starting at x=320,y=60 at ending at x=420,y=160auto
roi = image[60:160, 320:420]
cv2.imshow("ROI", roi)
#cv2.waitKey(0)

# Resizing images
# resize the image to 200x200px, ignoring aspect ratio
resized = cv2.resize(image, (200, 200))
cv2.imshow("Fixed Resizing", resized)
#cv2.waitKey(0)
# fixed resizing and distort aspect ratio so let's resize the width
# to be 300px but compute the new height based on the aspect ratio
r = 300.0/w
print("ratio = ", r)
dim = (300, int(h * r))
print(f"New dimension is {dim}")
resized = cv2.resize(image, dim)
cv2.imshow("Aspect Ratio Resize", resized)
#cv2.waitKey(0)
# manually computing the aspect ratio can be a pain so let's use the
# imutils library instead
resized = imutils.resize(image, width=300)
# In a single line of code, we’ve preserved aspect ratio and resized the image
cv2.imshow("Imutils Resize", resized)
#cv2.waitKey(0)

# Rotating an image
# let's rotate an image 45 degrees clockwise using OpenCV by first
# computing the image center, then constructing the rotation matrix,
# and then finally applying the affine warp
center = (w // 2, h // 2) # calculate the center (x, y)-coordinates of the image, // perform integer math
M = cv2.getRotationMatrix2D(center, -45, 1.0) # rotation matrix, rotate the image 45 degrees clockwise
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Open CV Rotation", rotated)
#cv2.waitKey(0)
# rotation can also be easily accomplished via imutils with less code
rotated = imutils.rotate(image, -45)
cv2.imshow("Imutils Rotation", rotated)
#cv2.waitKey(0)
# OpenCV doesn't "care" if our rotated image is clipped after rotation
# so we can instead use another imutils convenience function to help
# us out
rotated = imutils.rotate_bound(image, 45)
cv2.imshow("Imutils Bound Rotation", rotated)
#cv2.waitKey(0)
# The rotate_bound function of imutils will prevent OpenCV from clipping the image during a rotation

# Smoothing an image
# apply a Gaussian blur with a 11x11 kernel to the image to smooth it,
# useful when reducing high frequency noise
blurred = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Blurred", blurred)
#cv2.waitKey(0)

# Drawing on an image
# draw a rectangle, circle, and line on an input image
# drawing operations on images are performed in-place
# draw a 2px thick red rectangle surrounding the face
output = image.copy()
cv2.rectangle(output, (320, 60), (420, 160), (0, 0, 255), 2) # (320, 60) top-left, (420, 160) bottom-right pixel, (BGR)
cv2.imshow("Rectangle", output)
#cv2.waitKey(0)
# let’s place a solid blue circle in front of Dr. Ellie Sattler’s face
# draw a blue 20px (filled in) circle on the image centered at
# x=300,y=150
output = image.copy()
cv2.circle(output, (300, 150), 20, (255, 0, 0), -1)
cv2.imshow("Circle", output)
#cv2.waitKey(0)
# draw a 5px thick red line from x=60,y=20 to x=400,y=200
output = image.copy()
cv2.line(output, (60, 20), (400, 200), (0, 0, 255), 5)
cv2.imshow("Line", output)
#cv2.waitKey(0)

# how OpenCV’s putText function works
# draw green text on the image
output = image.copy()
cv2.putText(output, "OpenCv + Jurassic Park!!!", (10, 25),
            cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)
