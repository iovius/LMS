images = []
#"za vsako ime v seznamu filenames"
for filename in filenames:
    #uporabite funkcijo read_and_process_image
    read_and_process_image(filename, images, 1.2)
    
#preberite dimenzije slike; h ... višina, w ... širina
h, w = images[0].shape

for i,image in enumerate(images):
    cv2.imshow("slika"+str(i), image)

cv2.waitKey()
cv2.destroyAllWindows()
