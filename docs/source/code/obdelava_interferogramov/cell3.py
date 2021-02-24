#funkcija za prikaz skalirane slike
def imshow(wndname, im):
    
    m = np.nanmin(im)
    M = np.nanmax(im)
    cv2.imshow(wndname, (im-m)/(M-m))
    
