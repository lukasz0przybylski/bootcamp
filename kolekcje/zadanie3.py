lista = [100, -100, 2, -2, 100, 2, -2, 0]

licznik_dodatnich = 0
licznik_ujemnych = 0

for liczba in lista:
    if liczba > 0:
        licznik_dodatnich += 1
    elif liczba < 0:
        licznik_ujemnych += 1

print(f"liczba dodatnich: {licznik_dodatnich}, liczby ujemne {licznik_ujemnych}")