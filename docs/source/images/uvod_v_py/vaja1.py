import cv2

image = cv2.imread('/home/iovius/Downloads/Lenna_(test_image).png')
cv2.imshow('my image', image)
cv2.waitKey()

cv2.destroyAllWindows()