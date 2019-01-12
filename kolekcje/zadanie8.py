text = input("Podaj tekst: ")

#text = "Ala ma <kota>, a kot ma Alę"

ile_znakow = 0

#text1 = "Ala ma kota"
#text2 = "Ala <ma> kota"
#text3 = "Ala <>ma kota"


dlugosc = 0
licz = False

for znak in text:
    if znak == "<":
        licz = True
    elif znak == ">":
        licz =False
        break #opcjonalnie
    elif licz:
        dlugosc += 1

#print(dlugosc)
#assert dlugosc == 0

print(f"liczba znakow pomiedzy nawiasami <> wynosi {dlugosc}")