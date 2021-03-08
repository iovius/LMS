.. _twyman_green:

Twyman-Greenov interferometer
-------------------------------------------

.. |2pi| replace:: :math:`{2\pi}`
.. |pi_pol| replace:: :math:`{\pi/2}`
.. |dfi| replace:: :math:`{\Delta\phi}`
.. |dx_pos| replace:: :math:`{\Delta x_{poz.miz}}`

.. |nbsp| unicode:: 0xA0 
   :trim:
   
.. |f_prednost_1| replace:: Ne potrebujemo umerjanja, saj poznamo dimenzije pikslov, snop pa je kolimiran
.. |f_prednost_2| replace:: Visoka ločljivost zajema.
.. |f_slabost_1| replace:: Ne moremo nastaviti časa osvetlitve (presvetljene slike)
.. |f_slabost_2| replace:: Ne moremo nastaviti hitrosti zajema
.. |k_prednost_1| replace:: Lahko nastavljamo osvetljevanje ipd...
.. |k_prednost_2| replace:: Nastavljanje hitrosti zajema.
.. |k_slabost_1| replace:: Uporaba posredika (papir pred kamero) - dodaten šum.
.. |k_slabost_2| replace:: Omejena ločljivost.


Pri tej vaji boste uporabljali polariziran *He-Ne* laser z valovno dolžino *633 nm* in premerom žarka *0,8* |nbsp| *mm*.

.. figure:: images/twyman_green/shema.png
	:alt: reStructuredText, the markup syntax
	:scale: 70 %
	:align: center
	
	Slika 1. Shema Twyman-Greenovega interferometra.

Praktične naloge:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Razširjevalnik žarka je sestavljen iz leč *f*\ :sub:`1`\ = *7,5 mm* in *f*\ :sub:`2`\ = *150 mm* ter zaslonke za prostorsko filtriranje žarka. Razdaljo med lečama nastavite z uporabo strižnega interferometra. Fotografirajte in razložite interferograme, ko je kolimacijska leča preblizu, predaleč in v pravilni poziciji.
#. Sestavite *Twyman-Greenov* interferometer. Pri tem uporabite ploščati delilnik žarka dimenzij *25×35 mm*, kvadratno zrcalo *25×25 mm* (kot referenčno zrcalo – *M1*) in zrcalo (*M2*), katerega obliko površine morate izmeriti. Sestavljajte po naslednjem vrstnem redu:

	* Za kolimator postavite delilnik žarka pod kotom *45°*. Delilnik vpnite v prijemalo tako, da zagotovite nemoteno širjenje prepuščenega in odbitega žarka!
	* Kakšna mora biti smer polarizacije glede na delilnik žarka, da je sekundarni odboj z delilnika žarka minimalen? Skicirajte! Laserja ne obračajte, da se ne spremeni lokacija žarka glede na zaslonko v razširjevalniku žarka!
	* Zrcali postavite tako, da sta pravokotni glede na posamezen žarek.
	* S finim nastavljanjem orientacije enega od zrcal skušajte doseči interferogram, ki bo imel približno deset prog orientiranih enkrat vertikalno in drugič horizontalno. Interferograma fotografirajte in razložite, kakšna je ukrivljenost valovnih front.
	
#. Sedaj, ko je sistem postavljen, zamenjajte merjeno zrcalo (*M2*) za zrcalo, ki je pritrjeno na zvočnik. Sistem zopet nastavite tako, da boste videli interferogram s približno 5imi vertikalnimi progami.
#. Na mesto zaslona (kjer ste interferograme opazovali do sedaj) postavite bodisi fotoaparat brez objektiva bodisi kamero, pred katero je nameščen papirnat zalon. #. Z generatorjem napetosti generirajte "žagast profil" napetosti, tako da se bo zvočnik počasi približeval in oddaljeval. Na kameri bi morali videti, da se progre "peljejo" nekaj časa v eno stran, nato pa se obrnejo in nazaj. 

	.. note::
		Vsak izmed omenjenih načinov zajemanja ima svoje prednosti in slabosti.
		
		**Foroaparat**
		
		+-----------------+----------------+
		|Prednosti        |Slabosti        |
		+=================+================+
		||f_prednost_1|   ||f_slabost_1|   |
		+-----------------+----------------+
		||f_prednost_2|   ||f_slabost_2|   |
		+-----------------+----------------+
		
		**Kamera**
		
		+-----------------+----------------+
		|Prednosti        |Slabosti        |
		+=================+================+
		||k_prednost_1|   ||k_slabost_1|   |
		+-----------------+----------------+
		||k_prednost_2|   ||k_slabost_2|   |
		+-----------------+----------------+


#. Posnemite sekvenco. Računajte s tem, da bomo morali na naslednji vaji izluščiti slike, pri katerih bodo proge zamaknjene po :math:`\pi /2`.