a = int(input("podaj pierwsza liczbe : "))
b = int(input("podaj droga liczbe : "))
operacja = input("Podaj rodzaj operacji : ")

if operacja == '+':
    print(a + b)

elif operacja == '-':
    print(a - b)

elif operacja == '/':
    if b == 0:
        print("operacja niedozwolona")
    else:
        print(a / b)

elif operacja == '*':
    print(a * b)

else:
    print("operacja nie jest wspierana")
