#text = input("Podaj tekst: ")

text = "Ala ma kota aeiouy"

ile_samoglosek = 0

SAMOGLOSKI = 'aeiouy'

for litera in text:
    if litera in SAMOGLOSKI:
        ile_samoglosek += 1

print (ile_samoglosek == 10)


#ile_samoglosek2 = 0
#for samogloska in SAMOGLOSKI:
