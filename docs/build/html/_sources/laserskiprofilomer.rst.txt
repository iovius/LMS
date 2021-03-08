.. _laserskiprofilomer:

Razvoj programske opreme laserskega 3D merilnika
--------------------------------------------------------------------------------

.. note::
   Če še nimate nameščenega Pythona in OpenCVja sledite navodilom na povezavi: :ref:`navodila_python`.

Uvod
^^^^


Cilj vaje je praktično spoznati osnove laserske triangulacije in izdelati programsko opremo za enostaven linearni laserski profilomer. Sistem in programska oprema za zajem sekvence merilnih slik sta predhodno pripravljena, vaša naloga pa je, da napišete program, ki bo iz te sekvence slik rekonstruiral obliko merjene površine.

Oprema
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Linearna koračna miza
- Krmilnik koračne mize
- Linijski laserski projektor
- Kamera

Potek vaje
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Ogled sistema (na koračno mizo sta pod kotom pritrjena kamera in laserski projektor, ogledamo si sliko na kameri pri različnih nastavitvah kamere in različnih odbojnostih).
- Zajem sekvence merilnih slik.
- Izdelava programa za transformacijo (`Python <https://www.python.org/>`_  & `OpenCV <https://opencv.org/>`_ ).
- Prikaz izmerkov; preverili bomo ujemanje rekonstruirane površine z referenčno.

Osnovni pojmi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: images/laserski_profilomer/triangulacija2.png
   :alt: reStructuredText, the markup syntax

   Slika 1. Shema triangulacije z označenimi merami.

Skica merilnega sistema je prikazana na *sliki 1*. Projektor je postavljen na mestu *P* in projicira svetlobno ravnino proti merjeni površini. Kamera je postavljena na mestu, označenem s *C*. *Koordinatni sistem* (*k.s.*) merilnika (*KS*\ :sub:`merilnika`\ ) je postavljen na presečišče laserske ravnine in pravokotne projekcije središča leče na lasersko ravnino. Model preslikave temelji na uporabi perspektivne projekcije z enostavno geometrijo kamere z luknjico (*camera obscura*, angl. *pinhole camera*). Senzor je postavljen na razdalji *f* od koordinatnega izhodišča. Optična os objektiva prebada ravnino kamere na koordinati (*c*\ :sub:`U`\ , *c*\ :sub:`V`\ , *angl. principal point*) merjeno glede na zgornji levi rob senzorja (standard pri navajanju položaja točke pri senzorjih, zaslonih, slikah etc.). Projektor je glede na koordinatno izhodišče premaknjen le v *X* smeri za razdaljo *P*\ :sub:`X`\  in projicira svetlobno ravnino pod kotom *α* glede na optično os objektiva kamere.

.. figure:: images/laserski_profilomer/merilna_slikaT.jpg
   :alt: reStructuredText, the markup syntax
   :scale: 20 %
   :align: center

   Slika 2. Ena iz množice slik. Poiskati moramo lokacijo sentra presečne krivulje v k.s. kamere.

Na *sliki 2* je prikazana slika, kot jo vidi kamera. Vidimo lahko, da je merjena površina v osrednjem delu nekoliko dvignjena glede na spodnji in zgornji del. Označena sta *k. s.* slike (*KS*\ :sub:`slike`\ ) in *k. s.* kamere (*KS*\ :sub:`kamere`\ ), ki leži na mestu preboda optične osi. Označeni sta tudi smer *u* in *v*.

.. note::
   *Slika 2* je transponirana, kar pomeni, da sta smeri *v* in *u* zamenjani. Sliko transponiramo zato, ker se je laže premikati po vrstici, kot po stolpcu.

Merilnik se med merjenjem translatorno premika v *X* smeri in ob tem zajel *N* slik. Glede na to, da sta hitrosti premikanja in zajemanja slik konstantni, lahko določimo premik merilnika med dvema zaporednima slikama kot:

.. math::
   x_{\text{STEP}} = \frac{ x_{\text{MOVE}}}{N}

kjer sta *x*\ :sub:`MOVE`\  celoten premik med merjenjem in *x*\ :sub:`STEP`\  premik med dvema zaporednima slikama. Z vsake slike pa lahko razberemo obliko osvetljenega profila površine in tako dobimo površino kot množico zaporednih profilov.
Za izračun koordinate posamezne točke profila v *k. s.* merilnika, moramo najprej poiskati koordinate posamezne točke profila v *k. s.* kamere (na senzorju) na posamezni sliki. V praksi to pomeni, da moramo v vsaki vrstici (za vsak *v*) poiskati center presečne krivulje v smeri *u* (koordinato *u*) (glejte *sliko 2*).

Glavni program
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

V tem delu programa bomo spisali ogrodje programa. Njegova glavna naloga je, da prebere vsako sliko in s pomočjo funkcije za iskanje presečne krivulje (ki jo bomo napisali ločeno) na vsaki sliki najde lokacijo maksimumov intenzitete. Uporabljali bomo programski jezik *Python* v kombinaciji s knjižnico *OpenCV*. V pomoč pri izdelavi programa naj vam bo diagram poteka (glejte :ref:`priloga1`). Na predvideno mesto (osnova je že pripravljena) napišete jedro programa. Rekonstrukcijo površine boste naredili posebej, kot funkcijo na vnaprej pripravljenem mestu. Bodite pozorni, kako se naslavlja elemente v matriki (primer: :math:`B(i,j)`  ... je *i* koordinata vrstice ali stolpca ?).

.. figure:: images/laserski_profilomer/zapisovanje_profilov.jpg
   :alt: reStructuredText, the markup syntax
   :scale: 13 %
   :align: center

   Slika 3. Skica povezava funkcije ``DetectLine()`` in matrike profilov.
   
Zaznane profile na sliki boste zapisali v matriko profilov. Logiko matrike profilov lahko vidite na *sliki 3*. Dolžina vrstic mora biti enaka dimenziji slike v v smeri (npr. če so slike visoke 640 slikovnih elementov (s. e.), mora vsaka vrstica sprejeti po 640 elementov), število vrstic pa mora biti enako številu zajetih slik *N* (npr. če smo zajeli 300 slik, torej mora imeti matrika profilov 300 vrstic). Na vsaki sliki bomo tako
v vsaki vrstici poiskali položaj presečne krivulje v smeri *u*. Npr. če je na 17. sliki v 37. vrstici položaj presečne krivulje na koordinati 103, bomo zapisali ``profiles(17, 37) = 103``.Pri pisanju programa naj vam bosta v pomoč Priloga 1 in template programa.

Sledite naslednjemu postopku:

#. Na začetku programa najavite in nastavite globalne spremenljivke, ki jih bomo potrebovali tekom celotnega programa (npr. mapa, kjer se nahajajo datoteke, število merilnih slik, alociramo prostor za profile).
#. Začnite zanko.
#. Generirajte ime slike in jo naložite v spomin. Namig: Uporabite ``cv2.imread()``
#. Sliko transponirajte (to storite izključno zaradi lažje obdelave, saj se je laže premikati po vrstici kot po stolpcu) in jo pretvorite v primeren format (32 bitna števila s plavajočo vejico). Namig: ``cv2.transpose(...)``.
#. Na tem mestu kličite funkcijo ``detect_profile(...)``. Kot drugi parameter podajte kazalec na vrstico matrike profilov, ki ima isti indeks kot trenutna slika, ki jo obdelujemo (glejte *sliko 3*).
#. Zaključite zanko.
#. Rekonstruirajte površino.

Funkcija ``detect_profile(...)``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Uporabite predlogo ``detect_profile(image, profile, filter_size)``.

1. Filtrirajte sliko z *Gaussovim filtrom*. Širina filtrirnega okna mora biti širša od presečne krivulje na sliki! Namig: ``cv2.GaussianBlur(...)``

2. Izračunajte odvod slike. Namig: ``cv2.Sobel(...)``

3. Poiščite lokacijo prevoja na presečni krivulji.

   a. Prevojev na sliki je lahko več, a uporabite predpostavko, da je intenziteta na mestu prevoja presečne krivulje večja od prevojev na drugih mestih. Namig: preverite, ali je intenziteta ne tem mestu večja, kot na predhodno zaznanem mestu prevoja.

   b. Poiščite lokacijo prevoja. Uporabite v prejšnjem koraku izračunani odvod intenzitete. Namig: Iščemo samo maksimume; razmislite, katere prehode torej iščemo.

   c. Napredno: Poiščite lokacijo središča presečne krivulje (prevoja) s podtočkovno ločljivostjo. Namig: Glejte spodnjo sliko (slika 4). 
   
.. figure:: images/laserski_profilomer/subpixel_accuracy.jpg
   :alt: reStructuredText, the markup syntax
   :scale: 8 %
   :align: center

   Slika 4. Skica za izračun podtočkovne ločljivosti.

4. Rezultat morala biti vektor, ki je enako dolg kot slika v smeri *v*.

Rekonstrukcija površine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Normalizirane lokacije presečne krivulje izračunamo po spodnjih enačbah:

.. math::
   U_N = \frac{U_d \cdot du}{f} =  \frac{(U - c_u) \cdot du}{f} 

in

.. math::
   V_N = \frac{V_d \cdot dv}{f} =  \frac{(V - c_v) \cdot dv}{f} 

kjer sta *U*\ :sub:`N`\  in *V*\ :sub:`N`\  normalizirani koordinati (smerna vektorja žarka, ki izhaja iz senzorja proti merjeni površini), *c*\ :sub:`u`\  in *c*\ :sub:`v`\  lokaciji centra slike v smeri *u* in *v*, *du* in *dv* velikosti senzorskega elementa v *u* in *v* smeri, ter f goriščna razdalja objektiva kamere.
Oddaljenost merjene točke v koordinatnem sistemu merilnika v *z* smeri *z*\ :sub:`M`\  izračunamo kot:

.. math::
   z_M = \frac{P_X}{\tan(\alpha - \arctan(\frac{V_N}{f}))} 

kjer je α triangulacijski kot in *P*\ :sub:`X`\  razdalja med kamero in projektorjem.
Koordinato točke *x*\ :sub:`M`\  izračunamo kot:

.. math::
   y_M = z_M \cdot U_N

Razmislite, kako izračunamo koordinato *x*\ :sub:`M`\  . (Namig: izkoristite for zanko, kakšen je korak med
mestoma zajema dveh zaporednih slik?)

Vizualizacija rezultatov
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Za vizualizacijo rezultatov uporabite osnovno funkcionalnost Pythona.

Priloge
^^^^^^^^^^^^^^^^

  * :ref:`priloga1`
  * :ref:`priloga2`
  * :ref:`priloga3`
