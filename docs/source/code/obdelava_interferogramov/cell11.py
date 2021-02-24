#prikažite končni rezultat
imshow('phaseUW', phase_unwrapped2)
cv2.waitKey()
cv2.destroyAllWindows()
save_float_mtx("e:\\temp\\srf",phase_unwrapped2)
