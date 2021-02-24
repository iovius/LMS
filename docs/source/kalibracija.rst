.. _kalibracija:

Umeritev laserskega 3D merilnika
-------------------------------------------------

Uvod
^^^^^^

Cilj vaje je spoznati osnovne pristope in praktično izvesti umeritev laserskega rotacijskega merilnika.

Oprema
^^^^^^^^^^^^^^^^^^^^^^^^^

- Laserski rotacijski 3D merilnik – Merkur.
- Koračna miza.
- Referenčna površina.
- Programska oprema za izračun optimalnih transformacijskih parametrov.

Potek vaje
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Ogled sistema.
- Zajem sekvence umeritvenih meritev.
- Izvedba umeritve.
- Primerjava površin pred in po umeritvi.

Predstavitev parametrov rekonstrukcije
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Notranji parametri:
   - **f**		goriščna razdalja leče	[mm]
   - **cu**		lokacija presečišča optične osi leče in senzorske ravnine v U smeri								[št. senzorskih elementov]
   - **cv**		lokacija presečišča optične osi leče in senzorske ravnine v V smeri								[št. senzorskih elementov]
   - **alfa**	triangulacijski kot					[°]
   - **beta**	kot nagiba senzorskega elementa glede na pravokotnico optične osi kamere; pozitivna smer je proti Scheimpflugovi korekciji			[°]
   - **psi**		rotacija kamere okrog lastne optične osi		[°]
   - **Py**		lega projektorja glede na kamerin k. s. v Y smeri	[mm]
   - **Pz**		lega projektorja glede na kamerin k. s. v Z smeri	[mm]
   - **du**		dimenzija senzorskega elementa v U smeri		[mm]
   - **dv**		dimenzija senzorskega elementa v V smeri		[mm]
   - **k0**		parameter distorzije kamere
   - **k1**		parameter distorzije kamere
   - **k2**		parameter distorzije kamere
   - **k3**		parameter distorzije kamere
   - **Ry**		lega k. s. projektorja glede na vrtičše merilnika (k. s. modula) v Y smeri	[mm]
   - **Rz**		lega k. s. projektorja glede na vrtičše merilnika (k. s. modula) v Z smeri	[mm]
   - **Ko_rot**	korekcija zasuka projektorja okrog njegove osi (odstopanje od vzporednosti s kamero)								[°]
   - **domega**	kotni zasuk mizice pri nem koraku motorja		[°]
- Zunanji parametri
   - **TX**		translacija v X smeri	[mm]
   - **TY**		translacija v Y smeri	[mm]
   - **TZ**		translacija v Z smeri	[mm]
   - **RX**		rotacija okrog X osi	[°]
   - **RY**		rotacija okrog Y osi	[°]
   - **RZ**		rotacija okrog Z osi	[°]

Nastavitev programa
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Z uporabo merilnega traku, kotomera in priložene dokumentacije ocenite začetne približke transformacijskih parametrov. Parametri, ki jih je potrebno oceniti so:

   - **cu**;	kot začetni približek vzemite polovično število slikovnih elementov v U smeri
   - **cv**;	kot začetni približek vzemite polovično število slikovnih elementov v V smeri
   - **alfa**
   - **Py**
   - **Pz**
   - **du**; poglejte v dokumentacijo kamere
   - **dv**; poglejte v dokumentacijo kamere
   - **domega**

2. Ostale parametre bomo določili s pomočjo umeritvenega programa.

3. Ko ste ocenili začetne približke, odprite LabView program calibration for rotational profilomer (ver 2_0 for prf). Spreminjate lahko naslednje nastavitve:

   a. **Detection parameters**:
   
      i. **NofSurf** … število odprtih umeritvenih meritev
      ii. **first srf** … indeks prve meritve
      iii. **SurfIncr** … kolikšen je inkrement med dvema meritvama (1 … zaporedne meritve, 2 … vsaka druga itd …); če povečujete, je potrebno ustrezno povečati DZ (pomik med dvema zaporednima odprtima meritvam)
      iv. **first N prf.**, **last N prf.**, **prf. start**, **prf. end** … parametri, s katerimi »obrežemo meritev«, uporabite v primeru šuma o robovih meritve	
   b. **TRP & opt out**

4. Ostale parametre spreminjaje le v nujnih primerih in po posvetovanju z asistentom.

Zagon optimizacije
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Predlagamo, da za umerjanje uporabite naslednji »algoritem«:

1. Ob nastavljenih začetnih približkih odprite eno samo meritev in jo vizualno primerjaje z idealno meritvijo (**gumb draw** ideal). Če so odstopanja res velika (predvsem **merilo**), preverite začetne približke.
2. Če meritev *ni vsaj približno* v merilu (na merilo v Y smeri vpliva predvsem parameter **domega**), poskusite ročno spreminjati kot triangulacije (**alfa**), kot med dvema profiloma (**domega**) in razdaljo med kamero in projektorjem (**Py**) ter goriščno razdaljo leče (**f**).
3. Zaženite optimizacijo zunanjih parametrov (**TX**, **TY**, **TZ**, **RX**, **RY**, **RZ**), da poravnate površino z referenčno (kanali morajo sovpadati).
4. Ko standardna deviacija odstopkov med izmerjeno in referenčno površino pade pod 3-4 mm, lahko (za kratek čas) poskusite vklopiti tudi optimizacijo kota triangulacije (**alfa**), goriščne razdalje objektiva (**f**), kota med dvema profiloma (**domega**), sredine slike (**cu**, **cv**) in razdalje med kamero in projektorjem (**Py**). Rezultat vseskozi vizualno nadzorujte. Če se meritev povsem »podre«, optimizacijo ustavite.
5. Če se oblika površine ni povsem »podrla«, odprite dodatne meritve in preverite, kako vplivajo na standardno deviacijo odstopkov (SDO). Če je oblika vseh rekonstruiranih površin približno pravilna, SDO pa je drastično narasla, preverite, ali sta **SurfInc** in **DZ** pravilna.
6. Če imate občutek, da umeritev konvergira v pravo smer (smo v globalnem minimum),vklopite umeritev vseh parametrov, se udobno namestite in čakajte … Ko pade standardna deviacija pod približno 1,3 mm ste (skoraj) zagotovo v globalnem minimumu in **lahko optimirate vse parametre**.

Če se vam meritev povsem podre, preverite, kateri parameter je ušel in se vrnite korak ali dva nazaj.

Zabeležite rezultate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Končni rezultat, ki ga morate predstaviti v poročilu, je SDO med referenčno in izmerjeno površino in dobljeni transformacijski parametri. Naredite tudi »screen shot« polja odstopkov (gumb **draw diff**) in ga priložite poročilu.
Primerjajte začetno in končno referenčno površino, ter preverite, kako parametri, ki so težko izmerljivi/ocenljivi vplivajo na obliko rekonstruirane površine in SDO.

