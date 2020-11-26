import cv2
print(cv2.__version__)
original3= cv2.imread("images/original3.jpg")
print("Data Type: ", type(original3))
print("Image Shape: ", original3.shape)
print("Image Size: ", original3.size)
print("Element Type: ", original3.dtype)

cv2.imshow("Original Image", original3)
cv2.waitKey(0)

blue_ori = original3[:, :, 0]
cv2.imshow("Blue chanel", blue_ori)
cv2.waitKey(0)

# function resize()
for width in (100, 200, 400):
    resized = cv2.resize(original3, (width, width), interpolation=cv2.INTER_LINEAR)
    print("Resized Image Width: ", resized.shape[0])
    cv2.imwrite(f"images/reszied_{width}.jpg", resized)


