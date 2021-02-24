import cv2
import numpy as np

image = cv2.imread('/home/iovius/Documents/docs/source/uvod_v_py/images/Lenna_(test_image).png')
image = image.astype(np.float32)

image_filter_1 = cv2.GaussianBlur(image,(5,5),3)

kernel = cv2.getGaussianKernel(5, 3, cv2.CV_32F)
image_filter_2 = cv2.sepFilter2D(image,cv2.CV_32F,kernel,kernel)

difference = image_filter_1 - image_filter_2

print("kernel:\n", kernel)
print("\ndifference:\n", (np.sum(difference)))