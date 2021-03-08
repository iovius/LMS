:orphan:

.. _navodila_python:

Navodila za namestitev Pythona in OpenCVja
----------------------------------------------------------

V nadaljevanju so navodila, kako namestiti **Python** in **OpenCV**. Če imate drugo verzijo Windowsov, so možne manjše razlike napram tem navodilo, načeloma pa je postopek zelo podoben.

Namestitev Pythona
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pojdite na `povezavo <https://www.anaconda.com/products/individual>`__  in prenesite instalacijsko datoteko.

.. figure:: images/namestitev_py/1.JPG
   :alt: reStructuredText, the markup syntax
   :scale: 100 %
   :align: center
   
Če se vam pojavi spodnje okno, ga zaprite, saj se bo prenos datoteke izvršil v ozadju.

.. figure:: images/namestitev_py/2.JPG
   :alt: reStructuredText, the markup syntax
   :scale: 100 %
   :align: center
   
   
Ko je datoteka prenesena, jo zaženite.

.. figure:: images/namestitev_py/3.JPG
   :alt: reStructuredText, the markup syntax
   :scale: 100 %
   :align: center
   
   
.. figure:: images/namestitev_py/4.JPG
   :alt: reStructuredText, the markup syntax
   :scale: 100 %
   :align: center


.. figure:: images/namestitev_py/5.JPG
   :alt: reStructuredText, the markup syntax
   :scale: 100 %
   :align: center


.. figure:: images/namestitev_py/6.JPG
   :alt: reStructuredText, the markup syntax
   :scale: 100 %
   :align: center


Izberite datoteko, kamor želite namestiti Python. V mojem primeru je to »C:\\ProgramData\\Anaconda3«. Zapomnite si to mesto!


.. figure:: images/namestitev_py/7.JPG
   :alt: reStructuredText, the markup syntax
   :scale: 100 %
   :align: center



.. figure:: images/namestitev_py/8.JPG
   :alt: reStructuredText, the markup syntax
   :scale: 100 %
   :align: center


Počakajte, da se namestitev dokonča.


.. figure:: images/namestitev_py/9.JPG
   :alt: reStructuredText, the markup syntax
   :scale: 100 %
   :align: center



.. figure:: images/namestitev_py/10.JPG
   :alt: reStructuredText, the markup syntax
   :scale: 100 %
   :align: center



.. figure:: images/namestitev_py/11.JPG
   :alt: reStructuredText, the markup syntax
   :scale: 100 %
   :align: center


S tem je namestitev Pythona končana.

Sedaj je treba namestiti še OpenCV za Python. Pojdite na `povezavo <https://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv>`__  in prenesite datoteko *opencv_python-3.4.2-cp36-cp36m-win_amd64.whl*.


.. figure:: images/namestitev_py/15.JPG
   :alt: reStructuredText, the markup syntax
   :scale: 100 %
   :align: center


Ko je datoteka prenesena, pojdite zopet v **Anaconda Prompt**. Premaknite se v mapo, kjer je prenesena datoteka. V mojem primeru je datoteka v »C:\\Users\\Urbanus Pavlovius\\Downloads«, torej se v to mapo premaknem z ukazom »cd c:\\Users\\Urbanus Pavlovius\\Downloads« (pri vas vpišite mapo, kjer je datoteka, spredaj pa mora biti »cd «). Nato namestite knjižnico z ukazom »*pip install opencv_python-3.4.2-cp36-cp36m-win_amd64.whl*«.


.. figure:: images/namestitev_py/16.JPG
   :alt: reStructuredText, the markup syntax
   :scale: 100 %
   :align: center



.. figure:: images/namestitev_py/17.JPG
   :alt: reStructuredText, the markup syntax
   :scale: 100 %
   :align: center


Če vidite nekaj podobnega, je bila namestitev uspešna.
Sedaj naredite še bližnjico za zagon Pythona. Da ne boste imeli težav s končnicami najprej omogočite končnice in skrite mape.
Pojdite v **Nadzono ploščo (Control Panel)** in izberite **Folder Options**.



.. figure:: images/namestitev_py/18.JPG
   :alt: reStructuredText, the markup syntax
   :scale: 100 %
   :align: center


Označite »**Show hidden files, folders, and drives**« in odznačite »**Hide extension for known file types**«.


.. figure:: images/namestitev_py/19.JPG
   :alt: reStructuredText, the markup syntax
   :scale: 100 %
   :align: center


Poiščite, kje imate nameščen Python. V mojem primeru je to v mapi *C:\\ProgramData\\Anaconda3*. Pojdite v mapo *Scripts*.


.. figure:: images/namestitev_py/20.JPG
   :alt: reStructuredText, the markup syntax
   :scale: 80 %
   :align: center


Sedaj odprite **Notepad** in napišite ukaz: **»start /d »ime_mape_kjer je_Python_scripts«jupter notebook »ime_mape_kamor_želite_shranjevati_Python_datoteke««**.


.. figure:: images/namestitev_py/21.JPG
   :alt: reStructuredText, the markup syntax
   :scale: 90 %
   :align: center

V mojem primeru je **»ime_mape_kjer je_Python_scripts«** enak *»C:\\ProgramData\\Anaconda3\\Scripts«*, **»ime_mape_kamor_želite_shranjevati_Python_datoteke«** pa *»C:\\Users\\Urbanus Pavlovius\\Documents\\Python«*. 

.. warning::
   Pazite, da ta mapa obstaja in da se niste zatipkali!


V to mapo boste kasneje prenesli tudi vaše programe.
Nato datoteko shranite kot *»Python.bat«*.

.. warning::
   Pazite, da bo ime datoteke res *»Python.bat«* in ne naprimer *»Python.bat.txt«*, saj v tem primeru ne bo delovalo.


.. figure:: images/namestitev_py/22.JPG
   :alt: reStructuredText, the markup syntax
   :scale: 100 %
   :align: center


Zaprite **Notepad**.
Dvokniknite na ikono **Python.bat**.


.. figure:: images/namestitev_py/23.JPG
   :alt: reStructuredText, the markup syntax
   :scale: 80 %
   :align: center


Moralo bi se zagnati takole okno.


.. figure:: images/namestitev_py/24.JPG
   :alt: reStructuredText, the markup syntax
   :scale: 80 %
   :align: center


Odprl se bo tudi **Jupyter notebook** v vašem brskalniku. Ko boste v **»ime_mape_kamor_želite_shranjevati_Python_datoteke«** skopirali tudi vaše programe, jih boste videli v Jupytru. Drugače pa nov program začnete pisati s klikom na *New→ Python 3*.
