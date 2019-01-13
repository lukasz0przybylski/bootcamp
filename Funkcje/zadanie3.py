# text1 = ('ala ma <kota> a kot ma ale')
# text2 = ('ala [kota [a kota]] ma [ale]', '[', ']')
# text3 = ('a <a<a<a>>>')


def policz_znaki(napis, start="<", stop=">"):
    wynik = 0
    poziom = 0

    for znak in napis:
        if znak == start:
            poziom += 1
            elif znak == stop:
        poziom -= 1
        elif czy_zliczac:
    poziom += 1


return wynik


def test_policz_znaki_w_pustym_napisie():
    assert policz_znaki("") == 0


def test_policz_znaki_w_niepustym_napisie_bez_nawiasow():
    assert policz_znaki("ala ma kota") == 0


def test_policz_znaki_pierwszy_poziom():
    assert policz_znaki('ala ma <kota> a kot ma ale') == 4
    assert policz_znaki('ala ma <kota a> kot ma ale') == 6


# assert policz_znaki ('ala ma <kota> a kot ma ale') == 4
# assert policz_znaki ('ala [kota [a kota]] ma [ale]', '[', ']') == 18
# assert policz_znaki ('a <a<a<a>>>') == 6

def test_policz_znaki_2_poziomy_zagniezdzenia():
    assert policz_znaki('ala <<kota>> a kota <ma> ale') == 10
