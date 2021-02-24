import numpy as np
import cv2

dimensions = [500,500]

black = np.ones(dimensions, np.uint8)*0
gray = np.ones(dimensions, np.uint8)*126
white = np.ones(dimensions, np.uint8)*255

cv2.imshow('white', white)
cv2.imshow('gray', gray)
cv2.imshow('black', black)
cv2.waitKey()

cv2.destroyAllWindows()