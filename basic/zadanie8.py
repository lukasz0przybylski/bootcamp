
wymiar_a = int(input("szerokosc : "))
wymiar_b = int(input("dlugosc : "))
wymiar_h = int(input("wysokosc : "))

objetosc = wymiar_a * wymiar_b * wymiar_h

print(f"Objetosc wynosi : {objetosc}")
print(f"Czy wieksza od 1 listra: {objetosc > 1000}")



if objetosc > 2000:
    print("Objetosc jest wieksza niez 2 litr")
elif objetosc > 1000:
    print("Objetosc jest wieksza niez 1 litr")
else:
    print("Objetosc jest mniejsza od 1 litr")

print("To jest koniec programu")