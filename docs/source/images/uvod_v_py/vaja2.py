import cv2

cam = cv2.VideoCapture(0)
flip = False

while True:
    retval, frame = cam.read()
    if not retval:
        break
    if flip:
        frame = cv2.flip(frame,1)
    cv2.imshow("frame", frame)
    key = cv2.waitKey(10)
    if key == 27:
        break
    elif key == ord('f'):
        flip = not flip
        
        
cam.release()
cv2.destroyAllWindows()
    
