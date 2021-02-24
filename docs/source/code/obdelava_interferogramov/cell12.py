#prikažite končni rezultat z upoštevanjem ROI

#izračunajte standardno deviacijo med slikami
STD = np.std(images,0)
#preverite, kje je STD večji od 0.01
ROI = STD > 0.01;
#skopirajte razvito sliko v phsUW 
phsUW = phase_unwrapped2.copy();
#v phsUW nastavite vrednosti, kjer je ROI enak Fasle na NaN
phsUW[ROI == False] = np.NaN;

#izrišite sliko
imshow('STD', phsUW)
cv2.waitKey()
cv2.destroyAllWindows()
