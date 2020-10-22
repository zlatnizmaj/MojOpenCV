import sys
import cv2
from colr import color

print(sys.version)
print("Ta la Gao va Bo")

cv2.imshow("Fuchsia", (255, 0, 255))
print(color("Hello world.", fore="red", style="bright"))
print(color('Hello there.', fore=(255, 0, 0), back=(0, 0, 0)))