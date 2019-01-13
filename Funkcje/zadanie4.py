def formatuj(*napisy):
    napis = "\n".join(napisy)
    return napis


def test_firmatuj_napis_bez_znacznikow():
    assert formatuj("Hello World!") == "Hello World!"

def test_firmatuj_wiele_napis_bez_znacznikow():
    assert formatuj()

