import cv2
import numpy as np

dimensions = [500, 500]
N = 100

image = np.ones(dimensions,np.uint8)*126

ind_v = np.random.randint(0, dimensions[0], N)
ind_u = np.random.randint(0, dimensions[0], N)

for i in range(N):
    if 0 == np.random.randint(0,2,1):
        image[ind_v[i],ind_u[i]] = 0
    else:
        image[ind_v[i],ind_u[i]] = 255

image_med = cv2.medianBlur(image,7)
    
cv2.imshow("image", image)
cv2.imshow("image_med", image_med)
cv2.waitKey()

cv2.destroyAllWindows()
