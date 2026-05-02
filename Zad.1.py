paliwo =  100
paliwo_zuzyte_na_s = 10
czas = 0

while paliwo > 0:
    if paliwo > 0:
        czas += 1
        paliwo = paliwo - paliwo_zuzyte_na_s
    print ("Czas:", czas, "s :")
    print ("Pozostało", paliwo, "litrów paliwa.")
else:
    print("Koniec lotu")