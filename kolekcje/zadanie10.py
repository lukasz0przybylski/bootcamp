#text = input("podaj tekst")
from collections import defaultdict


znaki= {}
#text = "ala ma kaota"


for znak in text:
    #if znak in znaki:
    #    znaki[znak] =+ 1
    #else:
    #    znaki[znak] = 1
    #
    #znaki[znak] = 1
    znaki[znak] = znaki.get(znak, 0) + 1

print("Stataystyka")