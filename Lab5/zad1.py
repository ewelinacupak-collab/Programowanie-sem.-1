import math

def pierwiastki(a,b,c):

    """
    Funkcja oblicza pierwiastki kwadratowe równania ax^2 + bx + c = 0

    Args:
    param a: współczynnik przy x^2, liczba rzeczywista. Nie może być 0.
    param b: współczynnik przy x, liczba rzeczywista.
    param c: wyraz wolny, liczba rzeczywista.

    returns:
    Funkcja zwraca krotkę z pierwiastkami równania kwadratowego.
    Jeśli delta < 0, zwraca informację o ujemnej delcie.
    Jeśli delta > 0, zwraca dwa pierwiastki równania.
    Jeśli delta = 0, zwraca dwa takie same pierwiastki.

    raises:
    Funkcja wyrzuca ValueError jeśli a = 0, bo nie jest to wtedy funkcja kwadratowa.
    """
    if a == 0:
        raise ValueError("a nie może być zerem")

    delta = b ** 2 - 4 * a * c

    if delta < 0:
        return "delta ujemna"

    if delta > 0:
        sqrtdelta = math.sqrt(delta)
        x1 = (-b + sqrtdelta) / (2*a)
        x2 = (-b - sqrtdelta) / (2*a)
        return round(x1, 1), round(x2, 1)
    else:
        return round(x1, 1), round (x1, 1)




print(pierwiastki(2,1,3))
