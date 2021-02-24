#izračunajte sinusni del
sine = (images[0]-images[3])+(images[1]-images[2])
#pomnožite sinusni del z tan_alpha
sine *= tan_alpha
#izračunajte cosinusni del
cosine = (images[1]+images[2])-(images[0]+images[3])

#izračunajte fazo
phase = np.arctan2(sine, cosine)

imshow("Phase",phase)
cv2.waitKey()
cv2.destroyAllWindows()
# save_float_mtx("e:\\temp\\M",phase)
