# Co się stanie? Czy kod się wykona, czy wystąpi błąd? Jeśli błąd, podaj jego typ i powód.
# def t(x, *, y, z=0):
#  return x + y + z
# val= t(1, 2, z=3)

# Funkcja nie wykona się, ponieważ po * wszystkie argumenty funkcji powinny być podane z nazwą.
# Próba wywołania funkcji z parametrami t(1,2,=3) nie uda się, ponieważ parametr y jest wyoływany pozycyjnie, a nie z nazwą.
# Wystąpi błąd typu TypeError.

#Poprawna funkcja

def t(x, *, y, z=0):
    return x + y + z
val= t(1, y=2, z=3)
print(val)


# Wyjaśnij co dokładnie zwróci y oraz jak Python rozdzielił argumenty.
# f = lambda a, /, *args, b=0: (a, sum(args) + b)
# y = f(3, 4, 5, b=2)

# y zwróci krotkę z pierwszym elementem a = 3, oraz kolejnym sum(args) + b = 4+5+2
# Rozdzielenie argumentów: argument a przed / musi być argumentem pozycyjnym, kolejne argumenty są przedstawione jako krotka
# i trafiają do *args, argument b moża ustawić jedynie z nazwą.