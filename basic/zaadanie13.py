# dzien1 = int(input("Temperatura dnia 1: "))
# dzien2 = int(input("Temperatura dnia 2: "))
# dzien3 = int(input("Temperatura dnia 3: "))
# dzien4 = int(input("Temperatura dnia 4: "))
# dzien5 = int(input("Temperatura dnia 5: "))
# dzien6 = int(input("Temperatura dnia 6: "))
# dzien7 = int(input("Temperatura dnia 7: "))
#
# srednia_temp = (dzien1 + dzien2 + dzien3 + dzien4 + dzien5 + dzien6 + dzien7) / 7
#
# print(f"Srednia temperatura tygodnia {srednia_temp})

ile_dni = 7

temp = 0
i = 0

while i < ile_dni:
    temp_i = float(input(f"Podaj temarature w dniu {i}: "))
    temp += temp_i
    i += 1

print("Srednia temparatura wynosiła: ", temp / ile_dni)
