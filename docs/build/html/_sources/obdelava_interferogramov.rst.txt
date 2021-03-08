.. _obdelava_interferogramov:

Računalniška analiza interferogramov
---------------------------------------------

.. note::
   Če še nimate nameščenega *Python*-a in *OpenCV*-ja sledite navodilom na povezavi: :ref:`navodila_python`.

Na prejšnji vaji smo zajeli slike interferogramov, ki jih želimo sedaj računalniško obdelati. Ker bo skripta razmeroma dolga, jo bomo razdelili na več celic. Sledite navodilom, ki so zapisana v komentarjih.

.. note::
	Če ne uporabljate *Jupyter Notebooka*, boste morali vse celice zapisati v eno skripto.
	
.. note::
   Besedilo se vedno nanaša na **sledečo celico**.

V prvi celici bomo uvozili knjižnice, ki jih potrebujemo (``cv2`` in ``numpy``). Prav tako lahko definiramo spremenljivki π in 2π (ker se ime spremenljivke v Pythonu ne sme začeti s števil, jo bomo poimenovali π2).

.. literalinclude:: code/obdelava_interferogramov/cell1.py
	:language: python
	:linenos:
	

V naslednji celici bomo napisali funkcijo, ki bo prebrala in sprocesirala posamezno sliko. Definicijo funkcije moramo začeti z ukazom ``def``. ``read_and_process_image(filename, images, resize_factor)`` pomeni, da je *read_and_process_image* ime funkcije, *filename*, *images* in *resize_factor* pa so argumenti, ki jih bomo morali podati.


.. literalinclude:: code/obdelava_interferogramov/cell4.py
	:language: python
	:linenos:
	

V tej celici podamo imena posameznih slik in jih zapišemo v *list*.

.. warning::
	Spomnite se, kako navajamo poti na disku!

.. literalinclude:: code/obdelava_interferogramov/cell5.py
	:language: python
	:linenos:

S sledečo celico bomo prebrali slike, jih dodali v *list* ``images`` in prikazali.

.. literalinclude:: code/obdelava_interferogramov/cell6.py
	:language: python
	:linenos:

Sedaj bomo začeli z izračunom. V pomoč naj vam bodo *slajdi* s predavanj (:ref:`carre`). V tej celici želimo izračunati vrednost :math:`{\alpha}(x,y)`. Če pogledate, kaj bomo morali storiti v naslednjem koraku, vidite, da je izračun :math:`arctan` nekoliko nesmiselen, saj bomo morali potem v naslednjem koraku izračunati :math:`tan`, tako da namesto :math:`{\alpha}(x,y)` izračunajmo kar :math:`tan({\alpha}(x,y))`.

.. literalinclude:: code/obdelava_interferogramov/cell7.py
	:language: python
	:linenos:

Ko smo izračunali :math:`tan({\alpha}(x,y))` nadaljujemo z izračunom *faze* (:math:`{\Delta}{\Phi}(x,y)`).

.. note::
   Izračun *arkustangensa kvocienta dveh števil* je precej "zahtevna" operacija, saj imamo *6* možnih primerov. Zato ima praktično vsaka *matematična* knjižnica (ki da kaj nase) fukcijo `atan2 <https://en.wikipedia.org/wiki/Atan2>`_. V ``numpy`` jo najdemo kot ``arctan2``.

.. literalinclude:: code/obdelava_interferogramov/cell8a.py
	:language: python
	:linenos:

Ker smo za izračun faze uporabili fukcijo :math:`arctan` (v našem primeru v resnici :math:`arctan2`) je *faza* omejena na inteval :math:`[-\frac{\pi}{2}, \frac{\pi}{2} ]` (ker smo uporabili :math:`arctan2` smo v resnici omejeni na inteval :math:`[-\pi, \pi ]`). Kakorkoli, ker želimo dobiti zvezen potek *faze* moramo izvesti t.i. *razvijanje faze* (angl.: `phase unwrapping <https://ccrma.stanford.edu/~jos/fp/Phase_Unwrapping.html>`_). Osnovna ideja (enostavnega algoritma za razvijanje faze) je, da se *pomikamo* po *fazi* in spremljamo, kje se pojavijo nezveznosti. Od tega mesta naprej prištejemo ali odštejemo :math:`2\pi`, odvisno od tega, v katero smer se pojavi nezveznost.

.. literalinclude:: code/obdelava_interferogramov/cell8b.py
	:language: python
	:linenos:

Vizualizirajte rezultat.

.. literalinclude:: code/obdelava_interferogramov/cell9.py
	:language: python
	:linenos:
	
Precej verjetno vidite naj podobnega srednjemu stolpcu na spodnji sliki. Želimo pa rezultat, kot je v zadnjem stolpcu.

.. figure:: images/obdelava_interferogramov/uw-1smer.png
	:alt: reStructuredText, the markup syntax
	:scale: 60 %
	:align: center
	
	Slika 1. Izvorne *faze* (prvi stolpec), *faza* kot bo razvita po našem algoritmu (sredinski stolpec) in rezultat, kot ga želimo (zadnji stolpec).
	
Težava je v tem, da našo *sliko faze* razvijamo samo z leve proti desni, v primeru kot je zgoraj levo na *sliki 1* pa se do sredinskega polja pa nabere že kar nekaj *napake*.

Postopek razvijanja moramo zato ponoviti še enkrat, tokrat v navpični smeri.

.. literalinclude:: code/obdelava_interferogramov/cell10.py
	:language: python
	:linenos:
	

Vizualizirajte rezultat *faze*.

.. literalinclude:: code/obdelava_interferogramov/cell11.py
	:language: python
	:linenos:
	

Če vas moti *šum* okoli faze (ljubkovalno imenovan tudi "šavje"), lahko preverite vidljivost signala na posameznem mestu in izrišete le točke, z visoko vidljivostjo.

.. literalinclude:: code/obdelava_interferogramov/cell12.py
	:language: python
	:linenos:
	

