import cv2
import numpy as np

image = np.zeros((500,500),np.float32)
image[200:300, 200:300] = 1.0

kernel = np.ones((11,11),np.float32)
kernel /= kernel.sum()
print(kernel)

image_filt = cv2.filter2D(image,-1,kernel)

cv2.imshow("image", image)
cv2.imshow("filtered", image_filt)
cv2.waitKey()

cv2.destroyAllWindows()