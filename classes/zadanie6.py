
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def lenght(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

def test_vectore_lenght():
    assert Vector(3, 4) 


def test_vector_init():
    vectore_1 = Vector(x=1, y=2)
    vectore_2 = Vector(x=1, y=2)
    assert vectore_1.x == 1
    assert vectore_2.y == 2


def test_vector_add():
    vectore_1 = Vector(x=1, y=2)
    vectore_2 = Vector(x=1, y=2)
    vectore_3 = vectore_1 + vectore_2
    assert vectore_3.x == 2
    assert vectore_3.y == 4
    assert vectore_1.x == 1
    assert vectore_2.y == 2


def test_vector_sub():
    vectore_1 = Vector(x=1, y=2)
    vectore_2 = Vector(x=1, y=2)
    vectore_3 = vectore_1 - vectore_2
    assert vectore_3.x == 2
    assert vectore_3.y == 4


def test_vector_init():
    vectore_1 = Vector(x=1, y=2)
    vectore_2 = Vector(x=1, y=2)
    assert vectore_1 * vectore_2 == 1 * 1 + 2 * 2


def test_vectore
