:orphan:

.. _priloga3:

Ogrodje programa (Python)
---------------------------------------

.. code-block:: python

   import cv2
   import numpy as np
   import matplotlib.pyplot as plt
   from mpl_toolkits.mplot3d import Axes3D


.. code-block:: python

   #funkcija za shranjevanje matrik
   def save_float_mtx(filename, M):
      h, w = M.shape
      f = open(filename,'w')
	  
      for v in range(h):
         for u in range(w):
            f.write(str(M[v, u])+' ')
         f.write('\n')
      f.close()
	  

.. code-block:: python

   #funkcija za detekcijo profila na sliki
   #image ... slika, na kateri iščemo profil
   #profile ... list, kamor zapišemo profil
   #filter_size ... dimenzija filtra
   
   def detect_profile(image, profile, filter_size):
      #preberite dimenzije slike; h ... višina slike, w ... širina slike
      
      #filtrirajte vstopno sliko; cv2.GaussianBlur()
      image_flt = 
      #izračunajte odvod filtrirane slike; cv2.Sobel()
      derivative = 
    
      #"za vsako vrstico"
      for v 
         #maksimalna intenziteta je enaka nič
         maxInty = 0;
         #"za vsak element v vrstici"
         for u 
            #preberite trenutni element odvoda v vrstici
            p_drv = 
            #preberite naslednji element odvoda v vrstici
            p_drv_next = 
            #preberite trenutno vrednost intenzitete 
            p_inty = 
            
            #preverite, ali je to mesto prevoja
            #"če je trenutna vrednost odvoda večja ali enaka 0 in hkrati naslednja vrednost odvoda manjša od 0"
            if
                #je intenziteta na mestu tega prevoja večja kot na prejšnjem
                if
                    #v mesto profila, ki pripada tej vrstici zapišite lokacijo prevoja
                    profile[] = 
                    #nastavite trenutno inteziteto kot maksimalno intenziteto


.. code-block:: python

   #nastavite ime mape, kjer se nahajajo slike kot path
   path = 
   #nastavite število slik, ki jih želite obdelati
   n_of_imgs = 
   #nastavite indeks prve slike
   start_ind = 
   #inicializirajte matriko profilov, vsaka vrstica te matrike pripada svoji sliki, tip naj bo float32
   profiles = 

   #"za vsako sliko"
   for i 
      if(i%10 == 0):
         print(i/n_of_imgs)
      #preberite BW sliko
      image = 
      #spremenite podatkovni tip iz uint8 v float32 in ustrezno skalirajte
    
      #uporabite funkcijo detect_profile
      detect_profile()
    
   alpha =  #triangulacijski kot
   Py =  #razdalja med kamero in projektorjem v Y smeri - "baseline"
   f =  #goriščna razdalja objektiva
   cu =  #sredina slike v U smeri (horizontalni) merjeno od levega roba
   cv =  #sredina slike v V smeri (vertikalni) merjeno od zgornjega roba
   du =  #dimenzija slikovnega elementa v U smeri
   dv =  #dimenzija slikovnega elementa v V smeri
   dx =  # korak mize med dvema zaporednima slikama v Y smeri
   #preberite število profilov in dolžino profilov
   n_of_prf, l_of_prf = 
   #inicializirajte matriko Xov tipa float32
   X = 
   #inicializirajte matriko Yov tipa float32
   Y = 
   #inicializirajte matriko Zov tipa float32
   Z = 

   #"za vsak profil"
      for 
         #"za vsak element v profilu"
         for u 
            #izračunajte smerni vektor v U smeri
            un = 
            #izračunajte smerni vektor v V smeri
            vn = 
            #izračunajte Z koordinato merjene točke in jo zapišite na pripadajoče mesto v Z matriki
            Z =
            #izračunajte Y koordinato merjene točke in jo zapišite na pripadajoče mesto v Y matriki
            Y = 
            #izračunajte X koordinato merjene točke in jo zapišite na pripadajoče mesto v X matriki
            X = 
   
   fig = plt.figure()
   ax = plt.axes(projection = '3d')
   ax.plot_surface(X, Y, -Z)
   plt.show()

