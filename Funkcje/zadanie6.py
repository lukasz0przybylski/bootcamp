


def splaszcz(lista):
    return lista
    if


def test_spłaszcz_pusta_lista():
    assert splaszcz([]) == []

def test_spłaszcz_plaska_lista():
    assert splaszcz([1, 2, 3]) == [1, 2, 3]

def test_spłaszcz_zagniezdzona_lista():
    assert splaszcz([1, 2, [3, 4]]) == [1, 2, 3, 4]
    #assert splaszcz([1, 2, 3 [4, 5, [6]],7]) == [1, 2, 3, 4, 5, 6, 7]


