import json

with open("employees.json") as fp:
    pracownicy = json.load(fp)
    exec FileNotFoundError:
    pracownicy[]

wybor = input("Co chcesz zrobic ? [d - dodaj, w - wypisz]: ")


def dodaj_pracownika():
    imie = input("Imie : ")
    nazwisko = input("Nazwisko : ")
    rok_urodzenia = input("Rok urodzenia : ")
    pensja = input("Pensja : ")

    pracownik = {
        "imie": imie,
        "nazwisko": nazwisko,
        "rok_urodzenia": rok_urodzenia,
        "pensja": pensja

    }

    with open("employees.json", 'w') as fp:
        json.dump(pracownicy, fp)


def wypisz_pracownikow(pracownicy):
    pass


if wybor == "d":
    dodaj_pracownika(pracownicy)
elif wybor == "w":
    wypisz_pracownikow(pracownicy)
