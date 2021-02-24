#funkcija za branje in procesiranje slik
#filename ... lokacija slike na disku
#images ... seznam, kamor shranimo slike
#resize_factor ... faktor, za keterega spremenimo velikost slik
def read_and_process_image(filename, images, resize_factor):
    #preberite sliko v barvah s funkcijo cv2.imread()
    im =
    #preberite dimenzije slike z metodo .shape
    h, w =
    #spremenite dimenzije slike s funkcijo cv2.resize()
    im = cv2.resize
    #"razbite" sliko po posameznih kanalih; cv2.split()

    #filtrirajte sliko - razmislite, kateri kanal; cv2.GaussianBlur()

    #spremenite podatkovni tip vrednosti v float32 in ustrezno skalirajte

    #v seznam images dodajte končno sliko
    images.append