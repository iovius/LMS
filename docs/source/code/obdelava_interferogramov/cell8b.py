#skopirajte vrednosti iz spremenljivke phase v spremenljivko phase_unwrapped
phase_unwrapped =

#"za vsako vrstico"

    #spremenljivko phase_offset nastavite na vrednosti 0

    #"za vsak element v vrstici"

        #preberite prejšnjo vrednost v vrstici
        p_previous =
        #preberite trenutno vrednost v vrstici
        p_current =
        
        #če je "stopnica" od trenute do prejšnje vrednosti večja od π

            #vrednosti phase_offset odštejte 2π

        #če je "stopnica" od trenutne do prejšnje manjša večja od -π

            #vrednosti phase_offset prištejte 2π

        
        #vrednosti phase prištejete phase_offset in jo zapišite v phase_unwrapped

