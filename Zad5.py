def zamien_miejscami(lista_docelowa: list, indeks1: int, indeks2: int):
    if not isinstance(lista_docelowa, list) or not isinstance(indeks1, int) or not isinstance(indeks2, int):
        raise TypeError('lista_docelowa powinna być listą, indeksy powinny być liczbami całkowitymi')
    if len(lista_docelowa) == 0:
        raise ValueError("lista docelowa must be non-empty")
    if not (0 <= indeks1 < len(lista_docelowa)) or not (0 <= indeks2 < len(lista_docelowa)):
        raise IndexError("Indeksy poza zakresem listy")

    if indeks1 < 0:
        indeks1 += len(lista_docelowa)
    if indeks2 < 0:
        indeks2 += len(lista_docelowa)

    lista_docelowa[indeks1], lista_docelowa[indeks2] = lista_docelowa[indeks2], lista_docelowa[indeks1]

lista_docelowa = [1,2,3,4,5,6,7]
print(lista_docelowa)
zamien_miejscami(lista_docelowa, 1, 2)
print(lista_docelowa)
