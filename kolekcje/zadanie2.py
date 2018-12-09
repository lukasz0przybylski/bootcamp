liczby = []
i = 0
while i < 10:
    liczba = input("podaj liczbe lub k by zakonczyc")
    if liczba == 'k':
        break
    liczba = int(liczba)
    liczby.append(liczba)
    i += 1

print("srednia wynosi", sum(liczby) / len(liczby))


