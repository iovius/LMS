#vrednost phase_unwrapped skopirajte v phase
phase_unwrapped2 = phase_unwrapped.copy()
#izračunajte indeks sredinskega stolpca
u_scan = int(w/2)
#postavite vrednost phase_offset na 0
phase_offset = 0

#"za vsako vrstico"
for v in range(1,h):
    #preberite vrednost prejšnjega elementa v sredinski vrstici
    p_previous = phase_unwrapped[v-1, u_scan]
    #preberite vrednost trenutnega elementa v sredinski vrstici
    p_current = phase_unwrapped[v, u_scan]
    
    #izračunajte razliko med trenutno in prejšnjo
    diff_c_p = p_current - p_previous
    #če je "stopnica" od prejšnje do trenutne vrednosti večja od π
#     if diff_c_p > π:
#         #deljite z 2π
#         diff_c_p /= π2
#         #zaikrožite
#         diff_c_p = np.round(diff_c_p)
#         #pomnožite z 2π
#         diff_c_p *= π2
#         #odštejte vrednost od phase_offset
#         phase_offset -= diff_c_p
        
#     #če je "stopnica" od trenutne do prejšnje vrednosti večja od π
#     if diff_c_p < -π:
    #deljite z 2π
    diff_c_p /= π2
    #zaikrožite
    diff_c_p = np.round(diff_c_p)
    #pomnožite z 2π
    diff_c_p *= π2
    #odštejte vrednost od phase_offset
    phase_offset -= diff_c_p
       
    #celotni treutni vrstici prištejte vrednost phase_offset
    phase_unwrapped2[v,:] += phase_offset
