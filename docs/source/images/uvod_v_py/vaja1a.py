import cv2

image = cv2.imread('/home/iovius/Downloads/Lenna_(test_image).png')

[blue, green, red] = cv2.split(image)
image_merged = cv2.merge([red, green, blue])

cv2.imshow('red', red)
cv2.imshow('green', green)
cv2.imshow('blue', blue)
cv2.imshow('my image', image)
cv2.imshow('image merged', image_merged)
cv2.waitKey()

cv2.imwrite('/home/iovius/Downloads/Lenna_(test_image).png', image_merged)

cv2.destroyAllWindows()