def sum_digits(n):

    """
    Funkcja obliczająca rekurencyjnie sumę cyfr liczby.

    param n: liczba całkowita, której cyfry zostaną zsumowane. Jeśli liczba będzie ujemna, zostanie potraktowana jako dodatnia.

    returns:
    Zwraca, liczbę całkowitą, sumę cyfr liczby n.
    """

    n = abs(n)

    if n < 10:
        return n
    else:
        return (n % 10) + sum_digits(n // 10)

print(sum_digits(-123))
