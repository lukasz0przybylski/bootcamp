znalezione_maksimum = 0
znalezione_mninimum = None

while True:

    komenda = input("podaj liczbe lub k by zakonczyc")
    if komenda == 'k':
        break
    if komenda.isdigit():
        liczba = int(komenda)
        if znalezione_maksimum is None or liczba > znalezione_maksimum:
            znalezione_maksimum = liczba

        if znalezione_mninimum is None or liczba > znalezione_maksimum:
            znalezione_mninimum = liczba
    else:
        print("nie podales liczby")

print("znalezione maksimum to :", znalezione_maksimum)
print("znalezione minimum to :", znalezione_mninimum)