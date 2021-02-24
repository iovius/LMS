import cv2
import numpy as np

slika1 = np.zeros((500, 500), np.uint8)

slika2 = slika1

slika2[200:300, 200:300] = 255

cv2.imshow('slika1', slika1)
cv2.imshow('slika2', slika2)

cv2.waitKey()
cv2.destroyAllWindows()