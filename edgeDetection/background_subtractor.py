# https://www.sicara.ai/blog/2019-03-12-edge-detection-in-opencv
# Moving objects edge detection
"""
What if we don’t care about the tables and walls in the background?
The way this tutorial will present you to extract moving objects contours is the background subtraction.
The next example presents the createBackgroundSubtractorMOG2 function of OpenCV.
It extracts the moving parts of the images (middle image below).
Pay attention to the morphologyEx function:
It dilates the moving objects
Then shrinks them back.
The moving part of the image is then used as a mask.
It crops the edges computed with canny, keeping only the moving part.
"""
import cv2
import numpy as np

cap = cv2.VideoCapture("cafe.mp4")
if (cap.isOpened()==False):
    print("Error to open video clip!!!")

fgbg = cv2.createBackgroundSubtractorMOG2(history=10, varThreshold=2, detectShadows=False)

# Read the video
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Extracting the foreground
        edges_foreground = cv2.bilateralFilter(gray, 9, 75, 75)
        foreground = fgbg.apply(edges_foreground)
        # Smooth out to get the moving area
        kernel = np.ones((50, 50), np.uint8)
        foreground = cv2.morphologyEx(foreground, cv2.MORPH_CLOSE, kernel)
        # Apply static edge extraction
        edges_filtered = cv2.Canny(edges_foreground, 60, 120)

        # crop off the edges out of the moving area
        cropped = (foreground // 255) * edges_filtered
        # Stacking the images to print them together for comparision
        images = np.hstack((gray, edges_filtered, cropped))
        cv2.imshow("Frame-BackgroundExtractor", images)

        # Press Q to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    # Break the loop
    else:
        break

cap.release()
# close all the frames
cv2.destroyAllWindows()