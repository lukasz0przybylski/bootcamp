
miasto_a = input("Miasto A: ")
miasto_b = input("Miasto B: ")
dystans = int(input(f"Dystans: {miasto_a} - {miasto_b}"))
paliwo = int(input("Cena paliwa: "))
spalanie = int(input("Spalanie na 100 km: "))



koszt = (dystans / 100) * spalanie * paliwo

print(f"Koszt perzejazdu {miasto_a} - {miasto_b} to {koszt} PLN")
