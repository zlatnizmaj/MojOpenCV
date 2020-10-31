# https://medium.com/sicara/opencv-edge-detection-tutorial-7c3303f10788
# https://www.sicara.ai/blog/2019-03-12-edge-detection-in-opencv

"""
Loads and displays a video
"""

# Import OpenCV
import cv2
import numpy as np

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture("cafe.mp4")

# Check if camera opened successfully
if (cap.isOpened()==False):
    print("Error opening video stream or file")

# Read the video
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:

        # Converting the image to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # cv2.imshow("Frame RGB", frame)
        # Display the resulting frame
        # cv2.imshow("Frame GrayScale", gray)
        # Press Q on keyboard to exit
        # if cv2.waitKey(25) & 0xFF == ord('q'):
        #     break

        # The Canny Filter, Still objects edge detection
        # Using the Canny Filter to get contours
        edges = cv2.Canny(gray, 20, 30)
        # Using the Canny filter with different parameters
        edges_high_thresh = cv2.Canny(gray, 60, 120) # The higher the thresholds, the cleaner the edges

        # A nice trick to smooth out the image without blurring the edges is called
        # bilateral filtering
        # how the plant in the background or the left man’s tie both look messy?
        # Smoothing without removing edges
        gray_filtered = cv2.bilateralFilter(gray, 7, 50, 50)
        # Apply the canny filter
        edges_filtered = cv2.Canny(gray_filtered, 60, 120)

        # Stacking the images to print them together
        # For comparision
        images = np.hstack((gray, edges, edges_high_thresh, edges_filtered))
        # Display the resulting frame
        cv2.imshow("Frame-Canny-BilateralFiltering", images)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    # Break the loop
    else:
        break

# When everything done, release the video capture object
cap.release()
# Cloise all the frames
cv2.destroyAllWindows()


