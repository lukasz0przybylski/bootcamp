class Przedmiot:
    def __init__(self, nazwa, bonus):
        self.nazwa = nazwa
        if isinstance(bonus, int):
            self.bonus_do_ataku = bonus
        else:
            raise ValueError ("Bonus powinien byc liczba")






class Postac:
    def __init__(self, imie, atak, zdrowie):
        self.imie = imie
        self._atak = atak
        self.zdrowie = zdrowie
        self.max_zdrowie = zdrowie
        self.ewipunek = 0

    @property
    def atak(self):
        return self._atak

    def otrzymaj_obrazenia(self, obrazenia):
        self.zdrowie -= obrazenia
        if self.zdrowie < 0:
            self.zdrowie = 0

    def wylecz(self, pkt_zdrowia):
        self.zdrowie += pkt_zdrowia
        if self.zdrowie > self.max_zdrowie:
            self.zdrowie = self.max_zdrowie

    def dodaj_przedmiot(self):






def test_postac_dodaj_przedmiot():
    postac = Postac("Rafał", 5, 200)
    przedmiot = Przedmiot("Rekawice grzmoty", 40)
    assert przedmiot not in postac.ewipunek
    postac.dodaj_przedmiot(przedmiot)
    assert przedmiot in postac.ewipunek

def test_nowa_postac():
    postac = Postac("Albert", 1, 20)
    assert postac.imie == "Albert" and postac.atak == 1 and postac.zdrowie == 20 and postac.max_zdrowie == 20


def test_obrazenia():
    postac = Postac("Rafał", 5, 200)
    assert postac.zdrowie == 200
    postac.otrzymaj_obrazenia(80)
    assert postac.zdrowie == 120
    postac.otrzymaj_obrazenia(200)
    assert postac.zdrowie == 0


def test_leczenie():
    postac = Postac("Rafał", 5, 200)
    postac.otrzymaj_obrazenia(80)
    assert postac.zdrowie == 120
    postac.wylecz(50)
    assert postac.zdrowie == 170


def test_leczenie_nieboszczyka():
    postac = Postac("Rafał", 5, 200)
    postac.otrzymaj_obrazenia(800)
    assert postac.zdrowie == 0
    postac.wylecz(50)
    assert postac.zdrowie == 0


def test_za_duze_leczenie():
    postac = Postac("Rafał", 5, 200)
    postac.otrzymaj_obrazenia(80)
    assert postac.zdrowie == 120
    postac.wylecz(500)
    assert postac.zdrowie == 200
