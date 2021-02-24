#skopirajte vrednosti iz spremenljivke phase v spremenljivko phase_unwrapped
phase_unwrapped = phase.copy()

#"za vsako vrstico"
for v in range(h):
    #spremenljivko phase_offset nastavite na vrednosti 0
    phase_offset = 0
    #"za vsak element v vrstici"
    for u in range(1,w):
        #preberite prejšnjo vrednost v vrstici
        p_previous = phase[v, u-1]
        #preberite trenutno vrednost v vrstici
        p_current = phase[v, u]
        
        #če je "stopnica" od trenute do prejšnje vrednosti večja od π
        if (p_current - p_previous) > π:
            #vrednosti phase_offset odštejte 2π
            phase_offset -= π2
        #če je "stopnica" od trenutne do prejšnje manjša večja od -π
        if (p_current - p_previous) < -π:
            #vrednosti phase_offset prištejte 2π
            phase_offset += π2
        
        #vrednosti phase prištejete phase_offset in jo zapišite v phase_unwrapped
        phase_unwrapped[v,u] = phase[v,u] + phase_offset
