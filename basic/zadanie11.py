x = int(input("Podaj pozycje gracza x : "))
y = int(input("Podaj pozycje gracza y : "))

# czy jest poza planasza
if x < 0 or x > 100 or y < 0 or y > 100:
    print("jestes poza plansza")
elif x > 90 and y > 90:
    print("jestes w gornym prawym rogo")
elif x > 90 and y > 10:
    print("jestes w dolnym prawym rogo")
elif x > 10 and y > 90:
    print("jestes w dgornym lewym rogo")
elif x > 10:
    print("jestes w dolnej krawedzi")
