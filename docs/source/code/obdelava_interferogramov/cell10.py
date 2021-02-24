# vrednost phase_unwrapped skopirajte v phase_unwrapped2
phase_unwrapped2 =
# izračunajte indeks sredinskega stolpca; pazite na tip!!
u_scan =
# postavite vrednost phase_offset na 0
phase_offset = 0

# "za vsako vrstico"

    # preberite vrednost prejšnjega elementa v sredinski vrstici
    p_previous =
    # preberite vrednost trenutnega elementa v sredinski vrstici
    p_current =
    
    # izračunajte razliko med trenutno in prejšnjo
    diff_c_p =

    #deljite z 2π
    diff_c_p
    #zaikrožite
    diff_c_p =
    #pomnožite z 2π
    diff_c_p
    #odštejte vrednost od phase_offset
    phase_offset
       
    #celotni treutni vrstici prištejte vrednost phase_offset
    phase_unwrapped2[v,:]
