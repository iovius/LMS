.. _obdelava_3D_meritev:

Obdelava 3D meritev
-------------------------------------

Uvod
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Pri tej nalogi boste z rotacijskim laserskim profilomerom, ki smo ga umerili na prejšnji vaji, izmerili serijo meritev istega objekta z več različnih pogledov. Meritve boste nato obdelali, sestavili in poravnali v programskem okolju Geomagic Studio (GM).

Izmerite merjeni objekt iz več pogledov
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Merjeni objekt postavite pred merilnik na primerno oddaljenost in ga izmerite. Pri tem poskrbite, da se med zajemanjem posamezne meritve merilnik in merjeni objekt ne bosta premikala. V nasprotnem primeru lahko pride do nenatančnih meritev, ki jih ne bo mogoče poravnati. Zato bodite med merjenjem **pazljivi in natančni**.
Objekt izmerite iz toliko pogledov, da bo izmerjena celotna površina. Pazite, da bo med dvema sosednjima meritvama dovolj prekrivanja (priporočamo približno 30 % prekrivanje) in da je na območju prekrivanja kakšna značilka (angl.: *feature*).

.. figure:: images/obdelava/prekrivanje.jpg
   :alt: reStructuredText, the markup syntax
   :scale: 40 %
   :align: center

   Slika 1. Prenizka stopnja prekrivanja (levo), primerna stopnja prekrivanja (desno).


Uvoz množice meritev v GM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

V GM bomo meritve uvozili v obliki standardnega trikotniškega formata *.VRML* (včasih imenovan tudi *.wrl*) s funkcijo *Import* (**File → Import**).

.. note::
   Naslednjo meritev izberete s tipko *F3*, prejšnjo s tipko *F4*, vse meritve izberete s tipko *F5*, vse, razen izbranih meritev pa skrijete s tipko *F2*.

.. warning::
   Zaradi velike količine podatkov, ki jih GM obdela ob vsakem klicu funkcije, funkcija *UNDO* deluje le izjemoma, zato **vmesne rezultate shranjujte sproti pod različnimi imeni**.

Priprava meritev
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Precej verjetno je, da je merilnik poleg samega merjenega objekta izmeril tudi del okolice. Ta ni predmet naloge in bo le oteževala poravnavo. Posamezno meritev zato najprej »očistite«; izbrišite vse površine, ki ne pripadajo merjenem objektu.

.. note::
   Izberite vsaj eno točko na površinah, ki jih želite obdržati in izberite *Bounded Components* (**Select→Select Components→Bounded Components**), nato pa desni klik in *Reverse Selection* (**RMC→Reverse Selection**). Tako boste izbrali vse površine, ki niso sklenjene z na začetku izbranimi točkami.

.. figure:: images/obdelava/izvorna_vs_ociscena.jpg
   :alt: reStructuredText, the markup syntax
   :scale: 40 %
   :align: center

   Slika 2. Izvorna meritev (levo) in "očiščena" meritev (desno).

Ročna poravnava (sestavljanje)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Meritve najprej poravnajte ročno. Pri tem koraku ne izgubljajte preveč časa s pretirano natančno poravnavo, saj boste to storili v naslednjem koraku z uporabo temu namenjenih funkcij. Dovolj je, da so meritve vsaj približno pravilno medsebojno orientirane.
Najprej izberite vse meritve, ki jih želite poravnati in izberite *Manual Registration* (**Alignment→Manual Registration**). Na levi se odpre pogovorno okno, kjer izberete način poravnave (**A**), površino, ki bo fiksna (**B**) in površino, ki jo bomo poravnali na fiksno (**C**). Izbirate lahko med poravnavo z določitvijo ene soležne točke (*1RP*) ali več kot treh soležnih točk (*NPR*). Način *1RP* je uporaben predvsem v primerih, ko ne najdete veliko soležnih točk, hkrati pa je prekrivanje razmeroma veliko. Pred uporabo tega načina je priporočljivo, da obe površini orientirate v približno enak pogled. Način *NPR* uporabljate kadar lahko najdete množico soležnih točk, želite hitreje zlagati površine ali poravnava z *1PR* ne uspe. Ni potrebe, da bi določili *N* povsem istih točk; manjše razlike v mestu klika nimajo vpliva na algoritem, saj se nato običajno naknadno sproži še funkcija *Register* (**D**), ki odpravi manjše odstopke med poravnanima površinama. Če ste z rezultatom zadovoljni pritisnite gumb *Next* (**E**) in na poravnani površini poravnajte naslednjo površino. Tako (na grobo) zložite skupaj vse meritve. Pomembno je, da ob tem vizualno preverjate, kako so površine medsebojno orientirane, saj lahko kakšna površina »uide«.

.. figure:: images/obdelava/UI2.jpg
   :alt: reStructuredText, the markup syntax
   :scale: 60 %
   :align: center

   Slika 3. Slika uporabniškega vmesnika z označenimi osnovnimi gumbi, ki jih boste potrebovali.

Globalna poravnava
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ko ste »na grobo« poravnali oz. sestavili vse površine zaženite funkcijo *Global Registration* (**Alignment→Global Registration**). Tako bo algoritem »na fino« poravnal vse površine med seboj. Rezultat vizualno preverite, predvsem na mestih, kjer bi bila morebitna neuspešna poravnava še posebej očitna.

.. figure:: images/obdelava/GR-pred-po.jpg
   :alt: reStructuredText, the markup syntax
   :scale: 40 %
   :align: center

   Slika 4. Meritvi po ročni on pred globalno poravnavo (leva), meritvi po globalni poravnavi (desno).

Končna obdelava
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ko so vse površine poravnane tudi »na fino« jih združite v eno samo površino. To storite z ukazom *Merge* (**Polygons→Merge**). Po želji nastavite lokalno in globalno filtriranje, želeno število točk, dodatno globalno poravnavo ipd…
Na mestih, kjer se posamezne meritve prekrivajo ali je prisotnega nekoliko več šuma pogosto pride do nepravilnega kombiniranja meritev, kar ima za posledico nepravilno obliko površin. GM nam ponuja vrsto orodij, s pomočjo katerih lahko te nepravilnosti odpravimo. V tej fazi se lotite tudi morebitnega odstranjevanja reliefnih markerjev (če ste jih uporabljali). Prva metoda je, da reliefne markerje iz površin enostavno izrežemo, druga pa, da uporabite funkcijo *Defeature* (**Polygons→Defeature**). Ker je uporaba markerjev potrebna le na površinah, ki nimajo izrazitih geometrijskih značilnosti, se interpolacijske metode zapolnjevanja lukenj izkažejo za precej uspešne in na površini ni vidnih ostankov markerja. Če so ti prisotni, je bilo izbrano mesto izbrano neposrečeno.

.. figure:: images/obdelava/final.jpg
   :alt: reStructuredText, the markup syntax
   :scale: 40 %
   :align: center

   Slika 5. Poravnane meritve (levo), združene meritve (sredina), končni rezultat merjenja z zapolnjenimi luknjami in zglajenimi vidnimi šivi (desno).

