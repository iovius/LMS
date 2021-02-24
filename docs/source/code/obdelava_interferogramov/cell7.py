#odštejte vrednosti slike 2 od vrednosti slike 1
I1m2 = images[1] - images[2]
#odštejte vrednosti slike 3 od vrednosti slike 0
I0m3 = images[0] - images[3]
#izračunajte števec
dividend = 3*I1m2 - I0m3
#izračunajte imenovalec
divisor = I0m3 + I1m2

#preverite, da imenovalec ni enak 0
divisor[np.abs(divisor) < 0.0000001] = 0.0000001

#izračunajte tan_alpha
tan_alpha = np.sqrt(np.abs(dividend/divisor))
