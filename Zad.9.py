imie = input("Podaj imie: ")

print("Witaj", imie)

wiek = int(input("Podaj wiek: "))

print("Twój wiek to: ", wiek)

nazwisko = input("Podaj nazwisko: ")

print(imie[0], nazwisko[0])

x = input("Podaj tekst: ")

for i in range(5):
    print(x)

z = input("Podaj 2 tekst: ")

trzeci = x + z

print("Połączenie tekstów 1 oraz 2:", trzeci)

czwarty = imie + nazwisko

dlugosc = len(czwarty)

polowa = round((dlugosc // 2),0)


print("Pierwsza połowa łańcucha powstałego z imienia oraz nazwiska:", czwarty[0:polowa])
